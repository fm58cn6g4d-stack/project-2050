// Optional browser QA for the story page: requires Playwright and Chromium; never contacts remote sources.
// Serve index/public-2050 first:  python3 -m http.server 8765 --bind 127.0.0.1 --directory index/public-2050
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const path = require('node:path');
const fs = require('node:fs');
const root = path.resolve(__dirname, '../../../..');
const url = 'http://127.0.0.1:8765/story.html';
const shots = path.join(root, 'build/story-review');
const launch = process.env.PUBLIC_PRODUCT_BROWSER ? {executablePath: process.env.PUBLIC_PRODUCT_BROWSER} : {};

(async () => {
  fs.mkdirSync(shots, {recursive: true});
  const browser = await chromium.launch({headless: true, ...launch});
  try {
    for (const [name, width, height] of [['phone-320', 320, 700], ['phone', 390, 844], ['tablet', 768, 1024], ['desktop', 1440, 1000]]) {
      const page = await browser.newPage({viewport: {width, height}, reducedMotion: 'reduce'});
      const errors = [];
      page.on('pageerror', e => errors.push(e.message));
      page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
      await page.route('**/*', route => route.request().url().startsWith('http://127.0.0.1:8765/') ? route.continue() : route.abort());
      await page.goto(url);
      const [scroll, inner] = await page.evaluate(() => [document.documentElement.scrollWidth, innerWidth]);
      assert.ok(scroll <= inner, `${name}: horizontal scroll ${scroll} > ${inner}`);
      assert.equal(await page.locator('h1').count(), 1);
      const essays = await page.locator('article.essay').count();
      assert.ok(essays >= 5 && essays <= 8);
      assert.equal(await page.locator('.scene .fiction').count(), essays);
      assert.equal(await page.locator('.limits').count(), essays);
      // Every scene drawing has a text alternative; every evidence link lands on a note.
      for (const label of await page.locator('.scene svg').evaluateAll(n => n.map(s => s.getAttribute('aria-label') || ''))) {
        assert.ok(label.startsWith('Imagined scene:'));
      }
      const broken = await page.evaluate(() => [...document.querySelectorAll('a[href^="#"]')]
        .map(a => a.getAttribute('href').slice(1)).filter(id => !document.getElementById(id)));
      assert.deepEqual(broken, []);
      // Keyboard: the skip link is first, visible on focus, and moves to the essays.
      await page.keyboard.press('Tab');
      assert.equal(await page.evaluate(() => document.activeElement.className), 'skip');
      assert.ok((await page.locator('.skip').boundingBox()).y >= 0);
      await page.keyboard.press('Enter');
      await page.waitForURL(/#essays$/);
      // Reading order: a contents link brings its essay heading into view; a note link reaches its note.
      await page.locator('.toc a[href="#climate"]').click();
      const box = await page.locator('#climate-title').boundingBox();
      assert.ok(box && box.y >= -1 && box.y < height, `${name}: climate heading not in view`);
      await page.locator('#climate sup.cite a').first().click();
      await page.waitForURL(/#climate-n1$/);
      assert.ok(await page.locator('#climate-n1').isVisible());
      // The chart has a table view that opens from the keyboard.
      await page.locator('#dividend-chart summary').focus();
      await page.keyboard.press('Enter');
      assert.ok(await page.locator('#dividend-chart table').isVisible());
      assert.equal(await page.locator('#dividend-chart tbody tr').count(), 11);
      // Readable type at phone width.
      const size = await page.locator('.prose p').first().evaluate(p => parseFloat(getComputedStyle(p).fontSize));
      assert.ok(size >= 16, `${name}: body text ${size}px`);
      assert.deepEqual(errors, []);
      await page.goto(url);
      await page.screenshot({path: path.join(shots, `${name}-top.png`)});
      await page.screenshot({path: path.join(shots, `${name}-full.png`), fullPage: true});
      await page.close();
    }
    console.log('Story page browser checks passed at 320, 390, 768 and 1440 px; captures in build/story-review/');
  } finally {
    await browser.close();
  }
})().catch(e => { console.error(e); process.exit(1); });

// Optional browser QA: requires Playwright and Chromium, never contacts remote sources.
const {chromium} = require('playwright');
const assert = require('node:assert/strict');
const path = require('node:path');
const fs = require('node:fs');
const root = path.resolve(__dirname, '../../..');
const url = 'http://127.0.0.1:8765/index.html';
const shots = path.join(root, 'build/public-product-review');
(async () => {
  fs.mkdirSync(shots, {recursive:true});
  const browser = await chromium.launch({headless:true, executablePath:process.env.PUBLIC_PRODUCT_BROWSER || '/usr/bin/chromium', args:['--no-sandbox']});
  try {
    const page = await browser.newPage({viewport:{width:1440,height:1000}});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.route('https://**', route => route.abort());
    await page.goto(url);
    assert.equal(await page.locator('.chapter:visible').count(), 1);
    for (const id of ['home','care','climate','work','commons','connections']) {
      await page.locator(`.map-legend [data-stop="${id}"]`).click();
      assert.equal(await page.locator('.chapter:visible').getAttribute('id'), id);
      assert.equal(await page.evaluate(()=>document.activeElement.id), `title-${id}`);
      await page.locator(`#${id} summary`).click();
      assert.ok(await page.locator(`#${id} .sources`).isVisible());
    }
    await page.goBack();
    assert.equal(await page.locator('.chapter:visible').getAttribute('id'), 'commons');
    await page.goto(url+'#climate');
    assert.equal(await page.locator('.chapter:visible').getAttribute('id'), 'climate');
    await page.locator('.map-legend [data-stop="home"]').focus();
    await page.keyboard.press('Enter');
    assert.equal(await page.locator('.chapter:visible').getAttribute('id'), 'home');
    if (await page.locator('#home details').getAttribute('open') !== null) await page.locator('#home summary').click();
    await page.locator('#home summary').focus();
    await page.keyboard.press('Enter');
    assert.ok(await page.locator('#home table').isVisible());
    assert.match(await page.locator('#home table').innerText(), /8\.73%/);
    await page.locator('#home summary').click();
    await page.goto(url);
    await page.screenshot({path:path.join(shots,'desktop.png'),fullPage:true});
    for (const width of [320,390,768]) {
      await page.setViewportSize({width,height:844});
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth <= innerWidth), `overflow at ${width}`);
      await page.locator('.map-legend [data-stop="climate"]').click();
      const bounds = await page.locator('#title-climate').boundingBox();
      assert.ok(bounds && bounds.y >= -1 && bounds.y < 844, `focused chapter outside viewport at ${width}`);
      await page.locator('.map-legend [data-stop="home"]').click();
    }
    await page.setViewportSize({width:390,height:844});
    await page.goto(url);
    await page.screenshot({path:path.join(shots,'mobile.png'),fullPage:true});
    await page.emulateMedia({reducedMotion:'reduce'});
    await page.locator('.map-legend [data-stop="work"]').click();
    assert.ok(await page.locator('#work').isVisible());
    await page.goto(url.replace('index.html','directions.html'));
    assert.equal(await page.locator('.direction').count(),3);
    await page.setViewportSize({width:1200,height:1000});
    await page.screenshot({path:path.join(shots,'directions.png'),fullPage:true});
    const noJS = await browser.newContext({javaScriptEnabled:false});
    const fallback = await noJS.newPage();
    await fallback.goto(url);
    assert.equal(await fallback.locator('.chapter:visible').count(), 6);
    await noJS.close();
    assert.deepEqual(errors, []);
    console.log('PASS: 6 places, evidence, keyboard/focus, history, deep link, 320/390/768px reflow, reduced motion, no-JS and 3 direction mockups');
    console.log('Screenshots: '+shots);
  } finally {await browser.close();}
})().catch(error => {console.error(error); process.exit(1);});

// Role: runs sync.js against a stand-in for the Figma plugin API, so the script is checked before it spends a real MCP call.
// Usage: node models/tools/public-product/design/figma/test_sync.js  (exits 1 on failure)
const fs = require('fs'), path = require('path'), assert = require('assert');
const code = fs.readFileSync(path.join(__dirname, 'sync.js'), 'utf8');
const made = [], removed = [];
const node = (name, w, h, ch = []) => ({ name, width: w, height: h, type: 'FRAME', children: ch, appendChild(c) { this.children.push(c); }, findOne(f) { return this.children.find(f); } });
const frames = {}, sections = { '7:2': { name: 'A' }, '7:3': { name: 'B' }, '7:4': { name: 'C' } };
for (const [id, nm, w, h] of [['5:616', 'C · Scene 3 clinic · phone 390', 390, 380], ['5:683', 'C · Scene 3 clinic · desktop 1440', 720, 980], ['5:770', 'C · Scene 6 apartment · phone 390', 390, 380], ['5:836', 'C · Scene 6 apartment · desktop 1440', 720, 980]]) {
  const clock = { type: 'TEXT', remove() { throw new Error('clock removed'); } };
  const old = { type: 'RECTANGLE', remove() { removed.push(id); } };
  const pic = node('Illustration · old', w, h, [clock, old]); pic.id = id + '-pic';
  frames[id] = node(nm, w, h, [pic]);
}
const figma = {
  loadFontAsync: async () => {}, setCurrentPageAsync: async () => {},
  getNodeByIdAsync: async id => frames[id] || sections[id] || { name: 'page' },
  createNodeFromSvg: s => { assert(s.startsWith('<svg') && s.endsWith('</svg>'), 'bad SVG'); assert(!/red.?cross/i.test(s)); made.push(s); return {}; },
};
const run = new (Object.getPrototypeOf(async function () {}).constructor)('figma', code);
run(figma).then(out => {
  assert.strictEqual(out.length, 4); assert.strictEqual(made.length, 4); assert.strictEqual(removed.length, 4);
  assert(made[0].includes('#2A9D8F') && made[0].includes('width="390"'), 'clinic phone picture');
  assert.strictEqual(sections['7:4'].name, 'C · Flat graphic (working direction)');
  console.log('sync.js OK:', out.map(o => o.slice(0, 1).concat(o.slice(2)).join(' ')).join('; '));
}).catch(e => { console.error('FAIL', e.message); process.exit(1); });

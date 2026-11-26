// Role: writes the cast sheet and the two scene pictures for direction C as SVG (stage H step H9).
// Usage: node models/tools/public-product/design/people/build_people.js  (writes cast.svg, scene-clinic.svg, scene-home.svg here)
// Status: draft placeholders, November 26, 2026. Each scene shows one household, from H8's day.json (#509):
// scene 3 is Jordan's urgent care visit, scene 6 is Eli's room in Carol and Dev's house.
const fs = require('fs'), path = require('path');
const { person, CAST, SCALE } = require('./people.js');
const INK = '#14213D';
const inner = s => s.replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '');
function place(p, cx, foot, h) {
  const hh = h * SCALE(p), ww = hh * 120 / 250;
  return `<g transform="translate(${(cx - ww / 2).toFixed(1)} ${(foot - hh).toFixed(1)}) scale(${(hh / 250).toFixed(4)})">${inner(person(p))}</g>`;
}
const R = (x, y, w, h, f, st = true) => `<rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${w.toFixed(1)}" height="${h.toFixed(1)}" fill="${f}"${st ? ` stroke="${INK}" stroke-width="3"` : ''}/>`;
const C = (x, y, r, f) => `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${r.toFixed(1)}" fill="${f}" stroke="${INK}" stroke-width="3"/>`;

function scene(which, W, H) {
  const h = (W < 500 ? 0.5 : 0.4) * H, foot = 0.94 * H;
  let s = '';
  if (which === 'clinic') {
    // Jordan's urgent care visit (day.json, jordan / clinic): he holds out a bandaged hand to a nurse; his hard hat on the chair.
    s += R(0, 0, W, H, '#FFC93C', false) + R(-3, H * 0.8, W + 6, H * 0.2 + 3, '#FFF8E6');
    s += R(W * 0.06, H * 0.1, W * 0.3, H * 0.26, '#FFF8E6');                       // window
    s += R(W * 0.72, H * 0.06, W * 0.12, W * 0.12, '#FFF8E6')                       // plus sign
      + R(W * 0.775, H * 0.06 + W * 0.02, W * 0.01, W * 0.08, '#B5371B', false)
      + R(W * 0.74, H * 0.06 + W * 0.055, W * 0.08, W * 0.01, '#B5371B', false);
    s += R(W * 0.04, H * 0.62, W * 0.2, H * 0.03, '#B5371B') + R(W * 0.05, H * 0.65, W * 0.02, H * 0.15, INK, false) + R(W * 0.21, H * 0.65, W * 0.02, H * 0.15, INK, false); // chair
    s += `<path d="M${W * 0.09} ${H * 0.62} Q${W * 0.09} ${H * 0.55} ${W * 0.14} ${H * 0.55} Q${W * 0.19} ${H * 0.55} ${W * 0.19} ${H * 0.62} Z" fill="#FFC93C" stroke="${INK}" stroke-width="3"/>`; // hard hat on the chair
    const jordan = { ...CAST.jordan, hardhat: false, toolbelt: false, reach: true, bandage: true };
    s += place(jordan, W * 0.44, foot, h) + place(CAST.nurse, W * 0.7, foot, h);
  } else {
    // Eli's room in his parents' house (day.json, carol-dev / home): a single bed, a toolbox, a calendar with circled
    // dates, an apartment listing on the desk. Eli at the desk; Carol and Dev at the door.
    s += R(0, 0, W, H, '#FFE9A8', false) + R(-3, H * 0.8, W + 6, H * 0.2 + 3, '#FFF8E6');
    s += R(W * 0.02, H * 0.66, W * 0.26, H * 0.08, '#2A9D8F') + R(W * 0.02, H * 0.6, W * 0.07, H * 0.06, '#FFF8E6') + R(W * 0.02, H * 0.74, W * 0.02, H * 0.06, INK, false); // bed
    s += R(W * 0.34, H * 0.12, W * 0.18, H * 0.16, '#FFF8E6');                      // calendar
    for (let r = 0; r < 3; r++) for (let c = 0; c < 4; c++) {
      const x = W * 0.36 + c * W * 0.035, y = H * 0.15 + r * H * 0.04;
      s += R(x, y, W * 0.025, H * 0.025, '#FFE9A8', false);
      if ((r * 4 + c) % 5 === 1) s += C(x + W * 0.0125, y + H * 0.0125, W * 0.016, 'none');
    }
    s += R(W * 0.3, H * 0.6, W * 0.24, H * 0.03, '#8A5A3C') + R(W * 0.31, H * 0.63, W * 0.02, H * 0.17, INK, false) + R(W * 0.51, H * 0.63, W * 0.02, H * 0.17, INK, false); // desk
    s += R(W * 0.42, H * 0.565, W * 0.08, H * 0.035, '#FFF8E6');                    // the printed listing
    s += R(W * 0.32, H * 0.555, W * 0.08, H * 0.045, '#B5371B');                    // toolbox
    s += R(W * 0.66, H * 0.22, W * 0.32, H * 0.58, '#FFF8E6');                      // doorway
    s += place(CAST.eli, W * 0.42, foot, h) + place(CAST.carol, W * 0.7, foot, h) + place(CAST.dev, W * 0.86, foot, h);
  }
  const title = which === 'clinic' ? "Placeholder: Jordan's urgent care visit, scene 3 (direction C)" : "Placeholder: Eli's room in Carol and Dev's house, scene 6 (direction C)";
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img"><title>${title}</title>${s}</svg>`;
}

// The cast sheet: one row, grouped by family, every figure at the same scale.
const groups = [['Jordan', ['jordan', 'dani']], ['Maya and Sam', ['maya', 'sam', 'theo', 'nora', 'hector', 'lupe']], ['Carol and Dev', ['carol', 'dev', 'eli']], ['Supporting', ['nurse']]];
const col = 170, gap = 40, top = 70, foot = 420, h = 340;
let x = 30, cast = '';
for (const [label, keys] of groups) {
  cast += `<text x="${x + 10}" y="${top - 26}" font-family="Space Grotesk, sans-serif" font-size="18" font-weight="700" fill="${INK}">${label}</text>`;
  for (const k of keys) {
    const p = CAST[k], cx = x + col / 2;
    cast += place(p, cx, foot, h);
    cast += `<text x="${cx}" y="${foot + 30}" font-family="Space Grotesk, sans-serif" font-size="14" font-weight="700" text-anchor="middle" fill="${INK}">${p.name}</text>`;
    cast += `<text x="${cx}" y="${foot + 48}" font-family="Space Grotesk, sans-serif" font-size="12" text-anchor="middle" fill="${INK}">${p.role}</text>`;
    x += col;
  }
  x += gap;
}
const CW = x;
const out = {
  'cast.svg': `<svg xmlns="http://www.w3.org/2000/svg" width="${CW}" height="500" viewBox="0 0 ${CW} 500" role="img"><title>The cast, placeholders (direction C), from H8's day.json</title><rect width="100%" height="100%" fill="#FFF8E6"/>${cast}</svg>`,
  'scene-clinic.svg': scene('clinic', 720, 980),
  'scene-home.svg': scene('home', 720, 980),
};
for (const [f, c] of Object.entries(out)) fs.writeFileSync(path.join(__dirname, f), c + '\n');
console.log(Object.keys(out).join(' '), CW);

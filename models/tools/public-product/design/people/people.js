// Role: placeholder people for direction C (flat graphic), stage H step H9. Each person is a flat SVG figure:
// head, hair, neck, torso with shoulders, arms with hands, trousers, a skirt or a dress, shoes, and a simple face.
// Adults, children and a newborn have their own proportions: a child's head is about a quarter of their height,
// an adult's about a sixth, and a newborn is a swaddled bundle. The cast and their jobs follow H8's day.json (#509).
// Status: draft placeholders for layout, November 26, 2026. The final art follows briefs.md, not these shapes.
// Every figure is drawn in a 120 x 250 box with the feet at y=244; the scenes scale children down by age.
const INK = '#14213D';

// Vertical layout per build. Adult: head 1/6.5 of height. Child (about 4): head about 1/4.4, shorter legs.
const BUILD = {
  adult: { headCy: 40, headR: 19, neckTop: 56, neckBot: 76, torsoTop: 74, armTop: 82, hand: 150, legTop: 146, shoulder: 24, waist: 19, hip: 20 },
  child: { headCy: 33, headR: 27, neckTop: 56, neckBot: 70, torsoTop: 68, armTop: 76, hand: 140, legTop: 158, shoulder: 21, waist: 19, hip: 18 },
};

function person(p) {
  if (p.kind === 'baby') return baby(p);
  const g = BUILD[p.kind === 'child' ? 'child' : 'adult'];
  const w = p.w || 1, cx = 60, sw = 2.5, foot = 244;
  const S = `stroke="${INK}" stroke-width="${sw}" stroke-linejoin="round" stroke-linecap="round"`;
  const skin = p.skin, top = p.top, bot = p.bottom || '#3D4A66', hair = p.hair || '#2B1B14';
  const shoulder = g.shoulder * w, waist = g.waist * w, hip = g.hip * w, legTop = g.legTop;
  const hand = p.armsUp ? g.armTop + 40 : g.hand;
  let o = '';

  // lower body
  if (p.lower === 'skirt' || p.lower === 'dress') {
    const sc = p.lower === 'dress' ? top : bot, hem = legTop + (foot - legTop) * 0.45;
    o += `<rect x="${cx - 12}" y="${hem - 6}" width="8" height="${foot - hem}" fill="${skin}" ${S}/>`;
    o += `<rect x="${cx + 4}" y="${hem - 6}" width="8" height="${foot - hem}" fill="${skin}" ${S}/>`;
    o += `<path d="M${cx - hip + 1} ${legTop - 6} L${cx + hip - 1} ${legTop - 6} L${cx + hip + 9} ${hem} L${cx - hip - 9} ${hem} Z" fill="${sc}" ${S}/>`;
  } else {
    o += `<path d="M${cx - hip} ${legTop - 6} L${cx - 1} ${legTop - 6} L${cx - 2} ${foot - 4} L${cx - hip + 2} ${foot - 4} Z" fill="${bot}" ${S}/>`;
    o += `<path d="M${cx + 1} ${legTop - 6} L${cx + hip} ${legTop - 6} L${cx + hip - 2} ${foot - 4} L${cx + 2} ${foot - 4} Z" fill="${bot}" ${S}/>`;
  }
  o += `<path d="M${cx - hip} ${foot - 6} h${hip - 2} v6 h-${hip + 4} q0 -6 6 -6 Z" fill="${p.shoes || INK}" ${S}/>`;
  o += `<path d="M${cx + 2} ${foot - 6} h${hip - 2} q6 0 6 6 h-${hip + 4} Z" fill="${p.shoes || INK}" ${S}/>`;

  // arms
  const sleeveColor = p.sleeve || top;
  const sleeve = p.shortSleeve ? g.armTop + (hand - g.armTop) * 0.4 : hand - 6;
  for (const s of [-1, 1]) {
    const x0 = cx + s * (shoulder - 5), x1 = cx + s * (shoulder + 5 + (p.armsUp ? -2 : 0));
    if (p.reach && s === 1) continue; // drawn later, held out in front
    const xs = x0 + (sleeve - g.armTop) * ((x1 - x0) / (hand - g.armTop));
    o += `<path d="M${x0 - 4} ${g.armTop} L${x0 + 4} ${g.armTop} L${x1 + 4 * s} ${hand} L${x1 - 4 * s} ${hand} Z" fill="${skin}" ${S}/>`;
    o += `<path d="M${x0 - 5} ${g.armTop - 2} L${x0 + 5} ${g.armTop - 2} L${xs + 5} ${sleeve} L${xs - 5} ${sleeve} Z" fill="${sleeveColor}" ${S}/>`;
    const bandaged = p.bandage && s === 1 && !p.reach;
    o += `<circle cx="${x1}" cy="${hand + 2}" r="5.5" fill="${bandaged ? '#FFFFFF' : skin}" ${S}/>`;
  }

  // torso
  const tb = p.lower === 'dress' ? legTop + 2 : legTop - 4, t0 = g.torsoTop;
  o += `<path d="M${cx - shoulder} ${t0 + 18} Q${cx - shoulder} ${t0 + 2} ${cx - 10} ${t0} L${cx + 10} ${t0} Q${cx + shoulder} ${t0 + 2} ${cx + shoulder} ${t0 + 18} L${cx + waist} ${tb} L${cx - waist} ${tb} Z" fill="${top}" ${S}/>`;
  // open layers over the torso: a work jacket, a cardigan, a coverall bib or a safety vest
  const panels = (fill, low) => `<path d="M${cx - shoulder - 1} ${t0 + 18} Q${cx - shoulder - 1} ${t0 + 1} ${cx - 10} ${t0 - 1} L${cx - 5} ${t0 - 1} L${cx - 5} ${low} L${cx - waist - 2} ${low} Z M${cx + shoulder + 1} ${t0 + 18} Q${cx + shoulder + 1} ${t0 + 1} ${cx + 10} ${t0 - 1} L${cx + 5} ${t0 - 1} L${cx + 5} ${low} L${cx + waist + 2} ${low} Z" fill="${fill}" ${S}/>`;
  if (p.jacket) o += panels(p.jacket, tb);
  if (p.cardigan) o += panels(p.cardigan, tb + 8);
  if (p.vest) o += panels(p.vest, tb - 6) + `<path d="M${cx - shoulder + 2} ${t0 + 40} h${shoulder - 7} M${cx + 5} ${t0 + 40} h${shoulder - 7}" stroke="#FFF8E6" stroke-width="4"/>`;
  if (p.coverall) o += `<rect x="${cx + 4}" y="${t0 + 22}" width="12" height="9" fill="#FFF8E6" ${S}/>`;
  if (p.lanyard) o += `<path d="M${cx - 8} ${t0} L${cx} ${t0 + 34} L${cx + 8} ${t0}" fill="none" stroke="#B5371B" stroke-width="2"/><rect x="${cx - 6}" y="${t0 + 32}" width="12" height="15" fill="#FFF8E6" ${S}/>`;
  if (p.toolbelt) o += `<rect x="${cx - waist - 2}" y="${tb - 10}" width="${2 * waist + 4}" height="8" fill="#8A5A3C" ${S}/><rect x="${cx - waist - 6}" y="${tb - 4}" width="12" height="16" fill="#8A5A3C" ${S}/><rect x="${cx + waist - 6}" y="${tb - 4}" width="12" height="16" fill="#8A5A3C" ${S}/>`;
  if (p.stethoscope) o += `<path d="M${cx - 8} ${t0 + 4} Q${cx - 14} ${t0 + 36} ${cx} ${t0 + 38} Q${cx + 12} ${t0 + 36} ${cx + 8} ${t0 + 4}" fill="none" ${S}/><circle cx="${cx}" cy="${t0 + 40}" r="3.5" fill="#B5371B" ${S}/>`;

  if (p.reach) { // the right arm held out, as when showing a hand to a nurse
    const x0 = cx + shoulder - 6, y0 = g.armTop + 2, x1 = cx + shoulder + 34, y1 = g.armTop + 30;
    o += `<path d="M${x0} ${y0 - 6} L${x1} ${y1 - 5} L${x1} ${y1 + 5} L${x0 - 2} ${y0 + 8} Z" fill="${skin}" ${S}/>`;
    o += `<path d="M${x0} ${y0 - 7} L${x0 + 16} ${y0 + 3} L${x0 + 14} ${y0 + 15} L${x0 - 3} ${y0 + 9} Z" fill="${sleeveColor}" ${S}/>`;
    o += `<circle cx="${x1 + 2}" cy="${y1}" r="6" fill="${p.bandage ? '#FFFFFF' : skin}" ${S}/>`;
  }
  // neck, then head, hair and face drawn at adult size and scaled to the build's head
  o += `<rect x="${cx - 6}" y="${g.neckTop}" width="12" height="${g.neckBot - g.neckTop}" fill="${skin}" ${S}/>`;
  const k = g.headR / 19, Sh = `stroke="${INK}" stroke-width="${(sw / k).toFixed(2)}" stroke-linejoin="round" stroke-linecap="round"`;
  let back = '', head = '';
  const hs = p.hairStyle || 'short';
  if (hs === 'long') back += `<path d="M41 40 Q40 18 60 18 Q80 18 79 40 L81 80 L39 80 Z" fill="${hair}" ${Sh}/>`;
  if (hs === 'afro') back += `<circle cx="60" cy="36" r="25" fill="${hair}" ${Sh}/>`;
  if (hs === 'bun') back += `<circle cx="60" cy="15" r="9" fill="${hair}" ${Sh}/>`;
  if (hs === 'pony') back += `<path d="M74 30 Q92 40 84 66 Q78 50 72 42 Z" fill="${hair}" ${Sh}/>`;
  head += `<circle cx="60" cy="40" r="19" fill="${skin}" ${Sh}/>`;
  if (hs === 'short' || hs === 'pony' || hs === 'bun') head += `<path d="M41 40 Q40 19 60 19 Q80 19 79 40 Q72 28 58 29 Q48 30 41 40 Z" fill="${hair}" ${Sh}/>`;
  if (hs === 'long') head += `<path d="M41 42 Q40 19 60 19 Q80 19 79 42 Q66 26 41 42 Z" fill="${hair}" ${Sh}/>`;
  if (hs === 'crop') head += `<path d="M42 34 Q60 14 78 34 Q60 26 42 34 Z" fill="${hair}" ${Sh}/>`;
  if (hs === 'bald') head += `<path d="M41 44 Q40 32 46 28 L47 42 Z M79 44 Q80 32 74 28 L73 42 Z" fill="${hair}" ${Sh}/>`;
  if (hs === 'afro') head += `<path d="M41 38 Q60 22 79 38 Q70 28 60 29 Q50 28 41 38 Z" fill="${hair}" ${Sh}/>`;
  if (p.beard) head += `<path d="M43 44 Q46 62 60 62 Q74 62 77 44 Q68 52 60 52 Q52 52 43 44 Z" fill="${hair}" ${Sh}/>`;
  if (p.mustache) head += `<path d="M52 49 Q60 45 68 49 Q60 52 52 49 Z" fill="${hair}" ${Sh}/>`;
  head += `<circle cx="53" cy="42" r="1.9" fill="${INK}"/><circle cx="67" cy="42" r="1.9" fill="${INK}"/>`;
  head += `<path d="M55 ${p.mustache ? 54 : 50} Q60 ${p.mustache ? 57 : 54} 65 ${p.mustache ? 54 : 50}" fill="none" stroke="${INK}" stroke-width="${(2 / k).toFixed(2)}" stroke-linecap="round"/>`;
  if (p.glasses) head += `<circle cx="53" cy="42" r="5.5" fill="none" ${Sh}/><circle cx="67" cy="42" r="5.5" fill="none" ${Sh}/><path d="M58.5 42 h3" ${Sh}/>`;
  if (p.hardhat) head += `<path d="M39 30 Q40 12 60 12 Q80 12 81 30 Z" fill="#FFC93C" ${Sh}/><rect x="35" y="28" width="50" height="5" fill="#FFC93C" ${Sh}/>`;
  const placed = `<g transform="translate(${cx} ${g.headCy}) scale(${k.toFixed(4)}) translate(-60 -40)">`;

  let props = '';
  if (p.holding === 'baby') props += bundle(cx - 4, g.armTop + 34, 1);
  if (p.cane) props += `<path d="M${cx - shoulder - 10} ${hand + 2} L${cx - shoulder - 14} ${foot}" fill="none" stroke="${INK}" stroke-width="4" stroke-linecap="round"/>`;
  if (p.mug) props += `<rect x="${cx + shoulder + 1}" y="${hand - 6}" width="11" height="13" fill="#FFF8E6" ${S}/>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="120" height="250" viewBox="0 0 120 250">${placed}${back}</g>${o}${placed}${head}</g>${props}</svg>`;
}

// A newborn in a swaddle: a blanket shape with a small head, drawn at (x, y) at scale k.
function bundle(x, y, k) {
  const S = `stroke="${INK}" stroke-width="${(2.5 / k).toFixed(2)}" stroke-linejoin="round"`;
  return `<g transform="translate(${x} ${y}) scale(${k})"><path d="M-24 2 Q-24 -12 -4 -12 L20 -10 Q28 -6 26 4 Q24 14 4 14 L-14 14 Q-24 12 -24 2 Z" fill="#FFE9A8" ${S}/><circle cx="-18" cy="-4" r="9" fill="#B07A52" ${S}/><path d="M-26 -8 Q-18 -16 -10 -8" fill="none" ${S}/><circle cx="-21" cy="-4" r="1.2" fill="${INK}"/><circle cx="-15" cy="-4" r="1.2" fill="${INK}"/></g>`;
}
function baby() {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="120" height="250" viewBox="0 0 120 250">${bundle(66, 222, 1.7)}</svg>`;
}

// The cast, from day.json's people (#509). Ages are placeholders for drawing; H8 gives the jobs and relations.
const CAST = {
  jordan: { name: 'Jordan', role: 'apprentice electrician', family: 'jordan', skin: '#A8714D', hair: '#1E1410', hairStyle: 'crop', top: '#FF8A6B', bottom: '#3D4A66', w: 0.95, shortSleeve: true, hardhat: true, toolbelt: true },
  dani: { name: 'Dani', role: "Jordan's roommate", family: 'jordan', skin: '#C98E5E', hair: '#1E1410', hairStyle: 'long', top: '#6B4E9B', bottom: '#14213D', w: 0.9 },
  maya: { name: 'Maya', role: 'dental hygienist, on leave', family: 'maya-sam', skin: '#E0B08A', hair: '#5A2E1A', hairStyle: 'pony', top: '#B5371B', bottom: '#14213D', w: 1.05, armsUp: true, holding: 'baby' },
  sam: { name: 'Sam', role: 'shift lead, distribution center', family: 'maya-sam', skin: '#6B4430', hair: '#1E1410', hairStyle: 'short', beard: true, top: '#3D4A66', bottom: '#2A9D8F', w: 1.35, vest: '#FFC93C' },
  theo: { name: 'Theo', role: 'their son, in pre-K', family: 'maya-sam', kind: 'child', age: 4, skin: '#9C6A48', hair: '#1E1410', hairStyle: 'afro', top: '#FFC93C', bottom: '#2A9D8F', w: 1.0, shortSleeve: true },
  nora: { name: 'Nora', role: 'their newborn', family: 'maya-sam', kind: 'baby', age: 0 },
  hector: { name: 'Hector', role: "Sam's father, retired", family: 'maya-sam', skin: '#7A4E36', hair: '#D9D9D9', hairStyle: 'bald', mustache: true, top: '#FFF8E6', bottom: '#8A5A3C', w: 1.1, glasses: true, mug: true },
  lupe: { name: 'Lupe', role: "Sam's mother", family: 'maya-sam', skin: '#7A4E36', hair: '#D9D9D9', hairStyle: 'bun', top: '#FFF8E6', cardigan: '#6B4E9B', lower: 'skirt', bottom: '#3D4A66', w: 1.25, cane: true },
  carol: { name: 'Carol', role: 'school office manager', family: 'carol-dev', skin: '#F0C9A8', hair: '#B8B8B8', hairStyle: 'short', top: '#FF8A6B', lower: 'skirt', bottom: '#14213D', w: 1.4, glasses: true, lanyard: true },
  dev: { name: 'Dev', role: 'bus mechanic', family: 'carol-dev', skin: '#B07A52', hair: '#4A4A4A', hairStyle: 'bald', beard: true, top: '#3D4A66', bottom: '#3D4A66', w: 1.15, coverall: true },
  eli: { name: 'Eli', role: 'their son', family: 'carol-dev', skin: '#F0C9A8', hair: '#C27A3A', hairStyle: 'short', top: '#FFF8E6', jacket: '#B5371B', bottom: '#14213D', w: 0.85 },
  nurse: { name: 'The nurse', role: 'not a family member', family: null, skin: '#4E3324', hair: '#1E1410', hairStyle: 'bun', top: '#2A9D8F', bottom: '#2A9D8F', w: 1.0, stethoscope: true, shortSleeve: true },
};

// Height of a figure relative to an adult's, for placing it in a scene.
const SCALE = p => (p.kind === 'baby' ? 1 : p.kind === 'child' ? 0.6 : 1);

if (typeof module !== 'undefined') module.exports = { person, CAST, SCALE };

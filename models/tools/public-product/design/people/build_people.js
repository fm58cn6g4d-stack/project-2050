// Role: writes the cast sheet and the two scene pictures for direction C as SVG (stage H step H9).
// Usage: node models/tools/public-product/design/people/build_people.js  (writes cast.svg, scene-clinic.svg, scene-home.svg here)
const fs=require('fs'), path=require('path');
const {person,CAST}=require('./people.js');
const INK='#14213D';
const inner=s=>s.replace(/^<svg[^>]*>/,'').replace(/<\/svg>$/,'');
function place(key,cx,foot,h){ const p=CAST[key]; const sc=p.small?0.5:p.child?0.68:1; const hh=h*sc, ww=hh*120/250;
  return `<g transform="translate(${(cx-ww/2).toFixed(1)} ${(foot-hh).toFixed(1)}) scale(${(hh/250).toFixed(4)})">${inner(person(p))}</g>`; }
const R=(x,y,w,h,f,st=true)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${f}"${st?` stroke="${INK}" stroke-width="3"`:''}/>`;
function scene(which,W,H){ const h=(W<500?0.5:0.4)*H, foot=0.94*H; let s='';
  if(which==='clinic'){ s+=R(0,0,W,H,'#FFC93C',false)+R(-3,H*0.8,W+6,H*0.2+3,'#FFF8E6')+R(W*0.42,H*0.08,W*0.24,H*0.24,'#FFF8E6')+R(W*0.74,H*0.16,W*0.2,H*0.64,'#B5371B')+R(W*0.03,H*0.68,W*0.4,H*0.035,INK,false);
    s+=[['grandma',0.1],['maya',0.24],['son',0.36],['jordan',0.56],['doctor',0.82]].map(([k,x])=>place(k,x*W,foot,h)).join(''); }
  else { s+=R(0,0,W,H,'#FFE9A8',false)+R(-3,H*0.8,W+6,H*0.2+3,'#FFF8E6')+R(W*0.56,H*0.07,W*0.36,H*0.3,'#FFF8E6')+R(W*0.02,H*0.66,W*0.12,H*0.14,'#FF8A6B')+R(W*0.05,H*0.56,W*0.1,H*0.1,'#FF8A6B');
    s+=[['grandpa',0.12],['sam',0.27],['daughter',0.38],['eli',0.52],['carol',0.69],['dev',0.86]].map(([k,x])=>place(k,x*W,foot,h)).join(''); }
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img"><title>Placeholder: ${which==='clinic'?'the clinic, 9:00 am':'the apartment, 2:00 pm'} (direction C)</title>${s}</svg>`; }
const keys=Object.keys(CAST); let cast=''; keys.forEach((k,i)=>{ cast+=place(k,40+i*150+75,420,340)+`<text x="${40+i*150+75}" y="450" font-family="Space Grotesk, sans-serif" font-size="13" text-anchor="middle" fill="${INK}">${CAST[k].name.split(' (')[0]}</text>`; });
const out={ 'cast.svg':`<svg xmlns="http://www.w3.org/2000/svg" width="${keys.length*150+80}" height="480" viewBox="0 0 ${keys.length*150+80} 480" role="img"><title>The cast, placeholders (direction C)</title><rect width="100%" height="100%" fill="#FFF8E6"/>${cast}</svg>`,
 'scene-clinic.svg':scene('clinic',720,980), 'scene-home.svg':scene('home',720,980) };
for(const [f,c] of Object.entries(out)) fs.writeFileSync(path.join(__dirname,f),c+'\n');
console.log(Object.keys(out).join(' '));

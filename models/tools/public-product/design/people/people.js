// Role: placeholder people for direction C (flat graphic), stage H step H9. Each person is a flat SVG figure:
// head, hair, neck, torso with shoulders, arms with hands, trousers, a skirt or a dress, shoes, and a simple face.
// Status: draft placeholders for layout, November 25, 2026. The final art follows briefs.md, not these shapes.
// Flat graphic person, viewBox 0 0 120 250 (feet at y=246). Navy line, flat fills.
const INK='#14213D';
function person(p){
  const w=p.w||1, cx=60, sw=2.5;
  const S=`stroke="${INK}" stroke-width="${sw}" stroke-linejoin="round" stroke-linecap="round"`;
  const skin=p.skin, top=p.top, bot=p.bottom||'#3D4A66';
  const shoulder=24*w, waist=19*w, hip=20*w;
  let back='', front='', o='';
  // hair behind head
  const hair=p.hair||'#2B1B14';
  if(p.hairStyle==='long') back+=`<path d="M${cx-19} 40 Q${cx-20} 18 ${cx} 18 Q${cx+20} 18 ${cx+19} 40 L${cx+21} 80 L${cx-21} 80 Z" fill="${hair}" ${S}/>`;
  if(p.hairStyle==='afro') back+=`<circle cx="${cx}" cy="36" r="25" fill="${hair}" ${S}/>`;
  if(p.hairStyle==='bun') back+=`<circle cx="${cx}" cy="15" r="9" fill="${hair}" ${S}/>`;
  if(p.hairStyle==='pony') back+=`<path d="M${cx+14} 30 Q${cx+32} 40 ${cx+24} 66 Q${cx+18} 50 ${cx+12} 42 Z" fill="${hair}" ${S}/>`;
  // legs / lower body
  const legTop=146, foot=244;
  if(p.lower==='skirt'||p.lower==='dress'){
    const sc=p.lower==='dress'?top:bot;
    o+=`<rect x="${cx-12}" y="${legTop+40}" width="8" height="${foot-legTop-44}" fill="${skin}" ${S}/>`;
    o+=`<rect x="${cx+4}" y="${legTop+40}" width="8" height="${foot-legTop-44}" fill="${skin}" ${S}/>`;
    o+=`<path d="M${cx-hip+1} ${legTop-6} L${cx+hip-1} ${legTop-6} L${cx+hip+9} ${legTop+46} L${cx-hip-9} ${legTop+46} Z" fill="${sc}" ${S}/>`;
  } else {
    const lw=Math.max(12,13*w);
    o+=`<path d="M${cx-hip} ${legTop-6} L${cx-1} ${legTop-6} L${cx-2} ${foot-4} L${cx-hip+2} ${foot-4} Z" fill="${bot}" ${S}/>`;
    o+=`<path d="M${cx+1} ${legTop-6} L${cx+hip} ${legTop-6} L${cx+hip-2} ${foot-4} L${cx+2} ${foot-4} Z" fill="${bot}" ${S}/>`;
  }
  // shoes
  o+=`<path d="M${cx-hip+0} ${foot-6} h${hip-2} v6 h-${hip+4} q0 -6 6 -6 Z" fill="${p.shoes||INK}" ${S}/>`;
  o+=`<path d="M${cx+2} ${foot-6} h${hip-2} q6 0 6 6 h-${hip+4} Z" fill="${p.shoes||INK}" ${S}/>`;
  // arms (behind torso edges)
  const armTop=82, hand=p.armsUp?120:150;
  const sleeve=p.shortSleeve?108:hand-6;
  for(const s of [-1,1]){
    const x0=cx+s*(shoulder-5), x1=cx+s*(shoulder+5+(p.armsUp?-10:0));
    o+=`<path d="M${x0-4} ${armTop} L${x0+4} ${armTop} L${x1+4*s} ${hand} L${x1-4*s} ${hand} Z" fill="${skin}" ${S}/>`;
    o+=`<path d="M${x0-5} ${armTop-2} L${x0+5} ${armTop-2} L${x0+s*(sleeve-armTop)*((x1-x0)/(hand-armTop))*s+5} ${sleeve} L${x0+s*(sleeve-armTop)*((x1-x0)/(hand-armTop))*s-5} ${sleeve} Z" fill="${top}" ${S}/>`;
    o+=`<circle cx="${x1}" cy="${hand+2}" r="5.5" fill="${skin}" ${S}/>`;
  }
  // torso with shoulders
  const tb=p.lower==='dress'?legTop+2:legTop-4;
  o+=`<path d="M${cx-shoulder} 92 Q${cx-shoulder} 76 ${cx-10} 74 L${cx+10} 74 Q${cx+shoulder} 76 ${cx+shoulder} 92 L${cx+waist} ${tb} L${cx-waist} ${tb} Z" fill="${top}" ${S}/>`;
  if(p.coat) o+=`<path d="M${cx-shoulder-1} 92 Q${cx-shoulder-1} 75 ${cx-10} 73 L${cx-4} 73 L${cx-4} 190 L${cx-hip-6} 190 Z M${cx+shoulder+1} 92 Q${cx+shoulder+1} 75 ${cx+10} 73 L${cx+4} 73 L${cx+4} 190 L${cx+hip+6} 190 Z" fill="#FFFFFF" ${S}/>`;
  if(p.apron) o+=`<path d="M${cx-12*w} 96 L${cx+12*w} 96 L${cx+15*w} 158 L${cx-15*w} 158 Z" fill="#FFFFFF" ${S}/><path d="M${cx-12*w} 96 L${cx-8} 76 M${cx+12*w} 96 L${cx+8} 76" fill="none" ${S}/>`;
  if(p.coat) o+=`<path d="M${cx-8} 78 Q${cx-14} 110 ${cx} 112 Q${cx+12} 110 ${cx+8} 78" fill="none" ${S}/><circle cx="${cx}" cy="114" r="3.5" fill="#B5371B" ${S}/>`;
  // neck + head
  o+=`<rect x="${cx-6}" y="58" width="12" height="18" fill="${skin}" ${S}/>`;
  o+=`<circle cx="${cx}" cy="40" r="19" fill="${skin}" ${S}/>`;
  // hair on top
  const hs=p.hairStyle||'short';
  if(hs==='short'||hs==='pony'||hs==='bun') front+=`<path d="M${cx-19} 40 Q${cx-20} 19 ${cx} 19 Q${cx+20} 19 ${cx+19} 40 Q${cx+12} 28 ${cx-2} 29 Q${cx-12} 30 ${cx-19} 40 Z" fill="${hair}" ${S}/>`;
  if(hs==='long') front+=`<path d="M${cx-19} 42 Q${cx-20} 19 ${cx} 19 Q${cx+20} 19 ${cx+19} 42 Q${cx+6} 26 ${cx-19} 42 Z" fill="${hair}" ${S}/>`;
  if(hs==='crop') front+=`<path d="M${cx-18} 34 Q${cx} 14 ${cx+18} 34 Q${cx} 26 ${cx-18} 34 Z" fill="${hair}" ${S}/>`;
  if(hs==='bald') front+=`<path d="M${cx-19} 44 Q${cx-20} 32 ${cx-14} 28 L${cx-13} 42 Z M${cx+19} 44 Q${cx+20} 32 ${cx+14} 28 L${cx+13} 42 Z" fill="${hair}" ${S}/>`;
  if(hs==='afro') front+=`<path d="M${cx-19} 38 Q${cx} 22 ${cx+19} 38 Q${cx+10} 28 ${cx} 29 Q${cx-10} 28 ${cx-19} 38 Z" fill="${hair}" ${S}/>`;
  if(p.beard) front+=`<path d="M${cx-17} 44 Q${cx-14} 62 ${cx} 62 Q${cx+14} 62 ${cx+17} 44 Q${cx+8} 52 ${cx} 52 Q${cx-8} 52 ${cx-17} 44 Z" fill="${hair}" ${S}/>`;
  // face
  front+=`<circle cx="${cx-7}" cy="42" r="1.9" fill="${INK}"/><circle cx="${cx+7}" cy="42" r="1.9" fill="${INK}"/>`;
  front+=`<path d="M${cx-5} 50 Q${cx} 54 ${cx+5} 50" fill="none" stroke="${INK}" stroke-width="2" stroke-linecap="round"/>`;
  if(p.glasses) front+=`<circle cx="${cx-7}" cy="42" r="5.5" fill="none" ${S}/><circle cx="${cx+7}" cy="42" r="5.5" fill="none" ${S}/><path d="M${cx-1.5} 42 h3" ${S}/>`;
  // props
  let props='';
  if(p.keys) props+=`<circle cx="${cx+shoulder+6}" cy="${(p.armsUp?120:150)+12}" r="5" fill="#FFC93C" ${S}/><path d="M${cx+shoulder+6} ${(p.armsUp?120:150)+17} v10" ${S}/>`;
  if(p.box) props+=`<rect x="${cx-30}" y="96" width="60" height="42" fill="#FF8A6B" ${S}/><path d="M${cx-30} 110 h60" ${S}/>`;
  if(p.cane) props+=`<path d="M${cx-shoulder-10} 152 L${cx-shoulder-14} ${foot}" fill="none" stroke="${INK}" stroke-width="4" stroke-linecap="round"/>`;
  if(p.card) props+=`<rect x="${cx+shoulder}" y="${(p.armsUp?120:150)-14}" width="18" height="24" fill="#FFF8E6" ${S}/>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="120" height="250" viewBox="0 0 120 250">${back}${o}${front}${props}</svg>`;
}
const CAST={
 jordan:{name:'Jordan, 26 (on his own)',skin:'#A8714D',hair:'#1E1410',hairStyle:'crop',top:'#2A9D8F',bottom:'#3D4A66',w:0.95,apron:true,shortSleeve:true},
 maya:{name:'Maya, 34',skin:'#E0B08A',hair:'#5A2E1A',hairStyle:'pony',top:'#B5371B',bottom:'#14213D',w:1.0},
 sam:{name:'Sam, 36',skin:'#6B4430',hair:'#1E1410',hairStyle:'short',beard:true,top:'#FFC93C',bottom:'#2A9D8F',w:1.35,shortSleeve:true},
 son:{name:'Leo, 8 (Maya and Sam\'s son)',skin:'#9C6A48',hair:'#1E1410',hairStyle:'afro',top:'#FF8A6B',bottom:'#3D4A66',w:0.95,child:true,shortSleeve:true},
 daughter:{name:'Ana, 4 (their daughter)',skin:'#9C6A48',hair:'#2B1B14',hairStyle:'bun',top:'#2A9D8F',lower:'dress',w:0.95,child:true,small:true,shortSleeve:true},
 grandma:{name:'Grace, 71 (Sam\'s mother)',skin:'#5A3A28',hair:'#D9D9D9',hairStyle:'afro',top:'#6B4E9B',lower:'skirt',bottom:'#3D4A66',w:1.3,glasses:true,cane:true},
 grandpa:{name:'Walter, 74 (Sam\'s father)',skin:'#5A3A28',hair:'#D9D9D9',hairStyle:'bald',top:'#FFF8E6',bottom:'#8A5A3C',w:1.05,glasses:true},
 carol:{name:'Carol, 63',skin:'#F0C9A8',hair:'#B8B8B8',hairStyle:'short',top:'#FF8A6B',lower:'skirt',bottom:'#14213D',w:1.4,glasses:true},
 dev:{name:'Dev, 64',skin:'#B07A52',hair:'#4A4A4A',hairStyle:'bald',beard:true,top:'#3D4A66',bottom:'#8A5A3C',w:1.15,box:true,armsUp:true},
 eli:{name:'Eli, 31 (Carol and Dev\'s son)',skin:'#F0C9A8',hair:'#C27A3A',hairStyle:'short',top:'#FFFFFF',bottom:'#14213D',w:0.85,keys:true,armsUp:false},
 doctor:{name:'The clinic doctor (not a family member)',skin:'#4E3324',hair:'#1E1410',hairStyle:'long',top:'#2A9D8F',bottom:'#14213D',w:1.0,coat:true}
};
if(typeof module!=='undefined') module.exports={person,CAST};

const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(()=>chromium.launch());
const html='<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'+require('fs').readFileSync('index.html','utf8')+'</body></html>';
for(const [w,n,scheme] of [[1280,'desk','light'],[400,'phone','dark']]){const p=await b.newPage({viewport:{width:w,height:900},colorScheme:scheme});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.setContent(html);await p.waitForTimeout(3000);console.log(n,'errors',errs,'scrollW',await p.evaluate(()=>document.documentElement.scrollWidth));await p.screenshot({path:n+'.png',fullPage:true});}
await b.close()})();

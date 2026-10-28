import subprocess
n=subprocess.check_output(['node','-e',"console.log(Object.keys(require('./model.js').RANGES).length)"]).decode().strip()
head='<title>Carbon Dividend Model</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500&family=IBM+Plex+Mono:wght@400;500&display=swap">\n'
b=open('body.part').read()
open('index.html','w').write(head+open('css.part').read()+"\n"+b.replace("37 inputs",n+" inputs")+"\n<script>\n"+open('model.js').read()+"\n"+open('hh.js').read()+"\nconst CEX="+open('cex.json').read()+";\n</script>\n<script>\n"+open('ui.part').read()+"\n</script>\n")

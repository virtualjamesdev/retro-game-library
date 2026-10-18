# Builds the lite app's index.html from the main app: loads Neutralino's scripts directly.
import sys,re
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read()
start=s.index('<script>\n/* Lite desktop app (Neutralino): load its client library')
end=s.index('</script>',start)+len('</script>')
s=s[:start]+'<script src="/js/neutralino.js"></script>'+s[end:]
open(dst,'w').write(s)
print('lite index written')

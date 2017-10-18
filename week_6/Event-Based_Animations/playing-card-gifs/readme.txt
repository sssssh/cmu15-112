png images from:  http://www.jfitz.com/cards/
converted to gif format using “sips” command in OS X:
   for i in *.png; do sips -s format gif "${i}" --out “${i%png}gif”; done
also renamed files and deleted a few others
naming: <suit><rank>, extra suit == “x”,x1=blank, x2=joker1, x3=joker2

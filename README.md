# 🏔️ Summit Read Me

This is a simple Python app that uses Tessreact from Google for optical character recognition (OCR) to read and summarize a set of images.

## Mac Instructions

1. First, clone the Summit git repo:
   ```
   git clone https://github.com/scidsg/summit.git && cd summit
   ```

2. Add the images you want to summarize in the `images/` folder.

3. Then, run the script:
   ```
   chmod +x summit.sh && ./summit.sh
   ```

## Example Output

The app will include a summary file with a list of the top 10 words across all images, their counts, and the files from which they were found. Individual text files are saved for corresponding images with the words they contain, making search easy. When running the commands above, you should see an output similar to this:

```
glennsorrentino@m1 summit % chmod +x summit.sh && ./summit.sh
 ______     __  __     __    __     __    __     __     ______
/\  ___\   /\ \/\ \   /\ "-./  \   /\ "-./  \   /\ \   /\__  _\
\ \___  \  \ \ \_\ \  \ \ \-./\ \  \ \ \-./\ \  \ \ \  \/_/\ \/
 \/\_____\  \ \_____\  \ \_\ \ \_\  \ \_\ \ \_\  \ \_\    \ \_\
  \/_____/   \/_____/   \/_/  \/_/   \/_/  \/_/   \/_/     \/_/

🏔️ Summit is an OCR application to extract and summarize text from a set of images.

A free and open-source tool by Science & Design, Inc. - https://scidsg.org
🧑‍💻 Creating a virtual environment...
🎬 Activating the virtual environment...
📋 Installing required packages from requirements.txt...
Requirement already satisfied: pillow in /Users/glennsorrentino/Nextcloud/Git/read/venv/lib/python3.12/site-packages (from -r requirements.txt (line 1)) (10.3.0)
Requirement already satisfied: pytesseract in /Users/glennsorrentino/Nextcloud/Git/read/venv/lib/python3.12/site-packages (from -r requirements.txt (line 2)) (0.3.10)
Requirement already satisfied: packaging>=21.3 in /Users/glennsorrentino/Nextcloud/Git/read/venv/lib/python3.12/site-packages (from pytesseract->-r requirements.txt (line 2)) (24.0)
🚀 Summiting...
✅ Text from IMG_9673.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_9673.jpeg.txt
✅ Text from IMG_0405.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_0405.jpeg.txt
✅ Text from tesla.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/tesla.jpeg.txt
✅ Text from IMG_0265.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_0265.jpeg.txt
✅ Text from IMG_0227.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_0227.jpeg.txt
✅ Text from IMG_9666.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_9666.jpeg.txt
✅ Text from IMG_0368.jpeg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/IMG_0368.jpeg.txt
✅ Text from image.jpg has been saved to /Users/glennsorrentino/Nextcloud/Git/summit/text/image.jpg.txt
👍 Summary written to /Users/glennsorrentino/Nextcloud/Git/summit/text/📝 Summary.txt.
🏁 Script completed successfully.
glennsorrentino@m1 summit %
```

### Summary File

```
Top 10 words across all files:
[v]: 10
  Files: image.jpg
to: 9
  Files: IMG_0227.jpeg, IMG_0368.jpeg, IMG_9673.jpeg, image.jpg
haus: 8
  Files: image.jpg
+add: 7
  Files: image.jpg
and: 7
  Files: IMG_0368.jpeg, IMG_9673.jpeg, image.jpg
of: 7
  Files: IMG_0227.jpeg, IMG_0368.jpeg, IMG_9673.jpeg, image.jpg
@: 6
  Files: IMG_0227.jpeg, IMG_0265.jpeg, IMG_0368.jpeg, image.jpg, tesla.jpeg
a: 6
  Files: IMG_0368.jpeg, IMG_9673.jpeg, image.jpg
fries: 6
  Files: image.jpg
10: 5
  Files: IMG_0368.jpeg, image.jpg

Summary for IMG_9673.jpeg:
to: 3
this: 2
2: 1
a: 1
acknowledge: 1
and: 1
and/or: 1
andi: 1
aspirationel: 1
committed: 1
content,: 1
conversation: 1
create: 1
creating: 1
depictions: 1
fam: 1
future: 1
harméul: 1
impact,: 1
in: 1
includes: 1
inclusive: 1
inspirational: 1
is: 1
it: 1
its: 1
lean: 1
mistreatment: 1
more: 1
negative: 1
of: 1
or: 1
people: 1
program: 1
remove: 1
spark: 1
staries: 1
start: 1
storlesmatver: 1
togather.: 1
video: 1
want: 1
we: 1
will: 1
with: 1
your: 1

Summary for IMG_0405.jpeg:

Summary for tesla.jpeg:
mode: 2
service: 2
(: 1
.: 1
0): 1
=: 1
@: 1
[2: 1
additional: 1
agent: 1
alerts: 1
atom: 1
cneck: 1
computer: 1
driver: 1
ervice: 1
exit: 1
full: 1
gs.: 1
info: 1
intel: 1
jeven: 1
nifotaminacnt: 1
notes: 1
oa: 1
rein: 1
reinstall: 1
release: 1
resources: 1
s: 1
self-driving: 1
serice: 1
settengs: 1
software: 1
syjzeieb7lf735594: 1
vehicle: 1
y: 1
yobage: 1
{3}: 1

Summary for IMG_0265.jpeg:
di: 2
e: 2
lee: 2
micah: 2
-4: 1
6h: 1
@: 1
acquisire,: 1
analizzare: 1
dati: 1
diffondere: 1
documenti: 1
fughe: 1
hacking,: 1
rivelazionis: 1
uarte: 1

Summary for IMG_0227.jpeg:
5g}: 1
7:59: 1
=: 1
@: 1
ae: 1
awe: 1
beta.hushline.app: 1
eaten,: 1
ee: 1
eee: 1
here...: 1
hush: 1
i: 1
line: 1
menu: 1
messages: 1
no: 1
nothing: 1
of: 1
oll: 1
pays: 1
policy: 1
privacy: 1
private: 1
pu: 1
rowe: 1
see: 1
service: 1
sn: 1
terms: 1
to: 1
yet.: 1
|: 1
¢y: 1
—: 1
“295: 1

Summary for IMG_9666.jpeg:

Summary for IMG_0368.jpeg:
a: 4
the: 4
and: 3
for: 3
with: 3
10: 2
@: 2
action: 2
ago: 2
code: 2
hours: 2
in: 2
is: 2
it: 2
its: 2
of: 2
on: 2
r1: 2
rabbit: 2
release: 2
source: 2
spade: 2
they: 2
to: 2
"large: 1
(3: 1
1]: 1
[part: 1
about: 1
ap: 1
app-based: 1
apps:: 1
artificial: 1
ask: 1
automation: 1
background,: 1
been: 1
behalf: 1
blatant: 1
but: 1
call: 1
can: 1
claiming: 1
clear: 1
device,: 1
do: 1
doordash,: 1
ec: 1
even: 1
expose: 1
first: 1
four: 1
from: 1
github.com: 1
has: 1
highly: 1
intelligence: 1
interactions.: 1
it's: 1
job: 1
large: 1
let's: 1
liberate: 1
lie.: 1
making: 1
midjourney,: 1
model: 1
model".: 1
no: 1
only: 1
or: 1
painfully: 1
partial: 1
perform: 1
playwright: 1
publicized: 1
q]: 1
rabbit.tech: 1
rabbitscam: 1
readme: 1
readme.md: 1
reality,: 1
relying: 1
ro): 1
scripts: 1
several: 1
sight.: 1
simply: 1
so-called: 1
spotify,: 1
srera=sterrrrerprsstaat: 1
support: 1
tasks: 1
technical: 1
that: 1
there's: 1
they're: 1
this: 1
those: 1
ubereats.: 1
waves: 1
we're: 1
what's: 1
which: 1
why: 1
you: 1
you,: 1
your: 1
—: 1

Summary for image.jpg:
[v]: 10
haus: 8
+add: 7
fries: 6
&: 4
16.: 4
5.: 4
chicken: 4
pretzel: 4
10: 3
10.: 3
12.: 3
9.: 3
and: 3
cabbage: 3
cheese,: 3
fort: 3
lemon: 3
mustard: 3
of: 3
salad: 3
sauce,: 3
schnitzel: 3
smoked: 3
to: 3
toast: 3
trout: 3
we: 3
15.: 2
18.: 2
22.: 2
8.: 2
aioli: 2
all: 2
alpine: 2
bacon: 2
black: 2
bratwurst: 2
bun,: 2
cream,: 2
creamy: 2
eggs,: 2
farm: 2
food: 2
fried: 2
garlic: 2
lettuce,: 2
mashed: 2
mo: 2
mushroom: 2
no: 2
o8: 2
onions,: 2
pork: 2
potato: 2
roasted: 2
route: 2
sauce: 2
shaved: 2
slaw,: 2
sosse,: 2
spatzle: 2
star: 2
two: 2
vinaigrette: 2
(00d: 1
([v]: 1
(oled: 1
(served: 1
*: 1
+: 1
11.: 1
13.: 1
14.: 1
17.: 1
1d: 1
20.: 1
2018: 1
21+: 1
21.: 1
23.: 1
24.: 1
25.: 1
250: 1
29.: 1
4: 1
4.: 1
46%: 1
7.: 1
@: 1
a: 1
abe: 1
absolutelt: 1
adold: 1
age: 1
agt: 1
alaskan: 1
alcorol: 1
aleppo: 1
amo: 1
antome: 1
any: 1
aod: 1
apple: 1
arore: 1
arugula,: 1
ase: 1
asespatzle: 1
ass!: 1
august: 1
auth:: 1
autp: 1
baby: 1
bacon-potato: 1
ball: 1
bavarian: 1
baw: 1
be: 1
beavice: 1
beef: 1
beer: 1
beer-battered: 1
beet: 1
beet-cured: 1
berries,: 1
bf: 1
bia: 1
biersauce: 1
bless: 1
blumenkohl: 1
borne: 1
braised: 1
bratwurst,: 1
bread: 1
breaded: 1
breakfast*: 1
brisket: 1
broth,: 1
brunch: 1
brussels: 1
buttermilk-brined: 1
buttermilk-dill: 1
caramelized: 1
cauliflower,: 1
cheese: 1
cherry: 1
citrus,: 1
classic: 1
classical: 1
cod,: 1
come: 1
confit: 1
consuming: 1
copfricht: 1
cream: 1
creme: 1
croutons,: 1
crumbs: 1
cucumber,: 1
cured: 1
curry-ketchup: 1
currywurst: 1
de: 1
dep:: 1
deviled: 1
deyerace: 1
doner: 1
dumpling: 1
egg: 1
eggs: 1
eggs*: 1
emcouraged: 1
enforce: 1
est,: 1
fear.: 1
fennel: 1
fennel,: 1
fillet: 1
fingerling: 1
fischbrotchen: 1
fischteller: 1
fish: 1
fish,: 1
fish-plate,: 1
fondue,: 1
foote,: 1
for: 1
forest: 1
fou: 1
fraiche,: 1
french: 1
german: 1
gerosteter: 1
ghellfish: 1
goat: 1
god: 1
greens,: 1
grilled: 1
grone: 1
ground: 1
grune: 1
gruyere: 1
gurkensalat: 1
ham,: 1
have: 1
herb: 1
herbs: 1
herbs,: 1
horseradish: 1
hot: 1
human: 1
illness,: 1
ime: 1
imfaince: 1
important: 1
in: 1
increase: 1
inside: 1
jagerschnitzel: 1
jus,: 1
k: 1
kate: 1
kebab: 1
levain: 1
lies,: 1
lies.: 1
llaciamet: 1
logs: 1
loin,: 1
love: 1
mackerel: 1
madhaus: 1
maple: 1
may: 1
meats,: 1
menu: 1
mes: 1
mie: 1
migats: 1
might: 1
mixed: 1
mstblcteo: 1
muscheln: 1
mushrooms,: 1
mussels,: 1
mustard,: 1
noodles,: 1
note: 1
o'clock): 1
obatzda: 1
one: 1
onion,: 1
oth,: 1
ox: 1
pagpertt: 1
pan: 1
pancakes: 1
patties,: 1
pepper: 1
pets: 1
pickle: 1
pickled: 1
pita,: 1
plate: 1
please: 1
potato,: 1
potatoes: 1
potatoes,: 1
poultry,: 1
powdered: 1
preserved: 1
produces: 1
qeerhall: 1
radhaus: 1
radish,: 1
rchuel: 1
reaso®: 1
red: 1
remoulade,: 1
requests: 1
rights: 1
rillette,: 1
risk: 1
sacscryl: 1
sales: 1
salmon: 1
salmon,: 1
sandwich: 1
sandwich,: 1
sapett: 1
saturday: 1
sauerkraut: 1
sauerkraut,: 1
sausages: 1
scallion,: 1
seafood,: 1
seasonal: 1
secome: 1
served: 1
sh: 1
side: 1
sides: 1
smashburger*: 1
sotice: 1
sour: 1
specials: 1
sports.: 1
spread: 1
sprouts: 1
stand: 1
steamed: 1
sugar,: 1
summer: 1
sunday: 1
sunny: 1
surat.: 1
surcharc(: 1
sweet: 1
syrup: 1
ta: 1
tal: 1
tangy: 1
the: 1
thigh,: 1
tig: 1
tinned: 1
tm: 1
tocomsume: 1
today: 1
tomato,: 1
tomatoes,: 1
tour: 1
turkish: 1
tzatziki: 1
tzatziki,: 1
umder: 1
undee-cooked: 1
upon: 1
vinegar: 1
w/: 1
warning!: 1
wason.: 1
whipped: 1
whitefish,: 1
wo: 1
yogurt-dill: 1
‘radhaus: 1


```

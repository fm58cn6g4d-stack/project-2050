# A day in 2050: illustration briefs

Role: the art briefs for the front door (stage H step H9): the final-art brief for direction C, then one brief per scene. The scene briefs start from each family's `illustration` field in `models/tools/public-product/day/day.json` (H8, #509), which is the source; this file adds how direction C renders them and what to avoid. Status: **draft, November 26, 2026. Not published.** C (flat graphic) is the working direction: Espen said "I think bright and bold might be the way to go" (Espen, chat, November 25, 18:31 UTC). The earlier A and B rendering notes are in #505's version of this file.

Rules for every scene:
- The page labels every picture "imagined scene". The picture itself carries no words, except C's clock time, which is also in the text.
- No real people or likenesses, no real places a reader could identify, no party colors, flags, logos, slogans or campaign marks, and nothing that imitates an existing campaign's look.
- Cast the people as the composites they are: a range of ages, bodies, skin tones and abilities, ordinary clothes, no celebrities.
- Every picture needs alt text that says what happens in it, written with H8's copy, not as a caption of the art.
- **The three families (O1, `DEC-2026-11-25-23`):** the reader follows one of three families, and each scene has one picture per family that appears in it. The cast, their jobs and relations are H8's (`day.json`, `people`, #509); the final art draws them as the cast sheet does.

## The final art for direction C: characters and style

This brief is for the illustrator who replaces the placeholders. Espen's note on the first placeholders: "We're definitely going for stylized not anything like realistic but the shapes with the elongated half circle for their body makes them all look like they're wearing strange long robes" (Espen, chat, November 25, 18:31 UTC). The placeholders in `people/` and `screens/cast.png` show the proportions to start from, not the finished look.

- **Stylized, not realistic.** Flat color, no gradients or textures, a 2.5 to 3 px navy outline (`#14213D`, the C `line` token) at 1440 px, square ends on shapes, round joints. Faces are simple: dot eyes, a short smile line, glasses or a beard where the cast list says so. No photo references traced and no likeness of any real person.
- **Real bodies, not robes.** Every person has a distinct head, a neck, a torso with shoulders, two arms with hands, and two legs with shoes. Clothes follow the body and the job: tops, trousers, skirts, a hard hat and tool belt, a safety vest, a coverall, a work jacket, scrubs. Children are drawn with child proportions, not as shrunken adults: at four, Theo's head is about a quarter of his height (an adult's is about a sixth), with shorter legs and a rounder body. A newborn is a swaddled bundle in someone's arms.
- **Varied people.** A range of skin tones, hair (straight, curly, coiled, grey, bald, a bun, a ponytail), heights and body types, including heavier and thinner people, and older people who stand and move like older people (a cane for Lupe). Nobody is the default.
- **The cast (H8, `day.json`, #509; `screens/cast.png`):**
  - **Jordan:** a single man in his mid-twenties, an apprentice electrician who rents a room across town. Hard hat and tool belt at work, work clothes at the clinic. His roommate **Dani**, who was brought here as a child, takes her citizenship oath.
  - **Maya and Sam:** a couple in their thirties. Maya is a dental hygienist, home on leave with their newborn **Nora** (a swaddled bundle, never a small child); Sam is a shift lead at a distribution center (a safety vest at work). Their son **Theo** is four and in pre-K. Sam's parents live a few blocks away: **Hector**, retired, who came to the country as a young man, and **Lupe**, who has dementia (shown through the care she gets and her dignity, never as confusion played for effect).
  - **Carol and Dev:** a couple getting ready to retire. Carol is a school office manager, Dev a bus mechanic (a coverall). Their son **Eli**, in recovery from substance use, lives with them because he can't afford a place of his own (a work jacket).
  - **Supporting people** (the nurse, the pediatrician, the teacher, the home care aide, the crews, the candidate) are not family members and must not read as any real person.
- **Palette.** Only the C tokens: cream `#FFF8E6`, butter `#FFE9A8`, sun `#FFC93C`, navy `#14213D`, brick `#B5371B`, coral `#FF8A6B`, plus a teal `#2A9D8F` and a violet `#6B4E9B` for clothing, and skin and hair tones as needed. Walls and floors use the cream, butter and sun; navy is kept for outlines and the night scenes, so dark clothes don't vanish into a dark floor.
- **Composition.** People stand on a floor line at about 94% of the frame's height; the scene's main moment sits in the middle third so it survives the 390 px phone crop. No words in the picture except the clock time, which is decorative and repeated in the text.
- **Dark mode.** Each picture is delivered as SVG with its fills named after the tokens, so H10 can swap cream and butter for the dark `bg` and `surface` and keep the people's colors.
- **Deliverables.** One SVG per family moment in `day.json` at 1440 × 960 and a phone crop at 390 × 520, plus a character sheet (front view, each person at the same scale). Alt text comes from H8's copy, not from the illustrator.

## 1. A secure floor (`floor`)

- **Maya and Sam, 6:30 am, A kitchen: "The money comes on the first".** Early light in a small kitchen. A mother in a robe holds a newborn on her shoulder while checking a phone; a father pours cereal for a four-year-old still in pajamas.
- **Carol and Dev, 7:00 am, A kitchen: "Full benefits, on time".** A morning kitchen. A woman in reading glasses holds a printed statement; her husband reads over her shoulder; their grown son, in a work jacket, grabs a travel mug on his way out.

Direction C: Each family's statement or phone as a flat card with a check mark, the sun as a disc in the window. Calm, not celebration: the payment is routine.

## 2. Care: child care and pre-K (`childcare`)

- **Maya and Sam, 8:00 am, The pre-K classroom at the neighborhood school: "Pre-K, and a cap on what care costs".** A bright classroom of small tables. A father kneels to zip a little boy's jacket off; a teacher waves from a reading rug.

Direction C: The classroom tables as colored rectangles, the teacher and Theo as two figures meeting in the middle. Theo is drawn as a four-year-old, not a small adult.

## 3. Care: health (`clinic`)

- **Jordan, 12:30 pm, An urgent care clinic: "Stitches, and a small copay".** A bright clinic room. A young man in work clothes holds out a bandaged hand to a nurse; his hard hat sits on the chair beside him.
- **Maya and Sam, 9:30 am, The pediatrician's office: "A checkup with nothing to pay".** A pediatric exam room with a baby scale. A mother holds her newborn while a doctor listens with a stethoscope.
- **Carol and Dev, 9:00 am, A community clinic: "Treatment, covered like any other care".** A calm clinic waiting room with plants and a counselor's door ajar. A man in his thirties signs in at the desk; nobody asks for a card.

Direction C: No payment window, card reader or cashier's grille anywhere. Jordan's bandage as a white hand; Nora as a swaddled bundle; the counselor's door ajar as a block of light. No masks, gurneys or worry on faces.

## 4. Care: long-term care (`longterm`)

- **Maya and Sam, 10:30 am, Hector and Lupe's living room: "Help at home, savings intact".** A tidy living room with family photos. A home care aide helps an older woman with a cardigan; an older man sets out two cups of tea.
- **Carol and Dev, 10:30 am, The kitchen table: "Planning the trip".** A kitchen table covered in a map and travel brochures. An older couple point at a coastline, laughing.

Direction C: Dignity first: Lupe does most of the dressing with a hand from the aide, and Hector sets out the tea. For Carol and Dev, the map as a big flat shape with a coastline line.

## 5. Work (`work`)

- **Jordan, 6:45 am, A job site at the edge of town: "A trade, and a contract".** Early light over a fenced job site where a new battery building for the grid is going up. A young man in a hard hat and tool belt pulls cable with an older electrician; a union sticker on his lunch cooler.
- **Maya and Sam, 1:00 pm, A distribution center break room: "A raise that keeps up".** A break room with lockers and a vending machine. A man in a safety vest reads a pay stub; a union notice is pinned to the board behind him.

Direction C: The pay stub as a white card, the union notice as pinned squares with no readable words, no real union's name or colors. Jordan's hard hat and tool belt from the cast sheet.

## 6. Housing (`home`)

- **Jordan, 6:30 pm, A rented room in a shared apartment: "The rent is still the hard part".** A small bedroom in a shared apartment: a mattress, a desk with a laptop open to a budget, work boots by the door.
- **Carol and Dev, 2:00 pm, Eli's room: "A room at his parents', for now".** A spare bedroom in a family house, a little crowded: a single bed, a toolbox, a calendar with recovery meetings circled, an apartment listing printed on the desk.

Direction C: Jordan's room and Eli's room are small and a little crowded, not grim. The calendar's circled dates and the printed listing stay wordless. Eli's parents can stand at the door; the picture is about waiting, not about recovery.

## 7. Clean power (`power`)

- **Jordan, 4:00 pm, The job site, as a storm comes in: "Storm call".** Dark clouds roll over the job site. Workers lash down cable reels; a young man checks his phone, where a payment notice glows.
- **Maya and Sam, 4:00 pm, The front porch, as a storm comes in: "Storm season, dividend day".** A front porch with a stroller and a tricycle. A woman holding a baby watches dark clouds; a utility truck passes on the street.
- **Carol and Dev, 4:00 pm, The front porch, as a storm comes in: "Dividends with the check".** An older couple on a porch swing under a darkening sky, a dog at their feet, a tablet showing a deposit notice.

Direction C: The storm as one big navy cloud shape, porch lights and the deposit notice as the one yellow accent. No utility branding on the truck.

## 8. Immigration (`immigration`)

- **Jordan, 5:30 pm, The federal building: "Dani's oath".** A plain hearing room with flags. A young woman raises her right hand among a row of new citizens; a friend in work clothes holds up a phone to take her picture.
- **Maya and Sam, 11:00 am, Hector and Lupe's kitchen: "A photo on the fridge".** A refrigerator door covered in grandchildren's drawings and, in the middle, a framed photo of a man holding up a green card.

Direction C: A plain civic room, no seal or flag that imitates a real agency's. Hector's green-card photo on the fridge is a framed flat card among the children's drawings.

## 9. Democratic renewal (`democracy`)

- **Jordan, 7:30 pm, The public library: "Twenty-five dollars, matched".** A library meeting room with folding chairs. A candidate speaks at the front; a young man near the back holds a printed flyer.
- **Carol and Dev, 5:00 pm, On the phone: "Someone picks up".** A man on a landline in a hallway, a notepad in his hand, a Social Security envelope open on the side table.

Direction C: Folding chairs as repeated shapes. The candidate has no party, sign, pin or likeness to any real politician. The flyer and the envelope stay wordless.

## 10. Transportation (`transit`, optional scene, O2, `DEC-2026-11-25-24`)

- **Jordan, 10:15 pm, A night bus: "The route that survived".** The inside of a city bus at night, half full. A young man leans his head on the window; a repaired bridge passes outside, lit by new lamps.
- **Maya and Sam, 5:30 pm, The drive home: "Paying by the mile, without being tracked".** A small electric car at a stoplight in evening traffic, a car seat visible in the back; a dashboard odometer in close-up.

Direction C: The bus as a lit rectangle on a navy band, the repaired bridge as a clean arc, the car seat as a simple shape. No real transit agency's livery.

## 11. Fair financing (`money`, the page ends on the money, O3, `DEC-2026-11-25-25`)

- **Jordan, Night, Home: "What it costs, and who pays".** A phone screen in a dark room, showing a pay stub. The city lights beyond the window.
- **Maya and Sam, Night, The kitchen table: "What it costs, and who pays".** A kitchen table after the children are asleep: a laptop, a stack of bills, two mugs, a baby monitor.
- **Carol and Dev, Night, The living room: "What it costs, and who pays".** A living room lit by one lamp. An older couple on a couch with a notebook of figures; a third mug on the table for their son.

Direction C: The night scene: one lamp, a notebook or laptop, the mugs. Numbers belong to the text, never to the picture.

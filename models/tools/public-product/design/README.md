# A day in 2050: the visual design (H9)

Role: the front door's visual design (stage H step H9; `models/stage-h/1-audit.md`, part 3.1, row H9): a style frame, three directions (C is the working one), the exported design tokens, placeholder people and an illustration brief per scene. The content is H8's (`../day/`); the build is H10's. Status: **draft, November 25, 2026; revised the same evening for C, and on November 26 for H8's cast (#509). Nothing here is published, and nothing on the site changes.**

**Figma file:** "Project 2050: A day in 2050", https://www.figma.com/design/rOpzyCw7TQAz9a6B1As5AS (in Espen's drafts). **C redraw pending Espen's Figma approval:** the Figma file still shows the first placeholder people, the earlier cast names and the earlier labels. The current people are in `people/` and `screens/` here, and a later small push syncs the Figma file and its screenshots once Espen approves the write.

## Working direction: C, flat graphic

Espen, on the three directions: "I like the figma mockups a lot. Initially I was drawn to the A style, but C has really grown on me, and I think bright and bold might be the way to go. I know the pictures are placeholders but I do want the people to look better eventually. We're definitely going for stylized not anything like realistic but the shapes with the elongated half circle for their body makes them all look like they're wearing strange long robes hahaha" (Espen, chat, November 25, 18:31 UTC).

So C is the working direction, not yet a formal choice. **C. Flat graphic:** flat shapes, bold color blocks and a big clock time on every scene (Space Grotesk, Atkinson Hyperlegible). It is the clearest on a phone and the cheapest to make and keep, and it recolors for dark mode from the tokens. Its risk is reading like a campaign poster rather than a feature; the "imagined scene" tag, the plain copy and the absence of slogans keep it on the feature side.

- **Tokens.** C's values are now the top-level working set in `tokens.json` (`working_direction: "C"`). A and B stay in `tokens.json`, the Figma file and `screens/` as archived alternates:
  - **A. Warm editorial illustration** (archived): painted scenes in warm light, Fraunces and Source Serif 4.
  - **B. Documentary photo-real** (archived): staged photographs captioned "Imagined scene, staged", Literata.
- **People.** The first placeholders drew each person as a half circle on a long body. They are redrawn as stylized figures with heads, necks, shouldered torsos, arms, legs and clothes that fit their jobs, in varied ages, body types, skin tones and hair. The cast is H8's (`day.json`, #509): Jordan and his roommate Dani; Maya and Sam, their son Theo (four) and newborn Nora, and Sam's parents Hector and Lupe; Carol, Dev and their son Eli; and a nurse. Theo has a child's proportions (a bigger head and shorter legs, not a shrunken adult) and Nora is a swaddled bundle. Each scene picture shows one household: scene 3 is Jordan's urgent care visit, scene 6 is Eli's room in Carol and Dev's house (`people/`, `screens/cast.png`, `screens/scene-clinic.png`, `screens/scene-home.png`). They are still placeholders; the final art follows the C brief at the top of `briefs.md`.

The pictures in the frames are rough placeholders built from shapes, to show the layout, palette and mood. They are not the illustrations.

## Files

| File | Role |
| --- | --- |
| `tokens.json` | The tokens, exported from the Figma file's variables: the working set (C) at the top level, the shared type scale, the breakpoints, and for each direction its fonts, corner radii and light and dark colors |
| `check_tokens.py` | Checks every text and color pair in `tokens.json` against WCAG 2.2 AA; `--markdown` prints the table. Exits 1 on a failure |
| `frames.md` | Every frame in the Figma file, with a link to its node |
| `briefs.md` | The final-art brief for C (characters, cast and style), then one brief per scene, listing each family's moment from `day.json`'s `illustration` fields with how C renders it |
| `people/` | The placeholder people as SVG: `people.js` draws one person, `build_people.js` writes `cast.svg` and the two scene pictures (`node people/build_people.js`) |
| `figma/` | The Figma sync for C: a one-call `use_figma` script, its test, and one SVG per frame for placing by hand. It is waiting on the Starter plan's MCP quota (`figma/README.md`) |
| `screens/` | PNG exports: the style frame, each direction's four frames, the cast sheet and the two C scene pictures |

## What the design settles, whichever direction wins

- **One shared structure.** Top bar; the day as a strip of times; the family selector; the picture; the "Imagined scene" tag; time and place; the title; the flagship; the beats; "When it begins"; "The honest limit"; a button that opens the scene's detail. A direction changes the look, not the order.
- **The family selector (O1, `DEC-2026-11-25-23`).** "Whose day are you following?" with three choices. The chosen one carries a check mark and a heavier border, so it doesn't rely on color alone. On a phone the labels shorten to first names. The three families are H8's (`day.json`, #509): Jordan; Maya and Sam; Carol and Dev.
- **Type scale.** Display 64/68 desktop, 40/44 phone; heading 40/46 and 28/34; subhead 24/32 and 21/28; body 20/32 and 18/28; small 16/24 and 15/22; label 13/16. Body text never drops below 18 px on a phone.
- **"Imagined scene" on every scene.** A dark tag above the title, and in B also under every photograph.
- **Fonts.** All six are open-licence Google Fonts, so H10 can self-host them.
- **Transportation (O2, `DEC-2026-11-25-24`)** stays an optional scene; **the money (O3, `DEC-2026-11-25-25`)** closes the day. The scope is memo H4's option A (`DEC-2026-11-25-21`). Both have briefs; neither has a frame yet.

## Contrast (WCAG 2.2 AA)

`python3 models/tools/public-product/design/check_tokens.py` checks 80 pairs (ten per mode for the working set and for each direction): text, secondary text, links and accents on the background and on panels, the button label, the flagship label, the tag, and the focus ring at 3:1. All pass. In C, the working set, the lowest pair is 5.62:1 (the flagship label and the focus ring on the light background); body text is 15.08:1 light and at least 13:1 dark. The Figma style frame prints each ratio under its swatches. The line color is decorative and not held to a ratio. In C the placeholder's big clock is decorative, and the time also appears as text.

H10 still owes the checks a static palette can't do: text over the real illustrations (the design keeps text off pictures), focus order, screen readers and reduced motion.

## Notes for H10 and the next H9 pass

- **Figma plan limits.** The file is on Espen's Starter (free) plan: three pages at most, and one variable mode per collection. That is why the briefs share page 00 with the read-me, and why the cast sheet sits on the style-frame page. So light and dark are separate variables (`light/bg`, `dark/bg`, and so on) in one collection per direction, not two modes of one variable. If the plan changes, they can be folded into modes without changing `tokens.json`.
- **The variables are the source.** Frame fills and text colors are bound to the variables, so a color change in Figma carries to every frame. Re-export `tokens.json` after any change, then rerun `check_tokens.py`.
- **Next, once Espen confirms C:** C across all eleven scenes, the scene detail (opened), the money scene and the toolkit page, phone and desktop, in light and dark; then the illustrations to the briefs.
- **Eli's housing beat.** H7 (#508) found that Eli does not qualify for the rent awards' first stage; H8 rewrote the beat in #509 ("A room at his parents', for now"), and scene 6's picture now follows it: Eli's room in his parents' house, not a move-in.

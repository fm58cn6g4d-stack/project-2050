# A day in 2050: the visual design (H9)

Role: the front door's visual design proposal (stage H step H9; `models/stage-h/1-audit.md`, part 3.1, row H9): a style frame, three directions for Espen to choose from, the exported design tokens and an illustration brief per scene. The content is H8's (`../day/`); the build is H10's. Status: **draft proposal, November 25, 2026. Nothing here is published, and nothing on the site changes.**

**Figma file:** "Project 2050: A day in 2050", https://www.figma.com/design/rOpzyCw7TQAz9a6B1As5AS (in Espen's drafts).

## The question for Espen: which direction?

Each direction is shown on scene 3 (the clinic) and scene 6 (the apartment), at phone (390 px) and desktop (1440 px) width, with the family selector:

- **A. Warm editorial illustration.** Painted scenes in warm light that moves through the day, with a serif voice (Fraunces, Source Serif 4): a storybook for grown-ups, the most inviting of the three and the slowest to make, since it needs an illustrator for eleven paintings.
- **B. Documentary photo-real.** Wide photographs of ordinary places, staged with hired models and captioned "Imagined scene, staged", with a newspaper serif (Literata): the most concrete and credible-feeling, and the one that needs the most care so that no picture passes as a news photo.
- **C. Flat graphic.** Flat shapes, bold color blocks and a big clock time on every scene (Space Grotesk, Atkinson Hyperlegible): the clearest on a phone, the cheapest to make and keep, and it recolors for dark mode from the tokens. It is also the most poster-like, so it reads more like a campaign than a feature.

My recommendation is A for the front door: it suits a persuasive, optimistic story about ordinary people better than B's documentary realism, and it doesn't run B's risk of being mistaken for reporting. C is the better choice if speed and cost of production matter most.

The pictures in the frames are rough placeholders built from shapes, to show the layout, palette and mood of each direction. They are not the illustrations. The briefs say what the real ones should be.

## Files

| File | Role |
| --- | --- |
| `tokens.json` | The tokens, exported from the Figma file's variables: the shared type scale, the breakpoints, and for each direction its fonts, corner radii and light and dark colors |
| `check_tokens.py` | Checks every text and color pair in `tokens.json` against WCAG 2.2 AA; `--markdown` prints the table. Exits 1 on a failure |
| `frames.md` | Every frame in the Figma file, with a link to its node |
| `briefs.md` | One illustration brief per scene, from `day.json`'s `illustration` fields, with how each direction would render it |
| `screens/` | PNG exports: the style frame and each direction's four frames |

## What the design settles, whichever direction wins

- **One shared structure.** Top bar; the day as a strip of times; the family selector; the picture; the "Imagined scene" tag; time and place; the title; the flagship; the beats; "When it begins"; "The honest limit"; a button that opens the scene's detail. A direction changes the look, not the order.
- **The family selector (O1, `DEC-2026-11-25-23`).** "Whose day are you following?" with three choices. The chosen one carries a check mark and a heavier border, so it doesn't rely on color alone. On a phone the labels shorten to first names. The names in the frames (Jordan; Maya and Sam; Carol, Dev and Eli) are placeholders for H8.
- **Type scale.** Display 64/68 desktop, 40/44 phone; heading 40/46 and 28/34; subhead 24/32 and 21/28; body 20/32 and 18/28; small 16/24 and 15/22; label 13/16. Body text never drops below 18 px on a phone.
- **"Imagined scene" on every scene.** A dark tag above the title, and in B also under every photograph.
- **Fonts.** All six are open-licence Google Fonts, so H10 can self-host them.
- **Transportation (O2, `DEC-2026-11-25-24`)** stays an optional scene; **the money (O3, `DEC-2026-11-25-25`)** closes the day. The scope is memo H4's option A (`DEC-2026-11-25-21`). Both have briefs; neither has a frame yet.

## Contrast (WCAG 2.2 AA)

`python3 models/tools/public-product/design/check_tokens.py` checks 60 pairs (ten per direction and mode): text, secondary text, links and accents on the background and on panels, the button label, the flagship label, the tag, and the focus ring at 3:1. All pass. The lowest text pair is 5.62:1, and the focus rings are at least 5.6:1. The Figma style frame prints each ratio under its swatches. The line color is decorative and not held to a ratio. In C the placeholder's big clock is decorative, and the time also appears as text.

H10 still owes the checks a static palette can't do: text over the real illustrations (the design keeps text off pictures), focus order, screen readers and reduced motion.

## Notes for H10 and the next H9 pass

- **Figma plan limits.** The file is on Espen's Starter plan: three pages at most, and one variable mode per collection. So light and dark are separate variables (`light/bg`, `dark/bg`, and so on) in one collection per direction, not two modes of one variable. If the plan changes, they can be folded into modes without changing `tokens.json`.
- **The variables are the source.** Frame fills and text colors are bound to the variables, so a color change in Figma carries to every frame. Re-export `tokens.json` after any change, then rerun `check_tokens.py`.
- **Next, after Espen picks:** the chosen direction across all eleven scenes, the scene detail (opened), the money scene and the toolkit page, phone and desktop, in light and dark; then the illustrations to the briefs.
- **Check for H8:** scene 6 now follows the retired couple's son into a rent award. The awards go first to people with no home of their own, so H8 should confirm he fits before that pairing is used (`briefs.md`, scene 6).

# Figma sync for direction C

Role: brings the Figma file "Project 2050: A day in 2050" (https://www.figma.com/design/rOpzyCw7TQAz9a6B1As5AS) in line with the repository's direction C placeholders (stage H step H9). Status: **waiting, November 26, 2026.** The Figma Starter plan allows 20 MCP calls a month, and that quota is used up, so the sync has not run yet.

The pictures come from the same code as `../screens/`: `../people/people.js` and `../people/build_people.js`. Rebuild everything here with `node build_figma_sync.js`, then check the script with `node test_sync.js`.

## By hand (no MCP calls)

Open the Figma file, go to page "02 Directions", section C, and for each frame below:

1. Inside the frame, select the frame named "Illustration · …" and delete every layer in it except the clock text.
2. Drag the SVG file into that frame, set its position to 0, 0, and scale it to fill the frame. The desktop SVGs are 720 × 980; if the frame differs, scale with the aspect ratio locked.
3. Move the clock to the top of the layer list. Set it to navy `#14213D` and place it at the top left.

| Figma frame | Node | SVG |
| --- | --- | --- |
| C · Scene 3 clinic · phone 390 | `5:616` | `c-clinic-phone-390.svg` |
| C · Scene 3 clinic · desktop 1440 | `5:683` | `c-clinic-desktop-1440.svg` |
| C · Scene 6 apartment · phone 390 | `5:770` | `c-home-phone-390.svg` |
| C · Scene 6 apartment · desktop 1440 | `5:836` | `c-home-desktop-1440.svg` |

Optionally, rename the sections: "A · Warm editorial illustration (archived alternate)", "B · Documentary photo-real (archived alternate)" and "C · Flat graphic (working direction)".

## By MCP (one call)

When the quota allows, `sync.js` does all of the above in one `use_figma` call. It measures each frame, draws the picture at that size, keeps the clock and renames the sections. Afterwards, re-export `../screens/direction-c.png` and `../screens/style-frame.png`.

## Files

| File | Role |
| --- | --- |
| `build_figma_sync.js` | Writes `sync.js` and the four SVGs from `../people/` |
| `sync.js` | The generated `use_figma` script (do not edit by hand) |
| `test_sync.js` | Runs `sync.js` against a stand-in for the Figma API; exits 1 on failure |
| `c-*.svg` | One picture per C frame, named by scene and width |

---
name: vibecode-tells
description: Design guardrail and review checklist that keeps sites, landing pages, apps, and UI from looking "vibecoded" (generic AI-generated). Covers 30 tells such as harsh gradients, Lucide icons, Inter/Geist/Space Grotesk, liquid glass, radial orbs, bento grids, 3 feature cards, 3 pricing tiers, sparkle icons, emojis, em dashes, "it's not X, it's Y" copy, fake testimonials, and missing TOS/privacy pages. Use this skill whenever building or restyling any website, landing page, web app, HTML artifact, React/Vue component, dashboard, or marketing page, and whenever the user asks to review, audit, or critique a design, asks why something "looks AI-generated," "looks vibecoded," "looks like a template," or wants it to look custom, premium, or agency-built. Apply it while designing, not only after, even if the user never mentions vibecoding.
---

# Vibecode Tells

A site looks vibecoded when every visual and copy decision is the model's default. None of the 30 tells below is wrong in isolation; the problem is that they show up together, unchosen, on thousands of generated sites, so visitors pattern-match them to "nobody designed this." The fix is not to ban a list of things. The fix is to make deliberate choices that come from the brand, the product, and the audience, and to treat each tell as a default you must justify before using.

This skill runs in two modes. Use design mode whenever you are creating or restyling UI. Use review mode when asked to audit existing work, and also as a self-check at the end of design mode.

## Precedence

An explicit brand system beats this list. If a brand guide, design-system artifact, or user instruction specifies something on the list (say, a purple-and-black palette or Inter as the body face), follow it and do not argue. In review mode, note it as "brand-mandated" rather than a failure. The list governs defaults, not stated decisions.

## Design mode

Before writing any markup, settle these decisions in a few lines of reasoning, because every tell below is what happens when they are skipped:

1. Palette. Derive it from the brand or subject matter, not from "modern SaaS." One dominant neutral that is not pure white or pure black, one or two brand colors, and at most one accent. Name the reason for each color.
2. Type. Pick a display face and a text face with some character that fits the subject. Avoid Inter, Geist, and Space Grotesk unless mandated. System stacks, a serif, a humanist sans, a slab, or a mono used deliberately are all fine.
3. Surface language. Decide how elements separate from each other (hairline borders, tonal background shifts, spacing alone) instead of reaching for shadows, blur, and rounded cards everywhere.
4. Proof. Identify what real evidence exists: actual screenshots, real data, real customer names with permission, real numbers. Design around what exists. If nothing exists, leave the section out rather than invent it.
5. Copy voice. Write plainly and specifically. No em dashes, no "it's not X, it's Y" framing, no emoji as decoration.

Then build, and finish by running the review below on your own output. Fix any unjustified tell before presenting.

## The 30 tells and what to do instead

### Color
1. Harsh gradients. Saturated multi-hue gradients on backgrounds, buttons, or text. Instead use flat color, or a subtle same-hue tonal shift you could barely name.
3. Pure white background (#fff). Instead use a slightly tinted off-white or paper tone tied to the palette, or a genuinely dark or colored ground.
4. Rainbow coloring. Gradient text, multi-color headline words, a different color per card. Instead let one brand color carry emphasis.
20. Purple and black. The default "AI product" palette (violet/indigo accents on near-black). Instead choose a hue that belongs to this brand.
29. Neon colors. Fully saturated cyan, magenta, lime glows. Instead lower saturation and let contrast come from value, not chroma.
30. Basic pastel colors. Baby blue, blush pink, mint, butter yellow tiles. Instead use tints of the actual brand palette, with some warmth or grayness so they read as chosen.

### Type and copy
9. Em dashes. Use commas, periods, parentheses, or a spaced hyphen.
10. Inter, Geist, Space Grotesk. Choose type with a reason (see design mode step 2).
15. "It's not X, it's Y." Also "not just X, but Y," and struck-through "to-do list, second brain" reveals. State what the thing is and does, directly.
7. Emojis. No emoji as bullets, section markers, or headline garnish. Use them only where users themselves would (a chat product, a playful consumer brand that already uses them).

### Iconography
2. Lucide icons. The default React icon set is instantly recognizable. Prefer no icon where a word works, a custom or brand-specific SVG, or a less common set used sparingly and consistently.
16. Checkmark bullets. Green check lists for features. Use plain text, numbers, a short table, or real specifics that do not need decoration.
24. Sparkle icons. The universal "AI feature" glyph. Name the feature instead.
25. Animated arrows. Arrows that slide right on hover inside every CTA. A clear verb label is enough.

### Layout
6. Three feature cards in a row. Icon, title, two lines, times three. Instead show the product doing the thing, vary the rhythm, or use a single strong feature with depth.
13. Bento grids. Mixed-size rounded tiles as the default "features" section. Use them only when content genuinely has varied weight.
17. Three pricing tiers. Basic / Pro (Most popular) / Enterprise by reflex. Match the real pricing model; one price or two tiers is often more honest.
14. Terminal window. Fake macOS window chrome with traffic-light dots and a typing command. Show real output or real code only if the audience actually uses a terminal.
11. Colored left stripe. Thick colored border-left on callouts and cards. Use spacing, a label, or a background shift.

### Surface and effects
5. Drop shadows. Soft shadows on every card. Use borders or tonal layering; reserve elevation for things that actually float (menus, dialogs).
8. Liquid glass. Backdrop blur, frosted translucent panels. Use solid surfaces.
19. Soft corner radius. Large uniform radius (16px+) on everything. Pick a radius scale on purpose; small or zero radius often reads as more considered.
22. Radial orbs. Blurred glowing blobs behind the hero. Use a real image, a pattern tied to the brand, or nothing.
23. Dot grids. Dotted graph-paper backgrounds. Same as above.
28. Hover animations. Cards that lift, scale, or glow on hover by default. Keep hover states to clear, quick affordances (color or underline change) on things that are actually interactive.

### Trust and completeness
12. Fake testimonials. Invented names, stock avatars, "Sarah K., Founder." Use real quotes with permission, or omit the section. Never fabricate social proof.
18. No real product demos. Abstract illustrations instead of the product. Show real screenshots, a short recording, or a live interactive sample.
21. No skeleton loaders. Blank flashes or spinners while data loads. Add skeletons sized to the real content for any async region.
26. No TOS. Ship a Terms of Service page (or a clear placeholder route flagged to the user for legal review) and link it in the footer.
27. No privacy policy. Same, especially if the site has forms, analytics, or email capture.

For 26 and 27, do not draft binding legal text as if final. Create the pages and routes, fill with a clearly marked draft or placeholder, and tell the user they need review.

## Review mode

1. If there is a codebase or HTML file, run the scanner first for a fast, mechanical pass:
   `python scripts/scan.py <path-to-file-or-directory>`
   It flags code-level signals (gradients, lucide imports, font names, em dashes, emoji, backdrop blur, large radii, hover transforms, missing terms/privacy links, and more). It is heuristic: treat hits as leads, not verdicts, and expect false positives.
2. Then inspect visually or by reading the markup for the judgment calls a scanner cannot make: harsh vs. subtle gradients, whether cards are really a generic three-up, whether testimonials and demos are real, whether copy uses the "not X, it's Y" move.
3. Report in this format, most visible issues first:

   Verdict: one sentence on how vibecoded it reads overall and the two or three changes that would move it most.

   Then a table with columns: #, Tell, Status (Clear / Flag / Brand-mandated), Where (file:line or section), Fix.

   Only list tells that are Flag or Brand-mandated in the table; summarize the clear ones in one line.
4. When asked to fix, change the highest-impact tells first (palette, type, hero effects, fake proof), since those drive the first impression. Do not swap one default for another default (for example Lucide for Heroicons, or purple for teal with the same orbs).

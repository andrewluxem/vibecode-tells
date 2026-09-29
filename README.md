# vibecode-tells

An open source agent skill that keeps AI-built websites from looking AI-built.

Ask any coding agent for a landing page and you tend to get the same site: purple gradient headline, blurred orbs behind the hero, three feature cards with Lucide icons, a bento grid, three pricing tiers, and copy that says "It's not a to-do list. It's a second brain." None of those choices is wrong on its own. Together, unchosen, they tell visitors that nobody designed the thing.

This skill gives Claude (or any agent that reads skill files) a catalog of 30 of those tells, a design-time process that prevents them, and a review format plus a heuristic scanner that finds them in existing code.

## What's in the repo

`vibecode-tells/SKILL.md` is the skill itself. It has two modes. Design mode makes the agent settle palette, type, surface treatment, proof, and copy voice before writing markup, then self-review. Review mode audits existing work and returns a verdict plus a table of flagged tells with locations and fixes.

`vibecode-tells/scripts/scan.py` is a dependency-free Python scanner. It mechanically checks 26 of the 30 tells (gradients, Lucide imports, Inter/Geist/Space Grotesk, em dashes, emoji, backdrop blur, radial orbs, large radii, hover transforms, neon and pastel hex values, missing terms or privacy links, async code without skeleton loaders, and more). Fake testimonials, missing product demos, and subtler copy framing still need human or model judgment.

`tests/` holds fixtures and tests that keep the scanner honest as rules change.

## The 30 tells

Color: harsh gradients, pure white background, rainbow coloring, purple and black, neon colors, basic pastel colors.
Type and copy: em dashes, Inter/Geist/Space Grotesk, "it's not X, it's Y", emojis.
Iconography: Lucide icons, checkmark bullets, sparkle icons, animated arrows.
Layout: three feature cards in a row, bento grids, three pricing tiers, terminal window, colored left stripe.
Surface and effects: drop shadows, liquid glass, soft corner radius, radial orbs, dot grids, hover animations.
Trust and completeness: fake testimonials, no real product demos, no skeleton loaders, no terms of service, no privacy policy.

The skill treats these as defaults to justify, not absolute bans. An explicit brand system always wins; the review marks those cases "brand-mandated" instead of failing them.

## Install

Claude.ai: download `vibecode-tells.skill` from the latest release and upload it under Settings, Capabilities, Skills.

Claude Code: copy the `vibecode-tells/` folder into `~/.claude/skills/` (all projects) or `.claude/skills/` inside a project.

Other agents: point the agent at `vibecode-tells/SKILL.md` as a system or project instruction file.

## Run the scanner directly

```
python vibecode-tells/scripts/scan.py path/to/site
python vibecode-tells/scripts/scan.py path/to/site --json
python vibecode-tells/scripts/scan.py path/to/site --strict   # exit 1 on any flag, for CI
```

Hits are leads, not verdicts. Expect false positives, and please report them.

## Contributing

This list will age. New defaults appear every time model output shifts, and some tells here will stop being tells. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose a tell, retire one, or fix a scanner false positive.

## Credits

The original 30-item list was popularized by [@aj.on.ai](https://www.tiktok.com/@aj.on.ai) in a short video titled "30 reasons your site looks vibecoded." This repo expands it into rationale, alternatives, a review process, and tooling. Maintained by [Andrew Luxem](https://andrewluxem.com).

## License

MIT. See [LICENSE](LICENSE).

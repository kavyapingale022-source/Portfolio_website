---
name: Craftsman Digital
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c8'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c6c6c7'
  primary: '#ffffff'
  on-primary: '#2f3131'
  primary-container: '#e2e2e2'
  on-primary-container: '#636565'
  inverse-primary: '#5d5f5f'
  secondary: '#c6c6cf'
  on-secondary: '#2f3037'
  secondary-container: '#45464e'
  on-secondary-container: '#b4b4bd'
  tertiary: '#ffffff'
  on-tertiary: '#32302d'
  tertiary-container: '#e7e1dd'
  on-tertiary-container: '#676460'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c7'
  on-primary-fixed: '#1a1c1c'
  on-primary-fixed-variant: '#454747'
  secondary-fixed: '#e2e1eb'
  secondary-fixed-dim: '#c6c6cf'
  on-secondary-fixed: '#1a1b22'
  on-secondary-fixed-variant: '#45464e'
  tertiary-fixed: '#e7e1dd'
  tertiary-fixed-dim: '#cbc6c1'
  on-tertiary-fixed: '#1d1b19'
  on-tertiary-fixed-variant: '#494643'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
  surface-elevated: '#0A0A0A'
  border-subtle: '#27272A'
  pure-black: '#000000'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  display-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.03em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1280px
  gutter: 24px
  margin-x: 32px
  section-gap: 120px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is centered on a "Craftsman" aesthetic—a philosophy that celebrates precision, intentionality, and technical mastery. It is designed for a professional web developer portfolio where the code is as beautiful as the interface. 

The style is **Minimalist-Technic**, characterized by high-contrast monochromatic scales, generous whitespace, and meticulous attention to detail. It avoids unnecessary decoration, instead using structural elements like borders, monospaced accents, and subtle tonal layering to create a sense of depth and sophistication. The interface should feel like a high-end IDE or a bespoke editorial piece: focused, quiet, and exceptionally well-built.

## Colors

This design system utilizes a strictly monochromatic palette to maintain a high-end, focused atmosphere. 

- **Backgrounds:** The foundation is absolute black (`#000000`) to ensure a "true dark" experience, with `#050505` and `#0A0A0A` used for subtle depth and container nesting.
- **Typography:** Primary text is near-white (`#FAFAFA`) for maximum legibility. Secondary text and metadata use `#A1A1AA` to establish clear information hierarchy.
- **Accents:** Borders and structural lines use `#27272A`, providing a "ghost" framework that organizes content without overwhelming the visual field.

## Typography

The typography system relies on the interplay between three distinct styles:
1. **Headlines:** Use **Hanken Grotesk** (a high-quality alternative to Clash Display) for a bold, modern, and high-contrast look. These should be tight and impactful.
2. **Body Text:** Use **Inter** for its systematic clarity and excellent readability at small sizes.
3. **Technical Details:** Use **JetBrains Mono** for labels, tags, and small data points. This injects the "developer" DNA into the design, suggesting precision and technical expertise.

Vertical rhythm is maintained through a consistent 1.6x line height for body text, while headlines are kept tight to create a strong visual anchor.

## Layout & Spacing

This design system uses a **fixed-center grid** for desktop and a **fluid layout** for mobile devices. 

- **Grid:** A 12-column grid is used for main content areas with 24px gutters.
- **Sectioning:** Content sections are separated by significant vertical gaps (120px) to allow each project or skill set to breathe, reinforcing the "minimalist" aesthetic.
- **Rhythm:** Spacing follows a strict base-8 scale. For component internals, use `stack-sm` (8px) or `stack-md` (16px). For grouping related components (like a header and its description), use `stack-lg` (32px).
- **Responsive:** On mobile, margins reduce to 16px and the 12-column grid collapses into a single column.

## Elevation & Depth

Depth in this system is achieved through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows.

1. **Base Layer:** `#000000` for the page background.
2. **Elevated Surfaces:** Cards and containers use `#050505` or `#0A0A0A` to subtly lift them from the background.
3. **Outlines:** Every interactive or grouped element is contained by a 1px solid border using `#27272A`. This creates a crisp, architectural feel.
4. **Hover States:** Interaction is signaled by changing the border color from `#27272A` to `#FAFAFA` (white) or by applying a very subtle white-to-transparent gradient stroke. No heavy shadows or blurs are permitted.

## Shapes

The shape language is "Soft-Technical." To maintain a clean, professional look, roundedness is kept to a minimum. 

- **Components:** Buttons, input fields, and tags use a `0.25rem` (4px) radius. This is enough to prevent the UI from feeling aggressive while remaining sharp enough to feel precise.
- **Large Containers:** Cards or featured sections may use a `0.5rem` (8px) radius to soften the overall structure of the page. 
- **Skill Bars:** Progress bars should have a `2px` radius for a technical, bar-code-like appearance.

## Components

### Buttons
- **Primary:** Transparent background with a 1px `#FAFAFA` border and `#FAFAFA` text. On hover, invert the colors (white background, black text).
- **Secondary:** Transparent background with a 1px `#27272A` border and `#A1A1AA` text. On hover, border changes to `#FAFAFA`.

### Progress Bars (Skills)
- **Track:** Height of 4px, background color `#27272A`.
- **Fill:** Solid `#FAFAFA` with no gradients.
- **Labels:** Use `label-sm` (JetBrains Mono) placed above the bar, aligned to the left.

### Cards (Project Showcase)
- **Structure:** 1px solid border `#27272A`. Background `#050505`.
- **Interaction:** On hover, the border transitions to `#FAFAFA` and any monospaced labels within the card shift slightly (2px) to the right.

### Input Fields
- **Style:** Underline only or 1px border on all sides. Background is `#0A0A0A`.
- **Focus:** Border color changes to `#FAFAFA`. Text remains `#FAFAFA`.

### Footer
- **Design:** A structured 4-column layout separated by thin vertical 1px `#27272A` lines. 
- **Content:** Minimalist links in `label-md` and a "Time" or "Status" indicator in monospaced font to enhance the craftsman vibe.
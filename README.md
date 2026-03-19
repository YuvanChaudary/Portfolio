# Yuvan Chaudary's Portfolio

A clean, responsive, and performance-optimized personal portfolio for Yuvan Chaudary, showing experience as a Full Stack Developer, projects, and a professional skill set.

## Features
- **Dynamic Terminal Effect**: Shows a sleek, typed-out loading animation.
- **Custom Cursor & Interactions**: Features an adaptive and stylized mouse cursor that expands and highlights interactable elements. Disables gracefully on touch devices.
- **Scroll Reveal Animations**: Sections fade and slide in smoothly as the user browses down the page using `IntersectionObserver`.
- **Responsive Layout**: Designed mobile-first, adapting flawlessly to both small touch screens and large displays.
- **Contact Form Handlers**: Dynamically hooks into the user's local email client, pre-filling contact inputs. 
- **Security-First**: Enforces safe window opening policies via `noopener noreferrer` on target blank outgoing URLs.

## How to Run

Because this project relies entirely on modern vanilla web standards, it requires zero dependencies to view.

1. **Directly Applaud**: Simply double-click `portfolio.html` to open it natively in your default browser (Chrome, Edge, Firefox, Safari).
2. **Local Development Server**: To avoid CORS policies when injecting external assets in the future, serve the folder through a server like **VS Code Live Server** or using Python's built-in http daemon:
   ```bash
   python -m http.server 8000
   ```
   *Then access `http://localhost:8000/portfolio.html`.*

## Technologies Used
- **HTML5:** Core page structure and semantics.
- **CSS3 / Variables:** Custom variables layout (`--bg`, `--green`, `--text-muted`), responsive grid, media-queries, typography.
- **Vanilla JavaScript:** DOM manipulations, IntersectionObservers (scroll reveals), async typing scripts, cursor events.

## Directory Structure
- `portfolio.html`: The main page template housing the layout structure and script behavior.
- `style.css`: Extracted styles that unify the aesthetic, animations, and custom utility classes.
- `fix_portfolio.py`: Auto-generation/refactoring script created during a debugging phase to format and extract CSS correctly.

## Find me online
- **Email:** yuvanchaudary2004@gmail.com
- **LinkedIn:** [linkedin.com/in/yuvanchaudary](https://www.linkedin.com/in/yuvanchaudary)
- **GitHub:** [github.com/YuvanChaudary](https://github.com/YuvanChaudary)

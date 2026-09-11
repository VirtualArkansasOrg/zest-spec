# Zest Specification

Formal specification for the [Zest](https://getzest.dev) LTI content platform.

## What is Zest?

Zest is an LTI 1.3 tool that enables embedding interactive content (simulations, notebooks, assessments) inside Canvas LMS. Content authors package their work as zip files with a `zest.json` manifest and use the Bridge API to integrate with LTI grading, state persistence, and assessment features.

## Specification

**[Zest Specification v1.0.1](./spec/v1.0.1.md)** — The complete spec (current). [v1.0](./spec/v1.0.md) remains for reference; 1.0.1 is an errata release and packages written against 1.0 need no change.

Covers:
- **zest.json Manifest** — Content package metadata, grading mode, parameters, sandbox config
- **Bridge API v3.0** — Client-side JavaScript API (`window.Zest`) for context, grading, state, config
- **Content Conventions** — Standard file layout (`index.html`, `editor.html`, `review.html`, etc.)
- **Assessment Config** — Explore (guided text) and Quiz (auto-graded MC/TF) modes
- **Config Cascade** — Teacher config resolution (saved config, package default, none)
- **Event Log** — Compact interaction tracking format
- **Server API** — REST endpoints for upload, grades, state, config
- **postMessage Protocol** — Wrapper-to-content communication

## Quick Start

Minimal `zest.json`:

```json
{
  "name": "My Content",
  "version": "1.0.0",
  "grading": "none"
}
```

Minimal `index.html`:

```html
<!DOCTYPE html>
<html>
<head><title>My Content</title></head>
<body>
  <h1>Hello from Zest!</h1>
  <script src="/public/zest-bridge.js"></script>
  <script>
    Zest.onReady(function(context) {
      console.log('User:', Zest.getUser());
    });
  </script>
</body>
</html>
```

## Versioning

| Spec Version | Bridge API | Status |
|:---:|:---:|:---:|
| [1.0.1](./spec/v1.0.1.md) | 3.0.1 | **Current** (errata; compatible with 1.0 packages) |
| [1.0](./spec/v1.0.md) | 3.0.0 | Superseded |

A package declares the `major.minor` it targets in `zest.json` (`"zestSpec": "1.0"`). Servers accept any package whose major version they support; patch releases of the spec never change what a conformant package must do. Changes are listed in [CHANGELOG.md](./CHANGELOG.md).

## License

MIT. The names "Zest" and "Zestable" are trademarks of Virtual Arkansas (applications pending); see [TRADEMARKS.md](TRADEMARKS.md).

# Zest Specification

Formal specification for the [Zest](https://getzest.dev) LTI content platform.

## What is Zest?

Zest is an LTI 1.3 tool that enables embedding interactive content (simulations, notebooks, assessments) inside Canvas LMS. Content authors package their work as zip files with a `zest.json` manifest and use the Bridge API to integrate with LTI grading, state persistence, and assessment features.

## Specification

**[Zest Specification v1.0](./spec/v1.0.md)** — The complete spec.

Covers:
- **zest.json Manifest** — Content package metadata, grading mode, parameters, sandbox config
- **Bridge API v3.0** — Client-side JavaScript API (`window.Zest`) for context, grading, state, config
- **Content Conventions** — Standard file layout (`index.html`, `editor.html`, `review.html`, etc.)
- **Assessment Config** — Explore (guided text) and Quiz (auto-graded MC/TF) modes
- **Config Cascade** — Four-level teacher config resolution system
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
| 1.0 | 3.0.0 | **Current** |

## License

MIT. The names "Zest" and "Zestable" are trademarks of Virtual Arkansas (applications pending); see [TRADEMARKS.md](TRADEMARKS.md).

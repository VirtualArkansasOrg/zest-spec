# Changelog

All notable changes to the Zest specification.

## [1.0.1] — 2026-09-11 — Errata

Corrections so the text matches the reference server (zest-server 1.1) and the shipped Bridge 3.0.1. No package change is required; `"zestSpec": "1.0"` remains the declared version.

### Corrected
- **File types.** Uploads are checked against a denylist of executables, installers, desktop scripts, nested archives and shortcuts. 1.0 described an allowlist that the reference server had already replaced.
- **Upload limits.** There is no 500-file cap. Limits are 100 MB per package, 50 MB per file and a 100:1 compression ratio.
- **State size.** The student-state limit is 100 MB, not 10 MB (section 2, section 6 and section 7).
- **Default sandbox** is `allow-scripts allow-same-origin allow-popups allow-forms`, and the full boolean map is documented (`allowModals`, `allowTopNavigation`, `allowPresentation`, `allowDownloads` were missing).
- **Config cascade (section 5)** now describes what ships: one teacher-saved config per content item, then the package default, then none; `source` is `database | default | none`. The per-assignment level and its `override` / `content-default` sources are marked as planned for server 1.2 and Bridge 3.1. The Postgres table definition was removed; storage is not part of the specification.
- **`/health`** response shape.
- **Parameters** are documented as delivered through `param_<key>` form fields and `zest_param_<key>` custom variables, with a note that the reference picker does not yet render a form for them.
- Removed sprint numbers from headings and field notes.

### Added (Bridge 3.0.1, additive)
- `Zest.isAdmin()`; `Zest.isTeacher()` is true for Administrators as well as Instructors.
- `submitScore()` and `submitWork()` resolve with `agsStatus` (`ok | failed | skipped`), `agsError` and `submissionId`, and the `zest-submit-result` message carries the same fields. Content should surface a failed gradebook post to the student.
- `zest-context` documents `teacherView` and the `reviewMode` flag on the context.
- `POST /api/content/:contentId/duplicate`; `DELETE /api/content/:contentId` refuses while submissions or saved state exist; `.zest` files accepted on upload.

## [1.0] — 2026-05-27

First published specification: `zest.json` manifest, Bridge API 3.0, content file conventions, assessment config schema, config cascade, event log schema, server API and the postMessage protocol.

# Changelog

All notable changes to the Zest specification.

## Unreleased — shipped by zest-server 1.2 and Bridge 3.1, to be specified in 1.1

Additive behaviour a 1.0 package can rely on when `GET /api/info` lists the capability; none of it changes what a conformant package must do.

- `grading.idempotent`: `POST /api/grades/:contentId` accepts `clientSubmitId` (8 to 64 characters of `[A-Za-z0-9_-]`); the same id from the same user returns the first submission with `duplicate: true`. Bridge 3.1 derives it from the payload.
- `grading.ags-status`: submission responses carry `agsStatus`, `agsError`, `agsAttempts` and `contentVersion`; failed gradebook posts are retried by the server for 24 hours. Scores are scaled to the line item's maximum.
- `state.versioned`: state saves accept `baseVersion`, `source` (`sync` | `beacon` | `drain`) and `clientUpdatedAt`; responses carry `version`, `hashAlgo` (`md5` | `sha256`) and `conflict`. Sync status gains `'expired'`; `Zest.getSyncStatus()`.
- `config.per-assignment` (only when the server enables it): `Zest.getConfig(assignmentId?)`, `saveConfig(data, assignmentId?)`, `deleteConfig(assignmentId?)`; `GET /api/config/:contentId?v=2` returns `source` as `override` | `content-default` | `default` | `none` with the 1.0 vocabulary in `legacySource`; without `v=2` the 1.0 vocabulary stays in `source` and the level is in `resolvedFrom`. Saves with an `assignmentId` are refused with `409 { code: 'PER_ASSIGNMENT_DISABLED' }` where not enabled.
- `PUT /api/content/:contentId/files` replaces a package in place; `contentVersion` increments and each submission records the version it was made with.

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

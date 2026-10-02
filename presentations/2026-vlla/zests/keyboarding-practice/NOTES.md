# Keyboarding Practice (VLLA demo)

A copy of the production Keyboarding Practice zest (zest-creator `content/keyboarding-practice`, version 3.1.3) for the VLLA 2026 talk.

Changes from production (October 1, 2026):
- **Preview mode.** If no Canvas context arrives within 1.2 seconds (someone opened it from a QR code), it starts in preview with a banner. Everything works; nothing is saved or submitted. If a context arrives late, the page reloads and runs normally.
- **Name** changed to "Keyboarding Practice (VLLA demo)" and version to 3.1.3-vlla.1, so uploading it never offers to update the production copies. The picker matches copies by this name.

Everything else is unchanged. The production package still uses ES2017 syntax (async/await, arrow functions), unlike the ES5 the zest-creator conventions ask for.

# Tornelo Pages Hosting (No Laptop IP Dependency)

This setup hosts your two new standalone files on Cloudflare Pages.

## Files to deploy
- `tornelo-display-clean.html`
- `tornelo-player-card-clean.html`

Optional:
- `tornelo-player-qr.html`

## Steps
1. Create a free Cloudflare account.
2. Go to **Workers & Pages** > **Create application** > **Pages** > **Upload assets**.
3. Upload the two (or three) files above.
4. Deploy.
5. You will get a stable HTTPS URL like:
   - `https://your-project.pages.dev/tornelo-display-clean.html`
   - `https://your-project.pages.dev/tornelo-player-card-clean.html`

## Tournament workflow
1. Open the hosted display page.
2. Upload latest Tornelo round CSV.
3. Open the hosted player-card page on same browser/device for lookups.

## Important limitation
The uploaded CSV snapshot is stored in browser localStorage per device/browser.
So if you upload on one browser, another device will not see that data automatically.

If you want shared cross-device updates, add a small backend store (e.g. Cloudflare Worker + KV).

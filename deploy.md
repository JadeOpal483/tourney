# Deploy Tournament Host to Render (No Laptop Required)

This deploys your existing files to a cloud URL so players can always access:
- `display.html`
- `player-card.html`
- `player-qr.html`

## 1) Put this folder in a GitHub repo

From Terminal:

```bash
cd "/Users/ahmad/Documents/New project"
git init
git add .
git commit -m "tornelo host deploy setup"
```

Create an empty GitHub repo, then:

```bash
git remote add origin <YOUR_GITHUB_REPO_URL>
git branch -M main
git push -u origin main
```

## 2) Deploy on Render

1. Open [https://render.com](https://render.com)
2. `New` -> `Blueprint`
3. Connect your GitHub repo
4. Render detects `render.yaml`
5. Click `Apply`

Render will deploy and give you a URL like:
- `https://tornelo-host.onrender.com`

## 3) Test pages

Open:
- `https://YOUR-RENDER-URL/display.html`
- `https://YOUR-RENDER-URL/player-card.html`
- `https://YOUR-RENDER-URL/player-qr.html`

## 4) Tournament workflow (cloud)

1. Organizer opens display page on Render URL
2. Upload latest Tornelo CSV
3. Snapshot is saved to `/api/snapshot` on the cloud app
4. Players open player-card page and auto-refresh updates

## Important note

On Render free plan, service may sleep when inactive and filesystem is not guaranteed persistent forever.  
If snapshot disappears after a restart, just re-upload the latest CSV from display page.


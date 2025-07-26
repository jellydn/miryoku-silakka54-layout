# PR Preview Deployment Setup

This repository includes GitHub Actions for automatic PR preview deployments. Choose one of the following options:

## Option 1: Surge.sh (Simplest)

1. Sign up at [surge.sh](https://surge.sh)
2. Install Surge CLI: `npm install -g surge`
3. Get your token: `surge token`
4. Add secret to GitHub repo:
   - Go to Settings → Secrets → Actions
   - Add `SURGE_TOKEN` with your token value
5. Use `.github/workflows/preview-pr.yml`

## Option 2: Netlify (No token needed)

1. The repository includes `netlify.toml` configuration
2. PRs can be manually deployed by:
   - Visiting [app.netlify.com/drop](https://app.netlify.com/drop)
   - Dragging the project folder
3. For automatic deploys:
   - Connect your GitHub repo at [app.netlify.com](https://app.netlify.com)
   - Enable "Deploy Previews" in Site Settings → Build & Deploy

## Option 3: Vercel (Automatic)

1. Visit [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Vercel automatically creates preview deployments for all PRs
4. No configuration needed!

## Option 4: GitHub Pages (Manual)

For contributors without repo access:
1. Fork the repository
2. Enable GitHub Pages in your fork's Settings
3. Your preview will be at: `https://[username].github.io/miryoku-silakka54-layout/`

## Current Setup

This repository currently uses the simple preview information workflow (`.github/workflows/preview-pr-simple.yml`) which provides deployment instructions in PR comments.

To enable automatic deployments, choose one of the options above and:
1. Set up the required service
2. Add any necessary secrets
3. Enable the corresponding workflow
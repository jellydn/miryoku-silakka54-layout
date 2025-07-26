# PR Preview Deployment Setup

This repository includes GitHub Actions for deployment. Here are the available options:

## Current Setup

The repository uses the **Simple PR Information Workflow** which automatically comments on PRs with deployment options.

## Manual Preview Options

### Option 1: Vercel (Recommended - Automatic PR Previews)

1. Visit [vercel.com](https://vercel.com)
2. Click "Import Project"
3. Import from GitHub: `jellydn/miryoku-silakka54-layout`
4. Vercel will automatically:
   - Deploy the main branch
   - Create preview deployments for all PRs
   - Post preview links as PR comments

No configuration needed! The `vercel.json` file is already included.

### Option 2: Netlify (Easy Manual Deploy)

1. Visit [app.netlify.com/drop](https://app.netlify.com/drop)
2. Download the PR branch locally:
   ```bash
   git fetch origin pull/[PR-NUMBER]/head:pr-[PR-NUMBER]
   git checkout pr-[PR-NUMBER]
   ```
3. Drag the project folder to Netlify Drop
4. Get instant preview URL

The `netlify.toml` file is already configured.

### Option 3: GitHub Pages (For Forks)

1. Fork the repository
2. Go to Settings → Pages
3. Source: Deploy from a branch
4. Branch: main / root
5. Save

Your preview will be at: `https://[username].github.io/miryoku-silakka54-layout/`

The `static.yml` workflow will handle automatic deployments.

### Option 4: Local Preview

```bash
# Clone and checkout PR
git fetch origin pull/[PR-NUMBER]/head:pr-[PR-NUMBER]  
git checkout pr-[PR-NUMBER]

# Serve locally
npx serve
# or
python3 -m http.server 8000
```

### Option 5: CodeSandbox (Instant)

Open any PR directly in CodeSandbox:
```
https://codesandbox.io/s/github/jellydn/miryoku-silakka54-layout/tree/[BRANCH-NAME]
```

## For Repository Maintainers

To enable automatic PR previews:

1. **Vercel** (Easiest): Just connect the repo at vercel.com
2. **Netlify**: Connect repo and enable "Deploy Previews" in settings
3. **Surge.sh**: Add `SURGE_TOKEN` secret and enable `preview-pr.yml`

## Files Included

- `.github/workflows/static.yml` - GitHub Pages deployment for main branch
- `.github/workflows/preview-pr-simple.yml` - PR comment with deployment options
- `.github/workflows/preview-pr.yml.disabled` - Surge.sh deployment (requires token)
- `vercel.json` - Vercel configuration
- `netlify.toml` - Netlify configuration
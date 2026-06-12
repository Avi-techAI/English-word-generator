# Enable GitHub Actions

This project includes the daily workflow template at `docs/daily-word.workflow.yml`.

To activate it, copy that file to `.github/workflows/daily-word.yml`, commit it, and push:

```bash
mkdir -p .github/workflows
cp docs/daily-word.workflow.yml .github/workflows/daily-word.yml
git add .github/workflows/daily-word.yml
git commit -m "Enable daily word GitHub Actions workflow"
git push
```

If GitHub rejects the workflow file with a `workflow` scope error, refresh GitHub CLI authentication:

```bash
gh auth refresh -h github.com -s workflow
```

GitHub may show a browser device code. Complete that flow, then retry the commit and push.

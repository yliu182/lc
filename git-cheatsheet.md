# Git Cheatsheet

## 1. Switch Git Account for This Repo

```bash
git config user.name "Your Name"
git config user.email "your@email.com"
```

This only affects `/Users/yaoliu/Documents/lc`. Other repos still use the global config (`~/.gitconfig`).

## 2. Initial Checkin to Remote Repo

```bash
# Create repo on GitHub first (pick one):
gh repo create yliu182/lc --public --source=. --push
# OR create manually at https://github.com/new, then:

git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yliu182/lc.git
git push -u origin main
```

## 3. Future Modifications

```bash
# Check what changed
git status
git diff

# Stage and commit
git add <file>            # stage specific file
git add .                 # stage all changes

git commit -m "Your commit message"

# Push to GitHub
git push
```

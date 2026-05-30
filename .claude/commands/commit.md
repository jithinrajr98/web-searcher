# Commit
> Stage and commit recent changes to git with a generated commit message.

## Steps

1. Run `git status` to see what has changed.
2. Run `git diff` to understand what changed and why.
3. Run `git log --oneline -5` to match the existing commit message style.
4. Stage relevant changed files (avoid secrets like `.env`).
5. Write a concise commit message focused on the *why*, not the *what*.
6. Create the commit.
7. Run `git status` to confirm success.

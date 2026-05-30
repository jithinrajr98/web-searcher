# Commit
> Stage and commit recent changes to a new git branch. The branch name is derived from the commit message argument.

## Argument
The commit message is passed as `$ARGUMENTS`. If no argument is provided, ask the user for one.

## Steps

1. Run `git status` to see what has changed.
2. Run `git diff` to understand what changed and why.
3. Derive a branch name from `$ARGUMENTS` — lowercase, replace spaces with hyphens, strip special characters (e.g. `"fix login bug"` → `fix-login-bug`).
4. Create and switch to the new branch: `git checkout -b <branch-name>`.
5. Stage relevant changed files (avoid secrets like `.env`).
6. Commit using `$ARGUMENTS` as the commit message.
7. Run `git status` to confirm success.

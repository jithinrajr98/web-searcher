# Commit
> Stage and commit recent changes to a new git branch using an explicit branch name and commit message.

## Arguments
Two arguments are passed as `$ARGUMENTS` in the format: `<branch-name> <commit message>`.
- The first word is the branch name (e.g. `fix-login-bug`).
- Everything after the first word is the commit message.
If fewer than two arguments are provided, ask the user for the missing ones.

## Steps

1. Run `git status` to see what has changed.
2. Run `git diff` to understand what changed and why.
3. Parse `$ARGUMENTS`: the first word is the branch name, the rest is the commit message.
4. Create and switch to the new branch: `git checkout -b <branch-name>`.
5. Stage relevant changed files (avoid secrets like `.env`).
6. Commit using the parsed commit message.
7. Run `git status` to confirm success.

## Example
```
/commit fix-login-bug fix null pointer in login handler
```
Branch: `fix-login-bug`, commit message: `fix null pointer in login handler`.

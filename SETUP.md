# SETUP.md

Reference for environment setup and the daily Git workflow.

Written for **Windows + Git Bash**. On Mac/Linux, replace `.venv/Scripts/` with `.venv/bin/`.

---

## 1. Key concepts

### Git ≠ GitHub

| | What it is | Needs internet? |
|---|---|---|
| **Git** | Version control program on my machine | No |
| **GitHub** | A website hosting a copy of the repo | Yes |

Git works entirely offline. **Only `push`, `pull`, `fetch`, `clone` touch the network.**
`add`, `commit`, `branch`, `checkout`, `merge`, `log` are all local.

### The three areas

```
Working Directory  --git add-->  Staging Area  --git commit-->  Repository
(files I edit)                   (the "index")                  (.git/ - permanent)
```

- **Working directory** — the actual files I edit
- **Staging area** — a holding pen: "these changes go in my next commit"
- **Repository** — `.git/` — permanent snapshots. The whole history lives here.

Staging exists so I can split unrelated work into separate, clean commits.

### Branches ≠ environments

- **Branch** — a line of commits in Git. Laptop + GitHub.
- **Environment** — running infrastructure (dev / SIT / UAT / prod). Servers.

**Trunk-based (modern):** one long-lived branch (`main`). Short-lived feature branches come off it
and merge back via PR. The **same code artifact** is promoted through environments by CI/CD —
different config, same code.

Bronze/silver/gold (medallion) is a **data layering** concept. Nothing to do with Git branches.

### PR = Pull Request

A proposal: *"merge my branch into `main` — here's the diff, please review."*
A GitHub feature, not a Git feature. GitLab calls it a Merge Request.

Gives me: a reviewable diff, line comments, CI checks, an audit trail, and a gate.

---

## 2. One-time machine setup

### Verify

```bash
python --version
git --version
```

### VS Code terminal → Git Bash

`Ctrl+Shift+P` → `Terminal: Select Default Profile` → **Git Bash** → restart terminal.

> **Why:** every Spark cluster, Airflow worker, Databricks node and Docker container runs Linux.
> Bash is what the job uses. CMD/PowerShell speak different languages and would have to be unlearned.

### Git identity

```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --global credential.helper store
```

| Setting | Why |
|---|---|
| `user.name` / `user.email` | Stamped on every commit. **Email must match GitHub** or commits won't show on the contribution graph. |
| `init.defaultBranch main` | GitHub uses `main`; old Git defaults to `master`. Mismatch causes confusing push failures. |
| `core.editor "code --wait"` | VS Code instead of Vim. `--wait` pauses the terminal until the tab closes. |
| `credential.helper store` | Cache the token so it isn't re-typed. *(Plaintext — personal machines only.)* |

```bash
git config --global --list
cat ~/.gitconfig
```

> `.gitconfig` lives in **home** (`~`), not in the project. Different file from `.gitignore`.

### GitHub Personal Access Token

GitHub rejects passwords over HTTPS.

1. GitHub → Settings → Developer settings → Personal access tokens → **Tokens (classic)**
2. Generate → scope: **`repo`**
3. **Copy it — it can never be viewed again**
4. Paste as the *password* when Git prompts

---

## 3. New project

```bash
cd ~/projects
mkdir python-core
cd python-core

mkdir -p src tests data notes
touch README.md .gitignore requirements.txt data/.gitkeep

code .
```

| Path | Purpose |
|---|---|
| `src/` | Source code |
| `tests/` | Unit tests |
| `data/` | Input files — **contents not tracked** |
| `notes/` | Learning log |
| `requirements.txt` | pip dependency list (**package list**, not documentation) |

**`code .`** — `code` launches VS Code; `.` = "current directory".
VS Code needs a **root folder** for the explorer, search, Git integration, and interpreter picker.
File = text editor. Folder = IDE.

| Symbol | Means |
|---|---|
| `.` | current directory |
| `..` | parent directory |
| `~` | home directory |

### .gitignore — write BEFORE the first commit

```gitignore
# Virtual environment
.venv/
venv/

# Python
__pycache__/
*.py[cod]
*.egg-info/
.pytest_cache/

# Secrets
.env

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Data - keep the folder, ignore the contents
data/*
!data/.gitkeep
```

> Committing `.venv/` pushes thousands of files and looks amateur.

---

## 4. Virtual environment

### What it is

A **private, isolated copy of Python** with its own package folder.

```
Project A needs pandas 1.5
Project B needs pandas 2.1     <- impossible on a shared global Python
```

Each project gets `.venv/Lib/site-packages/`. They never collide.

### Create

```bash
python -m venv .venv
```

- `python` — run the interpreter
- `-m venv` — `-m` = "run a **module** as a script"; the module is `venv`
- `.venv` — folder to create (dot = hidden; universal convention)

### Activate — **every new terminal**

```bash
source .venv/Scripts/activate
```

- `source` — Bash: "run this **in my current shell** so changes persist"
  *(running it normally spawns a subshell and throws the changes away)*
- The script **prepends `.venv/Scripts/` to `PATH`**, so `python` and `pip` resolve to the venv's copies.

**That's the whole mechanism. Just PATH manipulation.**

```
(.venv) jpart@Parthiban MINGW64 ~/projects/python-core
```

Prove it:

```bash
which python    # before: system python
                # after:  .../python-core/.venv/Scripts/python
```

Leave: `deactivate`

### Point VS Code at it

`Ctrl+Shift+P` → `Python: Select Interpreter` → pick the one showing `('.venv': venv)`

Status bar must read: **`Python 3.x.x ('.venv': venv)`**

**Not showing?** VS Code only scans the **open workspace folder**. Run `code .` from inside the project.
Still not showing? `Enter interpreter path...` and paste the **Windows-format** path:

```
C:\Users\jpart\projects\python-core\.venv\Scripts\python.exe
```

*(Git Bash prints `/c/Users/...` — translate `/c/` → `C:\`, flip the slashes.)*

> **Two separate settings, both needed:**
> - **Terminal** → `source .venv/Scripts/activate` (so `python` runs the right one)
> - **VS Code** → Select Interpreter (so autocomplete, linting, debugger work)

### Packages

```bash
pip install --upgrade pip
pip install <package>

pip freeze > requirements.txt      # save exact versions
pip install -r requirements.txt    # rebuild from the list
```

**`.venv/` is never committed** — hundreds of MB, platform-specific.
Commit `requirements.txt` instead: **ship the recipe, not the meal.**

---

## 5. Connect to GitHub

### First commit (local — nothing has left the machine)

```bash
git init
git status
git add .
git status                 # confirm .venv/ is NOT listed
git commit -m "chore: initialise project structure"
git log --oneline
```

### Create the repo

[github.com/new](https://github.com/new) → name it → **Public** →
**do NOT** tick README / .gitignore / license *(they exist locally; adding them causes a conflict).*

### Link and push

```bash
git remote add origin https://github.com/USERNAME/REPO.git
git remote -v
git push -u origin main
```

- `origin` — a **nickname for the URL**. Nothing magic.
- `-u` — remember the branch↔remote pairing, so plain `git push` works afterwards

Paste the **PAT** as the password.

---

## 6. Daily workflow

**Never commit directly to `main`.** Branch → commit → push → PR → merge.

### Start of day

```bash
git checkout main
git pull origin main
git checkout -b day-01-basics
```

- `checkout` = switch to · `-b` = create first
- **`checkout` is purely local.** Nothing downloads. `.git/` already holds every branch.

### While working — repeat often

```bash
git status                              # which files changed?
git diff                                # what exactly changed?
git add src/day01_basics.py             # stage specific files, not `git add .`
git commit -m "feat: add fizzbuzz"
```

**Commit small and often.** 4–5 commits a day is correct.

### End of day

```bash
git push -u origin day-01-basics
```

GitHub: **Compare & pull request** → review **Files changed** → **Create** → **Merge**.

### Sync and clean up

```bash
git checkout main
git pull origin main            # bring the merge down (it happened on GitHub, not here)
git branch -d day-01-basics     # -d refuses if not fully merged - safe
git log --oneline
```

### The shape

```
                +- 1. branch off main
                |
main -----------+--------------------------->   (always clean, always working)
                 \                        /
                  \  2. commit           /  5. merge via PR
                   \  3. commit         /
                    \  4. push         /
                     +----------------+
                       day-01-basics
```

### Commit convention

`type: short imperative description` — "add", not "added".
Completes: *"If applied, this commit will ___"*

| Prefix | Use for |
|---|---|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `chore:` | Maintenance, deps, config |
| `docs:` | Documentation only |
| `refactor:` | Restructuring, no behaviour change |
| `test:` | Adding or fixing tests |
| `style:` | Formatting only |
| `perf:` | Performance |

```
BAD:   update / stuff / fixed it / final version 2
GOOD:  feat: add SCD Type 2 merge logic
       fix: handle null keys in broadcast join
       refactor: extract validation into separate module
```

---

## 7. Command reference

### Every session

```bash
cd ~/projects/python-core
source .venv/Scripts/activate
```

### Git — local (no internet)

| Command | Does |
|---|---|
| `git status` | What changed, and which area it's in. **Run constantly.** |
| `git diff` | Line-level changes, unstaged |
| `git diff --staged` | Line-level changes, staged |
| `git add <file>` | Stage a file |
| `git add -A` | Stage everything |
| `git reset <file>` | Unstage (changes **not** lost) |
| `git commit -m "msg"` | Snapshot what's staged |
| `git log --oneline` | Compact history |
| `git log --oneline --graph --all` | History as a branch diagram |
| `git show HEAD` | Most recent commit, in full |
| `git branch` | List branches (`*` = current) |
| `git checkout -b <name>` | Create + switch |
| `git checkout <name>` | Switch |
| `git branch -d <name>` | Delete a merged branch |
| `git stash` / `git stash pop` | Shelve changes / bring back |
| `git reflog` | **Every** HEAD move — disaster recovery |

### Git — network

| Command | Does |
|---|---|
| `git clone <url>` | First download of a repo |
| `git push` | Upload commits GitHub lacks |
| `git push -u origin <branch>` | First push of a new branch |
| `git pull origin main` | Download + merge from GitHub |
| `git remote -v` | Which URL is `origin`? |

### Python / venv

| Command | Does |
|---|---|
| `python -m venv .venv` | Create |
| `source .venv/Scripts/activate` | Activate |
| `deactivate` | Leave |
| `which python` | Which interpreter is actually running |
| `pip list` | What's installed here |
| `pip freeze > requirements.txt` | Save versions |
| `pip install -r requirements.txt` | Rebuild |
| `python src/file.py` | Run a script |

### Bash

| Command | Does |
|---|---|
| `pwd` | Where am I |
| `ls -la` | List all, incl. hidden dotfiles |
| `cd ..` / `cd ~` / `cd -` | Up / home / previous |
| `cat <file>` | Print a file |
| `mkdir -p a/b/c` | Nested dirs |
| `touch <file>` | Empty file |
| `rm <file>` | Delete |

---

## 8. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `(.venv)` not in prompt | Not activated | `source .venv/Scripts/activate` — **every new terminal** |
| `.venv` missing from Select Interpreter | Wrong folder open in VS Code | `code .` from project root; check Explorer sidebar |
| `import x` red but script runs | VS Code on system Python | Select Interpreter → `('.venv': venv)` |
| `git commit` refuses | No `user.name`/`user.email` | Run the `git config --global` commands |
| `git push` rejects password | GitHub blocks passwords | Use a Personal Access Token |
| `src refspec main does not match` | Local is `master`, GitHub expects `main` | `git branch -M main` then push |
| Commits missing from contribution graph | `user.email` ≠ GitHub email | Fix config; affects future commits only |
| Accidentally pushed `.venv/` | `.gitignore` written after first commit | `git rm -r --cached .venv` → commit → push |
| Stuck in Vim | `core.editor` not set | `Esc` `:q!` Enter. Then set `core.editor`. |
| Deleted something, panicking | — | `git reflog` — it finds almost anything |

---

## Non-negotiables

1. **Activate the venv every session.** New terminal = re-activate.
2. **Never commit `.venv/`, `.env`, or credentials.**
3. **Never commit directly to `main`.** Branch → commit → push → PR → merge.
4. **`git status` constantly.**
5. **Commit small and often.** Not one end-of-day dump.
6. **Conventional prefixes.** `feat:` `fix:` `chore:` `docs:` `refactor:` `test:`
7. **Type every line of code.** Never paste from a tutorial. Finger memory is the mechanism.
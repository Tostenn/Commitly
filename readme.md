Voici la version anglaise de ton README pour **Commitly**, fidèle à la version française mais adaptée avec fluidité :

---

## 🧠 The Problem: The Empty Commit Syndrome

![empty commit](https://cdn.jsdelivr.net/gh/Tostenn/Commitly/images/vide.jpeg)

You just wrapped up an intense dev session. You proudly run:

```bash
git add .
git commit ""
```

And then… nothing.

The cursor blinks. The quotes are empty. **No idea** what to write.  
How do you summarize what you just did? How do you follow commit conventions? Should you mention the ticket? Where? How?

That’s where **Commitly** comes in.

---

# 🚀 What is Commitly?

**Commitly** is a Python library that uses AI to **automatically generate smart commit messages** from your staged Git changes (`git diff --cached`).

No more writer’s block. Commitly gives you **clear, structured, multilingual** messages — even **splits large diffs into logical commits** if needed.

---

## 📦 Installation

Install Commitly via PyPI:

```bash
pip install commitly
```

> Make sure [Git](https://git-scm.com/) is installed and properly configured on your system.

---

## ⚙️ Main Features

### 🔹 `__init__(model=gpt_4o_mini, file_temp="commit.txt", lang="en")`

Creates a Commitly instance:

- `model`: AI model to use (default is `gpt_4o_mini` via [g4f](https://github.com/xtekky/gpt4free)).
- `file_temp`: temporary file name to save the commit message.
- `lang`: output language (`en` or `fr`).

---

### 🔹 `add(file: str) -> bool`

Adds a file to the Git staging area.

```python
commitly.add("app/models/user.py")
```

---

### 🔹 `generate_commit_message(...) -> dict | List[dict]`

Generates **one or more commit messages** from the current staged diff.

Parameters:

- `style_commit`, `format_commit`, `recommandation_commit`: customize commit style and instructions.
- `ticket`: ticket ID to include in the footer of the commit.
- `fact` (**bool**): enables **smart factorization** to split the diff into multiple coherent commits.

> ⚠️ Raises a `DiffEmptyException` if no changes are detected in staging.

---

### 🔹 `save_message_to_file(message: str) -> bool`

Saves a generated commit message to the temporary file.

---

### 🔹 `commit() -> bool`

Performs a Git commit using the message saved in the temp file and deletes it afterward.

---

### 🔹 `push()`

Pushes your changes to the remote repository.

---

### 🔹 `unstage(file: str)`

Removes a file from the staging area (`git reset <file>`).

---

### 🔹 `file_stage() -> List[str]`

Returns a list of currently staged files (`git diff --cached --name-only`).

---

### 🔹 `_run_cmd(cmd: str, return_code: bool = False)`

Internal method to execute shell commands.

---

## 🧪 Full Example

```python
from commitly.commitly import Commitly

commitly = Commitly()

# Stage a file
commitly.add("main.py")

# Generate a message with a ticket
message = commitly.generate_commit_message(ticket="#42")

# Save it and commit
commitly.save_message_to_file(message)
commitly.commit()
commitly.push()
```

---

## 🧠 Example with **smart factorization**

```python
messages = commitly.generate_commit_message(ticket="#42", fact=True)
for item in messages:
    print(item["commit"], ":", item["files"])
```

Example output:

```json
[
    {
        "commit": "feat[core]: add role management to authentication",
        "files": ["auth/roles.py", "auth/utils.py"]
    },
    {
        "commit": "docs: update setup guide",
        "files": ["docs/setup.md"]
    }
]
```

---

## 🧩 About the Commit Format

Generated messages follow a conventional structure:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer] ← ticket goes here (#1234)
```

Common types:

- `feat`: a new feature
- `fix`: a bug fix
- `docs`: documentation-only changes
- `refactor`: code changes that neither fix a bug nor add a feature
- `chore`: other routine tasks like config or CI changes

---

## 💡 Why use Commitly?

✅ Say goodbye to “wip” commits  
✅ Enforce a consistent commit standard across your team  
✅ Generate **logical, factorized commits** from complex diffs  
✅ Multilingual support (EN/FR)  
✅ Easy integration into any Git workflow

---

## 📋 License

MIT © 2025 Kouya Chance Boman Tosten

---

> Stop staring at your empty commit. Let **Commitly** tell the story of your code — one commit at a time.

---

Souhaites-tu que je t’aide à structurer le `README.md` dans ton dépôt GitHub ? Ou peut-être créer une documentation en ligne avec `mkdocs` ou `docsify` ?

## 🧠 Le Problème : le syndrome du commit vide

![illustration du vide](https://cdn.jsdelivr.net/gh/Tostenn/Commitly/images/vide.jpeg)

Vous venez de finir une session intense de développement. Vous exécutez fièrement :

```bash
git add .
git commit ""
```

Et là… le vide.

Votre curseur clignote, les guillemets sont vides, **aucune idée** ne vient. Comment résumer proprement ce que vous venez de faire ? Comment respecter les conventions de commit ? Et ce ticket, faut-il le mentionner ? Où ? Comment ?

C’est là que **Commitly** entre en jeu.

---

# 🚀 Commitly, c’est quoi ?

**Commitly** est une bibliothèque Python qui utilise l’intelligence artificielle pour générer automatiquement un **message de commit** clair et structuré à partir des changements que vous avez mis en cache (`git diff --cached`).

Fini le syndrome du commit vide. Commitly vous propose un message ou **plusieurs commits factorisés**, contextualisés, multilingues, et conformes à vos standards d’équipe.

---

## 📦 Installation

Installez Commitly depuis PyPI :

```bash
pip install commitly
```

> Assurez-vous d’avoir [Git](https://git-scm.com/) installé et correctement configuré.

---

## ⚙️ Fonctionnalités principales

### 🔹 `__init__(model=gpt_4o_mini, file_temp="commit.txt", lang="fr")`

Crée une instance de Commitly avec :

- `model` : modèle IA utilisé (par défaut `gpt_4o_mini` via [g4f](https://github.com/xtekky/gpt4free)).
- `file_temp` : nom du fichier temporaire pour enregistrer le message.
- `lang` : langue de génération (`fr` ou `en`).

---

### 🔹 `add(file: str) -> bool`

Ajoute un fichier à la zone de staging Git.

```python
commitly.add("app/models/user.py")
```

---

### 🔹 `generate_commit_message(...) -> dict | List[dict]`

Génère automatiquement **un ou plusieurs messages de commit** à partir du `diff` en cache.

Paramètres :

- `style_commit`, `format_commit`, `recommandation_commit` : personnalisation du style et des consignes.
- `ticket` : identifiant de ticket à inclure dans le pied du message.
- `fact` (**booléen**) : active la **factorisation intelligente** du diff en plusieurs commits logiques.

> ⚠️ Lève une `DiffEmptyException` si aucun changement n’est détecté dans la zone de staging.

---

### 🔹 `save_message_to_file(message: str) -> bool`

Sauvegarde un message généré dans le fichier temporaire.

---

### 🔹 `commit() -> bool`

Exécute un commit avec le message enregistré dans le fichier temporaire, puis le supprime.

---

### 🔹 `push()`

Pousse les changements vers le dépôt distant.

---

### 🔹 `unstage(file: str)`

Retire un fichier de la zone de staging (`git reset <file>`).

---

### 🔹 `file_stage() -> List[str]`

Retourne la liste des fichiers actuellement en staging (`git diff --cached --name-only`).

---

### 🔹 `_run_cmd(cmd: str, return_code: bool = False)`

Méthode interne pour exécuter des commandes shell.

---

## 🧪 Exemple complet

```python
from commitly.commitly import Commitly

commitly = Commitly()

# Mise en cache d’un fichier
commitly.add("main.py")

# Génération d’un message unique avec ticket
message = commitly.generate_commit_message(ticket="#42")

# Sauvegarde puis commit
commitly.save_message_to_file(message['commit'])
commitly.commit()
commitly.push()
```

---

## 🧠 Exemple avec **factorisation intelligente**

```python
messages = commitly.generate_commit_message(ticket="#42", fact=True)
for item in messages:
    print(item["commit"], ":", item["files"])
```

Exemple de sortie :

```json
[
    {
        "commit": "feat[core]: ajout de la gestion des rôles dans l’authentification",
        "files": ["auth/roles.py", "auth/utils.py"]
    },
    {
        "commit": "docs: mise à jour du guide d’installation",
        "files": ["docs/setup.md"]
    }
]
```

---

## 🧩 À propos du format de commit

Les messages générés suivent cette structure standard :

```text
<type>[étendue optionnelle]: <description>

[corps optionnel]

[pied optionnel]  ← ticket ici (#1234)
```

Types classiques :

- `feat` : nouvelle fonctionnalité
- `fix` : correction de bug
- `docs` : documentation
- `refactor` : amélioration sans changement de comportement
- `chore` : tâches techniques ou maintenance

---

## 💡 Pourquoi utiliser Commitly ?

✅ Évite les commits génériques type “wip”  
✅ Uniformise la convention de message au sein de l’équipe  
✅ Génère des commits factorisés **sans duplication de fichiers**  
✅ Multilingue (fr/en)  
✅ Intégration facile dans les workflows Git existants

---

## 📋 Licence

MIT © 2025 Kouya Chance Boman Tosten

---

> Fini le syndrome du commit vide. Laissez **Commitly** écrire l’histoire de votre code, commit après commit.


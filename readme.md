
## 🧠 Le Problème : le syndrome du commit vide

![ullustration du vide](/image/vide.webp)


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

Commitly est une bibliothèque Python qui utilise l’intelligence artificielle pour générer automatiquement un **message de commit** bien structuré à partir des changements que vous avez mis en cache (`git diff --cached`).

Fini le syndrome du commit vide. Commitly vous propose un message clair, contextualisé, avec ou sans ticket, en français ou en anglais, et conforme à vos standards d’équipe.

---

## ⚙️ Fonctionnalités

### `__init__(model=gpt_4o_mini, file_temp="commit.txt", lang="fr")`

Crée une instance de Commitly.

- `model` : modèle IA à utiliser (par défaut `gpt_4o_mini` via la bibliothèque [g4f](https://github.com/xtekky/gpt4free)).
- `file_temp` : nom du fichier temporaire dans lequel le message sera enregistré pour le commit Git.
- `lang` : langue de génération des messages (`fr` ou `en`).

---

### `add(file: str) -> bool`

Ajoute un fichier spécifique à la zone de staging Git.

```python
commitly.add("app/models/user.py")
```

Equivalent à :

```bash
git add app/models/user.py
```

---

### `generate_commit_message(style_commit=None, format_commit=None, recommandation_commit=None, ticket=None) -> str`

Génère automatiquement le message de commit à partir du diff actuel (`git diff --cached`).

- `style_commit` : personnalisation du style (type, étendue, etc.).
- `format_commit` : format général attendu du message.
- `recommandation_commit` : recommandations pour la rédaction.
- `ticket` : un identifiant de ticket optionnel à inclure dans le pied du message.

> **⚠️ Important** : Si aucun changement n’est en cache, cette méthode lève une exception `DiffEmptyException`.

---

### `save_message_to_file(message: str) -> bool`

Sauvegarde un message de commit généré dans le fichier temporaire défini (par défaut : `commit.txt`).

```python
commitly.save_message_to_file(message)
```

Utile pour utiliser ensuite ce fichier dans une commande `git commit`.

---

### `commit() -> bool`

Effectue le commit en utilisant le message contenu dans le fichier temporaire. Une fois le commit effectué, le fichier est automatiquement supprimé.

```python
commitly.commit()
```

---

### `push()`

Exécute une commande `git push` pour envoyer vos modifications vers le dépôt distant.

```python
commitly.push()
```

---

### `unstage(file: str)`

Retire un fichier de la zone de staging (l’équivalent de `git reset <file>`).

```python
commitly.unstage("README.md")
```

---

### `_run_cmd(cmd: str, return_code: bool = False)`

Méthode interne utilisée pour exécuter des commandes shell. Elle peut retourner soit :

- la sortie de la commande (`stdout`)
- le code de retour (`0` ou `1`) si `return_code=True`

---

## 🧪 Exemple complet

```python
from commitly import Commitly

commitly = Commitly()
commitly.add("main.py")
message = commitly.generate_commit_message(ticket="#42")
commitly.save_message_to_file(message)
commitly.commit()
commitly.push()
```

---

## 📸 Démo visuelle

![Exemple complet](./image/exemple-1.png)


---

## 🧩 À propos du format de commit

Le message généré suit cette structure :

```text
<type>[étendue optionnelle]: <description>

[corps optionnel]

[pied optionnel]  ← ticket ici (#1234)
```

Exemples de type :
- `feat` : nouvelle fonctionnalité
- `fix` : correction de bug
- `docs` : documentation
- `refactor` : amélioration du code sans changement de comportement
- `chore` : tâches annexes (maintenance, mise à jour, etc.)

---

## 📋 Licence

MIT © 2025 Kouya Chance Boman Tosten

---

> Fini le syndrome du commit vide. Laissez **Commitly** écrire l’histoire de votre code.
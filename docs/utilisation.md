# 🚀 Utilisation de base

```python
from commitly.commitly import Commitly

commitly = Commitly()
commitly.add("main.py")
msg = commitly.generate_commit_message(ticket="#42")
commitly.save_message_to_file(msg)
commitly.commit()
```

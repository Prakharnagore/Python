# pipenv install django

# pipenv shell

# django-admin startproject project_name .

# python3 manage.py runserver

# python3 manage.py startapp movies

# python3 manage.py makemigrations

# python3 manage.py migrate

# python3 manage.py createsuperuser

# pipenv install django-tastypie

---

## Using pip instead of pipenv

pipenv crashes on this project (`AttributeError: module 'functools' has no attribute 'cache'`) because `.venv` uses Python 3.8. Use pip inside the venv instead.

### 1. Activate the virtual environment

```
source .venv/bin/activate
```

Check it's active: `python --version` should say `3.8.20`.

### 2. Install packages

```
python -m pip install "django-tastypie~=0.14.0" "django==2.1"
```

- Keep `"django==2.1"` in the command so Django isn't upgraded.
- `~=0.14.0` installs the latest 0.14.x; tastypie 0.15+ needs Django 4.2+.
- After installing, add the package to `Pipfile` under `[packages]` by hand.

Without activating: `.venv/bin/python -m pip install <package>`

### 3. Run the server

```
python manage.py runserver
```

Open http://127.0.0.1:8000/movies/ — stop with `Ctrl+C`.

### 4. Deactivate

```
deactivate
```

### Useful commands

- `python -m pip list` — show installed packages
- `python manage.py migrate` — apply migrations (run after adding `'tastypie'` to `INSTALLED_APPS`)

claude --resume 58805582-c09a-4c31-ad13-306005f5d0b6

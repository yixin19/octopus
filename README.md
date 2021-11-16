# Octopus
Octopus is a movie management system

# Setup developer environment
1. Install [docker](https://docs.docker.com/get-docker/).
1. If you don't have it, install python [3.9](https://www.python.org/downloads/release/python-395/)
1. Install pipenv with `pip3 install pipenv`. For MacOs you can install it and add it to your PATH
   with `brew install pipenv`
1. Place yourself in the root of this folder, then run `pipenv install --dev`
1. Install commitlint: `npm install -g @commitlint/{config-conventional,cli}`
1. Install pre-commit hook: `pre-commit install`.
1. Copy the `.env.local` to a `.env` file to have all environment variables.

# Build server

1. Run the container docker of postgres: `docker compose up -d`
2. Place yourself in the **octopus** folder, and run `python manage.py migrate`
3. Finally, run the django server: `python manage.py runserver`
   You can now access to your local server on this url [localhost:8000]()
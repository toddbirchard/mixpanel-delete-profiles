# Mixpanel Delete User Profiles

![Python](https://img.shields.io/badge/Python-v^3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Mixpanel](https://img.shields.io/badge/Mixpanel-v4.5.0-blue.svg?longCache=true&logo=flickr&style=flat-square&logoColor=white&colorB=5E81AC&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/mixpanel-delete-users.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/mixpanel-delete-users/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/mixpanel-delete-users.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/mixpanel-delete-users/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/mixpanel-delete-users.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/toddbirchard/mixpanel-delete-users/network)

Avoid Mixpanel overage charges by identifying and deleting incomplete user profiles.

## Getting Started

This script assumes you've exported a CSV of your Mixpanel users via the Mixpanel UI, as I'm too lazy to write a script to do this for you.

### Installation

Install and run this bot via any of the 3 methods below:

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/toddbirchard/mixpanel-delete-users.git
$ cd mixpanel-delete-users
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```

**Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)**:

```shell
$ git clone https://github.com/toddbirchard/mixpanel-delete-users.git
$ cd mixpanel-delete-users
$ pipenv shell
$ pipenv update
$ python3 main.py
```

**Installation via [Poetry](https://python-poetry.org/)**:

```shell
$ git clone https://github.com/toddbirchard/mixpanel-delete-users.git
$ cd mixpanel-delete-users
$ poetry shell
$ poetry update
$ poetry run
```

### Configuration

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `MIXPANEL_API_TOKEN`: Your Mixpanel API token.

*Remember never to commit secrets saved in .env files to Github.*
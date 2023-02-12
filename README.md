<h1 align="center">Mini OpenAI Telegram bot</h1>
<p align="center">
  <a target="_blank" href="https://www.python.org/downloads/" title="Python Version"><img src="https://img.shields.io/badge/python-%3E=_3.11-purple.svg"></a>
  <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/LagrangeH/MiniOpenAITelegramBot">
  <img alt="GitHub" src="https://img.shields.io/github/license/LagrangeH/MiniOpenAITelegramBot">
</p>

## How to setup

1. [Install Python 3.11](https://www.python.org/downloads/)
2. [Install Poetry](https://python-poetry.org/docs/#installation)
3. Clone repository
```sh
git clone https://github.com/LagrangeH/MiniOpenAITelegramBot.git
```
4. Go to the root directory of the project
```sh
cd MiniOpenAITelegramBot/
```
5. Create Poetry virtual environment
```sh
poetry env use python3.11
```
6. Install dependencies
```sh
poetry install
```
7. Create `.env` and paste template from [`.env.dist`](./.env.dist)
```sh
cp .env.dist .env
```
8. Substitute your environment variable values in `.env`


## How to use
1. Update dependencies
```sh
poetry update
```
2. Run [`src/__main__.py`](./src/__main__.py)
```sh
poetry run python src/__main__.py
```

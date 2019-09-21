# Python3 Docker Starter

-   [nodemon](https://www.npmjs.com/package/nodemon) will be watching your python scripts and updating automatically if there are any changes

## Change Command

-   `docker-compose.yaml`
-   `main.py` will be executed by default

```yaml
command: src/main.py
```

-   Execute mutiple scripts in `src` folder at once

```yaml
command: run.sh
```

## Start

```bash
docker-compose up
```

## Clean Up

```bash
docker-compose down
```

## Install Python Modules

-   `requirements.txt`

```
bs4
regex
feedparser
```

-   Restart

```bash
docker-compose up --build
```

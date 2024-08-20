An expanding collection of easily adaptable **Aiogram** templates for building Telegram bots.

<br>

# Features
- Easily extensible and maintainable code
- Simple and clean architecture
- **RedisStorage** caching for retaining message history
- Ready-to-use **Alembic** migration system
- Modern DB engine

### Template 1
- Design UIs easily with **Aiogram Dialog**
### Template 2
- Localization with **Project Fluent**
- Enviroment configuration with **Poetry**

<br>
  
# Dependencies
- [Python 3.x](https://www.python.org/downloads/)
- [Aiogram 3.x](https://github.com/aiogram/aiogram)
- [Aiogram Dialog 2](https://github.com/Tishka17/aiogram_dialog)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/docs/) 
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Project Fluent](https://projectfluent.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Poetry](https://python-poetry.org/)

<br>

# Setup & usage
### [Template 1](https://github.com/avrtt/tg-bot-boilerplates/tree/main/template-1)

Clone the repository and navigate to the template folder:
```bash
git clone git@github.com:avrtt/tg-bot-boilerplates.git
cd tg-bot-boilerplates/template-1
```

Create an **.env** file with the following contents and fill the lines (`<...>`):

```env
API_TOKEN=<...>
POSTGRES_USER=bot_user
POSTGRES_PASSWORD=<...>
POSTGRES_DB=bot_db
DB_HOST=db
DB_PORT=5432
DB_NAME=bot_db
DB_USER=bot_user
DB_PASS=<...>
```

Build:
```shell
docker-compose up --build
```

In the **bot** container, run:
```shell
alembic revision --autogenerate -m "init"
```

For using migrations:
```shell
alembic upgrade head
```

For shutting down the bot:
```shell
docker-compose down -v
```

<br>

### [Template 2](https://github.com/avrtt/tg-bot-boilerplates/tree/main/template-2)

Rename `docker-compose.example.yml` to `docker-compose.yml` and `.env.dist` to `.env`. Configure `.env` in the same way.

Build:
```shell
make app-build
```

Start:
```shell
make app-run
```

Setup environment:
```shell
poetry install
```

Update DB tables structure. Make the migration script:
```shell
make migration message=MIGRATION_DESCRIPTION
```

Run migrations:
```shell
make migrate
```

### Translation
For updating translations, parse the new localization keys:
```shell
make i18n locale=TRANSLATION_LOCALE
```
Write new translations in `.ftl` (`translations/TRANSLATION_LOCALE`) and restart the bot.

<br>

# License
This templates are licensed under the MIT License - see the LICENSE file for details.




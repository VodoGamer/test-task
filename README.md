# Тестовое задание для bewise.ai

## Как запустить?

- Docker-compose

```sh
cp .env.example .env # изменять .env необязательно
docker-compose up --build
```

- Вручную

```sh
cp .env.example .env
vim .env # заполнить данные о заранее созданной таблице в Postgres
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src:app
```

### Примечания (Docker-compose)

- Для запуска в фоновом режиме добавить аргумент -d к команде второго пункта
- В `.env` можно указать порт, на котором будет работать сервис

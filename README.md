# Тестовое задание для bewise.ai

## Как запустить?

```sh
cp .env.example .env
docker-compose up --build
```

## Примечания

- При возникновении ошибки доступа к директории `postgres_data`:

```sh
sudo chmod -R 777 ./postgres_data
```

- Для запуска в фоновом режиме добавить аргумент -d к команде второго пункта
- В `.env` можно указать порт, на котором будет работать сервис
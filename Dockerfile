FROM python:3.11-slim

ENV TZ Europe/Moscow

ARG PROJECT_NAME
WORKDIR /$PROJECT_NAME

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

CMD [ "uvicorn", "src:app" ]
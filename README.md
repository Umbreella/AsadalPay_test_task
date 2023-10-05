# Asadal pay (REST-API)

## Backend

![python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white&style=for-the-badge&)
![fastapi](https://img.shields.io/badge/fastapi-009688?logo=fastapi&logoColor=white&style=for-the-badge&)
![poetry](https://img.shields.io/badge/poetry-60A5FA?logo=poetry&logoColor=white&style=for-the-badge&)

## Testing

![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

## Cloud & CI/CD

![docker](https://img.shields.io/badge/docker-2496ED?logo=docker&logoColor=white&style=for-the-badge&)
![githubactions](https://img.shields.io/badge/githubactions-2088FF?logo=githubactions&logoColor=white&style=for-the-badge&)

---

## Description

[Task Description](TaskDescription.pdf)

## Getting Started

### Environment variables

To run the application, you need to set all the environment variables:

* **[.env.mailer](.env)**

## Docker

* docker-compose.yaml

```yaml
version: "3"

services:
  smtp4dev:
    image: rnwood/smtp4dev:latest
    container_name: smtp4dev
    ports:
      - 8080:80

  asadalpay_test_task:
    image: umbreella/asadalpay_test_task:latest
    container_name: asadalpay_test_task
    ports:
      - 8000:8000
    environment:
      APP_APPLICATION_MAIL_SERVER: 'smtp4dev'
      APP_APPLICATION_MAIL_FROM: 'admin@admin.admin'
    depends_on:
      - smtp4dev
```

## Endpoints

* REST-API Docs

```
[your_ip_address]/api/docs/
```

## Logs

```commandline
/usr/src/app/mailer.log
```
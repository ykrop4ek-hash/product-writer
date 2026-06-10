# Product Description Generator

Веб-сервис для генерации описаний товаров с помощью AI (DeepSeek V3).

## Стек
- Python 3.11, Django 4.2
- DeepSeek API (OpenAI-compatible)

## Запуск локально

1. Клонировать репозиторий
2. Установить зависимости: `pip install -r requirements.txt`
3. Создать `.env` файл:
4. 
DEEPSEEK_API_KEY=sk-...
SECRET_KEY=твой_django_secret_key
`python manage.py migrate`
5. `python manage.py runserver`

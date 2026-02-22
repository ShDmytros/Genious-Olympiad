FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Код НЕ копіюємо — він прийде через volume

EXPOSE 8000

# Використовуємо Gunicorn замість runserver
CMD ["gunicorn", "studyease.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "300"]
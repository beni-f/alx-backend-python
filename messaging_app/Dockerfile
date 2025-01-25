FROM python:3.10

WORKDIR /messaging_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "messaging_app.wsgi:application", "--bind", "0.0.0.0:8000"]

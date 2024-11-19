FROM python:3.9

WORKDIR /app

RUN git clone https://github.com/djtoler/dep9be2.git .

WORKDIR /app/backend

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
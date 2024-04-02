# indica al contenedor desde que imagen empezar
FROM python:3.12.0-alpine3.17
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000
# comando que se ejecutara al iniciar el contenedor

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# docker build -t appointment .
# -t : el nombre que se le sa al contenedor
# . : que busque Dockerfile en el directorio actual
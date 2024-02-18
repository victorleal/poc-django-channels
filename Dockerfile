FROM python:3.11-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends default-libmysqlclient-dev python3-dev libpq-dev ldap-utils libsasl2-dev libldap2-dev

WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./src .

EXPOSE 8000

CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]

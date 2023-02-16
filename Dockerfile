FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN python3 manage.py collectstatic

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
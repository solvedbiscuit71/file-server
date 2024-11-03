FROM python:3.11-alpine

WORKDIR /root/app

COPY . .

RUN ["mkdir", "/root/vault"]

VOLUME ["/root/vault"]

ENV VAULT_DIR=/root/vault

RUN ["pip", "install", "-r", "requirements.txt"]

EXPOSE 8000 8000

CMD ["fastapi", "run", "--port", "8000", "server.py"]

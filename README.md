# File Server

A simple HTTP File Server for transferring files through LAN.

## Build and Run

Build the docker image
```bash
docker buildx build -t file-server .
```

Run the docker container
```bash
docker run -d --rm -v ~/vault:/root/vault -p 80:8000 --name fs file-server
```

Stop the docker container
```bash
docker stop fs
```

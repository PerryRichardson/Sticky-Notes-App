# Sticky Notes App

A Django-based sticky notes application, containerised using Docker.

## Prerequisites

- Docker Desktop installed and running

## Implementation Steps

### 1. Clone the repository
```bash
git clone https://github.com/PerryRichardson/Sticky-Notes-App.git
cd Sticky-Notes-App
```

### 2. Build the Docker image
```bash
docker build -t sticky-notes-app ./
```

### 3. Run the container
```bash
docker run -p 8000:8000 sticky-notes-app
```

### 4. Access the application
Open your browser and navigate to:
```
http://127.0.0.1:8000/notes/
```

### 5. Stop the container
Press `CTRL + C` in the terminal to stop the running container.

## Docker Hub

The image is also available on Docker Hub:
```
docker pull perryrich/sticky-notes-app
```
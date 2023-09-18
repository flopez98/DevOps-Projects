# Flask-Redis Docker Lab

This is a sample project that demonstrates how to use Flask with Redis, containerized with Docker, and orchestrated with Docker Compose. The application serves a simple API to interact with a Redis data store.

## Project Structure

Here's a brief overview of the project's structure:

```
.
├── Dockerfile             # Dockerfile for building the Flask app
├── README.md              # This README file
├── app.py                 # The Flask application
├── docker-compose.yml     # Docker Compose file to manage services
└── requirements.txt       # Python package dependencies
```

## Prerequisites

- Docker
- Docker Compose
- Basic knowledge of Python and Flask

## Getting Started

### Build and Run the Containers

Use Docker Compose to build and start the application and Redis containers.

```bash
docker-compose up --build
```

### Test the Application

Open your web browser or use `curl` to access the application:

- **Hello World**: [http://localhost:5000/](http://localhost:5000/)
- **Counter**: [http://localhost:5000/counter](http://localhost:5000/counter)

The Counter endpoint will increment the counter value in Redis every time you refresh the page.

## Cleanup

To stop and remove the running containers, use:

```bash
docker-compose down
```
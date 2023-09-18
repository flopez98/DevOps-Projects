# Flask-Redis-Frontend Docker Lab

This is a sample project that demonstrates how to use Flask with Redis and a React-based frontend, all containerized with Docker, and orchestrated with Docker Compose. The application serves a simple API to interact with a Redis data store and a frontend to display the counter.

## Project Structure

Here's a brief overview of the project's structure:

```bash
├── backend                 # Backend service directory
│   ├── app.py              # The Flask application
│   ├── Dockerfile          # Dockerfile for building the Flask app
│   └── requirements.txt    # Python package dependencies
├── frontend                # Frontend service directory
│   ├── Dockerfile          # Dockerfile for the React frontend
│   ├── package.json        # Frontend package configuration and dependencies
│   ├── package-lock.json   # Lock file for frontend dependencies
│   ├── public              # Static assets and index.html
│   ├── README.md           # Frontend-specific README
│   └── src                 # React application source files
├── docker-compose.yml      # Docker Compose file to manage services
└── README.md               # This README file (main documentation)
 
```

## Prerequisites

- Docker
- Docker Compose
- Basic knowledge of Python, Flask, and React

## Getting Started

### Build and Run the Containers

Use Docker Compose to build and start the application, frontend, and Redis containers.

```bash
docker-compose up --build
```

### Access the Application

Open your web browser or use `curl` to interact with the application:

- **Frontend**: [http://localhost:3000/](http://localhost:3000/)
- **Backend Hello World**: [http://localhost:5000/](http://localhost:5000/)
- **Backend Counter**: [http://localhost:5000/counter](http://localhost:5000/counter)
- **Backend Get Counter API**: [http://localhost:5000/get_counter](http://localhost:5000/get_counter)

The Frontend will display a counter value stored in Redis, and you can also reload the counter. The Backend provides multiple endpoints, including `/counter` for direct interaction with Redis, and `/get_counter` which is used by the frontend to fetch the counter value.

## Cleanup

To stop and remove the running containers, use:

```bash
docker-compose down
```
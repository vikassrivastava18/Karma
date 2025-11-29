# karma
## About the Project

Karma is a day-to-day task tracker designed to help users organize and manage their daily activities efficiently. Built using Docker, Django, and Vue.js, this application could be used for tracking tasks, setting priorities, and staying productive.
![Karma Logo](https://i.ibb.co/20DgyzGT/Screenshot-from-2025-06-13-10-08-19.png "Karma Logo")
## Features

- Create, update, and delete tasks.
- Set priorities and deadlines for tasks.
- View tasks in an intuitive and user-friendly interface.
- Track progress and stay organized.

## Prerequisites

Before running the application, ensure you have the following installed:

- Docker
- Docker Compose

## Running the Application

Follow these steps to run the application using Docker:

1. Clone the repository:
    ```bash
    git clone https://github.com/vikassrivastava18/karma.git
    cd karma
    ```

2. Build the Docker containers:
    ```bash
    docker-compose build
    ```

3. Start the application:
    ```bash
    docker-compose up
    ```

4. Access the application in your browser at `http://localhost:8080`.

## Stopping the Application

To stop the application, run:
```bash
docker-compose down
```


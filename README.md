# Script-Runner-Plus

Follow these steps to set up project:

## Prerequisites

1. Python installed on your system
2. Docker and docker-compose installed on your system

## Project Requirements

Project Name: **PythonScript Management and Execution**

**Description:**
Create a Python application that enables users to manage Python scripts through a tkinter desktop app and a Django web app. Users can create, delete, update, and view Python scripts, execute them locally, and capture execution results in a database. The project consists of two parts: a tkinter app and a Django app, both using the same database schema.

**Part 1: tkinter Python Script Management App**

- Users can create, delete, update, and view Python scripts.
- A play button is provided for each script to execute it locally.
- Execution results, including errors, are captured in a database.

**Database Schema:**

**Table 1: Script**
- Fields:
  - Script Name
  - Script Body

**Table 2: ExecutionLog**
- Fields:
  - script (foreign key)
  - Output
  - Execution Started At
  - Execution Completed At
  - Execution Time (in seconds)

**Part 2: Django Web App**

- A Django app is created with the same database schema.
- Data created, updated, or deleted in the tkinter app is synchronized with the Django app.
- Execution logs from script executions are propagated to the Django app.
- Data is displayed to users through Django templates.

**Integration:**

- MQTT is used for real-time data synchronization between the tkinter app and the Django app.

**Project Name:** PythonScript Sync and Execute Manager


## Getting Started

1. Clone this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the project files are located using the `cd` command.

### Set Environment variables

Create `.env` file and add below-mentioned variables at root directory of project.

    POSTGRES_DB=tk
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    
    MQTT_BROKER_HOST=mqtt
    MQTT_BROKER_PORT=1883
    
    REDIS_HOST=redis
    REDIS_PORT=6379



## Running the Project

Use Docker to configure and get started with all the required services.

    # For first time: To build images and run dockers
    docker-compose up --build

    # After first time: To start dockers from builded images
    docker-compose up
    

### To stop docker

Press `Ctrl+C` and then you can enter below command to remove containers
    
    docker-compose down

#### Navigate to `0.0.0.0:8000`, it will open django app in browser.

Note: After the django app and other services are up, you can continue with the `tkinter_app`. 
Instructions for starting tkinter app is mentioned in `./tkinter_app/README.md`
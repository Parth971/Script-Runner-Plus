# Tkinter + Django Application

Follow these steps to set up project:

## Prerequisites

1. Python installed on your system
2. Docker and docker-compose installed on your system

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
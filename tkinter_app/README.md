# Tkinter App

Follow these steps to set up and run the Python script:

## Prerequisites

1. Python installed on your system.
2. Postgres database installed and running
3. MQTT installed and running

## Getting Started

1. Clone this repository or download the script files to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script files are located using the `cd` command.

4. Create a virtual environment (optional but recommended):

    ```shell
    python -m venv venv
    ```

5. Activate the virtual environment:
    
    ```shell
    On Windows:
    venv\Scripts\activate

    On macOS and Linux:
    source venv/bin/activate
    ```

## Set Environment variables
Create `.env` file and add below-mentioned variables 

    POSTGRES_DB=tk
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5433
    
    MQTT_BROKER_HOST=localhost
    MQTT_BROKER_PORT=1883

Note: Can use docker to run postgres and mqtt services, make sure to update port and host values 

   
## Installation
Install the required Python packages by running the following command:

    pip install -r requirements.txt

   
## Running the Script
Install the required Python packages by running the following command:

    python main.py


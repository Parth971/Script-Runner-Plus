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

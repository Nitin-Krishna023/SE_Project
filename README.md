# BookYourTicket - CSCI-P565 Software Engineering Project

Welcome to the README for our CSCI-P565 Software Engineering Project, BookYourTicket! In this document, we will provide you with comprehensive instructions on how to get started with developing and running our software project. Please follow these steps carefully to ensure a smooth setup and execution.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- **Python 3.10+**: BookYourTicket is developed using Python, so you need to have Python 3.10 or a higher version installed on your machine.

## Setting up a Virtual Environment

We recommend using a virtual environment to manage project dependencies and isolate them from your system's Python installation. Here's how you can set up a virtual environment:

1. Open a terminal window.

2. Create a virtual environment named "venv" by running the following command:
   
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment by entering the following command:

   ```bash
   source venv/bin/activate
   ```

   Activating the virtual environment ensures that you are working within an isolated environment where you can install project-specific dependencies.

## Installing Project Dependencies

With the virtual environment activated, you can now install all the required dependencies by running the following command from the project's root directory:

```bash
pip3 install -r requirements.txt
```

This command will fetch and install all the necessary libraries and packages needed for BookYourTicket to run successfully.

**Note**: Depending on your operating system, you may need to install additional components or libraries to enable the creation of a virtual environment. Alternatively, you can choose to skip the virtual environment step and install all the packages directly onto your system. However, using a virtual environment is considered a best practice for managing dependencies.

## Setting up the Database

To run BookYourTicket, you'll need a database. Follow these steps to set up a test database:

1. Run the following command to create the database:

   ```bash
   python3 create_db.py
   ```

2. Copy the `config.py.example` file and rename it to `config.py`. This file contains configuration settings for the project, including database connection details.

## Running BookYourTicket

With your environment configured and the database set up, you can now run BookYourTicket locally. Simply execute the following command:

```bash
python3 run.py
```

This command will start the BookYourTicket website locally, allowing you to access and test the application in your web browser.

Congratulations! You've successfully set up and launched the BookYourTicket software engineering project. You can now begin developing and exploring its features. If you encounter any issues or have questions, please refer to our documentation or reach out to our project team for assistance. Happy coding!

## Building and Running the Docker Container

To simplify the deployment process, you can run the BookYourTicket software project within a Docker container. Follow these steps to build and run the Docker container for BookYourTicket:

### Prerequisites

Before you proceed, make sure you have Docker installed on your system. You can download and install Docker from the official website: [Docker Download](https://www.docker.com/get-started).

### Building the Docker Image

1. Open a terminal window.

2. Navigate to the root directory of the BookYourTicket project where the `Dockerfile` is located.

3. Build the Docker image by running the following command:

   ```bash
   docker build -t bookyourticket .
   ```

   This command creates a Docker image named `bookyourticket` based on the instructions in the `Dockerfile`.

### Running the Docker Container

4. After successfully building the Docker image, you can start a Docker container by executing the following command:

   ```bash
   docker run -d -p 8000:8000 bookyourticket
   ```

   - The `-d` flag runs the container in detached mode.
   - The `-p` flag maps port 8000 inside the container to port 8000 on your host system.

### Accessing BookYourTicket

5. Open your web browser and navigate to `http://localhost:8000` to access the BookYourTicket application running within the Docker container.

Now you have successfully built and run the BookYourTicket software project inside a Docker container. You can interact with the application by accessing it through your web browser. If you encounter any issues or have questions, please refer to our documentation or reach out to our project team for assistance. Happy exploring!
# CSV to JSON Converter - Flask Application

This is a simple Flask application that allows you to upload a CSV file and converts it to JSON format. It includes a REST API built using `flask_restful` to handle the conversion process, and the application is containerized using Docker.

## Features

- Upload a CSV file via a POST request.
- Converts CSV data into JSON format and returns it as a response.
- Easy setup with Docker for running locally or deploying in any environment.

---

## 1. Running the Application Locally

You can run this application locally using Docker. Below are the steps to get it up and running.

### 1.1. Clone the Repository

Start by cloning this repository from GitHub:

```bash
git clone https://github.com/yourusername/csv-to-json-flask.git
cd csv-to-json-flask
```

### 1.2. Build the Docker Image

Once inside the repository directory, you can create the Docker image using the `Dockerfile` provided:

```bash
docker build -t yourusername/csv-to-json-flask:v1.0 .
```

This will create a Docker image named `csv-to-json-flask` based on the code and dependencies specified in the `Dockerfile`.

### 1.3. Run the Docker Container

After the image has been built, you can run the Docker container with the following command:

```bash
docker run -d -p 5000:5000 yourusername/csv-to-json-flask:v1.0
```

This command will:
- Run the container in detached mode (`-d`).
- Map port `5000` of your local machine to port `5000` of the container, which is where the Flask application is running.

### 1.4. Testing the Application

You can test the application using **Postman** or **cURL**.

**Using Postman:**

- Method: `POST`
- URL: http://localhost:5000/upload_csv
- Body: Choose "form-data", add a key called `file` and upload the CSV file you want to convert.

**Using cURL:**

```bash
curl --location 'http://localhost:5000/upload_csv' \
--form 'file=@"/path/to/your/file.csv"'
```
Replace `"/path/to/your/file.csv"` with the path to your CSV file. The response will be the JSON conversion of your CSV data.

## 2. Development Environment Setup

If you want to run the application without Docker (for development or debugging):

1. Install Python 3.8 or higher.
2. Clone the repository (as shown above).
3. Set up a virtual environment and install the dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
4. Run the Flask app:
   ```bash
    flask run
   ```
By default, the app will run at `http://localhost:5000`.

## 3. Docker Hub Image

Alternatively, you can pull and run the pre-built Docker image from Docker Hub.

### Public Docker Hub Link
You can pull the Docker image using the following command:
```bash
docker pull bvpipare18/csv-to-json-app
```
Then, run the Docker container with:
```bash
docker run -d -p 5000:5000 bvpipare18/csv-to-json-app
```

## 4. API Documentation

### Endpoint: `/convert`
- Method: `POST`
- Description: Accepts a CSV file, converts it to JSON, and returns the JSON data.
- Content-Type: `multipart/form-data`
- Body:
  - Key: `file` (type: file)
  - Value: CSV file to be converted

- Response: JSON representation of the CSV file.

## 5. License

Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.
...
[Full text available at http://www.apache.org/licenses/LICENSE-2.0]



   

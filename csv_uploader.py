from flask_restful import Resource
from flask import request
import csv
import io

class UploadCSV(Resource):
    def post(self):
        if 'file' not in request.files:
            return {"error": "No file part in the request"}, 400

        file = request.files['file']

        if file.filename == '':
            return {"error": "No file selected"}, 400

        if not file.filename.endswith('.csv'):
            return {"error": "File is not a csv"}, 400

        file_stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_reader = csv.DictReader(file_stream)

        csv_data = [row for row in csv_reader]

        return csv_data, 200
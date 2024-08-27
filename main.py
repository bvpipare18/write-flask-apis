from flask import Flask
from flask_restful import Api
from csv_uploader import UploadCSV


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(UploadCSV, '/upload_csv')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
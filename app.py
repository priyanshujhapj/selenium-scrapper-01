from flask import Flask, request, Response
from scrapper import main
from merge import merge_files, clean
import subprocess


app = Flask(__name__)

@app.route('/', methods=['GET'])
def custom_hello():
    return Response("{'RES-STATUS': 'OK-200'}", status=200)

@app.route('/scrape', methods=['GET'])
def scrape_data():
    page = request.args['page']
    size = request.args['size']
    token = request.args['token']
    if token == "624d1ef9e048c1869166ddc8":
        main(int(page), int(size))
        json_object = merge_files(int(page))
        clean(int(page))
        return json_object
    else:
        return f'Token not matched!'

if __name__ == "__main__":
    command = 'gunicorn app:app --workers 4 --bind 0.0.0.0:3000 --timeout 300'
    server_process = subprocess.Popen(command, shell=True)
    # app.run()
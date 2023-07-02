from flask import Flask, request, Response
from scrapper import main
from merge import merge_files, clean

app = Flask(__name__)

@app.route('/', methods=['GET'])
def custom_hello():
    print("custom_hello()")
    return Response("{'RES-STATUS': 'OK-200'}", status=200)

@app.route('/scrape', methods=['GET'])
def scrape_data():
    print("scrape_data() triggered")
    page = request.args['page']
    print(f'PAGE:- {page}')
    size = request.args['size']
    print(f'SIZE:- {size}')
    token = request.args['token']
    print(f'TOKE:- {token}')
    if token == "624d1ef9e048c1869166ddc8":
        main(int(page), int(size))
        json_object = merge_files(int(page))
        clean(int(page))
        return json_object
    else:
        return f'Token not matched!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
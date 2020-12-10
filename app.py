from flask import Flask, render_template, send_from_directory, request
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addhistory')
def add_history():
    return render_template('add_history.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        file = database.write(f'\n{email}, {name}, {message}')


def connect_to_mongo():
    uri = 'mongodb+srv://samami:jWsSXAlSaXbge2eP@cluster0.vhyil.mongodb.net/general?retryWrites=true&w=majority'
    client = MongoClient(uri)
    db = client.general
    return db


def add_data(collection_name, data):
    db = connect_to_mongo()
    collection = db[collection_name].insert_one(data)


def get_data(collection_name):
    db = connect_to_mongo()
    data = db[collection_name].find()
    return data


@app.route('/submit_history', methods=['POST', 'GET'])
def submit_history():
    if request.method == 'POST':
        data = request.form.to_dict()
        add_data('work_history',data)
    return '<a href=http://ztmweb.samami.com/showhistory>Show History</a>'

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_mongo(data)
    return 'Form Submitted'


@app.route('/showhistory')
def show_history():
    data = list(get_data('work_history'))
    return render_template('show_history.html', data = data)


if __name__ == '__main__':
    app.run()


# mongodb passsword jWsSXAlSaXbge2eP
# mongousername samami
# mongodb+srv://samami:<password>@cluster0.vhyil.mongodb.net/<dbname>?retryWrites=true&w=majority
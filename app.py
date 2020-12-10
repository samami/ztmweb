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

def write_to_mongo(data):
    uri = 'mongodb+srv://samami:jWsSXAlSaXbge2eP@cluster0.vhyil.mongodb.net/general?retryWrites=true&w=majority'
    client = MongoClient(uri)
    db = client.general
    collection = db.firstcollection
    collection.insert_one(data)
    print("hello")
    for item in collection.find():
        print(item)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_mongo(data)
    return 'Form Submitted'



if __name__ == '__main__':
    app.run()


# mongodb passsword jWsSXAlSaXbge2eP
# mongousername samami
# mongodb+srv://samami:<password>@cluster0.vhyil.mongodb.net/<dbname>?retryWrites=true&w=majority
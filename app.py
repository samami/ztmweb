from flask import Flask, render_template, request, url_for
import dataio

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/addhistory')
def add_history():
    return render_template('add_history.html')


@app.route('/submit_history', methods=['POST', 'GET'])
def submit_history():
    if request.method == 'POST':
        data = request.form.to_dict()
        dataio.add_data('work_history',data)
    return '<a href=' + url_for('show_history') + '>Show History</a>'

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        dataio.add_data('first_collection', data)
    return 'Form Submitted'


@app.route('/showhistory')
def show_history():
    data = list(dataio.get_data('work_history'))
    return render_template('show_history.html', data = data)


if __name__ == '__main__':
    app.run()

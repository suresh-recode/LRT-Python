from flask import Flask, request

app = Flask("lrt")


@app.route('/testing', methods=['GET'])
def hello_world():
    return 'Get request'


@app.route('/testing1', methods=['POST'])
def hello_world1():
    return 'POST request'


@app.route('/testing2', methods=['POST'])
def hello_world2():
    if request.form.get('password') == 'lrt':
        val1 = int(request.form.get('value1'))
        val2 = int(request.form.get('value2'))
        return str(val1 + val2)
    else:
        return "Invalid password"


app.run()
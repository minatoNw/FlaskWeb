from flask import Flask, Response, request
import requests
import hashlib


app = Flask(__name__)
salt = "UNIQUE_SALT"
default_name = 'Minato'


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    name = default_name
    if request.method == 'POST':
        name = request.form['name']
        i = requests.get('http://172.100.0.3:8080/monster/')

    #salted_name = salt + name
    #name_hash = hashlib.sha256(salted_name.encode()).hexdigest()


    header = '<html><html><title>minato web </title></head><body>'
    body = '''<form method="POST">
                Hello <input type="text" name="name" value="">
                <input type="submit" value="submit">
                </form>
                <p>You looks like a:
                <img src="/monster/
            '''
    body += name + '"/>'
    footer = '</body></html>'

    return header + body + footer


@app.route('/monster/<name>')
def get_identicon(name):
    r = requests.get('http://172.100.0.3:8080/monster/' + name + '?size=80')
    image = r.content

    return Response(image, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
            

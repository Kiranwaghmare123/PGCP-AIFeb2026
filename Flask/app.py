from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "1234":
        return render_template('success.html', user=username)
    else:
        return "<h3>Invalid Username or Password</h3>"

if __name__ == '__main__':
    app.run(debug=True)
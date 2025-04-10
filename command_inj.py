from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Ping a Host</h2>
        <form action="/ping" method="get">
            Host: <input name="host" type="text">
            <input type="submit" value="Ping">
        </form>
    '''

@app.route('/ping')
def ping():
    host = request.args.get('host', '')
    command = f"ping -c 2 {host}"
    
    # Vulnerable to command injection
    output = os.popen(command).read()
    
    return f"<pre>{output}</pre>"

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/time')
def time():
    now = datetime.now()
    return str(now)

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
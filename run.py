from flask import Flask, jsonify
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def display_time():
    zone = datetime.now(ZoneInfo("America/New_York"))
    return jsonify(message="Current EST time",now=zone.isoformat(),readable_format=zone.strftime("%m/%d/%Y %I:%M %p"))

app.run(host='0.0.0.0',
        port=8080,
        debug=True)

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	return "Hello World"

@app.route("/devices/input")
def devices_inputs():
	return "Hello Input Devices"

@app.route("/devices/chromecasts")
def devices_chromecasts():
	return "Hello Chromecast Devices"

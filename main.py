from flask import Flask, render_template, send_from_directory
app = Flask('app')

@app.route('/')
def index():
    return send_from_directory('static/secret', 'index.html')

app.run(host='0.0.0.0', port=443, debug=True)

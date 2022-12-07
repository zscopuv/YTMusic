from flask import Flask, render_template, request, send_file
import logics as log

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/r')
def render():
    try:
        link = request.args.get('link')
    except:
        link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    log.create(link)
    return render_template("render.html")

@app.route('/f')
def file():
    try:
        link = request.args.get('link')
    except:
        link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    fileName = log.getName(link)

    return send_file(f"cache/{fileName}")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

app.run(host='0.0.0.0', port=81)

from flask import Flask, render_template, request, Response, send_file
import numpy as np
import pandas as pd
import sys
import os

PROJECT_DIR = os.getcwd()
TEMPLATE_DIRS = PROJECT_DIR

app=Flask(__name__, template_folder=TEMPLATE_DIRS)
app.config["CACHE_TYPE"] = "null"

@app.route("/")
def index():
    try:
        return render_template('webpages.html')
    except:
        return render_template('error.html', errormessage=sys.exc_info())

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_resource(path):  # pragma: no cover
	ext = path[-4:] 
    if ext in ['.jpg', '.gif', '.png', '.bmp']:
		try:
			return send_file(filename, mimetype='image/'+ext)
		except:
			return render_template('error.html', errormessage=sys.exc_info())

    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(os.getcwd(), path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    try:
        with open(complete_path, 'r') as content_file:
            content = content_file.read()
            #content = get_file(complete_path)

        return Response(content, mimetype=mimetype)
    except:
        return render_template('error.html', errormessage=sys.exc_info())

if __name__ == '__main__':
    app.debug=True
    app.run()

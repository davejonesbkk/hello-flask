from flask import Flask
from flask import render_template
from datetime import datetime
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template('base.html')

@app.context_processor
def inject_now():
	return {'now': datetime.utcnow()}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

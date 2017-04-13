from bottle import Bottle, run
from wordcount1.1.py import words, wordcount
app = Bottle()

@app.route('/<filename>/<word>')
def f():
    if filename='input1.1':
        return  '''<p>
        {wordcount[word]}
        </p>'''

run(app, host='0.0.0.0', port=8080, debug=True)

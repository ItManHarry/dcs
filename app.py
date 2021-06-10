from flask import Flask
#创建Flask实例
app = Flask('am')
@app.route('/dcs')
def index():
    return '<h1>DCS Part</h1>'
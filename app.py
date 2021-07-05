from flask import Flask,render_template,request
import pyshorteners

app=Flask(__name__)


@app.route('/',methods=['POST','GET'])
def homepage():
    return render_template('home.html')
@app.route('/natija',methods=['POST','GET'])
def natija():
    key=request.form.get('text')
    shortener=pyshorteners.Shortener()
    result=shortener.tinyurl.short(key)
    return render_template('home.html',result=result)

if __name__=='__main__':
    app.run(debug=True)

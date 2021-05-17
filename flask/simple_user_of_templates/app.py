from flask import Flask, render_template
import subprocess

app=Flask('myiiec')

@app.route('/search')
def mysearch():
    data=subprocess.getoutput('date /t')
    return(data)

@app.route('/mail')
def mymail():
    return render_template('e.html')

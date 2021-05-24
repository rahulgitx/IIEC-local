from flask import Flask, render_template, request
import subprocess
import os

app=Flask('realmyapp')

@app.route('/form')
def myform():
    data=render_template('myform.html')
    return data

@app.route('/tech', methods=['GET'])
def mycmd():
    cmd=request.args.get('cmd')  
    return "<pre>"+cmd+'</pre>'
    #return "<pre>"+subprocess.getoutput(cmd)+'</pre>' # <-- this will be used in linux

app.run(port=555, debug=True)
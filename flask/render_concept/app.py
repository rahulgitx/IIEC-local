from flask import Flask, render_template, request
import subprocess

app=Flask('realmyapp')

@app.route('/form')
def myform():
    data=render_template('myform.html')
    return data

@app.route('/tech', methods=['Get'])
def mycmd():
    mycmd=request.args.get('cmd')  
    return "<pre>"+'cmd'+'</pre>'
    #return "<pre>"+subprocess.getoutput(mycmd)+'</pre>'  <-- this will be used in linux

app.run(port=555, debug=True)
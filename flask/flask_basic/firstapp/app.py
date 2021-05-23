from flask import Flask

app=Flask('alqaeda')

@app.route('/mail')
def mailing():
    print('hello')
    return('mail')

@app.route('/search')
def searching():
    return('searching now...')
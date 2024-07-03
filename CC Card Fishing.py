from flask import *
app=Flask(__name__)
@app.route('/')
def bachi():
        return 'send this link in victim :http://bachi.free.nf/new.html'

if __name__=='__main__':
        app.run()
#-*- coding: UTF-8 -*-
from flask import Flask , url_for, render_template ,request
import subprocess
import os, sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/')
def index():
    p=subprocess.Popen('ls static/video', shell=True, stdout=subprocess.PIPE)
    files=p.stdout.readlines()
    if files: # files not empty
        return render_template('index.html', files=files)
    else:
        return render_template('404.html', error="emptydir"), 404

@app.route('/<videofile>')
def play(videofile):
    user_agent=request.headers.get('User-Agent')
    if os.path.exists('static/video/' + videofile):
        return render_template('player.html', user_agent=user_agent, videofile=videofile)
    else :
        return render_template('404.html', error="nofile"), 404

if __name__ == '__main__':
    #app.run(port=8000)
    app.run(host='0.0.0.0',port=8000 , debug=True)


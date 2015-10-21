import time
from flask import Flask
from findStrings import pronounCount
from celery import group, subtask
from driver import app

app = Flask(__name__)

@app.route("/")
def allTheTweets():
    #for x in range(0,20):
    
    s = subtask("findStrings.pronounCount","tweets_19.txt")    

    grouped = group(s)
    result = grouped()
    while(result.ready() == False):
        time.sleep(2)
    print result

    
#if __name__ == "__main__":
#    app.run()
    

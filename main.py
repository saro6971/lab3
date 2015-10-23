import time
from findStrings import pronounCount
from celery import group, subtask
from flask import jsonify
from collections import Counter
from driver import app

@app.route('/', methods=['GET'])
def tweetCountAll():
    for x in range(0,20):
        tasks = pronounCount.delay("tweets_"+ str(x) + ".txt")
    #tasks = pronounCount.delay("/home/sam/Desktop/tweets_19.txt.part")
    print "ja"

    while(tasks.ready() == False):
        time.sleep(4)

    res = tasks.get()
    #print res
    return jsonify(dict(res)), 200


if __name__ == '__main__':
    app.run()

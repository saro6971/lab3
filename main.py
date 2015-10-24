import time
from findStrings import pronounCount
from celery import group, subtask
from flask import jsonify
from collections import Counter
from driver import app


#@app.task()
@app.route('/', methods=['GET'])
def tweetCountAll():
    for x in xrange(0,20):
        tasks = pronounCount.delay("tweets_"+ str(x) + ".txt")
    #tasks = pronounCount.delay("/home/sam/Desktop/tweets_19.txt.part")
    #print "ja"

    while(tasks.ready() == False):
        time.sleep(4)

    res = tasks.get()
    print res
    #print res
    #counter = Counter()
    #for dic in res:
    #    counter.update(dic)

    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

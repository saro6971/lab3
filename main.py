import time
from findStrings import pronounCount
from celery import group, subtask
from flask import jsonify
from collections import Counter
from driver import app


#@app.task()
@app.route('/', methods=['GET'])
def tweetCountAll():
    for x in xrange(0,3):
        tasks = pronounCount.delay("tweets_"+ str(x) + ".txt")
    #tasks = pronounCount.delay("/home/sam/Desktop/tweets_19.txt.part")
    #print "ja"

    while(tasks.ready() == False):
        time.sleep(2)

    result = tasks.get()
    #print res
    triggerWordsTot = {"han" : 0, "hon" : 0, "den" : 0
                   , "hen" : 0 ,"denna" : 0, "denne" : 0}
    countAll = Counter()
    for dictionary in result:
        for word in dictionary:
            triggerWordsTot[word] += dictionary[word]

    print countAll
    return jsonify(dict(countAll))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

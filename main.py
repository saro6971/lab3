import time
import json
from findStrings import pronounCount
from celery import group, subtask
from flask import jsonify
from collections import Counter
from driver import app

#tasks = pronounCount.delay("/home/sam/Desktop/tweets_19.txt.part")
    #print "ja"
#@app.task()
@app.route('/', methods=['GET'])
def tweetCountAll():
    triggerWordsTot = {"han" : 0, "hon" : 0, "den" : 0, "det" : 0, "hen" : 0 ,"denna" : 0, "denne" : 0}
    for x in xrange(0,4):
        tasks = pronounCount.delay("tweets_"+ str(x) + ".txt")
        print "hejehjehjehej" + str(x)
        while(tasks.ready() == False):
            time.sleep(2)
        result = tasks.get()
        triggerWordsTot["han"] += result["han"]
        triggerWordsTot["hon"] += result["hon"]
        triggerWordsTot["den"] += result["den"]
        triggerWordsTot["det"] += result["det"]
        triggerWordsTot["hen"] += result["hen"]
        triggerWordsTot["denna"] += result["denna"]
        triggerWordsTot["denne"] += result["denne"]
    #for dictionary in result:
    #    for key in dictionary:
    #        triggerWordsTot[key] += dictionary[key]
    print triggerWordsTot
   # print triggerWordsTot
    return json.dumps(triggerWordsTot)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

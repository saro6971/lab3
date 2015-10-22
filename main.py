import time
from findStrings import pronounCount
from celery import group, subtask
from flask import jsonify
from collections import Counter
from driver import app

@app.route('/', methods=['GET'])
def tweetCountAll():

    queue = [pronounCount.s('tweets_{}.txt'.format(x)) for x in xrange(0,20)]
    g = group(queue)

    res = g()

    while (res.ready() == False):
        time.sleep(3)

    dicts = res.get()
    #counter = Counter()
    #for dic in dicts:
      #  counter.update(dic)

    return dicts

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
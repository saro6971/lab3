
import json
#from driver import celery
from celery import Celery
from flask import Flask

app = Flask(__name__)

app.config["CELERY_BROKER_URL"] = "amqp://"
app.config["CELERY_RESULT_BACKEND"] = "amqp"

celery = Celery('findStrings',  broker=app.config["CELERY_BROKER_URL"], backend=app.config["CELERY_RESULT_BACKEND"])

@celery.task()
#@app.task
def pronounCount(tweetfile):
    triggerWords = {"han" : 0, "hon" : 0, "den" : 0
                   , "hen" : 0 ,"denna" : 0, "denne" : 0}
    key = triggerWords.keys()
    
    with open(tweetfile,"r") as f:                     #read the file// make this generic for all files
        jsonDataLines = f.readlines()                             #reaad all the lines in file f
        for data in jsonDataLines:                                #for every line in all the lines
            if data != '\n' and "retweeted_status" not in data:                                      #disregard empty lines and retweets
                json_data = json.loads(data)                      #load data as json
                text = json_data["text"].split()                  #save word for word in text-list
                for words in text:                                #
                    if words.lower() in key:                      #for every word which corresponds to a key
                        triggerWords[words.lower()] += 1          # add 1 to that value
    #print type(triggerWords)                    
    return triggerWords
#pronounCount("/home/sam/Desktop/tweets_19.txt.part");

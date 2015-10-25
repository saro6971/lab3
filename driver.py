
from flask import Flask
from celery import Celery

app = Flask(__name__)

app.config["CELERY_BROKER"] = "amqp://"
app.config["CELERY_BACKEND"] = "amqp"

celery = Celery('findStrings',  broker=app.config["CELERY_BROKER"], backend=app.config["CELERY_BACKEND"])

#backend = query the status of a background task or retrive results
#broker = Specifies the url needed to connect to our broker
# amqp is a protocol that rabbitMQ uses

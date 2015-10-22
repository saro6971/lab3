
from flask import Flask
from celery import Celery

app = Flask(__name__)

app.config["BROKER"] = "amqp://"
app.config["BACKEND"] = "amqp"

celery = Celery('findStrings',  broker=app.config["BROKER"], backend=app.config["BACKEND"])

#backend = query the status of a background task or retrive results
#broker = Specifies the url needed to connect to our broker
# amqp is a protocol that rabbitMQ uses

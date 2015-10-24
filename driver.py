
from flask import Flask
from celery import Celery

app = Flask(__name__)

app.config["CELERY_BROKER_URL"] = "amqp://"
app.config["CELERY_RESULT_BACKEND"] = "amqp"

celery = Celery('findStrings',  broker=app.config["CELERY_BROKER_URL"], backend=app.config["CELERY_RESULT_BACKEND"])

#backend = query the status of a background task or retrive results
#broker = Specifies the url needed to connect to our broker
# amqp is a protocol that rabbitMQ uses

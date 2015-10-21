

from celery import Celery

app = Celery('findStrings', backend='amqp', broker='amqp://')

#backend = query the status of a background task or retrive results
#broker = Specifies the url needed to connect to our broker
# amqp is a protocol that rabbitMQ uses

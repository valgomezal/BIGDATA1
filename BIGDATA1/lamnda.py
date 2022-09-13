#Valentina Gomez
import json
import boto3
import datetime
from Scraping import lambda_handler1
from Pasar import lambda_handler2

def lambda_handler(event, context):
    #TODO implement
    lambda_handler1()
    lambda_handler2()
    

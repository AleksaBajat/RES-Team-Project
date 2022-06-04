from logging import exception
from ConnectToDatabase import *

def getReply(option,parameter):
    if(option==1):
        string= getAll()
    
    reply = open_connection_and_reply(string)
    return "aaa"

def getAll():
    return "Select * from Data"

def getByMonth(month):
    return

def getByAddress(address):
    return

def getByPowerConsumptionAbove(value):
    return

def getByPowerConsumptionBelow(value):
    return

def getByCity(city):
    return

def getByClientId(userId):
    return
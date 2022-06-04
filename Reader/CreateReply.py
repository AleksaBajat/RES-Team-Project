from logging import exception
from ConnectToDatabase import *

def getReply(option,parameter):
    string=""
    if(option=="1"):
        string= getAll()
    elif(option=="2"):
        string =getByMonth(parameter)
    elif(option=="3"):
        string =getByClientId(parameter)
    elif(option=="4"):
        string=getByCity(parameter)
    elif(option=="5"):
        string = getByPowerConsumptionAbove(parameter)
    elif(option=="6"):
        string = getByPowerConsumptionBelow(parameter)

    reply = open_connection_and_reply(string)
    return reply

def getAll():
    return "SELECT * FROM meterReadings"

def getByMonth(month, conn):
    sqlSelect = "Select * from meterReadings where month = " + month
    return sqlSelect

def getByAddress(address):
    return

def getByPowerConsumptionAbove(value):
    return

def getByPowerConsumptionBelow(value):
    return

def getByCity(city):
    return "SELECT * FROM meterReadings WHERE city = '" + city + "'"

def getByClientId(userId):
    return "SELECT * FROM meterReadings WHERE user_id ="+userId
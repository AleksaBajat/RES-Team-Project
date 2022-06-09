from logging import exception

def getQuery(option,parameter):
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

    return string

def getAll():
    return "SELECT * FROM meterReadings"

def getByMonth(month):
    sqlSelect = "SELECT * FROM meterReadings WHERE month = '" + month+"'"
    return sqlSelect

def getByPowerConsumptionAbove(value):
    sqlSelect = "SELECT * FROM meterReadings WHERE consumption >= " + str(value)
    return sqlSelect

def getByPowerConsumptionBelow(value):
    sqlSelect = "SELECT * FROM meterReadings WHERE consumption < " + str(value)
    return sqlSelect

def getByCity(city):
    return "SELECT * FROM meterReadings WHERE city = '" + city + "'"

def getByClientId(userId):
    return "SELECT * FROM meterReadings WHERE user_id ="+userId
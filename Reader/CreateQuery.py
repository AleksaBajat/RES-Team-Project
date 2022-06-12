def get_query(option,parameter):
    string=""
    if(option=="1"):
        string= get_all()
    elif(option=="2"):
        string =get_by_month(parameter)
    elif(option=="3"):
        string =get_by_clientId(parameter)
    elif(option=="4"):
        string=get_by_city(parameter)
    elif(option=="5"):
        string = get_by_power_consumption_above(parameter)
    elif(option=="6"):
        string = get_by_power_consumption_below(parameter)

    return string

def get_all():
    return "SELECT * FROM meterReadings"

def get_by_month(month):
    sqlSelect = "SELECT * FROM meterReadings WHERE month = '" + month+"'"
    return sqlSelect

def get_by_power_consumption_above(value):
    sqlSelect = "SELECT * FROM meterReadings WHERE consumption >= " + str(value)
    return sqlSelect

def get_by_power_consumption_below(value):
    sqlSelect = "SELECT * FROM meterReadings WHERE consumption < " + str(value)
    return sqlSelect

def get_by_city(city):
    return "SELECT * FROM meterReadings WHERE city = '" + city + "'"

def get_by_clientId(userId):
    return "SELECT * FROM meterReadings WHERE user_id = "+str(userId)
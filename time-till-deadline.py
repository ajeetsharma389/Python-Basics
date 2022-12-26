import datetime

currentDate = datetime.datetime.today()

#print(currentDate)

def calculate_deadLine(user_input):
    #take dictionary as input and separate course and date
    if type(user_input) == str:
        ### split the string
        splittedArray = user_input.split(":")
        if len(splittedArray) > 0:
            course = splittedArray[0]
            deadLine = splittedArray[1]
            #print(datetime.datetime.strptime('30.12.2022', '%d.%m.%Y'))
            deadLineDate = datetime.datetime.strptime(deadLine, "%d.%m.%Y")
            remaingDate = deadLineDate - currentDate
            print(f"{remaingDate.days} days is remaing")
    else:
        print("oooppps")

calculate_deadLine("python:30.01.2023")
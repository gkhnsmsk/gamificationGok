import json
import subprocess
import os
from datetime import date

GERMANY_AVARAGE = 4000
PATH = "" 
#"/home/pi/Documents/gameServer/"

# daily 
# (string) dailyValue
# add daily_avarage to the file
def daily(dailyValue):

  file_object = open(PATH+'last10values.txt', 'a')
  file_object.write(dailyValue)
  file_object.write("\n")
  file_object.close()

# save daily 
# (int) dailyValue
# add daily_avarage to the file
def history(dailyValue):

  today = date.today()
  dateStr = today. strftime("%d %b %Y ")
  sDaily = str(dailyValue)

  file_object = open(PATH+'history.txt', 'a')
  file_object.write(dateStr + "------> " + sDaily)
  file_object.write("\n")
  file_object.close()


# avarageCalculate 
# (string) dailyValue
# (int) num_lines
# (array) jsonOutput
# return (int)total
# reading the last 10 days energy
def avarageCalculate(dailyValue,num_lines,jsonOutput):
  
  file_object = open(PATH+'last10values.txt', 'r')
  lines = file_object.read().split(",")
  file_object.close()

  valueArray = lines[0].split("\n")
  total = 0

  for x in range(num_lines):
    if(valueArray[x] != ''):
     if (int(float(valueArray[x])) < GERMANY_AVARAGE):
      total += 1
 
  if (total == 11):
    total = 1
  
  jsonOutput[0]["daily"] = total
  file_object = open(PATH+'output.txt', 'w')
  file_object.write(json.dumps(jsonOutput))
  file_object.close()

  return total


def tenDayResult(jsonOutput,returnCurrentTotal):

  if (returnCurrentTotal < 4):
    jsonOutput[0]["bad"] += 1
  elif (returnCurrentTotal >= 4 and returnCurrentTotal < 7):
    jsonOutput[0]["cool"] += 1
  elif (returnCurrentTotal >= 7 and returnCurrentTotal < 10):
    jsonOutput[0]["good"] += 1
  else:
    jsonOutput[0]["perfect"] += 1
  
  file_object = open(PATH+'output.txt', 'w')
  file_object.write(json.dumps(jsonOutput))
  file_object.close()

# reading files from json output from Sensors
with open(PATH+'test.txt', 'r') as f:
    data = f.read()
    jstr = json.loads(data)


with open(PATH+'output.txt', 'r') as output:
    dataOutput = output.read()
    jsonOutput = json.loads(dataOutput)
  
# get and add daily_gesamt value to the file
dailyValue = jstr[6]["attributes"]["last_period"]
daily(dailyValue)
history(dailyValue)
# line counter of the last10values.txt
num_lines = sum(1 for line in open(PATH+'last10values.txt'))

# get avarage values of 
returnCurrentTotal = avarageCalculate(dailyValue,num_lines,jsonOutput)
 

if num_lines >= 11 :
  tenDayResult(jsonOutput,returnCurrentTotal)
  os.remove(PATH+"last10values.txt")
  daily(dailyValue)


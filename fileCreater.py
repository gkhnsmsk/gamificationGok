import json
import subprocess


def my_function(currentValue,avg,jsonOutput):

  newOutputValues=jsonOutput[0];

  print avg


# reading files from json output from Sensors
with open('test.txt', 'r') as f:
    data = f.read()
    jstr = json.loads(data)


with open('output.txt', 'r') as output:
    dataOutput = output.read()
    jsonOutput = json.loads(dataOutput)
    
# reading the last 10 days energy
file_object = open('temp10Values.txt', 'r')
lines = file_object.read().split(",")
file_object.close()
num_lines = sum(1 for line in open('temp10Values.txt'))

valueArray = lines[0].split("\n")
total = 0
for x in range(num_lines):
  total += int(round(float(valueArray[x])))

avg = total/num_lines

my_function(jstr[2]["state"],avg,jsonOutput)


file_object = open('last10values.txt', 'a')
file_object.write("\n")
file_object.write(jstr[2]["state"])
file_object.close()



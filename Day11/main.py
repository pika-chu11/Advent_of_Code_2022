import re
from collections import defaultdict
fileName = "input.txt"
def operation_cal(oper, num1, num2):
    num1 = int(num1)
    if num2 == "old\n":
        num2 = num1
    num2 = int(num2)
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1*num2
    elif oper == '/':
        return num1/num2
    
if __name__ == '__main__':
    # Set up
    items = {}
    operations = {}
    test = []   # integers
    throw = defaultdict(list)
    inspection = defaultdict(int)
    with open(fileName, "r") as f:
        line = f.readline()
        while line != '':
                num = re.findall(r'\d+', line)[0]
                line = f.readline()
                item = re.findall(r'\d+', line)
                items[num] = item
                line = f.readline()
                token = line.split(" ")
                operations[num] = token[-2:]
                line = f.readline()
                test.append(int(re.findall(r'\d+',line)[0]))
                line = f.readline()
                throw[num].append(re.findall(r'\d+', line)[0])
                line = f.readline()
                throw[num].append(re.findall(r'\d+', line)[0])
                line = f.readline()
                line = f.readline()

    mul = 1
    for i in range(len(test)):
        mul *= test[i]
        
    print(mul)

    for i in range(10000):
        for key in items:
            delete = []
            inspection[key] += len(items[key])
            for item in items[key]:
                calculation = operation_cal(operations[key][0], item, operations[key][1])               
                decreased_level = int(calculation)%mul
                divisor = test[int(key)]
                if (decreased_level%divisor == 0):
                    items[throw[key][0]].append(decreased_level)
                    delete.append(item)
                else:
                    items[throw[key][1]].append(decreased_level)
                    delete.append(item)
            for d in delete:
                items[key].remove(d)                

all_inspection = []
for key in inspection:
    all_inspection.append(inspection[key])
max1 = max(all_inspection)
all_inspection.remove(max1)
max2 = max(all_inspection)
all_inspection.remove(max2)
final = max1 * max2
print(final)

    

   
                
                
                
                
            
import re
import sys

def parseInput(text):

    operations = []

    on_operations = re.finditer(r'(ON)', text, re.I)
    off_operations = re.finditer(r'(OFF)', text, re.I)
    sum_operations = re.finditer(r'([+-]?\d+)', text)
    retrieve_operations = re.finditer(r'(=)', text)

    for match in on_operations:
        operations.append((match.group(1), match.start(1)))
    
    for match in off_operations:
        operations.append((match.group(1), match.start(1)))
    
    for match in sum_operations:
        operations.append((match.group(1), match.start(1)))
    
    for match in retrieve_operations:
        operations.append((match.group(1), match.start(1)))

    operations = sorted(operations, key=lambda x: x[1])

    operations = [operation[0].lower() for operation in operations]

    return operations

if __name__ == "__main__":

    operations = parseInput(sys.stdin.read())

    state = "on"
    total = 0
    for op in operations:
        if op == "on":
            state = "on"
        elif op == "off":
            state = "off"
        elif op == "=":
            print("Soma = " + str(total))
        elif state == "on":
            total += int(op)

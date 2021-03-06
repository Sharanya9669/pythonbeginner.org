#!/usr/bin/env python
import sys

# get operands & operator from command line arguments
if len(sys.argv) < 4:
    print 'Incorrect number of arguments: Expecting 3 arguments, %d given.' % (len(sys.argv) - 1)
    exit()
else:
    # operands have to be numbers
    try:
        operand1 = float(sys.argv[1])
        operand2 = float(sys.argv[3])
    except ValueError, e:
        print e
        exit()

    operator = sys.argv[2]

# calculate the result according to the operator
if operator == '+':
    result = operand1 + operand2
elif operator == '-':
    result = operand1 - operand2
elif operator == 'x':
    result = operand1 * operand2
elif operator == '/':
    result = operand1 / operand2

# show result
print '%.2f %s %.2f = %.2f' % (operand1, operator, operand2, result)

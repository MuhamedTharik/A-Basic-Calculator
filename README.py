a=int(input('Enter the number 1:'))
b=int(input('Enter the number 2:'))

print('select an operation to perform:')
print('+ for Addition')
print('- for Subtraction')
print('* for Multiplication')
print('/ for Division')

operation = input()

if operation =='+':
    result=a+b
    print(result)
elif operation =='-':
    result=a-b
    print(result)
elif operation =='*':
    result=a*b
    print(result)
elif operation =='/':
    result=a/b
    print(result)
else:
    print('The input is wrong')

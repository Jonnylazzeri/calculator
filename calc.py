import operator
ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul } # etc.

first_num = float(input("What's the first number?: "))
print('+\n-\n*\n/')

def calc(first_num):
  working = True
  while  working:
    operation = input('Pick an operation: ')
    second_num = float(input("What's the next number?: "))
    answer = ops[operation](first_num, second_num)
    print(f'{first_num} {operation} {second_num} = {answer}')
    keep_going = input("Would you like to keep going? type either 'yes' or 'no'... ").lower()
    if keep_going == 'yes':
      first_num = answer
    else:
      return answer
  
calc(first_num)
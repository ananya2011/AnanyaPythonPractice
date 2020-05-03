
question = 'How many apples do you eat in a month ?'

print(question)

input = input('Enter # of apples\n')

result = int(input) * 12

message = 'You eat '+repr(result)+ '  apples in an year'

print(message)
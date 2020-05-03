message = "How many times do you cycle in a week?"
print(message)
input = input('Enter the # of cycles / week \n ')

result= int(input) * 52

pmsg= 'You cycle ' + repr(result) + ' per year'

print(pmsg)
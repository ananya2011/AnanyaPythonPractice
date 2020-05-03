rate1 = input('enter the rate of apples')
rate2 = input('enter the rate of oranges')
rate3 =  input('enter the rate of mangoes')
quantity1 = input('enter the quantity of apples')
quantity2 =  input('enter the quantity of oranges')
quantity3 = input('enter the quantity of mangoes')
appletotal = (int(rate1) * int(quantity1))
orangetotal = (int(rate2) * int(quantity2))
mangototal = (int(rate3) * int(quantity3))
pocketmoney = 100
totalbill = (int(appletotal) + int(orangetotal)+ int(mangototal))
print('your total bill is ' + str (totalbill))
spent = pocketmoney - totalbill
print('balance amount = ' + str(spent))
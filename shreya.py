n = int(input('Enter how many pairs of shoes(>1):'))
p = int(input('Enter the number of shoes they can carry(<100):'))

shoe_price_dict = {}

print('enter prices for each pair:')
for i in range(n):
    temp = int(input(f'Enter price for piece{i+1}:'))
    shoe_price_dict[i] = temp

sum = 0
j = 0

while j<= p:
    for i in range(p):
        if shoe_price_dict[i] > 0:
            sum += shoe_price_dict[i]
        if shoe_price_dict[i] < 0:
            sum -= shoe_price_dict[i]
        j += 1

print('Sum they earned:', sum)


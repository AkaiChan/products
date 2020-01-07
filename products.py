listProducts = []
while True:
	strName = input("Please input product name: ")
	if strName == 'q':
		break
	strPrice = input("the price is: ")
	listProduct = [strName,strPrice]
	listProducts.append([strName,strPrice])
#print ( "Price of '",listProducts[0][0],"' is ", listProducts[0][1])

for p in listProducts:
	print("The price of ", p[0], " is ", p[1])
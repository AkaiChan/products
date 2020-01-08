listProducts = []
while True:
	strName = input("Please input product name: ")
	if strName == 'q':
		break
	strPrice = input("the price is: ")
	listProduct = [strName,int(strPrice)]
	listProducts.append([strName,strPrice])
#print ( "Price of '",listProducts[0][0],"' is ", listProducts[0][1])

for p in listProducts:
	print("The price of ", p[0], " is ", p[1])

with open("Products.csv", "w", encoding = "utf-8") as f:
	f.write("商品,價格\n")
	for p in listProducts:
		f.write(p[0] + "," + str(p[1]) + "\n")
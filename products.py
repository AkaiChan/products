#讀取檔案
listProducts = []
with open("products.csv", "r", encoding = "utf-8") as f:
	for line in f:
		if "商品,價格" in line:
			continue
		name, price = line.strip().split(',')
		listProducts.append([name, price])

# 讓使用者輸入
while True:
	strName = input("Please input product name: ")
	if strName == 'q':
		break
	strPrice = input("the price is: ")
	listProduct = [strName,int(strPrice)]
	listProducts.append([strName,strPrice])
#print ( "Price of '",listProducts[0][0],"' is ", listProducts[0][1])

# 進出購買紀錄
for p in listProducts:
	print("The price of ", p[0], " is ", p[1])

#寫入檔案
with open("Products.csv", "w", encoding = "utf-8") as f:
	f.write("商品,價格\n")
	for p in listProducts:
		f.write(p[0] + "," + str(p[1]) + "\n")
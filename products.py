import os

# 讀取檔案
def read_file(filename):
	listProducts = []
	with open(filename, "r", encoding = "utf-8") as f:
		for line in f:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(',')
			listProducts.append([name, price])
	return listProducts

# 讓使用者輸入''
def user_input(listProducts):
	while True:
		strName = input("Please input product name: ")
		if strName == 'q':
			break
		strPrice = input("the price is: ")
		listProducts.append([strName,strPrice])
	return listProducts
	#print ( "Price of '",listProducts[0][0],"' is ", listProducts[0][1])
# 進出購買紀錄
def print_products(listProducts):
	for p in listProducts:
		print("The price of ", p[0], " is ", p[1])
# 寫入檔案
def write_file(filename, listProducts):
	with open(filename, "w", encoding = "utf-8") as f:
		f.write("商品,價格\n")
		for p in listProducts:
			f.write(p[0] + "," + str(p[1]) + "\n")


def main():
	filename = "Products.csv"
	listProducts = []
	if os.path.isfile(filename):
		print("file is exised")
		listProducts = read_file(filename)
	else:
		print("file is not existed...")
	listProducts = user_input(listProducts)
	print_products(listProducts)
	write_file(filename, listProducts)

main()
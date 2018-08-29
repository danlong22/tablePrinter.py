tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def tablePrinter(tableData):#determine the width of each column
	columnWidth=[]
	for column in range(3):
		list = []
		for item in tableData[column]:
			list.append(len(item))
		columnWidth.append(max(list))

	#print the table passing the values in columnWidth to .rjust()

	#prints each column
	for i in range(len(tableData[0])):
		#prints the row
		for j in range (len(tableData)):
			print (tableData[j][i].rjust(columnWidth[j]) + ' ', end ='')
		print('\n')
tablePrinter(tableData)
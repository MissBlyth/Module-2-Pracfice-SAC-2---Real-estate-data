'''
PRACTICE SAC 2
Real estate data

Search and sort algorithm info:
list - refers to the array you are sending in
key - refers to the value you are looking for in the array
param - referes to the parameter you are searching, or sorting by. 

Apply the search and sort algorithms to get the following results

1. Search by suburb (input by user)
2. Sort by days on market
3. Search by salesid, return by sale price low to high

'''


#Linear search any array 
def LinearSearch(list, key, param):	
	#linear search, prints any matching results
	for x in list:
		if x[param] == key:
			print(x)

#Binary search a sorted array 
def BinarySearch(list, key, param):
	#set found to false
	found=False
	#print("start binary")
	results = []
	#get the length of the list
	iLen=len(list)
	#get the midpoint using floor division
	midP=iLen//2

	#if the key equals the midpoint
	if key == list[midP][param]:
		found=True
		#set found to true
		while True:
			#print the match
			print(list[midP])
			#add to an array
			results.append(list[midP])
			#check next item in array for math
			if key==list[midP+1][param]:
				#if matching, go to next list item
				midP += 1
			else:
				#break loop if no longer matching 
				break
			
	#if the length of the list is more than one item
	elif iLen > 1:
		#if the key is less than the midPoint value
		if key < list[midP][param]:
			#search the left side of the array
			return BinarySearch(list[:midP],key, param)
		else:
			#search the right side of the array
			return BinarySearch(list[midP:],key, param)
	#return true or false
	#print("end binary")
	return results

def SelectionSort(list, param):
    #make n equal the number of elements in the list array
    n = len(list)

    #loop through each item in the array
    for i in range(0,n):
        #set current item to smallest
        smallest = i

        #cycle through the rest of the arrya
        for j in range(i+1,n):
            #if a smaller item is found, set smallest to that item
            if list[j][param] < list[smallest][param]:
                smallest = j

        #after loop, put smallest back in array
        if smallest !=i:
            list[smallest], list[i] = list[i],list[smallest]

    #sends sorted list back to the main program
    return list

#quicksort algorithm 
def partition(array, start, end, param):
    #pivot value from first item
    pivot = array[start][param]  
    #index markers
    left = start + 1
    right = end

    #print(pivot,left,right)
    while True:
        # While the left marker and right marker have not crossed, and the right value is on the correct side of the pivot, move the right marker to the left by one place
        while left <= right and array[right][param] >= pivot: 
            right = right - 1

        # While the left marker and right marker have not crossed,         # and the left value is on the correct side of the pivot,
        # move the left marker to the right by one place
        while left <= right and array[left][param] <= pivot: 
            left = left + 1

        if left <= right:
            #Swap values at left and right pointer because they are both in the wrong place
            array[left], array[right] = array[right], array[left]
            # The loop continues
        else:
            # Break the outside loop because the left and right markers have met
            # but theres nothing to swap
            break

    array[start], array[right] = array[right], array[start]
    return right 

def quick_sort(array, start, end, param):
    if start >= end:
        return

    p = partition(array, start, end, param)
    quick_sort(array, start, p-1, param)
    quick_sort(array, p+1, end, param)




##read the file data into an associative array 


#initialise productarr
salesArr = []

#open producctlis file
myFile=open("sales.csv","r")
myFile.readline()

for line in myFile:
	#split line into 5 variables 
	Suburb,SalesID,DaysOnMarket,Reserve,SalePrice = line.split(",")

	#create mini dictionary (associative array) from variables, and add to sales arr
	salesArr.append({"Suburb":Suburb, "SalesID":SalesID,"DaysOnMarket":DaysOnMarket, "Reserve":Reserve,"SalePrice":int(SalePrice.strip("\n"))})

	#close sales file
myFile.close()

quick_sort(salesArr, 0, len(salesArr) -1, "SalesID")
#print(salesArr)

resultsArr=BinarySearch(salesArr,"AKH","SalesID")
#print(resultsArr)
quick_sort(resultsArr, 0, len(salesArr) -1, "SalesID")
print(resultsArr)

##provide a menu for the user to choose which function they would like to execute
## perform the relevant search and sort functions choosing the most efficient algorithms
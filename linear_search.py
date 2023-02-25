'''
This program implements a linear search on a list of items

Algorithm:
1. Start with first item in the list, and compare its value to the target
2. If the value equals the target, print the index of the item in the list
3. If the value does not equal to the target, check the next item in the list
4. Continnue doing this till you either find the value or reach the end of the list
'''

user_list=[1,2,3,4,5,6,7,8,9,10] #Start with a pre-defined list
#We have our list now
#Get the target value
target=int(input("Enter your target value:"))

#Define the linear search function
def linear_search(list, target): 
    for i in range(0, len(list)): #Iterate over all items in the list, starting from first
        if list[i]==target: #If you find the item equal to the target
            return i #Return the index of the item in the list
            break #Break from the for loop

result=linear_search(user_list, target) #Get result from the function defined above
if result==None: #If target not found in the code
    print("Target not found")
else: #If target found
    print(f"Target found at position",result, "in the list")
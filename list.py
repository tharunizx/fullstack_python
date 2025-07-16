'''Write a Python program to take 5 numbers as input from the user, store them in a list, and then:
Print the list in reverse order.
Print the sum and average of the numbers.'''
arr=[]
for i in range(5):
    num=int(input(f'Enter {i} number: '))
    arr.append(num)
def reverse(arr):
    for i in range(len(arr)-1,-1,-1):
        print(arr[i],end=" ")
print("Reverse order of the numbers:")
print(reverse(arr))
print("Sum of the 5 numbers is:",sum(arr))
print("Average of the 5 numbers is:",sum(arr)/len(arr))
#declare a Array
A =[]

#giving 8 user inputs

for i in range(1,8):
    A.append(int(input("Enter a Number : ")))
    
#print the numbers
print(A)

#declare function
def bubbleSort(A):
    n = len(A)
    for i in range(1,n):
        for j in range(1,n-i+1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1],A[j]

#call function
bubbleSort(A)
print("Ordered Array : ")
print(A)

                



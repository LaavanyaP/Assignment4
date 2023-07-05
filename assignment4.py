#Ques:1 Create a lambda function that add 25
num = int(input())
n = lambda x : x+25
print(n(num))

#Ques:2 Program to triple all numbers of given list using map()
num = list(map(int,input().split()))
def triple(n):
    return 3 * n

result = map(triple, num)
print("Triple of given list:", list(result))

#Ques:3 Program to square all numbers of given list using map()
num = list(map(int,input().split()))
def square(n):
    return n*n
output = map(square, num)
print("Square of given list:", list(output))
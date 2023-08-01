#Solução de um problema proposto pelo HackerRank
#Nome:Felipe Pinto Marinho
#Data:01/08/2023

#Inputs
n = int(input())
new_list = list(map(int, input().split()))

#Constraints
if n < 2 or n > 10:
    print("Invalid Value")

if max(new_list) > 100 or min(new_list) < -100:
    print("Invalid Values")

#Second maximum
result = list(filter(lambda a: a != max(new_list), new_list))
print(max(result))

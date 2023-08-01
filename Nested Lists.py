#Solução de um problema proposto pelo HackerRank
#Tema:Nested Lists
#Nome:Felipe Pinto Marinho
#Data:01/08/2023

#Inputs
N = int(input())

#Constraint
if N < 2 or N > 5:
    print("Invalid Value")

#Nested List
nested_list = [[input(), float(input())] for i in range(1, N+1)]

#Result
grades = list(nested_list[i][1] for i in range(0, N))
grades_new = list(filter(lambda a : a != min(grades), grades))
result = list(nested_list[i][0] for i in range(0, N) if nested_list[i][1] == min(grades_new))
for i in range(len(result)):
    print(sorted(result)[i])
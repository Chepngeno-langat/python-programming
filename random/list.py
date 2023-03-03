my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print(i)
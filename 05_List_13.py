t = int(input())
first_list = []
out_list = []
second_list = []
for i in range(t):
    x =int(input())
    first_list.append(x)

y = input()
while y != "-1":
    yy = y.split()
    for i in yy:
        second_list.append(int(i))
    y = input()

outer = first_list + second_list

counter = 1
for i in outer:
    if counter%2 == 1:
        out_list.insert(len(out_list),i)
        counter +=1
        print(out_list)
    else:
        out_list.insert(0,i)
        counter += 1
        print(out_list)

print(out_list)
na = int(input(""))
ls1=set(map(int , input("").split(" ")))
nb = int(input(""))
ls2=set(map(int , input("").split(" ")))
maa = set(ls1.union(ls2))
output =0
for i in maa:
    output+=1

output = str(output)
print(output)

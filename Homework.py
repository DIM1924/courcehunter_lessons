def odd_ball(arr):

    if "odd" in arr:
        ind = arr.index("odd")
        if ind in arr:
            return True
        else:
            return False

    else:
        print('Not found odd')

print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"]))
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"]))
print(odd_ball(["even",10,"odd",2,"even"]))
print(odd_ball(["even",10,2,"even"]))

# x =["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"]
# print(x[10])

def find_sum(n):
    x = set()

    for i in range(0,n+1,3):
         x.add(i)
    for i in range(0,n+1,5):
        x.add(i)
    print(x)
    return sum(x)

print(find_sum(20))

def get_name (names):
    x =[]
    for i in range(0,len(names)):
        if len(names[i]) == 4:
            x.append(names[i])
    return x

print(get_name(["Ryan","Kieran","Mark","John","David","Poul"]))

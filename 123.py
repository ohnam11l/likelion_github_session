
# def say(): 
# #     return 'Hi'

# def add(a,b):
# 		print (a+b)

# add(3,5)

def add_many(*abc):
    result = 0
    for i in abc:
        result += i
    return result
    
a = add_many(1,2,3,4,5,6,7,8,9,10)

print(a)


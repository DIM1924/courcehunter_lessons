# def hello(name, word):
#     print(f'hello {name}! Say {word}')
# hello('katty','Hi')
# hello('John', 'hi')

# def get_sum(x,y):
#     return x+y
#
# print(get_sum(4,78))

# def get_sum(*args):
#     return  sum(args)
# print(get_sum(1,5,6))
#
# def func (**kwargs):
#     print(kwargs)
# func(a=0,b=12,carprice = 800)

# def f(a,x,*args,**kwargs):
#     print(a)
#     print(x)
#     print(args)
#     print(kwargs)
# f(1,2,3,4,b='test',c='hi')
# def get_sum(a,b):
#     """
#     Возвращает сумму аргументов a и b.
#
#     :param a: Первый операнд
#     :type a:int
#     :param b: Второй операнд
#     :type b:int
#     :return: Return type int
#     """
#     return a+b
#
# # print(get_sum(1,2))
# a =5
# def f ():
#     a = 10
#     a+=1
#     print(a)
# print(a)
# f()
# print(a)
# a=5
# def f ():
#     global a
#     a+=1
#     print(a)
# print(a)
# f()
# print(a)
l =[1,2,3]
# def f(l):
#     return [i*2 for i in l]
# print(f(l))
def f2(l):
    def get_mult(x):
        return x*2
    return [get_mult(i)for i in l]
print(f2(l))
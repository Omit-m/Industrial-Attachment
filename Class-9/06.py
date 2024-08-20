def some(*args, **kwargs):
    print(args)
    print(kwargs)

some(1,2,3, a=10, b=30)




# home_practice

def sum_kwargs(**kwargs):
    summation =0
    for i in kwargs.values():
        summation+=i
    print ( kwargs )
    print(summation)
sum_kwargs(a=10, b=20, c=30)


def sum_args (*args):
    summ = 0
    for i in args:
        summ+=i
    print ( args )
    print(summ)
sum_args(2,3,4,5,3,4,4,4,4)
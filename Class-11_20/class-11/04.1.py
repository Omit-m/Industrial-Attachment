from time import sleep
from functools import lru_cache


@lru_cache(maxsize=30)
def lazy_function(value):
    print(f"Function called for {value}")

    sleep(3)

    result = value + 100

    print(f"Function finished for {value}")

    return result


print(lazy_function(10))
print(lazy_function(20))
print(lazy_function(30))
print(lazy_function(10))
print(lazy_function(20))
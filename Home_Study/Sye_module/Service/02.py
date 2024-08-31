"""
wrong approach :
the program give an error and he error is :
Traceback (most recent call last):
  File "E:\8 semister\Class_data\Industrial-Attachment\Home_Study\Sye_module\Service\02.py", line 11, in <module>
    from Server.one import hello
ModuleNotFoundError: No module named 'Server'


"""

import sys

sys.path.append ( r"E:\8 semister\Class_data\Industrial-Attachment" )

from Server.one import hello

# Call the `hello` function
hello()
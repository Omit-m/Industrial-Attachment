"""
APP FEATURE : Logged out a login user after 5 seconds
"""

import time

is_loggedin = True

print("5 second starts .... ")
time.sleep(5)

is_loggedin = not is_loggedin
print("5 second finish .... ")

print(f"Is user logged in ? {is_loggedin}")

import sys
import os


file_path = os.path.abspath(__file__)
prent_path = os.path.dirname(file_path)
root_path = os.path.dirname(prent_path)


sys.path.append(root_path)


from Server.one import connect

# Call the `hello` function
connect("omit")
import os


file_path = os.path.abspath(__file__)
print(file_path)
print("_____________________________________________")
prent_path = os.path.dirname(file_path)
print(prent_path)
print("_____________________________________________")
root_path = os.path.dirname(prent_path)
print(root_path)
print("_____________________________________________")
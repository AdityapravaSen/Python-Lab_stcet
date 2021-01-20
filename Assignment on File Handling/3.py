import os
if os.path.exists("hlo.txt"):
    os.remove("hlo.txt")
else:
    print("The file does not exist")

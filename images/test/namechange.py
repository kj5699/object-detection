import os
i=1
for filename in os.listdir():
    os.rename(filename, str(i) + ".jpeg")
    i= i +1


import os
i=1
for filename in os.listdir(os.curdir):

        os.rename(filename,str(i)+".jpeg")
        i+=1


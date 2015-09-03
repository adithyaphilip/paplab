import os
import shutil
def move(cd,f,lim):
    if(os.path.getsize(cd+"/"+f)<lim): return
    if(not os.path.exists(cd+"/"+f[0])): os.makedirs(cd+"/"+f[0])
    shutil.move(cd + "/" + f, cd + "/" + f[0]+"/"+f)
lim = int(input())
for i in next(os.walk("testdir"))[2]:
    move("testdir", i, lim)

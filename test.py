import glob

downloadpath ='/home/angus/projects/wyzant/carson/1'
x = (glob.glob(downloadpath +'/*'))
x = (x[-1].split('/'))
print(x[7][-3:])

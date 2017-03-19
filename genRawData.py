f  = open('data_seg.txt')
myStr=''
for line in f:
    lineList = line.split(' ')
    myStr+=' '.join(lineList[:len(lineList)-1])+'\n'
f.close()
f = open('rawData.txt','w')
f.write(myStr)
f.close()

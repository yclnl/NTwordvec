from openpyxl import load_workbook
import jieba
import jieba.analyse
import json
jieba.load_userdict('user_dict.txt')
stopwords = {}.fromkeys([ line.rstrip() for line in open('stopword.txt') ])



wb = load_workbook(filename = r'data.xlsx')
ws = wb.get_sheet_by_name((wb.get_sheet_names())[0])

id_map={}
idx = 0;
rows = ws.rows
replaceWord1='區公所'
replaceWord2='分局'
replaceWord3='戶政'
id_map = json.load(open('label_id.json'))
freqLabel=[]
mystr=''
for row in rows:
    inputText = (row[5].value)
    category = row[6].value
    if(inputText!=None and category != None ):
        if(category.find(replaceWord1)!=-1):
            category = replaceWord1;
        elif(category.find(replaceWord2)!=-1):
            category = '警察局'
        elif(category.find(replaceWord3)!=-1):
            category = '戶政事務所'
        seg_list = jieba.cut(inputText)
        reduceSeg=[]
        for seg in seg_list:
            if seg not in stopwords:
                reduceSeg.append(seg)
        if(category in id_map):
            mystr+=((" ".join(reduceSeg)) + ' '+category+'\n')
f = open('data_seg.txt','w')
f.write(mystr)
f.close()

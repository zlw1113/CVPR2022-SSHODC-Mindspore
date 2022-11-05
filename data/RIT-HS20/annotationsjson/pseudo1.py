import json
import numpy as np
file='data/RIT-HS20/annotationsjson/val_no_label.json'
file2='data/RIT-HS20/annotationsjson/submission.json'
file3='data/RIT-HS20/annotationsjson/pseudo.json'
with open(file,'r') as f,open(file2,'r') as f1,open(file3,'w') as f3:
    list=json.load(f)
    rrr=json.load(f1)
    a={}
    a["images"]=list['images']
    a['type']='instances'
    a['annotations']=rrr
    a['categories']=list['categories']
    json.dump(a,f3)
        # res=list[i]
        # res
        
        
    
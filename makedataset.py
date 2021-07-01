from os import listdir
from os.path import isfile, isdir, join
import json
# 指定要列出所有檔案的目錄
dev_path = "/home/yiying/Documents/trade-dst/newdata/data-0625/data-0625/dev"
train_path="/home/yiying/Documents/trade-dst/newdata/data-0625/data-0625/train"
test_path="/home/yiying/Documents/trade-dst/newdata/data/data/test_seen"
# 取得所有檔案與子目錄名稱
files1 = listdir(dev_path)
files2 = listdir(train_path)
files3 = listdir(test_path)

data_init=[]
for f in files1:
    print(f)
    fullpath = join(dev_path, f)
    with open(fullpath, newline='') as jsonfile:
        data = json.load(jsonfile)
        data_init=data_init+data
    
with open('/home/yiying/Documents/modifiied-trade-dst/dev_dials.json',"w") as writejson:
        json.dump(data_init, writejson, indent=4, sort_keys=True)

data_init=[]
for f in files2:
    print(f)
    fullpath = join(train_path, f)
    with open(fullpath, newline='') as jsonfile:
        data = json.load(jsonfile)
        data_init=data_init+data    
with open('/home/yiying/Documents/modifiied-trade-dst/train_dials.json',"w") as writejson:
        json.dump(data_init, writejson, indent=4, sort_keys=True)


data_init=[]
for f in files3:
    print(f)
    fullpath = join(test_path, f)
    with open(fullpath, newline='') as jsonfile:
        data = json.load(jsonfile)
        data_init=data_init+data    
with open('/home/yiying/Documents/modifiied-trade-dst/test_dials.json',"w") as writejson:
        json.dump(data_init, writejson, indent=4, sort_keys=True)
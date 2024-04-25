import json
data={"id":10,"model":"Audi","year":"2021","color":"Red"}
file=open('data.json','w',encoding='utf-8')
json.dump(data,file)
file.close()


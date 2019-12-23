import json
data = {}
data['kisiler'] = []
data['kisiler'].append({
    'isim':'Oguz',
    'sehir':'Kahramanmaras'
    })
data['kisiler'].append({
    'isim':'Osman',
    'sehir':'Kayseri'})
data['kisiler'].append({
    'isim':'Muhammed',
    'sehir':'Elazig'})
with open('data.txt','w') as outfile:
    json.dump(data, outfile)

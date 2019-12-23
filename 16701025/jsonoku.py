import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['kisiler']:
        print('Isim: '+ p['isim'])
        print('Sehir: '+ p['sehir'])
        print('')
oku = json.dumps(data, indent=4)
print(oku)
oku2 = json.dumps(data, ensure_ascii=False, indent=4)
print(oku2)
sirala = json.dumps(data,indent=4, sort_keys=True)
print(sirala)

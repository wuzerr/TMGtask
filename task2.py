import json

with open("data_test.json",'r') as f:
    obj = json.loads(f.read())
    
    for i in obj[::-1]:
        if i['surveyType'] == 'first':
            obj.remove(i)

    for i in obj:
        if ',' in i['documentType']:
            i['documentType'] = [x.strip() for x in i['documentType'].split(',')]
             


    open("result2.json","w").write(
        json.dumps(obj, indent=2, separators=(',', ': '))
    )   
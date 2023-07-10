import json

with open("data.json",'r') as f:
    obj = json.loads(f.read())
    
    for i in obj[::-1]:
        if i['surveyType'] == 'first':
            obj.remove(i)

    for i in obj:
        if ', ' in i['documentType']:
            i['documentType'] = i['documentType'].split(', ')
            


    open("test-file.json","w").write(
        json.dumps(obj, indent=2, separators=(',', ': '))
    )   
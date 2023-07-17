import json
import jsbeautifier

with open("data_test.json",'r') as f:
    obj = json.loads(f.read())
    
    for i in obj[::-1]:
        if i['surveyType'] == 'first':
            obj.remove(i)

    for i in obj:
        if ',' in i['documentType']:
            i['documentType'] = [x.strip() for x in i['documentType'].split(',')]

    options = jsbeautifier.default_options
    options.indent_size = 2
             


    open("result2.json","w").write(
        jsbeautifier.beautify(json.dumps(obj),options)
    )   

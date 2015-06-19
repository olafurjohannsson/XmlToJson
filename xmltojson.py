import json, xmltodict, sys, os.path

def convert(xml=None, filename=None):
   if filename:
      with open(filename) as f:
         data = ''.join(f.readlines())
         return convert(xml=data)
   else:
      return json.dumps(xmltodict.parse(xml))

if len(sys.argv) != 2:
   print('Usage python3 ./xmltojson <xml>')
else:
   if os.path.splitext(sys.argv[1])[1] == '.xml':
      print(convert(filename=sys.argv[1]))
   else:
      print(convert(xml=sys.argv[1]))



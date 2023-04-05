from robot.testdoc import JsonConverter, TestSuiteFactory
import json

datasources = ['CoAPs_user.robot']
options = {'name': None, 'doc': None, 'metadata': [], 'settag': [], 'test': [], 'suite': [], 'include': [], 'exclude': []}
suite = TestSuiteFactory(datasources)
json_converter = JsonConverter()
converted = json_converter.convert(suite)
with open("output.json", "w") as output_json:
    output_json.write(json.dumps(converted))

with open("output.txt", "w", encoding="utf_8") as output_txt:
    for test in converted['tests']:
        name = test['name'] + "\n"
        doc = test['doc'].replace("<p>","").replace("</p>","") + "\n\n"
        output_txt.write(name + doc)

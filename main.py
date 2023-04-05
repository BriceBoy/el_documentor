from robot.testdoc import JsonConverter, TestSuiteFactory
# import json

datasources = ['CoAPs_user.robot']
options = {'name': None, 'doc': None, 'metadata': [], 'settag': [], 'test': [], 'suite': [], 'include': [], 'exclude': []}
suite = TestSuiteFactory(datasources)
json_converter = JsonConverter()
converted = json_converter.convert(suite)
# with open("test2.json", "w") as output_file:
#     output_file.write(json.dumps(converted))
for test in converted['tests']:
    print(test['name'])
    print(test['doc'])
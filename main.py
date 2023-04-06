#!python

from robot.testdoc import JsonConverter, TestSuiteFactory
import json

class ElDocumentor():
    def __init__(self, robot_filepath: str):
        self.json_representation = JsonRepresentation(robot_filepath)

    def create_json_output(self, json_filepath):
        self.json_representation.write_json(json_filepath)
        print(f"{json_filepath} written !")

    def create_txt_output(self, txt_filepath):
        TxtMaker(self.json_representation).write_txt_file(txt_filepath)
        print(f"{txt_filepath} written !")

    def create_markdown_output(self, md_filepath):
        MarkdownMaker(self.json_representation).write_markdown_file(md_filepath)
        print(f"{md_filepath} written !")


class JsonRepresentation():
    def __init__(self, filepath):
        datasources = [filepath]
        suite = TestSuiteFactory(datasources)
        self.json_content = JsonConverter().convert(suite)

    def get_main_title(self):
        return self.json_content['name']
    
    def get_documentation(self):
        return self.json_content['doc'].replace("<p>","").replace("</p>","")
    
    def get_tests_dict(self):
        tests_dict = dict()
        for test in self.json_content['tests']:
            tests_dict[test['name']] = test['doc'].replace("<p>","").replace("</p>","")
        return tests_dict
    
    def write_json(self, json_filepath):
        with open(json_filepath, "w") as json_file:
            json_file.write(json.dumps(self.json_content))
    

class TxtMaker():
    def __init__(self, json_representation: JsonRepresentation):
        self.json_representation = json_representation

    def _get_formatted_main_title(self):
        return self.json_representation.get_main_title() + "\n"
    
    def _get_formatted_documentation(self):
        return self.json_representation.get_documentation() + "\n\n"

    def _get_formatted_tests(self):
        tests_content = ""
        for test_title, test_documentation in self.json_representation.get_tests_dict().items():
            tests_content += test_title + "\n"
            tests_content += test_documentation + "\n\n"
        return tests_content

    def write_txt_file(self, txt_filepath):
        content = self._get_formatted_main_title()
        content += self._get_formatted_documentation()
        content += self._get_formatted_tests()
        with open(txt_filepath, "w", encoding="utf_8") as txt_file:
            txt_file.write(content)

class MarkdownMaker():
    def __init__(self, json_representation: JsonRepresentation):
        self.json_representation = json_representation

    def _get_formatted_main_title(self):
        title = self.json_representation.get_main_title()
        return f"# {title}\n"

    def _get_formatted_documentation(self):
        return self.json_representation.get_documentation() + "\n\n"
    
    def _get_formatted_tests(self):
        tests_content = ""
        for test_title, test_documentation in self.json_representation.get_tests_dict().items():
            tests_content += f"## {test_title}\n"
            tests_content += test_documentation + "\n\n"
        return tests_content
    
    def write_markdown_file(self, md_filepath):
        content = self._get_formatted_main_title()
        content += self._get_formatted_documentation()
        content += self._get_formatted_tests()
        with open(md_filepath, "w", encoding="utf_8") as md_file:
            md_file.write(content)

if __name__ == "__main__":
    el_documentor = ElDocumentor("CoAPs_user.robot")
    el_documentor.create_json_output("test.json")
    el_documentor.create_txt_output("test.txt")
    el_documentor.create_markdown_output("test.md")
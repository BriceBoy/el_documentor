#!python

from robot.testdoc import JsonConverter, TestSuiteFactory
import argparse
import json
import os
import sys

OUTPUT_FILE_VALID_EXTENSIONS = [".txt", ".md", ".json"]

class ElDocumentor():
    def __init__(self, ):
        example = '''examples:
        python el_documentor.py -s test.robot -o doc.md
        python el_documentor.py --source-file test.robot --outputfile folder/doc.txt
        python el_documentor.py -s test.robot -o test.json
        '''

        self.args_parser = argparse.ArgumentParser(epilog=example, formatter_class=argparse.RawDescriptionHelpFormatter)
        self.args_parser.add_argument("-s", "--source-file", help="Path to the source file (.robot)", required=True)
        self.args_parser.add_argument("-o", "--output-file", help="Path to the output file (.md / .txt / .json)", required=True)

        self._check_args()
        self.json_representation = JsonRepresentation(self.args.source_file)

        if (self.args.output_file.endswith(".md")):
            self.create_markdown_output(self.args.output_file)
        elif (self.args.output_file.endswith(".txt")):
            self.create_txt_output(self.args.output_file)
        elif (self.args.output_file.endswith(".json")):
            self.create_json_output(self.args.output_file)
        else:
            print("Wrong outputfile format")
            return

    def _check_args(self):
        try:
            self.args = self.args_parser.parse_args()
            self._check_sourcefile_arg()
            self._check_outputfile_arg()
        except Exception as e:
            print("Unexpected parameter: " + str(e) + ", check the help documentation with -h !")
            sys.exit(0)

    def _check_outputfile_arg(self):
        file_extension = os.path.splitext(self.args.output_file)[1] # File extension incorrect
        if (not file_extension.lower() in OUTPUT_FILE_VALID_EXTENSIONS):
            print(f"Output file can not be '{file_extension}'! Only {OUTPUT_FILE_VALID_EXTENSIONS} formats are supported")
            sys.exit(0)

        if (not os.path.exists(os.path.dirname(self.args.output_file))): # Output folder not existing
            os.makedirs(os.path.dirname(self.args.output_file))

    def _check_sourcefile_arg(self):
        if (not os.path.exists(self.args.source_file)): # Source file not existing
            print(f"{self.args.source_file} does not exist!")
            sys.exit(0)

        file_extension = os.path.splitext(self.args.source_file)[1] # File extension not existing
        if (not file_extension.lower() == ".robot"):
            print(f"Source file can not be '{file_extension}'! Only '.robot' format is supported")
            sys.exit(0)

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
    el_documentor = ElDocumentor()
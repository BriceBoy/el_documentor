class TestCases:
    SECTION_TYPE = "Test Cases"

    def __init__(self, section_content):
        self.type = TestCases.SECTION_TYPE
        self.content = section_content
        self.test_cases : list(TestCase) = self.__get_test_cases()

    def __get_test_cases(self):
        test_cases = []
        test_case_content = []
        for line in self.content:
            if (self.__is_new_test_case(line)):
                if (test_case_content != None and test_case_content != []):
                    test_cases.append(TestCase(test_case_content))
                test_case_content = []
            else:
                test_case_content.append(line)
        test_cases.append(TestCase(test_case_content))
        return test_cases

    def __is_new_test_case(self, line):
        if (line.startswith("  ")):
            return False    
        if (line.startswith("\t")):
            return False 
        return True

    def to_str(self) -> str:
        representation = "=========================================================\n"
        representation += f"TYPE : {self.type}\n"
        representation += f"CONTENT : {self.content}\n"
        representation += "=========================================================\n"
        return representation

    def to_html():
        pass

class TestCase:
    def __init__(self, content):
        self.content = content
        self.__get_all_parts()

    def __get_script_usable_line(self, line):
        return line.strip().lower()

    def __get_documentation(self):
        return self.__get_sepcific_part("documentation")
            
    def __get_tags(self):
        return self.__get_sepcific_part("tags")
    
    def __get_setup(self):
        return self.__get_sepcific_part("setup")

    def __get_teardown(self):
        return self.__get_sepcific_part("teardown")

    def __get_sepcific_part(self, part_name):
        for line in self.content:
            usable_line = self.__get_script_usable_line(line)
            if (usable_line.startswith(f"[{part_name}]")):
                part = line.lstrip()[len(f"[{part_name}]"):].lstrip()
                self.content.remove(line)
                return part
    
    def __get_all_parts(self):
        self.documentation = self.__get_documentation()
        self.tags = self.__get_tags()
        self.setup = self.__get_setup()
        self.teardown = self.__get_teardown()

if __name__ == "__main__":
    import os
    with open(os.path.realpath(os.path.dirname(__file__)) + "\\..\\samples_robot\\test_cases.robot") as robot_file:
        content =  robot_file.readlines()
        test_cases = TestCases(content)
        for test in test_cases.test_cases:
            print(test.documentation)
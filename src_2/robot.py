import os

from settings import Settings
from tasks import Tasks
from test_cases import TestCases
from variables import Variables
from keywords import Keywords

class Robot:
    SECTIONS = ["keywords", "settings", "tasks", "test cases", "variables"]

    def __init__(self, robot_filepath):
        self.sections = []
        self.file_content = self.__read_file(robot_filepath)
        self.file_content = self.__refactor_mutilines_instructions()
        self.__get_sections()

    def __read_file(self, robot_filepath):
        """
        Read the content of the file at path robot_filepath and stores the content in self.file_content.

        Args:
            robot_filepath (str): Path to the .robot file

        Returns:
            list[str]: Lines of the .robot file
        """
        with open(robot_filepath) as robot_file:
            return robot_file.readlines()

    def __refactor_mutilines_instructions(self):
        """
        Refactor every multiline instruction in one line.
        Detects '...' caracters at the start of a multiline instruction and place it at the end of the previous line.
        Also remove comments.

        Returns:
            list[str]: Lines refactored to keep every instruction on one line
        """
        rearranged_lines = []
        current_line = ""
        previous_line = ""
        for line in self.file_content:
            current_line = line.replace("\n","")
            current_line = self.__remove_comments(current_line)
            if (current_line.strip().startswith("...")):
                current_line = previous_line + "    " + current_line.replace("...", "    ").lstrip()
                rearranged_lines[len(rearranged_lines) - 1] = current_line
            else:     
                rearranged_lines.append(current_line)
            previous_line = current_line
        return rearranged_lines

    def __remove_comments(self, line):
        """
        Remove comments from lines. Detects if a line starts with "#" or a word in a line starts with # as it is interpreted as a comment.

        Args:
            line (str): Line before comment removal

        Returns:
            str: Line without comment
        """
        if (not "#" in line):
            return line
        if (line.lstrip().startswith("#")):
            return ""

        temp_line = ""
        for word in line.split(" "):
            if (word.startswith("#")):
                break
            temp_line += word + " "
        return temp_line.rstrip()

    def __is_new_section(self, line):
        line = line.strip()
        if (line and line.startswith("***") and line.endswith("***")):
            return True
        else:
            return False

    def __get_sections_contents_array(self):
        sections = []
        currentLines = []

        for line in self.file_content:
            if (self.__is_new_section(line)):
                if (currentLines):
                    sections.append(currentLines)
                currentLines = []
                currentLines.append(line)
            else:
                currentLines.append(line)

        sections.append(currentLines) # Append last sections to array
        return sections

    def __get_sections(self):
        sections_contents_array = self.__get_sections_contents_array()
        for section in sections_contents_array:
            section_type = section[0].replace("*","").strip().lower()
            section_content = section[1:]
            if (section_type in Robot.SECTIONS):
                self.sections.append(self.__get_correct_section_instance(section_type, section_content))
                
    def __get_correct_section_instance(self, section_type, section_content):
        if (section_type == "keywords"):
            self.keywords_section = Keywords(section_content)
            return self.keywords_section
        elif (section_type == "settings"):
            self.settings_section = Settings(section_content)
            return self.settings_section
        elif (section_type == "tasks"):
            self.tasks_section = Tasks(section_content)
            return self.tasks_section
        elif (section_type == "test cases"):
            self.test_cases_section = TestCases(section_content)
            return self.test_cases_section
        elif (section_type == "variables"):
            self.variables_section = Variables(section_content)
            return self.variables_section
        else:
            print(f"ERROR: Unkonwn section {section_type}")
            return None

    def print_lines(self):
        for line in self.file_content:
            print(line)

    def print_sections(self):
        for section in self.sections:
            print(section.to_str())

    def debug_show_test_cases(self):
        for thing in self.test_cases_section.content:
            print(f"{thing}")


if __name__ == "__main__":
    robot = Robot(os.path.realpath(os.path.dirname(__file__)) + "\\..\\samples_robot\\full_sample.robot")
    # robot.print_lines()
    # robot.print_sections()
    robot.debug_show_test_cases()
class Robot():
    def __init__(self, file_path):
        self.lines = self.get_lines(file_path)
        self.refactor_multi_lines_instructions()

    def get_lines(self, file_path):
        with open(file_path, "r") as robot_file:
            return robot_file.readlines()

    def print_lines(self):
        for line in self.lines:
            print(line)

    def refactor_multi_lines_instructions(self):
        """
        Ramène les instructions sur plusieurs lignes en une seule et même ligne
        """
        rearranged_lines = []
        current_line = ""
        previous_line = ""
        for line in self.lines:
            current_line = line.replace("\n","")
            if (current_line.strip().startswith("...")):
                # print(repr(rearranged_lines[len(rearranged_lines) - 1]))
                # print(repr(current_line))
                current_line = previous_line + "    " + current_line.replace("...", "    ").lstrip()    # Concatène la ligne précédente et celle actuelle avec 2 espaces entre les deux
                rearranged_lines[len(rearranged_lines) - 1] = current_line
            else:     
                rearranged_lines.append(current_line)
            previous_line = current_line
        self.lines = rearranged_lines
    
    def is_new_section(self, line):
        """
        Fonction pour vérifier si la ligne actuelle correspond à une nouvelle section
        """
        line = line.strip()
        if (line and line.startswith("***") and line.endswith("***")):
            return True
        else:
            return False

def get_sections_array(self):
    """
    Fonction qui retourne un tableau contenant dans chaque case le contenu d'une section du fichier robot (Settings, Test Cases, Tests...)
    """
    sections = []
    currentLines = []
    for line in self.lines:
        if (not self.is_new_section(line)):
            currentLines.append(line)
        else:
            if (currentLines):
                sections.append(currentLines)
            currentLines = []
            currentLines.append(line)
    sections.append(currentLines)
    return sections

class Settings():
    def __init__(self, settings_lines):
        self.lines = settings_lines
        self.documentation = self.find_documentation()

    def find_documentation(self):
        for line in self.lines:
            line = line.strip()
            if (line and line.startswith("Documentation")):
                return line[len("Documentation"):].rstrip()

class Keywords():
    def __init__(self, keywords_lines):
        self.keywords = []

class Test_Cases():
    def __init__(self, test_cases_lines):
        self.test_cases = []

class Keyword:
    def __init__(self, keyword_lines) -> None:
        self.title = ""
        self.arguments = ""
        self.documentation = ""

class Test_Case:
    def __init__(self, test_case_lines) -> None:
        self.title = ""
        self.documentation = ""
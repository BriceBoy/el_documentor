SAMPLE_ROBOTS_DIR = "samples_robot/"
FILE = "sections.robot"

def get_parts(lines):
    print("\n\n===================== BEFORE =====================")
    for line in lines:
        print(line)
    lines = refactor_multilines_instructions(lines)
    print("\n\n===================== REFACTOR =====================")
    for line in lines:
        print(line)
    print("\n\n===================== SECTIONS =====================")
    sections = get_sections(lines)
    for section in sections:
        print(section[0])
    # print("\n\n===================== KEYWORDS =====================")
    # for line in lines:
    #     if (is_new_keyword(line)):
    #         print("Keyword : " + line)
    # print("\n\n===================== PARTS =====================")
    # parts = get_full_keywords(lines)
    # for part in parts:
    #     print(part)


def refactor_multilines_instructions(lines):
    """
    Fonction pour transformer les instructions sur plusieurs lignes en une seule ligne
    """
    rearranged_lines = []
    current_line = ""
    previous_line = ""
    for line in lines:
        current_line = line.replace("\n","")
        if (current_line.strip().startswith("...")):
            print(repr(rearranged_lines[len(rearranged_lines) - 1]))
            print(repr(current_line))
            current_line = previous_line + "    " + current_line.replace("...", "    ").lstrip()
            rearranged_lines[len(rearranged_lines) - 1] = current_line
        else:     
            rearranged_lines.append(current_line)
        previous_line = current_line
    return rearranged_lines

def is_new_keyword(line):
    """
    Fonction pour vérifier si la ligne actuelle correspond à un nouveau keyword
    """
    if (line and not line.startswith("  ") and not line.startswith("***")):
        return True
    else:
        return False

def get_full_keywords(lines):
    """
    Fonction qui renvoie un tableau avec le contenu complet de chaque keyword par case
    """
    keywords = []
    currentLines = []
    for line in lines:
        if (not is_new_keyword(line)):
            currentLines.append(line)
        else:
            keywords.append(currentLines)
            currentLines = []
            currentLines.append(line)
    keywords.append(currentLines)
    return keywords

def is_new_section(line):
    """
    Fonction pour vérifier si la ligne actuelle correspond à une nouvelle section
    """
    line = line.strip()
    if (line and line.startswith("***") and line.endswith("***")):
        return True
    else:
        return False

def get_sections(lines):
    """
    Fonction qui retourne un tableau contenant dans chaque case le contenu d'une section du fichier robot (Settings, Test Cases, Tests...)
    """
    sections = []
    currentLines = []
    for line in lines:
        if (not is_new_section(line)):
            currentLines.append(line)
        else:
            if (currentLines):
                sections.append(currentLines)
            currentLines = []
            currentLines.append(line)
    sections.append(currentLines)
    return sections

with open(SAMPLE_ROBOTS_DIR + FILE, "r") as robot_file:
    lines = robot_file.readlines()
    get_parts(lines)
class Tasks:
    SECTION_TYPE = "Tasks"

    def __init__(self, section_content):
        self.type = Tasks.SECTION_TYPE
        self.content = section_content
        self.tasks : list(Task) = []

    def to_str(self) -> str:
        representation = "=========================================================\n"
        representation += f"TYPE : {self.type}\n"
        representation += f"CONTENT : {self.content}\n"
        representation += "=========================================================\n"
        return representation

    def to_html():
        pass

class Task:
    def to_str() -> str:
        pass
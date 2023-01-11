class Variables:
    SECTION_TYPE = "Variables"

    def __init__(self, section_content):
        self.type = Variables.SECTION_TYPE
        self.content = section_content
        self.variables: list(Variable) = []

    def to_str(self) -> str:
        representation = "=========================================================\n"
        representation += f"TYPE : {self.type}\n"
        representation += f"CONTENT : {self.content}\n"
        representation += "=========================================================\n"
        return representation

    def to_html():
        pass

class Variable:
    def to_str() -> str:
        pass
class Settings:
    SECTION_TYPE = "Settings"

    def __init__(self, section_content):
        self.type = Settings.SECTION_TYPE
        self.content = section_content
        self.settings : list(Setting) = []

    def to_str(self) -> str:
        representation = "=========================================================\n"
        representation += f"TYPE : {self.type}\n"
        representation += f"CONTENT : {self.content}\n"
        representation += "=========================================================\n"
        return representation

    def to_html():
        pass

class Setting:
    def to_str() -> str:
        pass
class TestCases:
    SECTION_TYPE = "Test Cases"

    def __init__(self, section_content):
        self.type = TestCases.SECTION_TYPE
        self.content = section_content
        self.test_cases : list(TestCase) = []

    def to_str(self) -> str:
        representation = "=========================================================\n"
        representation += f"TYPE : {self.type}\n"
        representation += f"CONTENT : {self.content}\n"
        representation += "=========================================================\n"
        return representation

    def to_html():
        pass

class TestCase:
    def to_str() -> str:
        pass
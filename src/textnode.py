from enum import Enum


# 1. Define the TextType Enum
# This enum will categorize the different kinds of text content
# that a TextNode can hold. This makes our code more readable
# and less prone to errors than using raw strings for types.
# For a static website generator, common text types derived from
# markdown or similar markup would be:
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str = None):
        """
        Initialize a TextNode object.

        args:
            text (str): the actual text content of the node. ("Hello World", "My Link").
            text_type (TextType): The type of text this node represents (TextType.Bold, TextType.link)
            url (str, optional): the URL if the text_type is link or image. default is none.
        """
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        # check if 2 TextNode objects are equal
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    
    def __repr__(self):
        # reeturn as string a respresentation of the TextNode
        return f"TextNode(text={self.text}, text_type={self.text_type.value}, url={self.url})"
    

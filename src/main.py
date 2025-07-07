from textnode import TextNode, TextType

def main():
    """
    This function demonstrates the creation and printing of a TextNode object.
    It creates a TextNode with dummy values and then prints its string
    representation, which is defined by the __repr__ method in the TextNode class.
    """
    # Create a TextNode object with dummy values
    node = TextNode("Hello World", TextType.LINK, "https://www.boot.dev")
    
    # Print the string representation of the TextNode object
    print(node)
if __name__ == "__main__":
    main()
from src.textnode import TextNode
from src.utils.enums import TextNodeType

def main():        
    result = TextNode("This is a text node", TextNodeType.BOLD, "https://www.boot.dev")
    print(result)

if __name__ == "__main__":
    main()
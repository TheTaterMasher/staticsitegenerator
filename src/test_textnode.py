import unittest

from textnode import (
    TextNode,
    text_node_to_html_node
    )
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_text_node_to_html_node(self):
        node_text = TextNode("This is a text node", "text")
        node_bold = TextNode("This is bold text", "bold")
        node_italic = TextNode("This is italic text", "italic")
        node_code = TextNode("This is code", "code")
        node_link = TextNode("Click Me!", "link", "https://www.boot.dev")
        node_image = TextNode("This is an image", "image", "https://www.google.com/imghp?hl=en&ogbl")

        text_leaf_node = text_node_to_html_node(node_text)
        bold_leaf_noed = text_node_to_html_node(node_bold)
        italic_leaf_node = text_node_to_html_node(node_italic)
        code_leaf_node = text_node_to_html_node(node_code)
        link_leaf_node = text_node_to_html_node(node_link)
        image_leaf_node = text_node_to_html_node(node_image)

        self.assertEqual(text_leaf_node, LeafNode(None, value = "This is a text node"))
        self.assertEqual(bold_leaf_noed, LeafNode(tag = "b", value = "This is bold text"))
        self.assertEqual(italic_leaf_node, LeafNode(tag = "i", value ="This is italic text"))
        self.assertEqual(code_leaf_node, LeafNode(tag = "code", value = "This is code"))
        self.assertEqual(link_leaf_node, LeafNode(tag = "a", value = "Click Me!", props = {"href": "https://www.boot.dev"}))
        self.assertEqual(image_leaf_node, LeafNode(tag = "img", value = "", props = {"src": "https://www.google.com/imghp?hl=en&ogbl", "alt": "This is an image"}))
        
if __name__ == "__main__":
    unittest.main()
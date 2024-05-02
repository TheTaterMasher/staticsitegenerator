import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class testHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag = "a", value = "Click me!", props = {"href": "https://www.google.com"})
        node2 = LeafNode(tag = "a", value = "Click me!", props = {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        html_text = node.props_to_html()
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", html_text)
    def test_leaf_to_html(self):
        node = LeafNode(tag = "p", value = "This is a paragraph of text.")
        node2 = LeafNode(tag = "a", value = "Click me!", props = {"href": "https://www.google.com"})
        html_text = node.to_html()
        html_text2 = node2.to_html()
        self.assertEqual(html_text, "<p>This is a paragraph of text.</p>")
        self.assertEqual(html_text2, "<a href=\"https://www.google.com\">Click me!</a>")
    def test_parent_to_html(self):
        node = ParentNode(tag = "p", children = [LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text")])
        html_text = node.to_html()
        self.assertEqual(html_text, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

if __name__ == "__main__":
    unittest.main()

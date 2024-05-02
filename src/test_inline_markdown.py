import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_node_delimiter,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes
)

class TestInlineMarkdown(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        test_text_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(text_nodes, test_text_nodes)

    def test_split_node_delimiter(self):
        code_block_node = TextNode("This is text with a `code block` word", "text")
        split_code_block_node = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ]
        bold_node = TextNode("This is text with a **bolded** word", "text")
        split_bold_node = [
            TextNode("This is text with a ", "text"),
            TextNode("bolded", "bold"),
            TextNode(" word", "text"),
        ]
        italic_node = TextNode("This is text with an *italic* word", "text")
        split_italic_node = [
            TextNode("This is text with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word", "text"),
        ]
        bold1_list_node = TextNode("This is text with a **bold1** word", "text")
        bold2_list_node = TextNode("This is text with a **bold2** word", "text")
        bold3_list_node = TextNode("This is text with a **bold3** word", "text")

        list_test_node = [
            TextNode("This is text with a ", "text"),
            TextNode("bold1", "bold"),
            TextNode(" word", "text"),
            TextNode("This is text with a ", "text"),
            TextNode("bold2", "bold"),
            TextNode(" word", "text"),
            TextNode("This is text with a ", "text"),
            TextNode("bold3", "bold"),
            TextNode(" word", "text"),
        ]

        self.assertEqual(split_node_delimiter([code_block_node], "`", "code"), split_code_block_node)
        self.assertEqual(split_node_delimiter([bold_node], "**", "bold"), split_bold_node)
        self.assertEqual(split_node_delimiter([italic_node], "*", "italic"), split_italic_node)
        self.assertEqual(split_node_delimiter([bold1_list_node, bold2_list_node, bold3_list_node], "**", "bold"), list_test_node)
    
    def test_split_nodes_link(self):
        node = TextNode("This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and then theres more text","text")
        node1 = TextNode("This [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)","text")
        new_nodes = split_nodes_link([node, node1])
        test_nodes = [
            TextNode("This is text with an ", text_type_text),
            TextNode("link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
            TextNode(" and then theres more text", text_type_text),
            TextNode("This ", text_type_text),
            TextNode("link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" another ", text_type_text),
            TextNode("second link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        self.assertEqual(new_nodes, test_nodes)

    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) and then theres more text","text")
        node1 = TextNode("This image ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and this ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)","text")
        new_nodes = split_nodes_image([node, node1])
        test_nodes = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
            TextNode(" and then theres more text", text_type_text),
            TextNode("This image ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and this ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        self.assertEqual(new_nodes, test_nodes)

if __name__ == "__main__":
    unittest.main()
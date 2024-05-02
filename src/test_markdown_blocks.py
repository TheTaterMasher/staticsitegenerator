import unittest
from htmlnode import (
    ParentNode
)
from markdown_blocks import (
    block_type_paragraph,
    block_type_heading1,
    block_type_heading2,
    block_type_heading3,
    block_type_heading4,
    block_type_heading5,
    block_type_heading6,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
    markdown_to_blocks,
    block_to_blocktype,
    markdown_to_html_node
    )

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
"""
        markdown_text1 = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown_text)
        blocks1 = markdown_to_blocks(markdown_text1)
        test_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is a list item\n* This is another list item"
        ]
        test_blocks1 = [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ]
        self.assertEqual(blocks, test_blocks)
        self.assertEqual(blocks1, test_blocks1)
    
    def test_block_to_blocktype(self):
        markdown_text = """
# This is a heading

#### This is a different heading


> this is a quote

- more lists
- that are
- unordered lists

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

1. This is a ordered list item
2. This is another ordered list item
3. more order

Another paragraph
Or two

* more list
* items to
* test
"""
        blocks = markdown_to_blocks(markdown_text)
        block_types = []
        for block in blocks:
            block_types.append(block_to_blocktype(block))
        test_block_types = [
            block_type_heading1,
            block_type_heading4,
            block_type_quote,
            block_type_unordered_list,
            block_type_paragraph,
            block_type_ordered_list,
            block_type_paragraph,
            block_type_unordered_list
        ]
        self.assertEqual(block_types, test_block_types)
    
    def test_markdown_to_html_node(self):
        markdown_text = """
# This is a heading

#### This is a different heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

1. This is a ordered list item
2. This is another ordered list item
3. more order

another paragraph
or two

* more list
* items to
* test
"""
        html_node = markdown_to_html_node(markdown_text)
        print(html_node)
        #self.assertEqual(html_node, test_html_node)

if __name__ == "__main__":
    unittest.main()
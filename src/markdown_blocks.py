import re
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
block_type_paragraph = "paragraph"
block_type_heading1 = "h1"
block_type_heading2 = "h2"
block_type_heading3 = "h3"
block_type_heading4 = "h4"
block_type_heading5 = "h5"
block_type_heading6 = "h6"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unorderd_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block  == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def markdown_to_html_node(markdown):
    filtered_blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for filtered_block in filtered_blocks:
        #print(filtered_block)
        html_node = block_to_html_node(filtered_block)
        child_nodes.append(html_node)
    
    parent_node = ParentNode(tag="div", children=child_nodes, props=None)
    return parent_node

def block_to_html_node(block):
    blocktype = block_to_blocktype(block)
    if (
        blocktype == block_type_heading1
        or blocktype == block_type_heading2
        or blocktype == block_type_heading3
        or blocktype == block_type_heading4
        or blocktype == block_type_heading5
        or blocktype == block_type_heading6
        ):
        return heading_block_to_html_node(block, blocktype)
    if blocktype == block_type_paragraph:
        return paragraph_block_to_html_node(block)
    if blocktype == block_type_code:
        return code_block_to_html_node(block)
    if blocktype == block_type_quote:
        return quote_block_to_html_node(block)
    if blocktype == block_type_unordered_list:
        return unordered_list_block_to_html_node(block)
    if blocktype == block_type_ordered_list:
        return ordered_list_block_to_html_node(block)
    else:
        raise Exception("invalid block or blocktype")

def block_to_blocktype(block):
    if block.startswith("# "):
        return block_type_heading1
    if block.startswith("## "):
        return block_type_heading2
    if block.startswith("### "):
        return block_type_heading3
    if block.startswith("#### "):
        return block_type_heading4
    if block.startswith("##### "):
        return block_type_heading5
    if block.startswith("###### "):
        return block_type_heading6
    lines = block.split("\n")
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def heading_block_to_html_node(block, blocktype):
    text = block.lstrip("# ")
    children = text_to_children(text)
    return ParentNode(tag=blocktype, children=children)

def paragraph_block_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode(tag="p", children=children)

def code_block_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:3]
    children = text_to_children(text)
    code = ParentNode(tag="code", children=children)
    return ParentNode(tag="pre", children=[code])

def quote_block_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode(tag="blockquote", children=children)

def unordered_list_block_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode(tag="li", children=children))
    return ParentNode("ul", html_items)

def ordered_list_block_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode(tag="li", children=children))
    return ParentNode("ol", html_items)
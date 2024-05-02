import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)

def text_to_textnodes(text):
    new_nodes = []
    node = TextNode(text, text_type_text)
    new_nodes = split_node_delimiter([node], "**", text_type_bold)
    new_nodes = split_node_delimiter(new_nodes, "*", text_type_italic)
    new_nodes = split_node_delimiter(new_nodes, "`", text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

def split_node_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != text_type_text:
                new_nodes.append(node)
                continue
            split_nodes = []
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise Exception("Invalid Markdown syntax")
            for i in range(len(split_text)):
                if split_text[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(split_text[i], text_type_text))
                else:
                    split_nodes.append(TextNode(split_text[i], text_type))
            new_nodes.extend(split_nodes)
        return new_nodes

#this was the correct solution
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        node_text = node.text
        image_tuples = extract_markdown_images(node.text)
        if image_tuples == []:
            new_nodes.append(node)
            continue
        for tuple in image_tuples:
            split_text = node_text.split(f"![{tuple[0]}]({tuple[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.append(TextNode(tuple[0], text_type_image, tuple[1]))
            node_text = split_text[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, text_type_text))   
    return new_nodes

#this was my first attempt at this function
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        split_text = re.split(r"\[(.*?)\]\((.*?)\)", node.text)
        link_tuples = extract_markdown_links(node.text)
        if link_tuples == []:
            new_nodes.append(node)
        else:
            for text in split_text:
                is_in_tuple = False
                skip_text = False
                for tuple in link_tuples:
                    if text == tuple[0]:
                        is_in_tuple = True
                    elif text == tuple[1]:
                        skip_text = True
                if is_in_tuple:
                    for tuple in link_tuples:
                        if tuple[0] == text:
                            new_nodes.append(TextNode(tuple[0], text_type_link, tuple[1]))
                elif not skip_text:
                    if text == "" or text == " ":
                        continue
                    new_nodes.append(TextNode(text, text_type_text))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
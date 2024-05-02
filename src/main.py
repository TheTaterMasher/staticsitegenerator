from markdown_blocks import markdown_to_html_node
import os
def main():
    generate_pages_recursive("./content", "./template.html", "./public")

def extract_title(doc):
    title = ""
    split_doc = doc.split("\n\n")
    for text in split_doc:
        if text[0:2] == "# ":
            title += text
    if not title:
        raise Exception("Header required")
    return title.lstrip("# ")

def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path) or not os.path.exists(template_path):
        raise Exception("source or template files missing")
    if os.path.exists(dest_path):
        os.remove(dest_path)
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = ""
    template_file = ""
    with open(from_path) as file:
        markdown_file = file.read()
    with open(template_path) as file:
        template_file = file.read()
    title = extract_title(markdown_file)
    html_file = markdown_to_html_node(markdown_file).to_html()
    formated_html = template_file.replace(r"{{ Title }}", title)
    formated_html = formated_html.replace(r"{{ Content }}", html_file)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))
    with open(dest_path, 'a') as file:
        file.write(formated_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content = os.listdir(dir_path_content)
    for item in content:
        item_path = os.path.join(dir_path_content, item)
        item_dest_name = item.rstrip(".md") + ".html"
        item_dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            generate_page(item_path, template_path, os.path.join(dest_dir_path, item_dest_name))
        else:
            generate_pages_recursive(item_path, template_path, item_dest_path)

main()
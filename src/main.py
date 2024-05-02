from markdown_blocks import markdown_to_html_node
import os
def main():
    generate_page("./content/index.md", "./template.html", "./public/index.html")

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

    with open(dest_path, 'a') as file:
        file.write(formated_html)

main()
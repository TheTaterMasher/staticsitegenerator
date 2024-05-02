class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplemented("to_html method not implemented")
    def props_to_html(self):
        if self.props is None:
            return ""
        html_text = ""
        for prop in self.props:
            html_text += f' {prop}="{self.props[prop]}"'
        return html_text
    def __eq__(self, object):
        if self.tag == object.tag and self.value == object.value and self.children == object.children and self.props == object.props:
            return True
        else:
            return False
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
        

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value == None:
            raise ValueError("value member required for LeafNode")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.children == None:
            raise ValueError("required child argument")
        if self.tag == None:
            raise ValueError("required tag argument")
        children_html = ""
        for child in self.children:
            if child is None:
                continue
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children: {self.children}, props={self.props})"

from tree_sitter import Language, Parser
from tree_sitter_python import language

PY_LANGUAGE = Language(language())

parser = Parser(PY_LANGUAGE)

def parse_python_code(code):
    tree = parser.parse(bytes(code, "utf8"))
    return tree

def extract_classes_functions(code):
    tree = parser.parse(bytes(code, "utf8"))

    root = tree.root_node

    classes = []
    functions = []

    for child in root.children:

        if child.type == "class_definition":
            name_node = child.child_by_field_name("name")
            classes.append(name_node.text.decode())

        elif child.type == "function_definition":
            name_node = child.child_by_field_name("name")
            functions.append(name_node.text.decode())

    return {
        "classes": classes,
        "functions": functions
    }
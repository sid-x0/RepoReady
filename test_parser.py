from parser import extract_classes_functions

code = """
class User:
    pass

class Product:
    pass

def login():
    pass

def logout():
    pass
"""

result = extract_classes_functions(code)

print(result)
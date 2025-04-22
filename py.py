# find_imports.py
import os
import ast

project_path = "proxy-lite"  # change this to your project folder
imports = set()

for root, _, files in os.walk(project_path):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                try:
                    tree = ast.parse(f.read())
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for n in node.names:
                                imports.add(n.name.split('.')[0])
                        elif isinstance(node, ast.ImportFrom):
                            imports.add(node.module.split('.')[0])
                except:
                    pass

print("\n".join(sorted(imports)))

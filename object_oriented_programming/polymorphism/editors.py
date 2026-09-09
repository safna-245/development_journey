class Editors:

    def open(self):

        print("editor open method")

    def execute(self):

        print("execute traditional way python module_name.py")

class Vscode(Editors):

    def open(self):

        print("open with code .")

vscode_instance = Vscode()

vscode_instance.open()
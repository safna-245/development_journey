"""
abstraction:hide implementation details and shows only essential details

child class must have all methods in parent class 
"""
from abc import ABC, abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):

        pass

    @abstractmethod
    def debug(self):

        pass

    @abstractmethod
    def execute(self):

        pass

class Vscode(Editor):

    def open(self):

        print("open with code .")

    def debug(self):
    
        print("debuged..")

    def execute(self):

        print("executed...")
    

vscode_instance = Vscode()

vscode_instance.open()
"""
In software engineering, the delegation pattern is an object-oriented design pattern that allows object composition to achieve the same code reuse as inheritance.
In delegation, an object handles a request by delegating to a second object. The delegate is a helper object, but with the original context
"""

from abc import ABC, abstractmethod

class IPrinter(ABC):

    @abstractmethod
    def print(self):
        pass

class IScanner(ABC):

    @abstractmethod
    def scan(self):
        pass

class IPrintScanner(ABC):
    @abstractmethod
    def print(self):
        pass
    @abstractmethod
    def scan(self):
        pass

class Printer(IPrinter):

    def print(self):
        return "Printing..."

class Scanner(IScanner):
    def scan(self):
        return "Scanning....."

class PrintScanner(IPrintScanner):

    def print(self):
        printer = Printer()
        print(printer.print())
    
    def scan(self):
        scanner = Scanner()
        print(scanner.scan())

if __name__ == "__main__":
    printer: IPrinter  = PrintScanner()
    printer.print()

    scanner: IScanner = PrintScanner()
    scanner.scan()


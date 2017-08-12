"""
A python test file.
"""

class HelloWorld():
    """docstring for HelloWorld."""
    def __init__(self, n):
        self.n = n
        self.printer()


    def printer(self):
        for i in range(self.n):
            print i+1, ": Hello World!"

    def close(self):
        pass


def main():
    helloworld = HelloWorld(10)

if __name__ == "__main__":
    main()

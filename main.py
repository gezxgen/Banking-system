class Language:
    def __init__(self, name=""):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f"{self.name} is a programming language!"


def main():
    python = Language("Python")
    print(python)


if __name__ == "__main__":
    main()

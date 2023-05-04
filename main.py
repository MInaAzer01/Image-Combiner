class person:
    def __init__(self, name):
        self.name = name

    def __getname(self):
        print(self.name)

    def getname(self):
        person.__getname(self)


body = person("body")
body.getname()

class ss:
    def __init__(self,string):
        self.string = string
        self.len = len(string)
    def __add__(self,other):
        return self.len + other.len

class test():
    
    def __init__(self,name='Bot_1'):
        self.name = name

    def sayhi(self,msg="Hey! It's {name}.".format(name = self.name)):
        return "{name} says: {msg2}".format(name=self.name,msg2=msg)
        
    @classmethod
    def present(cls):
        return cls.sayhi()
a = test()
print(a.present())

from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self,app):
        pass
    def run(self,app):
        self.process(app)

class laptop(Computer):
    def process(self,app):
        print(f"{app} is running in laptop")

class mobile(Computer):
    def process(self,app):
        print(f"{app} is running in Mobile.")

lap=laptop()
lap.run("Chrome")
mob=mobile()
mob.run("PUBG")
class IChair():
    def get_dimensions(self):
        '''chair interface'''

class BigChair(IChair):

    def __init__(self):
        self.height = 80
        self.width = 70
        self.depth = 60

    def get_dimensions(self):
        return {"height":self.height, "width":self.width, "depth":self.depth}

class MediumChair(IChair):

    def __init__(self):
        self.height = 50
        self.width = 50
        self.depth = 40
        self.color = 'Green'

    def get_dimensions(self):
        return {"height":self.height, "width":self.width, "depth":self.depth}

class ChairFactory():

    def get_chair(chairtype):
        try:
            if chairtype == "BigChair":
                return BigChair()
            elif chairtype == "MediumChair":
                return MediumChair()
            raise AssertionError("Chair not found")

        except AssertionError as _e:
            print(_e)

if __name__=="__main__":
    CHAIR = ChairFactory.get_chair("MediumChair")
    print(CHAIR.get_dimensions())
    print(CHAIR.height)


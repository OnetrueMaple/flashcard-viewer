class Flashcard:
    id = ""
    front_content = ""
    back_content = ""

    def __init__(self, json=None):
        if(json != None):
            self.id = json["id"]
            self.front_content = json["front_content"]
            self.back_content = json["back_content"]

    # My C++ boilerplate code habits are showing. I didn't know that Python doesn't make this necessary at the time.
    def setID(self, id):
        self.id = id

    def setFront(self, front):
        self.front_content = front

    def setBack(self, back):
        self.back_content = back

    def getID(self):
        return self.id

    def getFront(self):
        return self.front_content

    def getBack(self):
        return self.back_content
class Card:
    def __init__(self):
        self.status = "new"
        self.word = ""
        self.translation = ""
        self.timeNext = 0
        self.numTimesCorrect = 0

    def getCardfromDb(self):
        return 

    def setCardToDb(self):
        return

    def setWord(self,status, word, translation):
        self.status = status
        self.word = word
        self.translation = translation

    def setTimeNext(self, timeNext):
        self.timeNext = timeNext

    def getTimeNext(self):
        return self.timeNext

    def getWord(self):
        return self.status, self.word, self.translation

    def calculateTimeNext(self):
        if (self.numTimesCorrect == 0):
            self.timeNext = 0
        elif(self.numTimesCorrect == 1):
            self.timeNext = 1
        elif(self.numTimesCorrect == 2):
            self.timeNext = 3
        elif(self.numTimesCorrect == 3):
            self.timeNext = 7
        else:
            self.timeNext = 30

    
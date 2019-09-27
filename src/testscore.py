class TestScore:
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score

    def getAverage(self):
        self.average = sum(self.score)/len(self.score)

    def printAverage(self):
        print(self.subject, self.average)


avgEng = TestScore("Eng", [50, 50, 50, 50, 50])
avgEng.getAverage()
avgEng.printAverage()

avgMath = TestScore("Math", [50, 50, 50, 50, 50])
avgMath.getAverage()
avgMath.printAverage()

class Data:
    def __init__(self):
        self.content1 = "これはテスト"
        self.content2 = "です"
        self.count = 0
    def txt(self):
        return self.content1 + str(self.count) + self.content2
    def yes(self):
        self.count += 1
    def no(self):
        self.count += 2
    def isQuestion(self):
        return self.count < 5

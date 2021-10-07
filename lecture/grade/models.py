'''
학생이름, 국어 kor, 영어 eng, 수학 math 를 입력 받아서
학생이름, 평균점수를 통해 A ~ F를 출력하시오.
'''


class Grade(object):

    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)

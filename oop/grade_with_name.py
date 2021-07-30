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

    @staticmethod
    def main():
        student = Grade(input('학생 이름 입력: '))
        for i in ['Korean', 'English', 'Math']:
            student.addScores(int(input(f'{i} 점수 입력: ')))

        avg = student.avg()
        print(f'{student.name}의 성적은...\n3과목 평균 점수: {avg:.2f}', end=', ')
        if avg >= 90:
            print('A 학점')
        elif avg >= 80:
            print('B 학점')
        elif avg >= 70:
            print('C 학점')
        elif avg >= 60:
            print('D 학점')
        elif avg >= 50:
            print('E 학점')
        else:
            print('F 학점')


Grade.main()
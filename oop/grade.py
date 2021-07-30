'''
국어 kor, 영어 eng, 수학 math 를 입력 받아서
평균점수를 통해 A ~ F를 출력하시오.
'''


class Grade(object):
    def __init__(self, name, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def average(self):
        return float(self.sum() / 3)

    # @staticmethod
    # def main():
    def avercontroll(self):
        aver = Grade(input('학생 이름 입력: '), int(input('국어점수 입력: ')), int(input('영어점수 입력: ')), int(input('수학점수 입력: '))).average()
        
        if aver >= 90:
            print(f'3과목 평균 점수: {aver:.2f}, A 학점')
        elif aver >= 80:
            print(f'3과목 평균 점수: {aver:.2f}, B 학점')
        elif aver >= 70:
            print(f'3과목 평균 점수: {aver:.2f}, C 학점')
        elif aver >= 60:
            print(f'3과목 평균 점수: {aver:.2f}, D 학점')
        elif aver >= 50:
            print(f'3과목 평균 점수: {aver:.2f}, E 학점')
        else:
            print(f'3과목 평균 점수: {aver:.2f}, F 학점')

# Grade.main()
from lecture.grade.models import Grade

if __name__ == '__main__':
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
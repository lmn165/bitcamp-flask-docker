from sklearn.ensemble import RandomForestClassifier
import mypandas as pd

from lecture.common.moels import ValueObject
from lecture.menu.models import menu2
from lecture.titanic.models import titanic_service

if __name__ == '__main__':
    vo = ValueObject()
    titanic = titanic_service()
    while 1:
        menu = menu2(['exit', 'plotting',
                           'preprocessing', 'learning'])
        if menu == 1:
            vo.train = titanic.new_model("train")
            vo.test = titanic.new_model("test")
            titanic.plot_survived_dead(vo)
            titanic.plot_pclass(vo)
            #titanic.plot_embarked(vo)
            titanic.plot_gender(vo)
        elif menu == 2:
            vo.train = titanic.new_model("train")
            vo.test = titanic.new_model("test")
            vo.id = vo.test['PassengerId']
            vo.label = titanic.create_label(vo)
            vo.train = titanic.drop_label(vo)
            vo = titanic.embarked_nominal(vo)

            vo = titanic.title_nominal(vo)
            vo = titanic.gender_nominal(vo)
            vo = titanic.age_ordinal(vo)
            vo = titanic.fare_ordinal(vo)
            vo = titanic.drop_feature(vo, 'Name', 'Cabin', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch', 'Ticket')
        elif menu == 3:

            print(f'SKLearn Algorithm Accuracy is {titanic.accuracy_by_classfier(vo)}')
            print(f'\nThe Info of Train is {vo.train.info()},\nThe Info of Test is {vo.test.info()}')
            print('#'*100)
            print(f' Test PassengerId ::: {vo.test["PassengerId"][0]}\n ')
            print(f' Train Pclass ::: {vo.train["Pclass"][0]}, Test Pclass ::: {vo.test["Pclass"][0]}\n')
            print(f' Train Embarked ::: {vo.train["Embarked"][0]}, Test Embarked ::: {vo.test["Embarked"][0]}\n')
            print(f' Train Title ::: {vo.train["Title"][0]}, Test Title ::: {vo.test["Title"][0]}\n')
            print(f' Train Gender ::: {vo.train["Gender"][0]}, Test Gender ::: {vo.test["Gender"][0]}\n')
            print(f' Train AgeGroup ::: {vo.train["AgeGroup"][0]}, Test AgeGroup ::: {vo.test["AgeGroup"][0]}\n')
            print(f' Train FareBand ::: {vo.train["FareBand"][0]}, Test FareBand :::  {vo.test["FareBand"][0]}\n')
            print(f'Null Count of Train is {vo.train.isnull().sum()} '
                  f'Null Count of Test is {vo.test.isnull().sum()}')
            # clf = RandomForestClassifier()
            # clf.fit(vo.train, vo.test)
            # prediction = clf.predict(vo.test)
            # pd.DataFrame({'PassengerId': vo.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)
        else:
            break

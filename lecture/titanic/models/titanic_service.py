<<<<<<< HEAD:lecture/titanic/legacy/models/titanic_service.py
from lecture.titanic.legacy.models.dataset import Dataset
import mypandas as pd
=======
from lecture.titanic.models.dataset import Dataset
import pandas as pd
>>>>>>> 35435834777e479117f611cc4465f5fe32d2ce9b:lecture/titanic/models/titanic_service.py
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

'''
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
    'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
'''
class TitanicService(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        return pd.read_csv(f"/data/{payload}.csv")
    '''
    ML(머신러닝) 에서의 지도학습은
    # axis: 축, 여기서는 지정된 축을 빼서 지움..
    this.train.drop('Survived', axis=1) -> 테이블에서 답을 빼서 지우고
    this.train['Survived'] -> 빼낸 답을 따로 담는다.
    
    @staticmethod
    this -> 외부(view) 에서 받아온 값을 하나로 감싼 것 
    '''
    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)
    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']
    '''
    *feature: 삭제할 속성들을 하나로 묶어서 받음
    '''
    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3}) # {} -> 인스턴스 의미
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3}) # {} -> 인스턴스 의미
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['Fare'] = this.train['Fare'].fillna(1)
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels={1, 2, 3, 4})
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1, 2, 3, 4})
        # qcut() 을 사용하면 자동으로 구간을 n등분 한다.
        # 타이타닉에서는 bins = [-1, 8, 15, 31, np.inf]    # inf 는 infinite(무한) 을 의미
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset["Title"] = dataset['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            dataset["Title"] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset["Title"] = dataset['Title'].replace('Mlle', 'Mr')
            dataset["Title"] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        combine = [this.train, this.test]
        sex_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].map(sex_mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6,
                       'Senior': 7}
        # qcut은 n등분을 하며, cut은 bins에 따라 커스터마이징 된 값으로 나눈다.
        for i in train, test:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    '''
    모델을 만듦
    10번을 반복하며, 랜덤으로...
    '''
    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)
    '''
    accuracy: 정확도
    round(np.mean(score) * 100, 2) 나온 값(실수)을 소수점 이하 2자리 까지 뽑고, *100
    -> ex) 0.2547 -> 0.25 -> 25
    '''
    def accuracy_by_classfier(self, this):
        score = cross_val_score(RandomForestClassifier(),
                                this.train,
                                this.label,
                                cv=self.create_k_fold(),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)


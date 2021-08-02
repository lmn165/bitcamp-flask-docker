from titanic.models.dataset import Dataset
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier


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
    *feature: 
    '''
    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    def embarked_nominal(self):
        return None

    def fare_oridnal(self):
        return None

    def title_nominal(self):
        return None

    def gender_norminal(self):
        return None

    def age_ordinal(self):
        return None

    def create_k_fold(self):
        return None

    def accuracy_by_classfier(self):
        return None



from titanic.models.dataset import Dataset
from titanic.models.titanic_service import TitanicService
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier

class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self, train, test):
        # view = self.view
        this = self.preprocessing(train, test)
        print(f'The Type of This is {type(this)}')
        print(f'The Type of Train is {this.train.head(2)}')
        print(f'The Type of Test is {this.test.head(2)}')
        return this

    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        return this
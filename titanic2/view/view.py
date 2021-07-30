from titanic2.models.dataset import Dataset
from titanic2.models.service import Service


class View(object):
    service = Service()
    data_set = Dataset()

    def modeling(self, test, train):
        this = self.data_set
        service = self.service
        this.test = service.new_model(test)
        this.train = service.new_model(train)
        print(f'The Type of This is {type(this)}')
        print(f'The Type of Train is {this.train.head(2)}')
        print(f'The Type of Test is {this.test.head(2)}')

    # def preprocessing(self, test, train) -> object:
    #     pass


if __name__ == '__main__':
    view = View()
    view.modeling('test.csv', 'train.csv')
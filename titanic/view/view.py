from titanic.models.dataset import Dataset
from titanic.models.service import Service


class View(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        # view = self.view
        this = self.preprocessing(train, test)
        print(f'여기는 타이타닉 패키지...')
        print(f'The Type of This is {type(this)}')
        print(f'The Type of Train is {this.train.head(2)}')
        print(f'The Type of Test is {this.test.head(2)}')

    def preprocessing(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        return this

if __name__ == '__main__':
    view = View()
    view.modeling('train.csv', 'test.csv')
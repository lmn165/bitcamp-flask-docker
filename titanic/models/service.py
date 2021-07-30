import pandas as pd

from titanic.models.dataset import Dataset


class Service(object):
    data_set = Dataset()

    def new_model(self, payload) -> object:
        this = self.data_set
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context+this.fname)


def create_train(this) -> object:
    return this


def create_label(this) -> object:
    return this


def drop_feature(this, *feature) -> object:
    return this


def embarked_nominal(this) -> object:
    return this


def fare_oridnal(this) -> object:
    return this


def title_nominal(this) -> object:
    return this


def gender_norminal(this) -> object:
    return this


def age_ordinal(this) -> object:
    return this


def create_k_fold() -> object:
    return None


def accuracy_by_classfier(this) -> str:
    return ""
from dataclasses import dataclass


@dataclass
class Dataset(object):
    context: str
    fname: str
    test: object
    train: object

    @property
    def context(self) -> str: return self._context
    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def test(self) -> object: return self._test
    @test.setter
    def test(self, test): self._test = test

    @property
    def train(self) -> object: return self._train
    @train.setter
    def train(self, train): self._train = train
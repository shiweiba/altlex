import sklearn

from chnlp.ml.sklearner import Sklearner

class SGD(Sklearner):
    def __init__(self):
        #super().__init__()
        Sklearner.__init__(self)
        self.classifier = sklearn.linear_model.SGDClassifier(n_iter=20,
                                                             penalty='elasticnet',
                                                             alpha=1.0000000000000001e-05)

    def _feature_importances(self):
        return self.model.coef_

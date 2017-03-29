# -*- coding: utf-8 -*-
"""The Thompson (Bayesian) index policy, using an average of 20 index. By default, it uses a Beta posterior.
Reference: [Thompson - Biometrika, 1933].
"""

__author__ = "Lilian Besson"
__version__ = "0.6"

import numpy as np
from .Thompson import Thompson
from .Beta import Beta


#: Default value of how many indexes are computed by sampling the posterior
#: for the ThompsonRobust variant.
AVERAGEON = 10


class ThompsonRobust(Thompson):
    """The Thompson (Bayesian) index policy, using an average of 20 index. By default, it uses a Beta posterior.
    Reference: [Thompson - Biometrika, 1933].
    """

    def __init__(self, nbArms, posterior=Beta, averageOn=AVERAGEON, lower=0., amplitude=1.):
        super(Thompson, self).__init__(nbArms, posterior=posterior, lower=lower, amplitude=amplitude)
        assert averageOn >= 1, "Error: invalid value for 'averageOn' parameter for ThompsonRobust, should be >= 1."
        self.averageOn = averageOn  #: How many indexes are computed before averaging

    def __str__(self):
        return "%s(averageOn = %i)" % (self.__class__.__name__, self.averageOn)

    def computeIndex(self, arm):
        """ Compute the current index for this arm, by sampling averageOn times the posterior and returning the average index. """
        return np.mean([self.posterior[arm].sample() for _ in range(self.averageOn)])

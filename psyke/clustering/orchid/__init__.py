from __future__ import annotations

from collections import Iterable

import numpy as np
import pandas as pd
from sklearn.base import ClassifierMixin
from tuprolog.theory import Theory

from psyke import Extractor
from psyke.clustering.creepy import CReEPy
from psyke.utils import Target


class ORCHiD(CReEPy):
    """
    Explanator implementing ORCHiD algorithm.
    """

    def __init__(self, predictor, depth: int, error_threshold: float, output: Target = Target.CONSTANT,
                 gauss_components: int = 5, ranks: list[(str, float)] = [], ignore_threshold: float = 0.0):
        super().__init__(predictor, depth, error_threshold, output, gauss_components, ranks, ignore_threshold)
        self.clustering = Extractor.cream(depth, error_threshold, Target.CLASSIFICATION if
                                          isinstance(predictor, ClassifierMixin) else output, gauss_components)

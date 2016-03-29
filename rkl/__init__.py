"""Computational kernels common in radar signal processing.

.. currentmodule:: rkl

Modules
-------

.. autosummary::
    :toctree:

    delay_multiply
    time_varying_conv

"""
from . import delay_multiply
from . import time_varying_conv

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

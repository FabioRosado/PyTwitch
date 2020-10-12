# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

from .api import Helix

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "pytwitch"
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound

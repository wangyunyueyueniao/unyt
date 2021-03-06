# -*- coding: utf-8 -*-
"""
Predefined useful aliases to physical units

Note that all of these names can be imported from the top-level unyt namespace.
For example::

    >>> from unyt import cm, g, s
    >>> data = [3, 4, 5]*g*cm/s
    >>> print(data)
    [3 4 5] cm*g/s

.. show_all_units::

"""

# -----------------------------------------------------------------------------
# Copyright (c) 2018, yt Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the LICENSE file, distributed with this software.
# -----------------------------------------------------------------------------

from unyt.unit_registry import default_unit_registry as _default_unit_registry
from unyt.unit_systems import add_symbols as _add_symbols

_add_symbols(globals(), registry=_default_unit_registry)

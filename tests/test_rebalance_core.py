# This file is part of rebalance-core.
#
# Copyright © 2020 Datto, Inc.
# Author: Alex Parrill <aparrill@datto.com>
#
# Licensed under the GNU Lesser General Public License Version 3
# Fedora-License-Identifier: LGPLv3+
# SPDX-2.0-License-Identifier: LGPL-3.0+
# SPDX-3.0-License-Identifier: LGPL-3.0-or-later
#
# rebalance-core is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rebalance-core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with rebalance-core.  If not, see <https://www.gnu.org/licenses/>.
#

from rebalance_core import __version__


def test_version():
    assert __version__ == "0.1.0"

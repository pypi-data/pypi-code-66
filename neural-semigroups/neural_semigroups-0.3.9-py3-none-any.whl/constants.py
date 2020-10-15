"""
   Copyright 2019-2020 Boris Shminke

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from os import environ, path

import torch

GAP_PACKAGES_URL = "https://www.gap-system.org/pub/gap/gap4/tar.bz2/packages/"
CAYLEY_DATABASE_PATH = path.join(environ["HOME"], "neural-semigroups-data")
CURRENT_DEVICE = (
    f"cuda:{torch.cuda.current_device()}"
    if torch.cuda.is_available()
    else "cpu"
)

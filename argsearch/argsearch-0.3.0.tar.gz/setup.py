# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['argsearch']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.1,<2.0.0',
 'scikit-optimize>=0.8.1,<0.9.0',
 'scipy>=1.5.2,<2.0.0',
 'sobol_seq>=0.2.0,<0.3.0',
 'tqdm>=4.49.0,<5.0.0']

entry_points = \
{'console_scripts': ['argsearch = argsearch:main']}

setup_kwargs = {
    'name': 'argsearch',
    'version': '0.3.0',
    'description': 'Run a command many times with different combinations of its inputs.',
    'long_description': '# argsearch\n`argsearch` is a simple and composable tool for sweeping over the arguments of another program.\nIt aims to easily automate tasks like hyperparameter tuning and setting simulation parameters, while only requiring that your program accepts command-line arguments in some form.\n\nKey features include:\n - Easy integration with any program that takes command-line arguments.\n - Support for searching over integer, floating-point, and categorical arguments with several search strategies.\n - Smart search algorithms, including Bayesian optimization and low-discrepancy random search.\n - The ability to produce JSON-structured output, making it composable with other command-line tools like [`jq`](https://stedolan.github.io/jq/).\n - Multiprocessing, enabling running many experiments in parallel.\n \n![MIT license badge](https://img.shields.io/github/license/maxwells-daemons/argsearch)\n![Python version badge](https://img.shields.io/pypi/pyversions/argsearch)\n\n## Examples\n### Basic usage\n```\n$ argsearch grid 3 "echo {a} {b}" --a 1 10 --b X Y\n--- [0] echo 1 X\n1 X\n--- [1] echo 5 X\n5 X\n--- [2] echo 10 X\n10 X\n--- [3] echo 1 Y\n1 Y\n--- [4] echo 5 Y\n5 Y\n--- [5] echo 10 Y\n10 Y\n100%|██████████████████████████████| 6/6 [00:00<00:00, 220.49it/s]\n```\n### Composing pipelines with `argsearch` and `jq`\n```\n$ argsearch --output-json repeat 2 "echo hello" | jq\n[\n  {\n    "step": 0,\n    "command": "echo hello",\n    "stdout": "hello\\n",\n    "stderr": "",\n    "returncode": 0\n  },\n  {\n    "step": 1,\n    "command": "echo hello",\n    "stdout": "hello\\n",\n    "stderr": "",\n    "returncode": 0\n  }\n]\n```\n\n```\n$ argsearch --output-json random 5 "echo {x}" --x LOG 1e-3 1e3 | jq -j \'.[] | .stdout\' | sort\n0.00346280772906192\n0.026690253595621032\n0.08766768693592873\n0.24965066831702154\n291.68909574884617\n```\n\n### Black-box optimization\n```\n$ argsearch maximize 13 "echo {a}" --a 1 1000  | tail\n--- [8] echo 249\n249\n--- [9] echo 116\n116\n--- [10] echo 999\n999\n--- [11] echo 1000\n1000\n--- [12] echo 1000\n1000\n```\n\n## Installation\n\n```\npip install argsearch\n```\n\n## Usage\n\n`argsearch` has 3 mandatory arguments:\n - A **search strategy** (`random`, `quasirandom`, `grid`, `repeat`, `maximize`, or `minimize`) and its configuration:\n    - For `random`, `quasirandom`, `maximize`, and `minimize`: the number of trials to run.\n    - For `grid`: the number of points to try in each numeric range.\n    - For `repeat`: the number of times to repeat the command.\n - A **command string** with **templates** designated by bracketed names (e.g. `\'python my_script.py --flag {value}\'`.\n -  A **range** for each template in the command string (e.g. `--value 1 100`).\n\nThen, `argsearch` runs the command string several times, each time replacing the templates with values from their associated ranges.\n\nAny optional arguments (`--num-workers`, `--output-json`, or `--disable-bar`) must appear before these.\nI recommend you single-quote the command string to avoid shell expansion issues. Templates may appear multiple times in the command string (e.g. to name an experiment\'s output directory after its hyperparameters).\n\n### Search Strategies\n\nThe search strategy determines which commands get run by sampling from the ranges.\nThe search strategies currently implemented are:\n - **Random search** samples uniformly randomly from specified ranges for a fixed number of trials.\n - **Quasirandom search** samples quasi-randomly according to a low-discrepancy [Sobol sequence](https://en.wikipedia.org/wiki/Sobol_sequence). This is recommended over random search in almost all cases because it fills the search space more effectively and avoids redundant experiments.\n - **Grid search** divides each numeric range into a fixed number of evenly-spaced points and runs once for each possible combination of inputs.\n - **Repeat** runs the same command a fixed number of times, and does not accept templates.\n - **Minimize** tries to minimize the program\'s output with [Bayesian black-box optimization](https://en.wikipedia.org/wiki/Bayesian_optimization).\n - **Maximize** is like minimize, but for maximization.\n \nMaximize and minimize both require that your program\'s last line of stdout is a single number, representing the quantity to optimize.\n\n### Ranges\n\nFor each template that appears in the command string, you must provide a range that determines what values may be substituted into the template.\nThree types of ranges are available:\n - **Floating-point ranges** are specified by a minimum and maximum floating-point value (e.g. `--value 0.0 1e3`).\n - **Integer ranges** are specified by a minimum and maximum integer (e.g. `--value 1 100`). Integer ranges are guaranteed to only yield integer values.\n - **Categorical ranges** are specified by a list of non-numeric categories, or more than two numbers (e.g. `--value A B C`, `--value 2 4 8 16`). Categorical ranges only draw values from the listed categories, and are not divided up during a grid search.\n \nFloating-point and integer ranges may be converted to **logarithmic ranges** by specifying `LOG` before their minimum and maximum (e.g. `--value LOG 16 256`).\nThese ranges are gridded and sampled log-uniformly instead of uniformly, so that each order of magnitude appears roughly equally often. \n \n### Output\n\nBy default, `argsearch` streams each command\'s output to the standard output/error streams as soon as it\'s available. \nWith the `--output-json` flag, `argsearch` will instead collect all output into a JSON string, printed to `stdout` at the end of the run.\nThis JSON data can be pretty-printed or wrangled with [`jq`](https://stedolan.github.io/jq/) for use in shell pipelines. \n\n### Multiprocessing\n\nProviding `--num-workers N` runs commands in parallel with N worker processes. In this case, output will only appear on the standard streams once each command\'s done, to avoid mixing output from different runs. The format remains the same, but results are not guaranteed to come back in any particular order.\n\n### License\n`argsearch` is licensed under the MIT License.\n',
    'author': 'Aidan Swope',
    'author_email': 'aidanswope@gmail.com',
    'maintainer': 'Aidan Swope',
    'maintainer_email': 'aidanswope@gmail.com',
    'url': 'https://github.com/maxwells-daemons/argsearch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

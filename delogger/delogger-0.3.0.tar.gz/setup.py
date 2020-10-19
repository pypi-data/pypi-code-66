# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['delogger',
 'delogger.decorators',
 'delogger.filters',
 'delogger.handlers',
 'delogger.loggers',
 'delogger.modes',
 'delogger.presets',
 'delogger.util']

package_data = \
{'': ['*']}

install_requires = \
['colorlog>=4.2.1,<5.0.0']

setup_kwargs = {
    'name': 'delogger',
    'version': '0.3.0',
    'description': 'delogger is a convenient logging package',
    'long_description': '# delogger\n\n[![PyPI](https://badge.fury.io/py/delogger.svg)](https://badge.fury.io/py/delogger)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/deresmos/delogger/blob/master/LICENSE)\n![test](https://github.com/deresmos/delogger/workflows/Python%20Test/badge.svg)\n![CodeQL](https://github.com/deresmos/delogger/workflows/CodeQL/badge.svg)\n\n## About\n\nDelogger is a Python package that makes easy use of decided logging.\n\n### Delogger\n\n- It behaves like normal logging.\n\n### DeloggerQueue\n\n- Non-blocking logging using QueueHandler.\n\n## Installation\n\nTo install Delogger, use pip.\n\n```bash\npip install delogger\n\n```\n\n## Sample\n\n### Debug stream and output log\n\n```python\nfrom delogger.presets.debug import logger\n\nif __name__ == "__main__":\n    logger.debug("debug msg")\n    logger.info("info msg")\n    logger.warning("warn msg")\n    logger.error("error msg")\n    logger.critical("critical msg")\n```\n\nOutput\n![debug_sample_output]()\n\nFile output (./log/20201010_164622.log)\n```\n2020-10-10 16:46:22.050 DEBUG debug_preset.py:4 <module> debug msg\n2020-10-10 16:46:22.050 INFO debug_preset.py:5 <module> info msg\n2020-10-10 16:46:22.051 WARN debug_preset.py:6 <module> warn msg\n2020-10-10 16:46:22.051 ERROR debug_preset.py:7 <module> error msg\n2020-10-10 16:46:22.051 CRIT debug_preset.py:8 <module> critical msg\n```\n\n\nand more [samples](https://github.com/deresmos/delogger/tree/main/tests)\n\n## Preset\n\n- `debug`: Output color debug log and save log file.\n- `debug_stream`: Output color debug log.\n- `output`: Save log file and notify to slack.\n- `profiler`: Same debug preset and seted profiles decorator.\n\n## Mode\n\n- `CountRotatingFileMode`: Backup count rotating.\n- `TimedRotatingFileMode`: Same logging.handlers.TimedRotatingFileHandler.\n- `SlackWebhookMode`: Log to slack. (Incomming webhook)\n- `SlackTokenMode`: Log to slack. (token key)\n- `StreamColorDebugMode`: Output color log. (debug and above)\n- `StreamDebugMode`: Output noncolor log. (debug and above)\n- `StreamInfoMode`: Output noncolor log. (info and above)\n- `PropagateMode`: Set Setropagate true.\n\n## Environment\n\n- `DELOGGER_NAME`: logger name for presets.\n- `DELOGGER_FILEPATH`: output log filepath for presets.\n- `DELOGGER_SLACK_WEBHOOK`: send slack for presets.\n\n## Decorator\n\nInject decorator into logger.\n\n### debuglog\n\n```text\nDEBUG 21:00:00 debug_log.py:32 START test args=(\'test\',) kwargs={}\nDEBUG 21:00:01 debug_log.py:39 END test return=value\n```\n\n### line_profile\n\nRequired [line_profiler](https://github.com/pyutils/line_profiler) package.\n\n```text\nDEBUG 21:38:22 line_profile.py:28 line_profiler result\nTimer unit: 1e-06 s\n\nTotal time: 6.4e-05 s\nFile: test.py\nFunction: test at line 6\n\nLine #      Hits         Time  Per Hit   % Time  Line Contents\n==============================================================\n     6                                           @logger.line_profile\n     7                                           def test(arg1):\n     8       101         43.0      0.4     67.2      for i in range(100):\n     9       100         21.0      0.2     32.8          pass\n    10         1          0.0      0.0      0.0      return i\n```\n\n### memory_profile\n\nRequired [memory_profiler](https://github.com/pythonprofilers/memory_profiler) package.\n\n```text\nDEBUG 21:40:31 memory_profile.py:25 memory_profiler result\nFilename: test.py\n\nLine #    Mem usage    Increment   Line Contents\n================================================\n     6    37.96 MiB    37.96 MiB   @logger.memory_profile\n     7                             def test(arg1):\n     8    45.43 MiB     7.47 MiB       a = [0] * 1000 * 1000\n     9    45.43 MiB     0.00 MiB       for i in range(100):\n    10    45.43 MiB     0.00 MiB           pass\n    11    45.43 MiB     0.00 MiB       return i\n```\n\n### line_memory_profile\n\nRequired [line_profiler](https://github.com/pyutils/line_profiler) and [memory_profiler](https://github.com/pythonprofilers/memory_profiler) package.\n\n```text\nDEBUG 21:41:08 line_memory_profile.py:70 line, memory profiler result\nTimer unit: 1e-06 s\n\nTotal time: 0.004421 s\nFile: test.py\nFunction: test at line 6\n\nLine #      Hits         Time  Per Hit   % Time    Mem usage    Increment   Line Contents\n=========================================================================================\n     6                                             37.96 MiB    37.96 MiB   @logger.line_memory_profile\n     7                                                                      def test(arg1):\n     8         1       4355.0   4355.0     98.5    45.43 MiB     7.47 MiB       a = [0] * 1000 * 1000\n     9       101         33.0      0.3      0.7    45.43 MiB     0.00 MiB       for i in range(100):\n    10       100         32.0      0.3      0.7    45.43 MiB     0.00 MiB           pass\n    11         1          1.0      1.0      0.0    45.43 MiB     0.00 MiB       return i\n```\n\n### add_line_profile\n\n- It can adjust the timing of profile output\n\nRequired [line_profiler](https://github.com/pyutils/line_profiler) package.\n\n```text\nDEBUG 21:45:55 line_profile.py:67 line_profiler_stats result\nTimer unit: 1e-06 s\n\nTotal time: 0.009081 s\nFile: test.py\nFunction: test at line 6\n\nLine #      Hits         Time  Per Hit   % Time  Line Contents\n==============================================================\n     6                                           @logger.add_line_profile\n     7                                           def test(arg1):\n     8         2       8957.0   4478.5     98.6      a = [0] * 1000 * 1000\n     9       202         71.0      0.4      0.8      for i in range(100):\n    10       200         52.0      0.3      0.6          pass\n    11         2          1.0      0.5      0.0      return i\n```\n',
    'author': 'deresmos',
    'author_email': 'deresmos@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/deresmos/delogger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

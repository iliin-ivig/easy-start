Put you static files here.

To get access to this `readme` file, you can run:
```python
import easy_start
import os

path_to_this_file = os.path.join(easy_start.__file__, 'static', 'README.md')
assert os.path.exists(path_to_this_file)
```
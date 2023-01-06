Put you static files here.

To get access to this `readme` file, you can run:
```python
import {{package_name}}
import os

path_to_this_file = os.path.join({{package_name}}.__file__, 'static', 'README.md')
assert os.path.exists(path_to_this_file)
```

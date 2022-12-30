# Installation
From cloned repo:
```sh
pip3 install path/to/cloned/repo
```

From cloud-based git repository:
```sh
pip3 install git+ssh://git@{{url}}
```

{% if scripts %}
# Scripts
This package provides the following scripts:

    {% for script in scripts %}
    - `{{script}}`
    {% endfor %}
{% endif %}

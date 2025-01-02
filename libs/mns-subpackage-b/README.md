# 

from https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages

`pytest libs/*/tests` or `python -m pytest /opt/libs/*/tests`
debugging: `python -m debugpy --listen 0.0.0.0:5679 --wait-for-client -m pytest --cache-clear /opt/libs/*/tests`
#!/bin/bash

pip install twine || pip3 install twine
python setup.py sdist || python3 setup.py sdist
twine upload \
    --username "pupil-labs" \
    --password "$PyPIPassword" \
    --skip-existing \
    ./dist/*

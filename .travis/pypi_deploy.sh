#!/bin/bash

pip install twine || pip3 install twine 
twine upload \
    --username "pupil-labs" \
    --password "$PyPIPassword" \
    --skip-existing \
    ./dist/*

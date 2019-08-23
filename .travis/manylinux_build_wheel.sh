#!/bin/bash

echo "Running manylinux_build_wheel for python" $1

export PATH=/opt/python/cp"$1"-cp"$1"m/bin:$PATH

cd /io
pip install --upgrade pip
pip install -r requirements_dev.txt
python setup.py bdist_wheel

for whl in /io/dist/*.whl; do
    auditwheel repair "$whl" --plat manylinux2010_x86_64 -w /io/dist/
done

rm /io/dist/*-linux_*
rm /io/dist/*-manylinux1_*

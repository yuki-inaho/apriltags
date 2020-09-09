#!/bin/bash

echo "Running manylinux_build_wheel for python" $1

export PATH=/opt/python/cp"$1"-cp"$1"m/bin:$PATH

cd /io
python -m pip install -U pip
python -m pip install build
python -m build .

for whl in /io/dist/*.whl; do
    auditwheel repair "$whl" --plat manylinux2010_x86_64 -w /io/dist/
done

rm /io/dist/*-linux_*
rm /io/dist/*-manylinux1_*

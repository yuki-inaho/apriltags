#!/bin/bash

echo "Running manylinux_build_wheel for python" $1

export PATH=/opt/python/cp"$1"-cp"$1"m/bin:$PATH

cd /io
pip install -U pip
pip install pep517
python -m pep517.build .

for whl in /io/dist/*.whl; do
    auditwheel repair "$whl" --plat manylinux2010_x86_64 -w /io/dist/
done

rm /io/dist/*-linux_*
rm /io/dist/*-manylinux1_*

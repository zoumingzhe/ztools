#!/usr/bin/bash
pushd `dirname $0`
pushd ../../

rm -rf "build"
rm -rf "dist"
rm -rf "*.egg-info"

python setup.py check
python setup.py sdist
python setup.py bdist_wheel --universal

popd
popd

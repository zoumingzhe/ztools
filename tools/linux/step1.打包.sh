rm -rf "../../build"
rm -rf "../../dist"
rm -rf "../../ztools.egg-info"


pushd `dirname $0`
pushd ../../
python setup.py check
python setup.py sdist
python setup.py bdist_wheel --universal
popd
popd

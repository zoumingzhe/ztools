rd/s/q "../../build"
rd/s/q "../../dist"
rd/s/q "../../ztools.egg-info"

pushd ../../
python setup.py check
python setup.py sdist
python setup.py bdist_wheel --universal
popd
pause

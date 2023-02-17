pushd %~dp0
pushd ..\..\

rd/s/q "build"
rd/s/q "dist"
rd/s/q "ztools.egg-info"

python setup.py check
python setup.py sdist
python setup.py bdist_wheel --universal

popd
popd

pause

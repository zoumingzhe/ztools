pushd `dirname $0`
pushd ../../

python -m twine upload dist/*

popd
popd

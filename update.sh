#!/bin/sh
rm dist/*
sudo python setup.py sdist
twine upload dist/* -r pypi
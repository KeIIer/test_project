#!/bin/bash

python setup.py sdist --formats=gztar --dist-dir  ./

virtualenv --python=python3.6 ~/test_venv
source ~/test_venv/bin/activate
pip install m3-project-1.0.0.tar.gz \
 --extra-index-url http://pypi.bars-open.ru/simple/ \
 --trusted-host pypi.bars-open.ru


python ~/test_venv/lib/python3.6/site-packages/m3_project/manage.py runserver 0.0.0.0:8000

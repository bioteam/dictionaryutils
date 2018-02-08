#!/bin/bash
set -e
pip install -r dev-requirements.txt
nosetests -v
python bin/dump_schema.py
set +e

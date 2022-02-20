#!/usr/bin/bash
THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$THISDIR"
source ./venv/Scripts/activate
python manage.py runserver

#!/bin/bash

TIME=$(date +"%Y-%m-%d")
PYTHON="python"


$PYTHON manage.py modscount 2> $TIME.dat
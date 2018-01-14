#!/usr/bin/env python
import os
import sys

import MySQLdb

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

# These environment variables are configured in app.yaml.
CLOUDSQL_CONNECTION_NAME = os.environ.get('comp3207-191316:europe-west2:travel')
CLOUDSQL_USER = os.environ.get('root')
CLOUDSQL_PASSWORD = os.environ.get('123456')

# -*- coding: utf-8 -*-
u"""Tests: context.

Bridges imports from application folder into /tests folder.

Created on Mar-2020
Author: Luís Prox
"""
# adding application path to allow importing project packages
import sys
import os.path
app_name_file = open('APP_NAME','r')
app_name = app_name_file.readline()
app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../hycontroller')
sys.path.insert(0, app_path)
print(app_path)

from apc import apc  # nopep8 pylint: disable=E0401
from api import templates  # nopep8 pylint: disable=E0401
from communication.opcda import OPCDA  # nopep8 pylint: disable=E0401
from connectors import sqlite  # nopep8 pylint: disable=E0401
from controller.task_manager import Task  # nopep8 pylint: disable=E0401
from api import rest_client  # nopep8 pylint: disable=E0401

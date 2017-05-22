#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functions import *
from guis import *

version = "1.0.7"

if check_version(version) is True:
    check_cfg()
    gui_login()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functions import *
from guis import *

version = "1.0.0"

if check_version(version) is True:
    check_cfg()
    gui_login()
else:
    showwarning('ERR0', 'LES VERSIONS DU CLIENT ET DU SERVEUR NE CONCORDENT PAS!')
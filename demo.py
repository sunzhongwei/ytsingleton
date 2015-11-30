#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from ytsingleton import SingleInstance


lockfile = "/tmp/demo_ytsingleton.lock"
instance = SingleInstance(lockfile)
time.sleep(10)

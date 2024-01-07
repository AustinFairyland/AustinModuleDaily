# coding: utf8
""" 
@File: test.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-07
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time
import random

import setuptools
from datetime import datetime

if __name__ == '__main__':
    print(setuptools.find_packages())
    major_number = 0
    subversion_number = 0
    stage_number = 5
    revise_number = 10
    if revise_number.__str__().__len__() < 5:
        nbit = 5 - revise_number.__str__().__len__()
        revise_number = "".join((("0" * nbit), revise_number.__str__()))
    else:
        revise_number = revise_number.__str__()
    date_number = datetime.now().date().__str__().replace("-", "")
    release_version = ".".join((major_number.__str__(), subversion_number.__str__(), stage_number.__str__()))
    revise_version = ".".join((revise_number.__str__(), date_number))
    test_version = ".".join((release_version, "".join(("rc", revise_version))))
    alpha_version = ".".join((release_version, "".join(("alpha", revise_version))))
    beta_version = ".".join((release_version, "".join(("beta", revise_version))))

    print(release_version)
    print(revise_version)
    print(test_version)
    print(alpha_version)
    print(beta_version)

# coding: utf8
"""
@ File: Base.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Linux Ubuntu 22.04.4 Kernel 6.2.0-36-generic 
@ CreatedTime: 2024/1/8
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import os


class Base:

    def __init__(self, project_home, *args, **kwargs):
        self.check_parameters(project_home)
        self.__project_home = project_home

    def check_parameters(self, project_home):
        if isinstance(project_home, str):
            raise TypeError("Project home path must be a str.")
        if not os.path.isdir(project_home):
            raise ValueError("Project home path does not exist.")

    @property
    def project_home(self):
        return self.__project_home

    @project_home.setter
    def project_home(self, value):
        self.check_parameters(project_home=value)
        self.__project_home = value

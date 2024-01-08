# coding: utf8
"""
@ File: DefaultData.py
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


class DefaultData:
    """Obtain Default Data"""

    @staticmethod
    def api_results() -> dict:
        """
        API results
        @author: Austin
        @return: results
        @rtype: dict
        """
        results = {"status": "failure", "code": 500, "data": None}
        return results

    @staticmethod
    def default_string() -> str:
        """
        Empty str
        @author: Austin
        @return: results -> ""
        @rtype: str
        """
        results = str()
        return results

    @staticmethod
    def default_int() -> int:
        """
        Default int
        @author: Austin
        @return: results -> 0
        @rtype: int
        """
        results = int()
        return results

    @staticmethod
    def default_float() -> float:
        """
        Default float
        @author: Austin
        @return: results -> 0.0
        @rtype: float
        """
        results = float()
        return results

    @staticmethod
    def default_bool() -> bool:
        """
        Default bool
        @author: Austin
        @return: results -> False
        @rtype: bool
        """
        results = bool()
        return results

    @staticmethod
    def default_list() -> list:
        """
        Empty list
        @author: Austin
        @return: results -> []
        @rtype: list
        """
        results = list()
        return results

    @staticmethod
    def default_tuple() -> tuple:
        """
        Empty tuple
        @author: Austin
        @return: results -> ()
        @rtype: tuple
        """
        results = tuple()
        return results

    @staticmethod
    def default_set() -> set:
        """
        Empty set
        @author: Austin
        @return: results -> set()
        @rtype: set
        """
        results = set()
        return results

    @staticmethod
    def default_dict() -> dict:
        """
        Empty dict
        @author: Austin
        @return: results -> {}
        @rtype: dict
        """
        results = dict()
        return results

    @staticmethod
    def default_none() -> None:
        """
        Default None
        @author: Austin
        @return: results -> None
        @rtype: NoneType
        """
        return None

    @staticmethod
    def default_bytes() -> bytes:
        """
        Empty bytes
        @author: Austin
        @return: results -> b''
        @rtype: bytes
        """
        results = bytes()
        return results

    @staticmethod
    def default_bytearray() -> bytearray:
        """
        Empty bytearray
        @author: Austin
        @return: results -> bytearray(b'')
        @rtype: bytearray
        """
        results = bytearray()
        return results

    @staticmethod
    def default_complex() -> complex:
        """
        Empty complex
        @author: Austin
        @return: results -> 0j
        @rtype: complex
        """
        results = complex()
        return results

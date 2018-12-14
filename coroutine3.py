#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@file: coroutine3.py
@time: 14/12/2018
@desc:  python3 协程
"""

import asyncio


@asyncio.coroutine
def test(i):
    print("test_1", i)
    r = yield from asyncio.sleep(1)
    print("test_2", i)


loop = asyncio.get_event_loop()
tasks = [test(i) for i in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

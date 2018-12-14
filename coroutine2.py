#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-14 18:43:27
# @Author  : yhk
"""
==============================================
   coroutine             
==============================================
"""
import gevent
from gevent import monkey;

monkey.patch_all()
import urllib2


def get_body(i):
    print("start {}".format(i))
    urllib2.urlopen("http://cn.bing.com")
    print("end {}".format(i))


tasks = [gevent.spawn(get_body, i) for i in range(3)]
gevent.joinall(tasks)

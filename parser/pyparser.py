#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     pyparser.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2021.02.04   23:03
-------------------------------------------------------------------------------
   @Change:   2021.02.04
-------------------------------------------------------------------------------
"""

import inspect
import timeit
import re
import pydoc

result = {
    'Function': [],
    'Data': [],
    'Class': {}
}

a = inspect.getmembers(timeit)
b = inspect.getmodule(timeit)

all = [i[0] for i in a]
print(all)

for i in a:
    current_obj = getattr(timeit, i[0])
    if inspect.isclass(current_obj):
        class_func = []
        c = inspect.getmembers(getattr(timeit, i[0]))
        for j in c:
            obj = getattr(getattr(timeit, i[0]), j[0])
            if inspect.isfunction(obj):
                class_func.append(j[0])
        result['Class'][i[0]] = class_func
    if inspect.isfunction(current_obj):
        result['Function'].append(i[0])
    if not re.match('^<.*$>?', str(i[1])) or isinstance(i[1], (str, int, list, dict)):
        # 是 str 或 int 或 list 或 dict 实例就是 Data
        if pydoc.visiblename(i[0], all, object):
            result['Data'].append(i[0])

print(len(a))
print(result)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数据访问测试代码"""

import www.orm
from www.models import User,Blog,Comment
import asyncio

async def test():
    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await www.orm.create_pool(loop=loop,host='127.0.0.1', port=3306,user='www-data', password='www-data',db='awesome')
    #没有设置默认值的一个都不能少
    u = User(name='Test', email='liadddndai9d1@126.com', passwd='1234567890', image='about:blank',id="12dd3d4dddfddads")
    await u.save()

# 把协程丢到事件循环中执行
loop = asyncio.get_event_loop()
loop.run_until_complete(test())

if loop.is_closed():
    sys.exit(0)
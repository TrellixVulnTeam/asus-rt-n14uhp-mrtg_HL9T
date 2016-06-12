#!/usr/bin/env python


__version__ = '0.1'
__author__ = 'Jason Wee'

import yaml

from router_statistics.routerStats import get_cpu_stat_from_router
stream = open("/etc/router_statistics/config.yaml", "r")
config = yaml.load(stream)
print get_cpu_stat_from_router(config)

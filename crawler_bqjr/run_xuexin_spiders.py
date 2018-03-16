# -*- coding: utf-8 -*-

from os import path as os_path
from sys import path as sys_path

sys_path.append(os_path.dirname(os_path.abspath(__file__)))

from crawler_bqjr.spiders.userinfo_spiders.xuexin2 import XuexinSpider
from run import run_multiple_spider_with_process


def crawl_xuexin_info(process_count=1):
    spider_dict = {"学信": XuexinSpider,
                   }

    run_multiple_spider_with_process(spider_dict, process_count)


if __name__ == '__main__':
    crawl_xuexin_info(process_count=1)

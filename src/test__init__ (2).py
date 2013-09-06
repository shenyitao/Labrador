# encoding: utf-8


from sina_weibo.fetcher import ComWeiboFetcher
import sina_weibo
import sys
import time
import memstorage

user = '397901611@qq.com'
pwd = 'ecnupass'

fetcher = ComWeiboFetcher(username=user, password=pwd)

login_ok = fetcher.check_cookie()

if not login_ok:
    print 'login failed.'
    sys.exit()

sina_weibo.main(fetcher,fetch_data='weibos',store_path='./file/',uids=memstorage.users_id_moniterd)


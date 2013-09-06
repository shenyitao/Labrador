# encoding: utf-8


from sina_weibo.fetcher import ComWeiboFetcher
import sina_weibo
import sys
import time
import memstorage


fetcher = ComWeiboFetcher(username=memstorage.user, password=memstorage.pwd)

login_ok = fetcher.check_cookie()

if not login_ok:
    print 'login failed.'
    sys.exit()

start = time.time()

sina_weibo.main(fetcher, fetch_data='follows', store_path='./file/', uids=memstorage.users_id_moniterd, uids_storage=memstorage.uids_url_moniterd)

#sina_weibo.main(fetcher, fetch_data='fans', store_path='./file/', uids=memstorage.users_id_moniterd, uids_storage=memstorage.uids_url2_moniterd)

#a = set(memstorage.uids_url_moniterd)
#b = set(memstorage.uids_url2_moniterd)

#print a & b

#c = list(a&b)
sina_weibo.main(fetcher, fetch_data='weibos', store_path='./file/', uids=memstorage.uids_url_moniterd, weibos_storage=memstorage.weibos_url_moniterd)

print 'crawl reposts and comments'
 
sina_weibo.main(fetcher, store_path='./file/', msg_urls=memstorage.weibos_url_moniterd)

cost_time = int(time.time() - start)
print 'finished: # connections: %s, cost time: %s' %(fetcher.n_connections, cost_time)
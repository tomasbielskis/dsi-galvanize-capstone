import pandas as pd
import numpy as np
import os
import requests
from timeit import Timer
import multiprocessing
import threading

def getmfpage(postid):
    """passed a post_id saves the page content for the post as a json file in data/posts"""
    url = 'https://www.metafilter.com/'
    page = requests.get(url+str(postid)).content
    d = pd.DataFrame(data={postid: [page]})
    path = 'data/posts/'
    d.to_json(path+str.(d.columns[0]))

def scrape_sequential(n):
    for p in dfposts.index[0:n]:
        if p not in os.listdir('data/posts'):
            getmfpage(p)

def scrape_parallel_concurrent(pool_size, post_list):
    pool = multiprocessing.Pool(pool_size)
    pool.map(getmfpage, post_list)
    pool.close()
    pool.join()

if __name__ == '__main__':
    dfposts = pd.read_csv('data/postdata_mefi.txt',sep='\t', header=1,
                        parse_dates=['datestamp'], skiprows=0, index_col='postid')
    n = 10
    pool_size = 4
    post_list = dfposts.index[0:n]
    # t = Timer(lambda: scrape_sequential(n))
    # print("Completed sequential in %s seconds." % t.timeit(1))

    t = Timer(lambda: scrape_parallel_concurrent(pool_size,post_list))
    print("Completed using threads in %s seconds." % t.timeit(1))

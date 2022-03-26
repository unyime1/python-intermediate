import threading
import os
import time
from urllib.request import urlretrieve
from typing import List
from numpy import round

IMGS_URL_LIST = \
    ['https://dl.dropboxusercontent.com/s/2fu69d8lfesbhru/pexels-photo-48603.jpeg',
     'https://dl.dropboxusercontent.com/s/zch88m6sb8a7bm1/pexels-photo-134392.jpeg',
     'https://dl.dropboxusercontent.com/s/lsr6dxw5m2ep5qt/pexels-photo-135130.jpeg',
     'https://dl.dropboxusercontent.com/s/6xinfm0lcnbirb9/pexels-photo-167300.jpeg',
     'https://dl.dropboxusercontent.com/s/2dp2hli32h9p0y6/pexels-photo-167921.jpeg',
     'https://dl.dropboxusercontent.com/s/fjb1m3grcrceqo2/pexels-photo-173125.jpeg',
     'https://dl.dropboxusercontent.com/s/56u8p4oplagc4bp/pexels-photo-185934.jpeg',
     'https://dl.dropboxusercontent.com/s/2s1x7wz4sdvxssr/pexels-photo-192454.jpeg',
     'https://dl.dropboxusercontent.com/s/1gjphqnllzm10hh/pexels-photo-193038.jpeg',
     'https://dl.dropboxusercontent.com/s/pcjz40c8pxpy057/pexels-photo-193043.jpeg',
     'https://dl.dropboxusercontent.com/s/hokdfk7y8zmwe96/pexels-photo-207962.jpeg',
     'https://dl.dropboxusercontent.com/s/k2tk2co7r18juy7/pexels-photo-247917.jpeg',
     'https://dl.dropboxusercontent.com/s/m4xjekvqk4rksbx/pexels-photo-247932.jpeg',
     'https://dl.dropboxusercontent.com/s/znmswtwhcdbpc10/pexels-photo-265186.jpeg',
     'https://dl.dropboxusercontent.com/s/jgb6n4esquhh4gu/pexels-photo-302899.jpeg',
     'https://dl.dropboxusercontent.com/s/rjuggi2ubc1b3bk/pexels-photo-317156.jpeg',
     'https://dl.dropboxusercontent.com/s/cpaog2nwplilrz9/pexels-photo-317383.jpeg',
     'https://dl.dropboxusercontent.com/s/16x2b6ruk18gji5/pexels-photo-320007.jpeg',
     'https://dl.dropboxusercontent.com/s/xqzqzjkcwl52en0/pexels-photo-322207.jpeg',
     'https://dl.dropboxusercontent.com/s/frclthpd7t8exma/pexels-photo-323503.jpeg',
     'https://dl.dropboxusercontent.com/s/7ixez07vnc3jeyg/pexels-photo-324030.jpeg',
     'https://dl.dropboxusercontent.com/s/1xlgrfy861nyhox/pexels-photo-324655.jpeg',
     'https://dl.dropboxusercontent.com/s/v1b03d940lop05d/pexels-photo-324658.jpeg',
     'https://dl.dropboxusercontent.com/s/ehrm5clkucbhvi4/pexels-photo-325520.jpeg',
     'https://dl.dropboxusercontent.com/s/l7ga4ea98hfl49b/pexels-photo-333529.jpeg',
     'https://dl.dropboxusercontent.com/s/rleff9tx000k19j/pexels-photo-341520.jpeg'
    ]


# this is our target function
def download_image(url: str, img_num: int) -> None:
    urlretrieve(url, f'images2/{img_num+1}.jpeg')


def download_images(img_url_list: List[str]) -> None:
    # validate inputs
    if not img_url_list:
        return
    os.makedirs('images2', exist_ok=True)

    # get time in seconds
    start = time.perf_counter()
    
    # create a list to store all of our threads
    threads = []
    
    # for every url in our list, parse the url and download its contents
    for img_num, url in enumerate(img_url_list):
        # create a new thread
        t = threading.Thread(target=download_image, args=(url, img_num))
        
        # start the new thread
        t.start()
        
        # add the new thread to our list of threads
        threads.append(t)
    
    # Instruct the main thread to wait for all child threads to complete before proceeding
    for thread in threads:
        thread.join()
            
    print(f"Retrieved {len(IMGS_URL_LIST)} images took {round(time.perf_counter() - start, 2)} seconds")


download_images(IMGS_URL_LIST)

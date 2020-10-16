#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# IDE: PyCharm 2019.1.2
# Author: Dajiang Ren<rendajiang@gagogroup.com>
# Created on 2019-06-01


import os

if __name__ == '__main__':

    bucket = "gago-data-test"
    prefix = "data-service/crop-growth/10m-real-growth/tiles/sss123456"
    access = "public-read"
    config = "/Users/gago/workspace/ndvi_product_line/gago-raster-tiler" \
             "-server/src/storage_config.json"
    cmd = "python raster2tiles.py -p mercator -s EPSG:4490 --zoom=0-13 -f " \
          "Lerc " \
          "-l -c %s -b %s " \
          "-x %s -t %s /Users/gago/temp/test/lerc_test/Result_v8.tif " \
          "/Users/gago/temp/test/lerc_test/temp"%(config, bucket,prefix,access)
    os.system(cmd)

    # cmd = "python raster2tiles.py -p mercator -s EPSG:4490 --zoom=0-13 -f " \
    #       "Lerc " \
    #       "-l /Users/gago/temp/test/lerc_test/Result_v8.tif " \
    #       "/Users/gago/temp/test/lerc_test/temp"
    # os.system(cmd)









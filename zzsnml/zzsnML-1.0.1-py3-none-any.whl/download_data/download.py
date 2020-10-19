from urllib import request, error
import sys
import zipfile
import tarfile
import socket

socket.setdefaulttimeout(15)
def progressbar(cur):
    percent = '{:.2%}'.format(cur)
    sys.stdout.write('\r')
    sys.stdout.write('[%-100s] %s' % ('=' * int(cur*100), percent))
    sys.stdout.flush()
    print(cur)

def schedule(blocknum,blocksize,totalsize):
    '''
    blocknum:当前已经下载的块
    blocksize:每次传输的块大小
    totalsize:网页文件总大小
    '''
    percent = 0
    if totalsize == 0:
        percent = 0
    elif totalsize == -1 and blocknum==0:
        print('响应失败，正在重新连接……')
        download()
    elif totalsize == -1 and blocknum != 0:
        pass
    else:
        percent = blocknum * blocksize / totalsize
        progressbar(percent)
    if percent > 1.0:
        percent = 1.0
        progressbar(percent)
    # print('\n'+'download : %.2f%%' %(percent))


def download(url = 'https://codeload.github.com/chengtingting980903/zzsnML/tar.gz/1.0.0', path = '1.0.0.tar.gz'):
    try:
        filename,headers = request.urlretrieve(url, path, schedule)
        print(headers)
    except error.HTTPError as e:
        print(e)
        print(url + ' download failed!' + '\r\n')
        print('请手动下载：%s' %url)
    except error.URLError as e:
        print(url + ' download failed!' + '\r\n')
        print('请手动下载：%s' %url)
        print(e)
    except Exception as e:
        print(e)
        print('请手动下载：%s' %url)
    else:
        print('\r\n' + url + ' download successfully!')
        return filename

def unzip(path = '1.0.0.zip'):
    zip_file = zipfile.ZipFile(path)
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件
    for f in zip_list:
        zip_file.extract(f)  # 循环解压文件到指定目录
    zip_file.close()  # 关闭文件，必须有，释放内存

def untar(path = '1.0.0.tar.gz'):
    tar = tarfile.open(path)
    tar.extractall()
    tar.close()

def download_decompress(url = 'https://codeload.github.com/chengtingting980903/zzsnML/tar.gz/1.0.0', path = '1.0.0.tar.gz'):
    filename = download(url, path)
    try:
        if str(filename).split('.')[-1] == 'zip':
            print('开始解压zip文件，请等待……')
            unzip()
            print('解压完成，可以使用')
    except Exception as e:
        print(e)
        print('解压失败，请手动解压')
    try:
        if str(filename).split('.')[-1] == 'gz':
            print('开始解压tar.gz文件，请等待……')
            untar()
            print('解压完成，可以使用')
    except Exception as e:
        print(e)
        print('解压失败，请手动解压')

# if __name__ == '__main__':
print('开始下载：https://codeload.github.com/chengtingting980903/zzsnML/tar.gz/1.0.0')
download_decompress()
print('开始下载：https://github.com/chengtingting980903/zzsnML/releases/download/1.0.0/data.zip')
download_decompress(url='https://github.com/chengtingting980903/zzsnML/releases/download/1.0.0/data.zip', path='data.zip')


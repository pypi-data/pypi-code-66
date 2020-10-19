import os
import ftplib
from ftplib import FTP
from flask import Flask, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from julei.kmeans import Kmeans
HOST = '127.0.0.1'
DEBUG = False
PORT = 8010
ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])

app = Flask(__name__)



# 限定上传文件最大不超过50M
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

html = '''

    <!DOCTYPE html>

    <title>文件传输</title>

    <h2>文件传输</h2>

    <form method='post' enctype='multipart/form-data'>
         <input type='file' name='file' multiple="multiple">
         <input type='submit' value='传输该文件'>
    </form>

    '''
htmls = '''

    <!DOCTYPE html>

    <title>文件传输</title>

    <h2>文件传输</h2>

    <form method='post' enctype='multipart/form-data'>
         <input type='submit' value='开始传输'>
    </form>

    '''
    
#连接并登陆FTP
def loginFTP():
    ftp = FTP()
    ftp.connect('192.168.1.196', 21)  # 连接的ftp sever IP和端口
    ftp.login('', '')  # 连接的用户名，密码如果匿名登录则用空串代替即可
    return ftp,True
# 判断文件类型是否符合要求
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[-1] in ALLOWED_EXTENSIONS
@app.route('/', methods=('GET', 'POST'))
def index():
    return ''

@app.route('/download', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        ftp, status = loginFTP()
        if status == True:
            ftp.cwd('./beida')
            files = request.files.getlist('file')
            # files = request.files['file']
            print(files)
            for file in files:
                if  allowed_file(file.filename):
                    print(file)
                    filename = secure_filename(file.filename)
                    ftp.storbinary('STOR ' + filename, file, blocksize=1024)
                else:
                    return html + '文件类型不匹配'
            return html + str(len(files)) + '个文件已经传输成功！'
        else:
            return html + '连接失败'
    return html

@app.route('/upload', methods=['GET', 'POST'])
# 上传整个目录下的文件
def ftpDownload():
    if request.method == 'POST':
        ftp, status = loginFTP()
        remote_path = './'
        local_path = './data'
        if not os.path.exists(local_path):
            os.makedirs(local_path)
        ftp.cwd(remote_path)
        # print(ftp.dir())
        for file in ftp.nlst():
            print(file)
            if  allowed_file(file):
                local_file = os.path.join(local_path, file)
                # print(file.rsplit('.', 1)[-1])
                # print(allowed_file(file))
                download_file(ftp=ftp, remote_file=file, local_file=local_file)
            else:
                print('文件类型有误')
        ftp.quit()
        return htmls +'传输成功'
    return htmls
def download_file(ftp, remote_file, local_file):
    try:
        buf_size = 1024
        file_handler = open(local_file, 'wb')
        ftp.retrbinary('RETR ' + remote_file, file_handler.write, buf_size)
        file_handler.close()
    except Exception as err:
        print('传输文件出错，出现异常：%s ' % err)
        

@app.route('/write/', methods=('GET', 'POST'))
def get_train():
    try:
        km = Kmeans()
        km.write()
    except Exception as err:
        print('出现异常：' + err)
        return 'lose'
    return '<h2>模型训练成功，相关文件已保存<h2>'

@app.route('/delete/', methods=('GET', 'POST'))
def delete_dir():
    print('当前工作目录为' + os.getcwd())
    for root,dir,files in os.walk('./data'):
        print('data文件夹中包含' + str(files))
        for file in files:
            if file.rsplit('.')[-1] == 'xlsx':
                os.remove('./data/' + file)
    if os.path.exists('./result'):
        shutil.rmtree('./result/')
    return '<h2>删除文件成功</h2>'

app.run(host=HOST, port=PORT, debug=DEBUG)

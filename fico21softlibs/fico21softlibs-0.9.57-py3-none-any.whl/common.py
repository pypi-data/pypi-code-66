################ import ################
import os
from os import system
import sys
import webbrowser
import logging
import pickle

import pyautogui
import pyodbc
import smtplib
import string
import time
import tempfile

if sys.platform != "win32":
    import fcntl

from urllib.request import urlopen
from logging.handlers import RotatingFileHandler
from string import Template

# ========================================================================================================#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# ========================================================================================================#
from sys import platform as _platform
from pandas.io.clipboard import clipboard_get, clipboard_set
from pynput.keyboard import Key, Controller
import pynput

# from settings import *
from fico21softlibs.settings import *

if _platform == 'win32' or _platform == 'win64':
    import win32api
    import win32con
################ import ################

class SingleInstanceException(BaseException):
    pass

class SingleInstance(object):

    """Class that can be instantiated only once per machine.

    If you want to prevent your script from running in parallel just instantiate SingleInstance() class. If is there another instance already running it will throw a `SingleInstanceException`.

    This option is very useful if you have scripts executed by crontab at small amounts of time.

    Remember that this works by creating a lock file with a filename based on the full path to the script file.

    Providing a flavor_id will augment the filename with the provided flavor_id, allowing you to create multiple singleton instances from the same file. This is particularly useful if you want specific functions to have their own singleton instances.
    """

    def __init__(self, flavor_id="", lockfile=""):
        self.initialized = False
        # ========================================================================================================#
        self.logger = CommonLib.create_logger('common')
        # ========================================================================================================#

        if lockfile:
            self.lockfile = lockfile
        else:
            basename = os.path.splitext(os.path.abspath(sys.argv[0]))[0].replace(
                "/", "-").replace(":", "").replace("\\", "-") + '-%s' % flavor_id + '.lock'
            self.lockfile = os.path.normpath(
                tempfile.gettempdir() + '/' + basename)

        #self.logger.debug("SingleInstance lockfile: " + self.lockfile)
        if sys.platform == 'win32':
            try:
                # file already exists, we try to remove (in case previous
                # execution was interrupted)
                if os.path.exists(self.lockfile):
                    os.unlink(self.lockfile)
                self.fd = os.open(
                    self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            except OSError:
                type, e, tb = sys.exc_info()
                if e.errno == 13:
                    self.logger.error("Another instance is already running, quitting.")
                    raise SingleInstanceException()
                print(e.errno)
                raise
        else:  # non Windows
            self.fp = open(self.lockfile, 'w')
            self.fp.flush()
            try:
                fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError:
                self.logger.warning("Another instance is already running, quitting.")
                raise SingleInstanceException()
        self.initialized = True

    def __del__(self):
        if not self.initialized:
            return
        try:
            if sys.platform == 'win32':
                if hasattr(self, 'fd'):
                    os.close(self.fd)
                    os.unlink(self.lockfile)
            else:
                fcntl.lockf(self.fp, fcntl.LOCK_UN)
                # os.close(self.fp)
                if os.path.isfile(self.lockfile):
                    os.unlink(self.lockfile)
        except Exception as e:
            if self.logger:
                self.logger.warning(e)
            else:
                print("Unloggable error: %s" % e)
            sys.exit(-1)

class CommonLib:
    def __init__(self):
        pass

    @staticmethod
    def restart():
        # Exception 발생하면 종료되도 상관은 없지만 종료가 안되면 더욱 큰문제가 될 수 있으므로 try, except 사용 안 함!!
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) # 배포판에서는 제대로 동작 함!!

    @staticmethod
    def insert_message_to_log(filename, message):
        try:
            l = []
            if os.path.isfile(filename):
                f = open(filename, 'rb')
                l = pickle.load(f)
                f.close()

            f = open(filename, 'wb')
            #l.append(message)
            l.insert(0, message)
            pickle.dump(l, f)
            f.close()
        except Exception as ex:  # 에러 종류
            print('ERROR(insert_message_to_log()) : ', ex)  # ex는 발생한 에러의 이름을 받아오는 변수

    @staticmethod
    def is_internet_connected():
        try:
            urlopen("https://www.google.com", timeout = 2)
            return True
        except Exception as ex:  # 에러 종류
            #print('ERROR(is_internet_connected()) : ', ex)  # ex는 발생한 에러의 이름을 받아오는 변수
            return False

    @staticmethod
    def create_logger(logger_name, logger_level=logging.ERROR, filename="log"):
        try:
            mylogger = logging.getLogger(logger_name)
            mylogger.setLevel(logger_level)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            stream_hander = logging.StreamHandler()
            stream_hander.setFormatter(formatter)
            mylogger.addHandler(stream_hander)

            # 최대 50MB짜리 로그 파일 2개 까지 생성!!
            file_handler = RotatingFileHandler(filename, maxBytes=50*1024*1024, backupCount=2)

            file_handler.setFormatter(formatter)
            mylogger.addHandler(file_handler)

            #mylogger.info(logger_name)
            return mylogger
        except Exception as ex:  # 에러 종류
            print('ERROR(create_logger()) : ', ex)  # ex는 발생한 에러의 이름을 받아오는 변수
            return None

    @staticmethod
    def open_url(url):
        try:
            webbrowser.open(url)
            if os.name == 'nt':
                os.system("echo %s | clip" % url)
            elif 'darwin' in sys.platform:
                os.system("echo '%s' | pbcopy" % url)
            else:
                pass
        except Exception as ex:  # 에러 종류
            print('ERROR(open_url()) : ', ex)  # ex는 발생한 에러의 이름을 받아오는 변수

    # ========================================================================================================#
    # pyqt5 에서 exception 발생시 종료 방지 방법
    # pyqt5 앱을 실행 시키기 전에, exception hook를 새로 define에서 바꿔주시면 됩니다.
    # 그러면 pyqt5 동작 중에도 강제로 프로그램이 종료되지 않을 거에요. 특히 .pyw 로 콘솔창 없이 하시는 분들은 위에기능은 필수적으로
    # 필요하실 듯 합니다.
    # 검증이 필요한 코드 임!! test!!
    # ========================================================================================================#
    @staticmethod
    def customized_exception_hook(exctype, value, traceback):
        logger = CommonLib.create_logger('customized_exception_hook')
        logger.error(f'customized_exception_hook(exctype, value, traceback) : exctype : {exctype}, value : {value}, traceback : {traceback}')
        logging.shutdown()

        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        # sys.exit(1)
    # ========================================================================================================#

    ##################################################################################
    '''
    두개 또는 세개의 리스트를 인자로 받아서 각각의 리스트에 순서대로 값을 추출해서 
    tuple로 조합해서 merge된 리스트를 리턴~~
    '''
    @staticmethod
    def merge_list(list1, list2):
        merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
        return merged_list

    @staticmethod
    def merge_list3(list1, list2, list3):
        merged_list = [(list1[i], list2[i], list3[i]) for i in range(0, len(list1))]
        return merged_list
    ##################################################################################

    @staticmethod
    def os():
        if _platform == "linux":
            return LINUX
        elif _platform == "linux2":
            return LINUX2
        elif _platform == "darwin":
            return MACOS
        elif _platform == "win32":
            return WINDOWS32
        elif _platform == "win64":
            return WINDOWS64
        return ''

    @staticmethod
    def db_connect(server, database, username, password):
        #server = 'DESKTOP-4MOPDCN\SQLEXPRESS'
        # server = '192.168.0.65'
        # database = 'DemoAppDB'
        # username = 'app'
        # password = 'senna.kang'
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        #cursor = cnxn.cursor()
        return cnxn #, cursor

    @staticmethod
    def get_contacts(filename):
        """
        Return two lists names, emails containing names and email addresses
        read from a file specified by filename.
        """
        names = []
        emails = []
        with open(filename, mode='r', encoding='utf-8') as contacts_file:
            for a_contact in contacts_file:
                fields = a_contact.split(":")
                names.append(fields[0].strip())
                emails.append(fields[1].strip())
        return names, emails

    @staticmethod
    def read_template(filename):
        """
        Returns a Template object comprising the contents of the
        file specified by filename.
        """
        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    @staticmethod
    def smtp_login(host, port, user_name, pwd):
        # set up the SMTP server
        smtp = smtplib.SMTP(host=host, port=port)
        smtp.starttls()
        smtp.login(user_name, pwd)

        return smtp

    '''
    str에 string.punctuation  = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'이 
    있다면 
            return True
    없다면 
            return False    
    '''
    @staticmethod
    def have_punctuation(str):
        invalidcharacters = set(string.punctuation)
        if any(char in invalidcharacters for char in str):
            return True
        else:
            return False

    '''
    모든 string.punctuation  = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 위치를 배열로 리턴!!
    '''
    @staticmethod
    def punctuation_pos(str):
        idx = 0
        result_list = []

        punctuations = string.punctuation
        for s in str:
            if punctuations.find(s) != NOT_FOUND:
                result_list.append(idx)
            idx += 1
        return result_list

    '''
    모든 string.punctuation  = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'을 제거
    '''
    @staticmethod
    def remove_punctuation(src_str):
        return src_str.translate(str.maketrans('', '', string.punctuation))

    # ========================================================================================================#
    '''
    related selenium
    '''
    # ========================================================================================================#
    @staticmethod
    def get_webdriver():
        if os.name == 'nt':
            # 윈도우즈에서는 테스트 진행 하지 않음!!
            # 나중에 프로젝트화 되면 솔루션 찾아서 처리 해야 함!!
            # chromedriver = r'C:\chromedriver.exe'
            chromedriver = r'.\chromedriver.exe'
        elif 'darwin' in sys.platform:
            chromedriver = "./chromedriver"

        os.environ["webdriver.chrome.driver"] = chromedriver
        chrome_options = Options()

        prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
        chrome_options.add_experimental_option("prefs", prefs)
        wd = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)

        wd.maximize_window()
        return wd

    @staticmethod
    def wd_wait(wd, timeout=10, presence_id=''):
        if presence_id == '':
            return 'presence_id is necessary'

        try:
            pg_loaded = WebDriverWait(wd, timeout).until(EC.presence_of_element_located((By.ID, presence_id)))
        except TimeoutError as ex:
            # print(ex)
            return "time out exception!! increase timeout more.."

        return pg_loaded

    @staticmethod
    def wd_send_keys(wd, keys):
        ActionChains(wd).send_keys(keys).perform()
    # ========================================================================================================#
    '''
    It's needed test 
    '''
    @staticmethod
    def wd_send_key_ctrl(wd, key):
        ActionChains(wd).key_down(Keys.COMMAND).send_keys(key).perform()
        # ActionChains(wd) \
        #     .key_down(Keys.COMMAND) \
        #     .key_down(key) \
        #     .key_up(key) \
        #     .key_up(Keys.COMMAND) \
        #     .perform()

    # @staticmethod
    # def send_keys(keys):
    #     keyboard = Controller()
    #     keyboard.type(keys)
    # ========================================================================================================#
    @staticmethod
    def get_clipboard_data():
        # if CommonLib.os() == WINDOWS32 or CommonLib.os() == WINDOWS64:
        #     win32clipboard.OpenClipboard()
        #     data = win32clipboard.GetClipboardData()
        #     win32clipboard.CloseClipboard()
        #     return data
        # else:
        return clipboard_get()

    @staticmethod
    def set_clipboard_data(data):
        # if CommonLib.os() == WINDOWS32 or CommonLib.os() == WINDOWS64:
        #     win32clipboard.OpenClipboard()
        #     win32clipboard.EmptyClipboard()
        #     win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, data)
        #     win32clipboard.CloseClipboard()
        #     return 'OK'
        # else:
        return clipboard_set(data)
    # ========================================================================================================#
    # Windows only
    # ========================================================================================================#
    # @staticmethod
    # def input_keys(data):
    #     if CommonLib.os() == WINDOWS32 or CommonLib.os() == WINDOWS64:
    #         send_keys("{VK_LCONTROL down}"
    #                   "a"
    #                   "{VK_LCONTROL up}")
    #         set_clipboard_data(data)
    #         send_keys("{VK_LCONTROL down}"
    #                   "v"
    #                   "{VK_LCONTROL up}")
    # @staticmethod
    # def paste_data(data): # function name wrapping only for easy remember
    #     CommonLib.input_keys(data)
    # ========================================================================================================#
    '''
    It's needed test 
    '''
    # @staticmethod
    # def send_key_ctrl(key):
    #     if CommonLib.os() == WINDOWS32 or CommonLib.os() == WINDOWS64:
    #         send_keys("{VK_LCONTROL down}"
    #                   "a"
    #                   "{VK_LCONTROL up}")
    #         set_clipboard_data(key)
    #         send_keys("{VK_LCONTROL down}"
    #                   "v"
    #                   "{VK_LCONTROL up}")
    #     else:
    #         pass
    # ========================================================================================================#
    # @staticmethod
    # def scroll(clicks=0, delta_x=0, delta_y=0, delay_between_ticks=0):
    #     """
    #     Source: https://docs.microsoft.com/en-gb/windows/win32/api/winuser/nf-winuser-mouse_event?redirectedfrom=MSDN
    #
    #     void mouse_event(
    #       DWORD     dwFlags,
    #       DWORD     dx,
    #       DWORD     dy,
    #       DWORD     dwData,
    #       ULONG_PTR dwExtraInfo
    #     );
    #
    #     If dwFlags contains MOUSEEVENTF_WHEEL,
    #     then dwData specifies the amount of wheel movement.
    #     A positive value indicates that the wheel was rotated forward, away from the user;
    #     A negative value indicates that the wheel was rotated backward, toward the user.
    #     One wheel click is defined as WHEEL_DELTA, which is 120.
    #
    #     :param delay_between_ticks:
    #     :param delta_y:
    #     :param delta_x:
    #     :param clicks:
    #     :return:
    #     """
    #
    #     if clicks > 0:
    #         increment = win32con.WHEEL_DELTA
    #     else:
    #         increment = win32con.WHEEL_DELTA * -1
    #
    #     for _ in range(abs(clicks)):
    #         win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, delta_x, delta_y, increment, 0)
    #         time.sleep(delay_between_ticks)
    # ========================================================================================================#

# test only
if __name__ == '__main__':
    # wd = CommonLib.get_webdriver()
    # wd.get('http:\\www.naver.com')
    # CommonLib.wd_send_keys(wd, 'dsdfsgshgjchkjhvk')
    #
    # CommonLib.send_keys(' send_keys')
    # time.sleep(2)
    # CommonLib.set_clipboard_data('paste by python')
    # CommonLib.wd_send_key_ctrl(wd,'a')
    # CommonLib.wd_send_key_ctrl(wd,'v')

    pass
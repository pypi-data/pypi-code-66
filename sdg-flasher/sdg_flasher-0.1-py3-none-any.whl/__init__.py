"""
Универсальный загрузчик ПО в микроконтроллеры:
avr8, 1887ve4u, avr16, 1986ve1t, 1986ve91t, stm32f4

Можно использовать из командной строки:
python -m sdg_flasher -p COM1 -c 500000_O_2 -d ve1t -a 85 -o w -f "ololo.hex"

Пример использования:
-------------
```python
from sdg_io import SdgIO
from sdg_flasher import Flasher

io = SdgIO('COM1', '115200_O_2')
Flasher(io, file='ololo.hex', device='ve1t, opt='wv', addr=b'\x01', rebootcmd='b'\x03').do()
```
"""

__version__ = '0.1'

import time
import sys
from struct import pack
from pathlib import Path
from intelhex import IntelHex
from sdg_dev import DevMaster, DevException
from sdg_utils import align


stm32f4 = {
    'packlen': 1024,
    'clear': True,
    'sectors': (  # Номер сектора начиная | Адрес | Размер в байтах
               # (0, 0x08000000, 16*1024), нулевой сектор занят бутлоадером
               (1, 0x08004000, 16 * 1024),
               (2, 0x08008000, 16 * 1024),
               (3, 0x0800C000, 16 * 1024),
               (4, 0x08010000, 64 * 1024),
               (5, 0x08020000, 128 * 1024),
               (6, 0x08040000, 128 * 1024),
               (7, 0x08060000, 128 * 1024),
               (8, 0x08080000, 128 * 1024),
               (9, 0x080A0000, 128 * 1024),
               (10, 0x080C0000, 128 * 1024),
               (11, 0x080E0000, 128 * 1024))
}

ve91t = {  # 0 сектор занят бутлоадером
    'packlen': 1024,
    'sectors': [(i, 0x08000000 + i * 0x1000, 0x1000) for i in range(1, 32, 1)]
}

ve1t = {  # ve1t - бутлоадер является частью программы
    'packlen': 1024,
    'sectors': [(i, i * 0x1000, 0x1000) for i in range(32)]
}

AVR8PAGESIZE = 64
AVR8BOOTPAGES = 1024 // AVR8PAGESIZE  # бутлоадер занимает 1кб в конце флешки
avr8 = {
    'packlen': AVR8PAGESIZE,  # Для AVR писать можно только целиком страницу!
    'sectors': [(i, i * AVR8PAGESIZE, AVR8PAGESIZE) for i in range(8192 // AVR8PAGESIZE - AVR8BOOTPAGES)],
    'eeprom': (0, 0, 512)
}

ve4u = {
    'packlen': AVR8PAGESIZE,  # Для AVR писать можно только целиком страницу!
    'noclear': True,  # стирать НЕ НАДО
    'sectors': [(i, i * AVR8PAGESIZE, AVR8PAGESIZE) for i in range(8192 // AVR8PAGESIZE - AVR8BOOTPAGES)],
    'eeprom': (0, 0, 512)
}

AVR16PAGESIZE = 128
AVR16BOOTPAGES = 2048 // AVR16PAGESIZE  # бутлоадер занимает 2кб в конце флешки
avr16 = {
    'packlen': AVR16PAGESIZE,  # Для AVR писать можно только целиком страницу mtu = pagesize!
    'sectors': [(i, i * AVR16PAGESIZE, AVR16PAGESIZE) for i in range(16384 // AVR16PAGESIZE - AVR16BOOTPAGES)],
    'eeprom': (0, 0, 512)
}


class Flasher(DevMaster):
    """ Универсальный загрузчик ПО в микроконтроллеры:
    avr8, 1887ve4u, avr16, 1986ve1t, 1986ve91t, stm32f4 """
    def __init__(self,
                 io,
                 filename,
                 device='ve91t',
                 opt='r',
                 addr: bytes = None,
                 reboot: bytes = None,
                 log=None):
        """ Универсальный загрузчик ПО в микроконтроллеры

        :param io: интерфейс ввода/вывода, должен иметь методы read(timeout)/write,
            для приема/передачи сообщений. В случае ошибок генерировать IOError.
        :param filename: Файл прошивки в формате bin или hex
        :param device: avr8, ve4u, avr16, ve1t, ve91t, stm32f4
        :param opt: r/w/v for read/write/verification
        :param addr: Адрес устройсатва, например b'\x01', или None - без адреса.
        :param reboot: Команда сброса, например b'\x03' или None -без команды, с перебросом питания
        :param log: объект Logger, если не задать будет получен автоматот
        """
        super().__init__(io, addr=addr, log=log)
        try:
            self.device = dict(stm32f4=stm32f4,
                               ve91t=ve91t,
                               ve1t=ve1t,
                               avr8=avr8,
                               ve4u=ve4u,
                               avr16=avr16)[device]
        except KeyError:
            self.log.error("device uncknown")
            sys.exit()
        self.packlen = self.device['packlen']
        self.opt = opt
        self.filename = filename
        self.rebootcmd = reboot
        self.wrbin = None
        self.log.info("device=%s size=%d packlen=%d" % (device, self._calc_device_size(), self.packlen))
        self.timer = time.time()

    def _calc_device_size(self):
        size = 0
        for i in self.device['sectors']:
            size += i[2]
        return size

    def do(self):
        while True:
            if self.do_flash():
                self.log.info(u"Complite")
                try:
                    self.send_exit()
                except DevException:
                    pass
                return True
            else:
                self.log.info(u"Fail! repit? 'N' - no; AnyKey - yes")
                x = input(">")
                print("")
                if x == 'n' or x == 'N':
                    return False

    def file_open(self, filename):
        try:
            if Path(filename).suffix == '.bin':
                fd = open(filename, 'rb')
                data = fd.read()
                fd.close()
            elif Path(filename).suffix == '.hex':
                ih = IntelHex(filename)
                device_start_addr = self.device['sectors'][0][1]
                if ih.minaddr() != device_start_addr:
                    self.log.warning(f"Начальный адрес в hex файле {ih.minaddr():08x}"
                                     f" не равен адресу device {device_start_addr:08x}")
                data = ih.tobinstr(start=device_start_addr)
            elif filename:
                self.log.error(f"Некорректное раcширение файла. Нужен *.bin или *.hex")
                return None
            else:
                self.log.error(f"Некорректное имя файла <{filename}>")
                return None
        except FileNotFoundError as e:
            self.log.error(f"Невозможно открыть файл {e}")
            return None
        data = align(data, alignlen=4)
        self.log.debug(f"bin len={len(data)}")
        return data

    def wait_connection(self):
        self.log.info("waiting connection")
        while 1:
            try:
                self.send_reboot()
            except DevException:
                pass
            for _ in range(5):
                try:
                    self.send_read(self.device['sectors'][0][1], 4, timeout=0.1)
                except DevException:
                    time.sleep(.1)
                else:
                    self.log.info("Connected!")
                    return

    def do_flash(self):
        if 'w' in self.opt and 'r' in self.opt:
            self.log.error(f"error opt {self.opt}")
        if 'r' in self.opt and 'v' in self.opt:
            self.log.error(f"error opt {self.opt}")
        if 'w' in self.opt:
            self.wrbin = self.file_open(self.filename)
            if not self.wrbin:
                time.sleep(2)
                exit()

        self.wait_connection()

        if 'r' in self.opt:
            rdbin = align(self.read_bin(self._calc_device_size()), alignlen=4)
            fd = open(self.filename, 'wb')
            fd.write(rdbin)
            fd.close()
            return True

        if 'w' in self.opt:
            need_clear = not self.device.get('noclear')
            if need_clear and not self.clear_flash(len(self.wrbin)):
                return False
            if not self.write_bin(self.wrbin):
                return False

        if 'v' in self.opt:
            rdbin = align(self.read_bin(len(self.wrbin)), alignlen=4)
            fd = open('tmp.bin', 'wb')
            fd.write(rdbin)
            fd.close()
            if self.wrbin == rdbin:
                self.log.info("Verification OK!")
                return True
            else:
                self.log.error("Verification FAIL!")
                return False
        else:
            return True

    def read_bin(self, size):
        self.log.info(f"Read {size}")
        rdbin = b''
        while len(rdbin) < size:
            if size - len(rdbin) > self.packlen:
                rx = self.send_read(self.device['sectors'][0][1] + len(rdbin), self.packlen, timeout=.2)
            else:
                rx = self.send_read(self.device['sectors'][0][1] + len(rdbin), size - len(rdbin), timeout=.2)
            if rx:
                rdbin += rx
            else:
                return b''
        self.log.debug("[%.2f]sec" % float(time.time() - self.timer))
        return rdbin

    def write_bin(self, data):
        self.log.info(f"Write {len(data)}")
        wrlen = 0
        while wrlen != len(data):
            if len(data) - wrlen > self.packlen:
                self.send_write(self.device['sectors'][0][1] + wrlen, data[wrlen:wrlen + self.packlen], timeout=0.5)
                wrlen += self.packlen
            else:
                self.send_write(self.device['sectors'][0][1] + wrlen, data[wrlen:], timeout=0.5)
                wrlen += len(data[wrlen:])
        self.log.debug("[%.2f]sec" % float(time.time() - self.timer))
        return True

    def clear_flash(self, size):
        self.log.info(u"Clear")
        clrsize = 0
        for i in self.device['sectors']:
            clrsize += i[2]
            self.log.debug(f"clear {i}")
            self.send_clear(i[0])
            if clrsize >= size:
                break
        self.log.debug("[%.2f]sec" % float(time.time() - self.timer))
        return True

    def send_reboot(self):
        if self.rebootcmd:
            self.send(self.rebootcmd, remix=0, timeout=.1)

    # cmd = addr, 0x77, a0, a1, a2, a3, x, x,   ..data..    (2 or 1 + 6 byte + data)
    # ack = addr, 0xF7, a0, a1, a2, a3, x, x,               (2 or 1 + 6 byte )
    def send_write(self, addr, data, timeout):
        self.log.debug(f"send_write {addr:08x} {len(data)}")
        self.send(b'w' + pack('I', addr) + b'\x00\x00' + data, ackfrmt='IH', timeout=timeout)

    # cmd = addr, 0x72, a0, a1, a2, a3, s0, s1              (2 or 1 + 6 byte)
    # ack = addr, 0xF2, a0, a1, a2, a3, s0, s1, ..data..    (2 or 1 + 6 byte + data)
    def send_read(self, addr, size, timeout):
        self.log.debug(f"send_read {addr:08x} {size}")
        ack = self.send(b'r' + pack('IH', addr, size), ackfrmt='raw', timeout=timeout)
        return ack[6:]

    #  cmd = addr + b'e'
    #  ack = addr + b'e'
    def send_exit(self):
        self.send(b'e', ackfrmt='', remix=0, timeout=0.05)

    # cmd = addr + b'c' + n
    # ack = addr + b'c' + n
    def send_clear(self, n):
        self.send(b'c' + bytes([n & 0xff]), ackfrmt='B', remix=0, timeout=1)



import time
import binascii
from gmssl import sm2

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def sm2_password(message, pubkey):
    """
    慧舟科技密码加密算法
    :param message: 明文
    :param pubkey: 公钥
    :return: 密文
    """
    pubkey = pubkey[2:]  # 取掉头部的两个字节
    message_bytes = bytes(message, encoding='utf-8')
    sm2_crypt = sm2.CryptSM2(public_key=pubkey, private_key='')
    password_bytes = sm2_crypt.encrypt(message_bytes, CipherMode=0)  # 加密
    password = '04' + binascii.b2a_hex(password_bytes).decode('utf-8')
    return password


def string_encode(string):
    """
    中文字符编码便于网络传输
    :param string: 目标字符
    :return: 返回编码后的字符
    """
    return string.encode()

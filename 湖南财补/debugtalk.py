import time
import rsa
import binascii

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def rsa_passwd(message, pubkey):
    message = message[::-1]
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537)  # 创建公钥
    msg = str(message).encode()
    passwd = rsa.encrypt(msg, key)  # 加密, 'nopadding'
    return binascii.b2a_base64(passwd)[:-1].decode()
import hashlib


def to_md5(str):
    h = hashlib.md5()
    h.update(str.encode(encoding='utf-8'))
    return h.hexdigest()
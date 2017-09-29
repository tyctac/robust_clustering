import ctypes
from utils import config
def get_ld(s1,s2):
    ll = ctypes.cdll.LoadLibrary
    lib = ll(config.get_home_dir() + "cpp_extension/ld.so")
    return lib.lev_distance(s1,s2)

if __name__ == '__main__':
    s1 = '12son23'
    s2 = 'son123'
    print get_ld(s1,s2)
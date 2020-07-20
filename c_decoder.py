import base64

class c_decoder():

    # 设置密码(str)
    def __init__(self, key):
        self.key = key
    
    # 解密密文clp (str or bytes) 模式mode
    def decode(self,clp,mode):
        if (mode==0):
            # 二进制按字节解密 (bytes)
            plain = [clp[i] ^ ord(self.key[i%len(self.key)]) for i in range(len(clp))]
            plain = bytes(plain)
            try:
                str = plain.decode(encoding='utf-8')
            except:
                try:
                    str = plain.decode(encoding='unicode_escape')
                except:
                    str = base64.encodebytes(plain).decode('utf-8')
        else:
            # 按unicode字符解密 (str)
            str = ''
            try:
                j = 0
                for i in range(len(clp)):
                    # 获取unicode码
                    unicode = ord(clp[i])
                    # 如果大于ffff 处理emoji
                    if (unicode > 0xffff):
                        # 与两个密码进行异或
                        code = unicode ^ ((ord(self.key[i+j % len(self.key)])<<10) + ord(self.key[i+j+1 % len(self.key)]))
                        str += chr(code)
                        j = j + 1
                    else:
                        str += chr(ord(clp[i]) ^ ord(self.key[i+j % len(self.key)]))
            except:
                str = ''
        return str
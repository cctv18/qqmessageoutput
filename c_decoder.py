import base64

class c_decoder():

    # 设置密码(str)
    def __init__(self, key):
        self.key = key
    
    # 解密密文clp (str or bytes) 模式mode
    def decode(self,clp,mode):
        if (clp==None):
            return ''
        if (mode==0):
            # 如果没有密码 不解密
            if (self.key==''):
                plain = clp
            else:
                # 二进制按字节解密 (bytes)
                plain = [clp[i] ^ ord(self.key[i%len(self.key)]) for i in range(len(clp))]
                plain = bytes(plain)
            try:
                strd = plain.decode(encoding='utf-8')
            except:
                try:
                    strd = plain.decode(encoding='unicode_escape')
                except:
                    strd = base64.encodebytes(plain).decode('utf-8')
        elif (mode==1):
            # 如果没有密码 直接返回str
            if (self.key==''):
                return str(clp)
            # 按unicode字符解密 (str)
            strd = ''
            try:
                j = 0
                for i in range(len(clp)):
                    # 获取unicode码
                    unicode = ord(clp[i])
                    # 如果大于ffff 处理emoji
                    if (unicode > 0xffff):
                        # 与两个密码进行异或
                        code = unicode ^ ((ord(self.key[i+j % len(self.key)])<<10) + ord(self.key[i+j+1 % len(self.key)]))
                        strd += chr(code)
                        j = j + 1
                    else:
                        strd += chr(ord(clp[i]) ^ ord(self.key[i+j % len(self.key)]))
            except:
                strd = ''
        return strd
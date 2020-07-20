from c_qq import c_qqex # 导入c_qq.py

# 配置
dbfile = 'test/563563.db'

# 解密key (一般为imei)
key = '1234567890'

# 导出路径
outdir = 'test/563563'

# 创建对象
q = c_qqex(dbfile,key,outdir)

# 获取所有信息
q.getInfo()

# 获取所有聊天记录
q.getMsgAll()

# 导出所有聊天记录
q.exMsgsAll()
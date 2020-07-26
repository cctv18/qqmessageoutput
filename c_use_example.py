from c_qq import c_qqex # 导入c_qq.py

# db文件位置
dbfile = 'test/563563.db'
dbfile2 = 'test/slowtable_563563.db'

# 解密key (一般为imei)
key = '1234567890'

# 导出路径
outdir = 'test/563563'

# 创建对象
q = c_qqex(dbfile,key,outdir)

# 获取所有信息
q.getInfo()

# 导出好友信息
q.exFriends()

# 导出群聊信息
q.exTroop()

# 导出群成员信息
q.exTroopMem()

# 导入数据
# q.connectDB(dbfile2)

# 获取指定好友
# q.getMsgFriends('77830', save=True)

# 获取指定群聊
# q.getMsgTroop('12890', save=True)

# 获取所有聊天记录
q.getMsgAll()

# 导出所有聊天记录
q.exMsgsAll()
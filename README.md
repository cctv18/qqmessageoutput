# qqmessageoutput

安卓QQ好友数据和聊天记录 解密并导出，基于[roadwide/qqmessageoutput](https://github.com/roadwide/qqmessageoutput)，gui参考了[Yiyiyimu/QQ_History_Backup](https://github.com/Yiyiyimu/QQ_History_Backup)。

可以一次性导出好友数据和所有聊天记录，如果数据较多，导出时请耐心等待。

# 1 使用方法

作为python库使用, 请参看c_use_example.py

GUI([GitHub下载](https://github.com/ctem049/qqmessageoutput/releases/download/1.1.210104/qex_v1.1.210104_win64.exe))使用：

![GUI](c_gui.png)

选择db路径和导出路径，输入解密key(一般为imei)，获取方法可见下文。选择导出所有记录或者指定的好友/群聊。

填入最后一项(*可留空不填*)可同时导出slowtable中的数据，即db路径(第一项)选择`你的QQ.db`，最后一项选择`slowtable_你的QQ.db`，即可同时导出两个数据库中的聊天记录。

# 2 获取db的方法

默认路径:

```
data\data\com.tencent.mobileqq\databases\你的QQ.db
data\data\com.tencent.mobileqq\databases\slowtable_你的QQ.db
```

更多参考方法: https://www.cnblogs.com/roadwide/p/11220211.html

# 3 获取key的方法

key是解密的密钥

当前新版QQ的解密密钥位于以下文件中：

```
data\data\com.tencent.mobileqq\files\kc
```

旧版QQ一般是手机序列号(imei)，拨号键盘下输入`*#06#`获取，或者位于：

```
data\data\com.tencent.mobileqq\files\imei
```

手机QQ的db文件加密方式是异或加密，如果找不到自己的key可以反向破解:

```
key = 原文 XOR 密文
```

# 4 win64打包

```
conda create -n qqm python=3.10
conda activate qqm
conda install pyinstaller
pyinstaller -F -w c_gui.py
```

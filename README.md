# qqmessageoutput

安卓QQ聊天记录导出/安卓QQ数据库解密，基于[roadwide/qqmessageoutput](https://github.com/roadwide/qqmessageoutput)。

可以一次性导出所有聊天记录。

# 1 本项目的使用方法

参看 c_use_example.py

# 2 获取db的方法

[安卓QQ聊天记录导出、备份完全攻略](https://www.cnblogs.com/roadwide/p/11220211.html)

默认路径：

```
data\data\com.tencent.mobileqq\databases\你的QQ.db
data\data\com.tencent.mobileqq\databases\slowtable_你的QQ.db
```

# 3 获取key的方法

key是解密的密钥，一般是手机序列号(imei)，拨号键盘下输入`*#06#`

部分新版qq的解密密钥则可能位于以下文件中

```
data\data\com.tencent.mobileqq\files\kc
```

手机QQ的db文件加密方式是异或加密，如果找不到自己的key可以反向破解:

```
key = 原文 XOR 密文
```
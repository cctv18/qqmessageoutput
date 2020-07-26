# GUI
# 参考: (https://github.com/Yiyiyimu/QQ_History_Backup/blob/0726e00c77d98aabe2d48c0516e6e0620027a19d/GUI.py)
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from c_qq import c_qqex

version = '200726'

# 处理函数

def deal():
    db, k, od, md, fr, tr, db2 = dbfile.get(), key.get(), outdir.get(), mode.get(), qq.get(), troop.get(), dbfile2.get()
    if (db=='' or k=='' or od==''):
        info.set('!请确认填写完整')
        return
    if (md=='friend' and fr==''):
        info.set('!请确认填写完整')
        return
    if (md=='troop' and tr==''):
        info.set('!请确认填写完整')
        return
    
    info.set('导出开始...')
    window.update_idletasks()
    try:
        q = c_qqex(db,k,od)

        # 获取所有信息
        info.set('获取基础信息...')
        window.update_idletasks()
        q.getInfo()
        # 导出好友信息
        q.exFriends()
        # 导出群聊信息
        q.exTroop()
        # 导出群成员信息
        q.exTroopMem()

        # 连接数据
        if not (db2==""):
            q.connectDB(db2)
        
        # 获取聊天记录
        info.set('获取聊天记录中, 请耐心等待...')
        window.update_idletasks()
        if (md=='all'):
            q.getMsgAll()
        elif (md=='friend'):
            q.getMsgFriends(fr, save=True)
        elif (md=='troop'):
            q.getMsgTroop(tr, save=True)
        else:
            info.set('!错误的模式')
        
        # 导出聊天记录
        info.set('导出聊天记录中, 请耐心等待...')
        window.update_idletasks()
        q.exMsgsAll()

    except Exception as e:
        info.set(repr(e))
        return ()
    info.set('导出完成...')

# 创建窗口
window = tk.Tk()
window.title('QQ聊天记录导出 @ctem049')
window.resizable(False, False)

ttk.Label(window, text="github.com/ctem049/qqmessageoutput ver{}".format(version)).grid(row=0, column=0, columnspan=4)

# 1 db文件选框
dbfile = tk.StringVar()
ttk.Label(window, text="db文件路径: ").grid(row=1, column=0, sticky="e")
e1 = ttk.Entry(window, textvariable=dbfile)
e1.grid(row=1, column=1)
def SelectPath():
    pathTmp = filedialog.askopenfilename()
    dbfile.set(pathTmp)
ttk.Button(window, text="选择", command=SelectPath, width=5).grid(row=1, column=3)

# 2 key输入框
key = tk.StringVar()
ttk.Label(window, text="解密key(imei): ").grid(row=2, column=0, sticky="e")
e2 = ttk.Entry(window, textvariable=key)
e2.grid(row=2, column=1, columnspan=3, sticky="ew", pady=3)

# 3 导出路径选择
outdir = tk.StringVar()
ttk.Label(window, text="导出路径: ").grid(row=3, column=0, sticky="e")
e3 = ttk.Entry(window, textvariable=outdir)
e3.grid(row=3, column=1)
def SelectOutdir():
    pathTmp = filedialog.askdirectory()
    outdir.set(pathTmp)
ttk.Button(window, text="选择", command=SelectOutdir, width=5).grid(row=3, column=3)

# 4 导出方式选择
mode = tk.StringVar()
mode.set('all')
def modeCheck():
    if (mode.get()=='friend'):
        e4.config(state='normal')
    else:
        e4.config(state='disabled')
    if (mode.get()=='troop'):
        e5.config(state='normal')
    else:
        e5.config(state='disabled')

# 4.1 导出全部
ttk.Radiobutton(window, text='导出所有记录', variable=mode, value='all', command=modeCheck).grid(row=4, column=0, sticky="e")

# 4.2 导出指定QQ号
ttk.Radiobutton(window, text='导出指定好友', variable=mode, value='friend', command=modeCheck).grid(row=5, column=0, sticky="e")
qq = tk.StringVar()
e4 = ttk.Entry(window, textvariable=qq, state='disabled')
e4.grid(row=5, column=1)

# 4.3 导出指定QQ群
ttk.Radiobutton(window, text='导出指定群聊', variable=mode, value='troop', command=modeCheck).grid(row=6, column=0, sticky="e")
troop = tk.StringVar()
e5 = ttk.Entry(window, textvariable=troop, state='disabled')
e5.grid(row=6, column=1)

# 5 高级
dbfile2 = tk.StringVar()
ttk.Label(window, text="db数据文件(高级): ").grid(row=7, column=0, sticky="e")
e6 = ttk.Entry(window, textvariable=dbfile2)
e6.grid(row=7, column=1)
def SelectDbfile2():
    pathTmp = filedialog.askopenfilename()
    dbfile2.set(pathTmp)
ttk.Button(window, text="选择", command=SelectDbfile2, width=5).grid(row=7, column=3)

# 6 导出
ttk.Button(window, text="导出", command=deal).grid(row=8, column=1)

# 7 状态栏
info = tk.StringVar()
ttk.Label(window, textvariable=info).grid(row=9)

# 窗口循环
window.mainloop()
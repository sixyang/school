import tkinter
from tkinter import messagebox
from tkinter import filedialog
import re,os


def open_file():
    default_dir = r'C:\Users\18273\Desktop'
    file_path = filedialog.askopenfilename(title='选择文件',initialdir=(os.path.expanduser(default_dir)))
    with open(file_path,'r',encoding='utf8') as file:
        content = file.read()
        text.insert('0.0',content)

def save_file():
    fname = tkinter.filedialog.asksaveasfilename(title='保存文件')
    with open(r'C:\Users\18273\Desktop\hello.txt','w',encoding='utf8') as f:
        
        f.write(text.get('0.0','end'))
        f.flush()
        messagebox.showinfo(title='message', message='save succed')

def paste_str():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    pasted_content = d.decode('utf8')
    a = text.mark_set('insert', '2.0')
    print(a)
    start = text.index('f')
    print(start)
        
def must_80():
    '''格式化输入文件'''
    content = text.get('0.0','end')
    nums = '1234567890'
    content_list = content.split('\n')
    for line,paragraph in enumerate(content_list):
        if len(paragraph) > 80:
            content_list[line] = paragraph[:80]
            content_list[line+1:line+1] = [paragraph[80:]]
        if not content_list[line].startswith(str(line)) and content_list[line][0:1] not in nums:
            content_list[line] = ' '.join([str(line+1),content_list[line]])
    content = '\n'.join(content_list)       
    text.delete('0.0','end')
    text.insert('0.0',content)


def re_match(text):
    '''正则匹配，获得文章内容的相关信息'''
    word_num_ = re.compile(r'\w')                       #英文，数字，_，汉字的匹配正则表达式
    num = re.compile(r'\d')                             #数字的匹配正则表达式
    space = re.compile(r'\s')                           #空格的匹配正则表达式

    words_num = 0                                       #英文，数字，_，汉字的个数
    nums = 0                                            #数字的个数
    spaces = 0                                          #空格的个数
    text_num = 0                                        #整个文本的字符个数
    
    num_find = num.findall(text)
    if num_find:
        nums += len(num_find)

    string_find = word_num_.findall(text)
    if string_find:            
        words_num += len(string_find)

    space_num = space.findall(text)
    if space_num:
        spaces += len(space_num)

    text_num += len(text)

    return (words_num-nums,nums,spaces,text_num)

def get_info():
    '''获得信息按钮的执行函数，点击获得信息就能触发这个函数。'''
    content = text.get('0.0','end')
    raw_information = re_match(content)
    al_num = raw_information[0]
    num_num = raw_information[1]
    space_num = raw_information[2]
    total_num = raw_information[3]
    information = '全部字母数：{} \n数字个数：{}\n空格个数：{}\n文章总字数：{}'.format(al_num,num_num,          space_num,total_num)
    messagebox.askquestion('文本信息',information)


def search_str():
    '''查询所需字符串在文章的位置'''
    search_regex = search_entry.get()                           #获得匹配字符串   
    content = text.get('0.0','end')                             #获得文本内容
    content_list = content.split('\n')
    span_li = []                                                #存储span值
    result = ''
    regex = re.compile(search_regex)                            #正则匹配式
    line = 1
    for i in content_list:
        rst = re.finditer(regex,i)
        for j in rst:
            span_li.append(j.span())
            result += '你想查找的字符串分别在第 {} 行的 第 {} 个。\n'.format(line,j.span()[0])
        line += 1
    messagebox.showinfo('查找结果',result)
    # print(span_li)
    return span_li


def replace_str():
    reped_index = search_entry.get()                            #被替换的字符串
    text_content = text.get('0.0','end')
    # search_index = re.search(rep_index).span()
    insert_content = insert_entry.get()                         #替换的字符串
    # index = search_str()
    content = text.get('0.0','end')                             #文本内容
    content_list = content.split('\n')
    span_li = []
    line = 1
    lines = []

    for index,element in enumerate(content_list):
        con = re.finditer(reped_index,element)                          #匹配的迭代器

        for i in con:
            span_li.append(i.span())
            lines.append(line)

        line += 1

    zip_ = zip(lines,span_li)
    
    for j in zip_:
        start = '.'.join([str(j[0]),str(j[1][0])])
        end = '.'.join([str(j[0]),str(j[1][1])])
        print(start,end)
        text.delete(start,end)
        text.insert(start,insert_content)

if __name__ == "__main__":

    window = tkinter.Tk()
    window.title('Python Notepad')
    window.geometry('1050x600')

    text = tkinter.Text(window,height=40,width=145,font=('宋体',10))
    text.pack()

    button = tkinter.Button(window,text='信息',command=get_info)
    button.place(x=20,y=565)

    search_button = tkinter.Button(window,text='查询',command=search_str)
    search_button.place(x=70,y=565)

    search_entry = tkinter.Entry(window,show='')
    search_entry.place(x=120,y=565)


    replace_button = tkinter.Button(window,text="替换",command=replace_str)
    replace_button.place(x=370,y=565)

    insert_entry = tkinter.Entry(window,show='')
    insert_entry.place(x=420,y=565)

    standard = tkinter.Button(window,text="格式化",command=must_80)
    standard.place(x=280,y=565)


    counter = 0
    menubar = tkinter.Menu(window)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Open', command=open_file)
    filemenu.add_command(label='Save', command=save_file)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=window.quit)


    window.config(menu=menubar)

    window.mainloop()

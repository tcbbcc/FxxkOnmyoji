#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: litian_cup@163.com
@software: pycharm
@file: tk_app.py
@time: 2021/1/15 15:45
@desc: 可视化界面
        1. [pip迁移](https://blog.csdn.net/weixin_38781498/article/details/94037008)：pip install -r requirements.txt
        2. [Python3入门之线程threading常用方法](https://www.cnblogs.com/chengd/articles/7770898.html)
        3. [threading之线程的开始,暂停和退出](https://www.cnblogs.com/cnhyk/p/13697121.html)
"""
import os
from dataclasses import dataclass
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from configure_tools import Configure
from function_tools import FuncRun
from system_hotkey import SystemHotkey
from mouse_action import MouseAction
from function_factory import FuncFactory
from time import sleep
import time
import datetime
from set_windows import SetWin
from methods import build_thread
from traceback import print_exc, format_exc


@dataclass
class InfoPip:

    def __post_init__(self):
        # 左边是入口，右边是出口
        self.line_info = ['', '', '']
        self.first_color = ''

    def get_two_var(self):
        """将当前的pip结果放到var中去，获得两个str"""
        return self.first_color, self.line_info[0], '\n'.join(self.line_info[1:])

    def set_first_line(self, info, color):
        """设置first line，进最新的值，出最后一个值"""
        self.first_color = color
        for i in range(len(self.line_info) - 1, 0, -1):
            self.line_info[i] = self.line_info[i - 1]
        self.line_info[0] = info

    def get_pip_history(self, info, color):
        """将上述功能进行合并"""
        self.set_first_line(info, color)
        return self.get_two_var()


@dataclass
class App:

    def __post_init__(self):

        self.init_area()
        self.global_var()
        self.init_tk()
        self.clear_logs()

    def global_var(self):
        """全局变量初始化"""

        # 初始坐标和颜色
        self.xy, self.color = '', ''
        # 初始化功能信息
        self.current_func = None

        # 日记文件，一天一个，每次启动时删除七天前的文件
        self.current_time = datetime.datetime.now()
        self.current_date = datetime.datetime.strftime(self.current_time, '%Y-%m-%d')

        log_file_name = self.current_date + '.txt'
        self.log_file = open('./logs/' + log_file_name, 'a+', encoding='utf-8')

    def init_tk(self):
        """初始化tk"""

        """读取各种配置"""
        frame_label_pad = self.settings.get_option('gui', 'frame_label_pad', 'int')
        label_ipadx = self.settings.get_option('gui', 'label_ipadx', 'int')
        button_ipadx = self.settings.get_option('gui', 'button_ipadx', 'int')
        cmb1_width = self.settings.get_option('gui', 'cmb1_width', 'int')
        cmb2_width = self.settings.get_option('gui', 'cmb2_width', 'int')
        e_xy_length = self.settings.get_option('gui', 'e_xy_length', 'int')
        e_color_length = self.settings.get_option('gui', 'e_color_length', 'int')
        windows_width_input = self.settings.get_option('gui', 'windows_width_input', 'int')
        block_color = self.settings.get_option('gui', 'block_color')

        default_windows_width = self.settings.get_option('windows', 'win1_loc').split(',')[-1]

        """设置各种字体"""
        # 标题字体的大小
        font_type = self.settings.get_option('font', 'font_type')
        font_label = (
            font_type,
            self.settings.get_option('font', 'font_size_1', 'int'))
        # 文字字体大小
        font_normal = (
            font_type,
            self.settings.get_option('font', 'font_size_normal', 'int'))
        # frame字体大小
        font_labelframe = (
            font_type,
            self.settings.get_option('font', 'font_size_label', 'int'))
        # log字体大小
        font_labelLog = (
            font_type,
            self.settings.get_option('font', 'font_size_log', 'int'))

        """底层root初始化"""
        self.root = Tk()
        self.root.title('狗贼v0.2  【作者：李英俊小朋友】')

        """frame1_外框，功能、运行、暂停、退出、调整界面"""
        self.frame_1 = LabelFrame(self.root, text='| 海的那边 |',
                                  labelanchor=N, font=font_labelframe,
                                  padx=frame_label_pad,
                                  pady=frame_label_pad, fg=block_color)
        self.f11 = Frame(self.frame_1)

        self.cmb1_value = StringVar()
        self.cmb2_value = StringVar()

        self.l1 = Label(self.f11, text='功能', font=font_normal, justify='left')
        self.l1.pack(side=LEFT, ipadx=label_ipadx, fill=Y)

        self.cmb1 = ttk.Combobox(self.f11, textvariable=self.cmb1_value,
                                 width=cmb1_width, font=font_normal)
        # 初始化功能名字，从ini文件中获取
        self.cmb1['values'] = self.ff.get_func_names()
        # 选择第一个为默认
        # self.cmb1.current(0)
        self.cmb1.bind('<<ComboboxSelected>>', self.get_list)
        self.cmb1.pack(side=LEFT, fill=Y)

        self.cmb2 = ttk.Combobox(self.f11, textvariable=self.cmb2_value,
                                 width=cmb2_width, font=font_normal)
        self.cmb2.bind('<<ComboboxSelected>>', self.get_key)
        self.cmb2.pack(side=LEFT, fill=Y)

        self.b2 = Button(self.f11, text='运行(r)', command=self.func_start, font=font_normal)
        self.b2.pack(side=LEFT, fill=BOTH, ipadx=button_ipadx, expand=True)

        self.b4 = Button(self.f11, text='暂停(p)', command=self.pause, font=font_normal, width=6)
        self.b4.pack(side=LEFT, fill=Y, ipadx=button_ipadx)

        self.f12 = Frame(self.frame_1)

        self.l_adjust = Label(self.f12, text='定宽', font=font_normal)
        self.l_adjust.pack(side=LEFT, fill=Y, ipadx=label_ipadx)

        # 宽度取值
        self.reset_windows_width = StringVar()
        self.e_width = Entry(self.f12, width=windows_width_input,
                             textvariable=self.reset_windows_width, font=font_normal, justify='center')
        self.e_width.insert(END, default_windows_width)
        self.e_width.pack(side=LEFT, fill=Y)

        self.b_adjust_win = Button(self.f12, text='调整界面(d)', font=font_normal,
                                   command=self.set_two_win_left)
        self.b_adjust_win.pack(side=LEFT, fill=Y, ipadx=button_ipadx)

        self.cb_var_whether_top = BooleanVar()
        self.cb1 = Checkbutton(self.f12, text='置顶', variable=self.cb_var_whether_top,
                               font=font_normal, onvalue=True, offvalue=False,
                               command=self.set_top_window,
                               justify='left',
                               )
        # 初始化是否置顶
        self.cb_var_whether_top.set(False)
        self.cb1.pack(side=LEFT, fill=Y, ipadx=label_ipadx)

        self.b4 = Button(self.f12, text='载入默认配置(l)', command=self.load_default_config, font=font_normal)
        self.b4.pack(side=LEFT, fill=Y, ipadx=button_ipadx)
        self.b5 = Button(self.f12, text='选择用户配置(L)', command=self.load_user_config, font=font_normal)
        self.b5.pack(side=LEFT, fill=BOTH, ipadx=button_ipadx, expand=YES)

        self.b3 = Button(self.f12, text='退出(c)', command=self.destroy, font=font_normal, width=6)
        self.b3.pack(side=LEFT, fill=Y, ipadx=button_ipadx)

        self.f13 = Frame(self.frame_1)

        self.f11.pack(fill=BOTH)
        self.f12.pack(fill=BOTH)
        self.f13.pack(fill=BOTH)

        """frame2外框_各种坐标处理"""
        self.frame_2 = LabelFrame(self.root, text='| 坐标之力 |', labelanchor=N, font=font_labelframe, padx=frame_label_pad,
                                  pady=frame_label_pad, fg=block_color)
        self.f21 = Frame(self.frame_2)

        self.l_xy = Label(self.f21, text='坐标', font=font_normal)
        self.l_xy.pack(side=LEFT, fill=Y, ipadx=label_ipadx)

        # 两个entry的值
        self.xy_value = StringVar()
        self.color_value = StringVar()

        self.e_xy = Entry(self.f21, width=e_xy_length,
                          textvariable=self.xy_value, font=font_normal, justify='center')
        self.e_xy.insert(END, self.xy)
        self.e_xy.pack(side=LEFT, fill=Y)

        self.l_c = Label(self.f21, text='颜色', font=font_normal)
        self.l_c.pack(side=LEFT, fill=Y, ipadx=label_ipadx)

        self.e_color = Entry(self.f21, width=e_color_length,
                             textvariable=self.color_value, font=font_normal, justify='center')
        self.e_xy.insert(END, self.color)
        self.e_color.pack(side=LEFT, fill=Y)

        self.f22 = Frame(self.frame_2)

        self.b1 = Button(self.f22, text='写入信息(w)', command=self.write_dict, font=font_normal)
        self.b1.pack(side=LEFT, fill=BOTH, ipadx=button_ipadx, expand=True)

        self.b_save_conf = Button(self.f22, text='保存为默认(s)', font=font_normal,
                                  command=self.save_config_as_default)
        self.b_save_conf.pack(side=LEFT, fill=BOTH, expand=YES)

        self.b_save_conf = Button(self.f22, text='保存到文件(S)', font=font_normal,
                                  command=self.save_config_to_file)
        self.b_save_conf.pack(side=LEFT, fill=BOTH, expand=YES)

        self.f21.pack(fill=BOTH)
        self.f22.pack(fill=BOTH)

        """frame3 待开发"""
        self.frame_3 = LabelFrame(self.root, text='| 献出心脏 |', labelanchor=N,
                                  font=font_labelframe,
                                  padx=frame_label_pad,
                                  pady=frame_label_pad,
                                  fg=block_color)
        self.f31 = Frame(self.frame_3)

        self.current_info = StringVar()
        self.l_first = Label(self.f31, textvariable=self.current_info, justify=LEFT, font=font_labelLog)
        self.l_first.pack(anchor=NW, side=TOP)

        self.history_info = StringVar()
        self.l_history = Label(self.f31,
                               textvariable=self.history_info,
                               # wraplength=200,
                               justify='left',
                               font=font_labelLog,
                               fg='grey'
                               )
        self.l_history.pack(anchor=NW, side=TOP)

        # self.l_me = Label(self.f31, text='作者：李英俊小朋友', justify=RIGHT)
        # self.l_me.pack(anchor=SE, side=BOTTOM)

        self.f31.pack(side=LEFT, fill=BOTH, expand=True)

        """布局"""
        # padx、pady是框架外部距离框架的距离
        self.frame_1.pack(side=TOP, fill=None, anchor=NW, padx=frame_label_pad, pady=frame_label_pad)
        self.frame_2.pack(side=LEFT, fill=Y, anchor=NW, padx=frame_label_pad, pady=frame_label_pad)
        self.frame_3.pack(side=LEFT, fill=BOTH, anchor=NW, padx=frame_label_pad, pady=frame_label_pad,
                          expand=True)

    def init_area(self):
        """初始化区域"""
        # 全局快捷键设置
        self.hk = SystemHotkey()
        self.hk.register(('alt', 'w'), callback=lambda e: self.write_dict())
        self.hk.register(('alt', 'c'), callback=lambda e: self.destroy())
        self.hk.register(('alt', 'r'), callback=lambda e: self.func_start())
        self.hk.register(('alt', 'p'), callback=lambda e: self.pause())
        self.hk.register(('alt', 's'), callback=lambda e: self.save_config_as_default())
        self.hk.register(('alt', 'shift', 's'), callback=lambda e: self.save_config_to_file())
        self.hk.register(('alt', 'l'), callback=lambda e: self.load_default_config())
        self.hk.register(('alt', 'shift', 'l'), callback=lambda e: self.load_user_config())
        self.hk.register(('alt', 'd'), callback=lambda e: self.set_two_win_left())

        # 移动鼠标
        self.ma = MouseAction()
        # 配置初始化
        self.settings = Configure('configures/config.ini')
        # 设置初始界面
        self.sw = SetWin()
        # 操作功能配置文件的工具
        self.ff = FuncFactory()
        # 信息输出栈
        self.info_stack = InfoPip()

    def show_info(self, word, fg='green'):
        """输出问题"""
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        w1_color, w1, w2 = self.info_stack.get_pip_history(word, fg)

        self.current_info.set(w1)
        self.l_first.configure(fg=fg)

        self.history_info.set(w2)

        # 写入日志
        self.log_file.write(current_time + ': \n' + w1 + '\n\n')

    def clear_logs(self):
        """清除7天前的日志数据"""
        keep_days = self.settings.get_option('logs', 'keep_days', 'int')
        path = './logs'
        delta_time = datetime.timedelta(days=keep_days)
        remove_date = self.current_time - delta_time

        count = 0
        for file_name in os.listdir(path):
            file_time = datetime.datetime.strptime(file_name.replace('.txt', ''), '%Y-%m-%d')
            if file_time < remove_date:
                os.remove(os.path.join(path, file_name))
                count += 1

        self.show_info('成功删除了【' + str(count) + '】个日志文件...', 'black')

    def set_top_window(self):
        """设置是否置顶"""
        if self.cb_var_whether_top.get():
            self.show_info('设置软件【置顶】')
            self.root.wm_attributes('-topmost', 1)
        else:
            self.show_info('取消软件【置顶】')
            self.root.wm_attributes('-topmost', 0)

    def set_two_win_left(self):
        """设置两个阴阳师的界面排在左边"""
        self.win_settings = self.settings.get_items('windows')
        handles = self.sw.find_onmyoji_handle()
        if handles[0] == 0:
            self.show_info('错误！未打开阴阳师！', 'red')
            return

        # 遍历阴阳师所有句柄
        count = 0
        for h in range(len(handles)):
            count += 1
            # 提取第h个坐标，h只有1的话，就只提取一个坐标
            loc = [int(temp) for temp in self.win_settings[h][1].split(',')]
            # 按照输入的最新宽度设置界面宽度
            repair_width = int(self.reset_windows_width.get())
            if repair_width != '':
                loc[-1] = repair_width
                # 如果输入了数值，则按数值来重设宽度
                if count == 1:
                    # 第一个界面，123不动，调整4
                    ...
                elif count == 2:
                    # 第二个界面，13不动，调整24
                    loc[1] = repair_width - 8
                elif count == 3:
                    # 第三个界面，右上，23不动，调整14
                    loc[0] = repair_width + 280
                else:
                    self.show_info('你有病不是？你打开这么多阴阳师干嘛啊？', 'red')
            try:
                self.sw.move_rect(handles[h], loc)
                self.show_info('成功调整界面！')
            except Exception as e:
                self.show_info('调整界面失败...', 'red')
                return

    def run(self):
        self.check_mouse_move()
        self.root.mainloop()

    def get_list(self, *args):
        """获取对应下拉框的list，方便写入后续下拉框"""
        cmb1_v = self.cmb1_value.get()
        # 从配置文件中获取功能类
        self.current_func = self.ff.init_config(cmb1_v)
        # 设置下拉框的值
        self.cmb2['values'] = self.current_func.get_procedure_names()

    def get_key(self, *args):
        """cmb2的对应的函数"""
        # return self.cmb2_value.get()
        ...

    def save_config_as_default(self):
        """保存当前设置"""
        try:
            self.current_func.save_function_to_json('templates/test.json')
            self.show_info('配置文件保存成功！')
        except Exception as e:
            self.show_info('错误！保存文件出错！', 'red')

    def save_config_to_file(self):
        try:
            file_path = asksaveasfilename(defaultextension='.json', filetypes=[("Json文件", ".json")], initialdir='dir',
                                          title='Save as')
            self.current_func.save_function_to_json(file_path)
            self.show_info('配置文件保存成功！')
        except Exception as e:
            # print(repr(e))
            self.show_info('错误！保存文件出错！', 'red')

    def show_func(self, func):
        """对于载入的func进行前端显示"""
        self.cmb1.set(func.get_func_name())
        self.cmb2['values'] = func.get_procedure_names()

    def load_default_config(self, path='templates/data.json'):
        """载入数据"""
        try:
            self.current_func = self.ff.create_function_from_json(path)
            # 载入后设置前端显示
            self.show_info('读取配置文件成功！')
            # print(self.current_func.get_data())
        except Exception as e:
            self.show_info('错误！读取配置文件出错！', 'red')

    def load_user_config(self):
        """载入用户数据"""
        file_path = askopenfilename()
        self.load_default_config(file_path)

    def pause(self):
        """暂停"""
        ...
        # TODO

    def write_dict(self):
        """将信息写入到dict中"""
        p_name = self.cmb2_value.get()
        if p_name != '':
            self.current_func.update(p_name, self.xy, self.color)
            # print(self.current_func.get_data())
            self.show_info('成功写入【' + p_name + '】的坐标...')

    def get_postion_color(self):
        """设置绑定后的按键操作的值"""

        def extend_color(color: tuple):
            """将rgb颜色转换为rgb_16进制"""
            ten_six = "#%02x%02x%02x" % (color[0], color[1], color[2])
            return str(color) + '_' + ten_six, ten_six

        temp_xy = self.xy
        self.xy, self.color = self.ma.get_mouse_postion_color().get_info()

        if self.xy != temp_xy:
            self.e_xy.delete(0, END)
            self.e_xy.insert(END, str(self.xy))
            self.e_color.delete(0, END)
            insert_info, tensix = extend_color(self.color)
            self.e_color.insert(END, insert_info)
            return tensix

    def check_mouse_move(self):
        """检测鼠标移动，实时显示鼠标位置和颜色"""

        def check_mouse():
            while True:
                # 显示颜色设置
                tensix = self.get_postion_color()
                if tensix != '#-1-1-1':
                    self.e_color.configure(fg=tensix)
                    self.l_c.configure(fg=tensix)
                else:
                    self.e_color.configure(fg='red')
                sleep(self.settings.get_option('mouse', 'mouse_check_speed', 'float'))

        build_thread(check_mouse, '鼠标颜色检查')

    def func_start(self):
        """运行"""
        # 当前配置文件中的字典
        self.show_info(self.current_func.get_func_name() + '启动...')

        # 这里检查None，是因为如果没有导入，或者没有选择的话，当前的功能类就是None，就不能运行
        if self.current_func is not None:
            fr = FuncRun(self.current_func)
            result_info = fr.func_demo()

            # 获取错误信息，正确就不输出了
            if result_info is not None:
                self.show_info(*result_info)
        else:
            self.show_info('错误！请创建流程，或者导入流程！', 'red')

    def destroy(self):
        self.root.quit()
        # 关闭日志文件
        self.log_file.close()


if __name__ == '__main__':
    App().run()

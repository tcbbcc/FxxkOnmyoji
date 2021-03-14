# 如何成为一名合格的阴阳带师

本脚本仅供学习参考，不收取任何费用，如果你是付钱获取的，那么你可真的憨批。

​                                                                                                 ——作者：李英俊小朋友

[TOC]

## 写在前面 | Write Head

这是一个关于 **阴阳师** 的脚本，如果你不小心点进来了，赶紧出去，现在还来得急。

**重要声明：**

1. 本软件不是无脑使用的软件，有学习门槛，不是基于图片识别而是基于自己思路的软件， 不保证以后不使用图片识别、人工智能等技术。本软件注重于学习编程，也是我学习python的记录或者说笔记，而不是鼓励大家去用脚本来打破游戏平衡，降低自己和他人的游戏体验。（**请怀着羞耻之心使用该脚本，顺带感谢一下无私的我**）

2. **仅供学习参考，不允许用于任何商业用途。** 使用该脚本造成的任何后果与本人无关（主要是怕网易干我哈哈哈，网易如果想招我是可以考虑下的嘻嘻，毕竟去年面过网易）

3. **严禁任何转载**，毕竟万一以后火了，网易要打我，我只能说，与我无瓜，需要删除的话及时跟我说啊，我删除不就完了嘛。 *如果非有人要转载我的，我也没办法了啊，我也没时间去告他对吧，所以如果有所传播，那网易你们去追责这些人嗷。（歪头）*

4. 发现任何bug都可以通过github、博客园或者csdn留言给我，联系方式在最后嗷，[**点我直达**](#contact)。最后，希望所有阴阳师玩家、爱好者都谨慎使用，技术无罪，怀璧其罪。（工作室biss）祝大家都能抽到喜欢的式神。

5. **献给所有为了梦想的 程序员们 / 阴阳师们 ~**

   @李英俊小朋友	20210110，山东烟台

6. 【20210212补充】因为是仅供学习参考，所以不会打包为.exe格式的嗷，现在不会，以后更不会，违者与我本人无关，请有关部门追究其相关的法律责任。（为什么不呢？都打包成.exe你跟我说你用来学习？学习？学个peach！但是打包的技术是要学习的，懂我的意思叭[暗示]）

> 如果网易也不问我，也不跟我沟通，就让CSDN、博客园、简书、bilibili搞我、删我博客，我告诉你嗷，这是在玩火。这样的话，我一定不会屈服的。（握拳）

## 使用方法 | Using Method

### 设计思路 | Design

1. 首先，我想做一个双开刷御魂的脚本。这就需要：**识别挑战的位置**

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210110081703644.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

2. 所以首先要做的就是：识别整个桌面上挑战的位置，然后点击，就可以开始刷图了对吧。

3. 这个观念也是这个脚本的核心，那就是从桌面上找到目标图片（挑战截图）中心的位置，然后利用鼠标模拟点击，实现各种流程的控制。后面无论是刷御魂也好，刷结界突破也好，带狗粮也是，都是这个思路。

4. **划重点了：** 

   1. 场景识别（通过多个点位识别）：都返回True则场景识别返回True
      1. `l`：该点颜色与写入颜色一致则返回True
      2. `n`：该点颜色与写入颜色不一致则返回True
   2. 进行操作（一般一个step只有一个操作）：
      1. `c`：单点点击
      2. `m`：多点点击
   3. 组合step（步骤）为function（功能）：
      1. 一个功能包含多个step
      2. 每个step多线程分别执行场景识别
      3. 识别成功后就进行操作
   4. 关联其他function（功能）：
      1. 配置connections：`connections=104-105`
      2. 主功能运行时，connections（关联功能）也会运行
      3. 适用于：关闭协同悬赏、接受同心之兰等

### 界面介绍 | Interface

### 操作说明 | Operation

### 快捷键位 | Hotkey

## 从零开始 | Start Zero

> 如果不懂编程的话，下面对你来说真的很难，但是没关系，所有的快乐都是努力之后得到的。成功的喜悦会覆盖所有的懊恼和气馁，一起加油叭。（有任何问题，很简单也不要紧，留言告诉我叭，我会在上面补充的。）

1. **下载`python3.78`**：[官网地址](https://www.python.org/downloads/release/python-378/)，然后安装啊啥的

2. **安装一个特殊的依赖包**：在cmd中输入：`pip install pyHook-1.5.1-cp37-cp37m-win_amd64.whl`，注意，这里的pyHook是拖进来的显示的应该是绝对路径，如下图：（[`pyhook`安装地址](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook)）

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210120224908459.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

3. 升级一下pip：`python -m pip install --upgrade pip -i https://pypi.douban.com/simple/` 

4. 去我的[GitHub](https://github.com/TinyHandsome/FxxkOnmyoji)，下载工程文件，解压。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012022520347.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

5. **安装依赖包**：打开文件夹，看到这个`requirements.txt`了没，跟上面安装`whl`一样，输入：`pip install -r requirements.txt -i https://pypi.douban.com/simple/` ，这里的`requirements.txt`也是要拖进来的，反正是个绝对路径和相对路径的问题。如果有不懂的，留言，我慢慢补充。（tips：按住shift+右键，可以在当前路径召唤`cmd`或者`powershell`）（懂编程的人，自己看着下包就好了，我这里有很多跟这个项目无关的包，懒得改了）

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012023005290.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   安装完毕：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210120231522657.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

## 项目计划 | Project Plan

### 版本控制 | Version

1. 【v0.1】老张手里还有，这个版本我自己都没有了，界面过于挫

2. 【v0.2】界面优化后的版本，增加了流程导入导出功能，可是只是针对单独的功能可以使用，盖亚~

3. 【v0.3】全（chuan）新的版本
   
   > 1. 识别页面多状态（新增l的非状态，n）后，点击
   > 2. 界面gui优化，好看太多了
   > 3. 配置文件优化，支持各种方式的配置文件融合
   > 4. 新增测试开关，目前关联开关的功能包括：
   >      1. UpdateConfigureTools中的软件打开次数计数，打开测试时重置计数器为0

### 计划列表 | Todo

*逆序显示，最新的思路在最上面。*

- [ ] 新增倒计时功能

  1. 时间到了之后自动暂停
  2. 倒计时与l和n等价，即达到某个条件/场景，触发什么操作

- [ ] 保存鼠标位置

  在点击之前保存现有位置，点击完成后回来（也要有随机值）

- [ ] 跳过检查

  1. 新增点标记
  2. 如果点的标记为ignore，则跳过检查，即该点可以没有值，没有值的时候，不进行操作。

- [ ] 增加补充点位功能

  - 发现新的状态后，直接在当前状态补充点位信息
  - 需要有个输入框，输入新增流程名
  - [20210314] **直接修改functions.ini，然后保存，利用【重载功能】实现点位的添加**
  - ~~定义点位补充的时间，放到类中~~  没必要
  - ~~所以一个功能中每个流程点的信息，必须封装为一个类，有创建时间，修改时间啊啥的（数据库？）~~  已实现
  - ~~**注意：**  检测到状态之后，不一定是点一下，可能是点多下，比如关闭双倍御魂，所以功能也要封装，一个功能可能要包含其他功能~~  已实现

- [ ] 添加时间戳、预计运行时间、剩余体力检测

  预计运行时间：每次战斗时间取均值

- [ ] 增加体力获取功能

  从有体力的界面中检测当前体力还剩多少，这样就可以自动计算脚本可以刷多久了

### 完成列表 | Finished

*正序显示，最新完成的功能在最下面。*

- [x] 防检测处理：20210117

  实现鼠标点击随机偏移，鼠标连点随机时间间隔

- [x] 优化配置文件：20210121

  自动读取功能配置文件中的流程信息（`functions.ini`）

- [x] 调整窗口大小，在界面输入值进行调整，点击后更新大小：20210123

  第一个窗口：`-10,0,300,width`

  第二个窗口：`-10,width-8,300,width`

  第三个窗口：`width+2,0,300,width`

- [x] 界面太长，需要重新布局：20210122

  - 调试前：

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021012123474372.png)

  - 调试后：

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210121235932819.png)

- [x] 设置界面是否置顶的选项：20210123

- [x] 新增log日志功能，自动清空7天前的日志：20210123

- [x] 优化输出功能：20210124

  - 建立信息输出队列，新建一个类，专门处理。
  - 输出放两个label，一个用来存最新，一个用来存历史
  
- [x] 实现保存到文件功能：20210124

- [x] 给用户写死第二个界面纵坐标和第三个位置横坐标的配置参数：20210130

- [x] 优化界面逻辑：20210208

  1. ~~打开界面后，获取default.json的配置文件，如果找不到配置文件，则将数据进行初始化。~~
  
     现在是打开界面之后，直接根据funtion.ini初始化，如果需要用自己的，直接导入就行。
  2. ~~初始化的时候（找不到默认配置文件）~~，将所有信息封装为[function]，然后初始化
  
- [x] 优化配置文件：20210208

  - [x] 新增非逻辑识别，即根据标记检测该点，检测对应才操作，还是检测不对应就操作

  - [x] 可以配置多个流程

  - [x] 全空的流程无法运行

  - [x] 封装流程，保存多个流程

  - [x] 流程信息跟配置文件关联，一一对应

  - [x] 配置信息json构造设想，相关类放在structure文件夹中

    ```python
    [
        # 多个function
        {
            "func_name": func_name,
            "func_code": func_code,
            # 是否展示该func
            "func_shown": func_shown,
            # 步骤分两种，一种是常规步骤
            "steps": [
                # 多个Step
                {
                    "step_name": step_name,
                    "points": [
                        # 每个步骤会有多个点位信息Point
                        {
                            "point_name": point_name,
                            "point_type": point_type,
                            "point_location": point_location,
                            "point_color": point_color,
                            # 0代表不点击
                            "click_times": click_times,
                        }
                    ],
                }
            ]
            # 另一种是关联步骤
            "connections": [c1, c2, c3]
        }
    ]
    ```
    
  - [x] ~~如果导入流程，重名的取导入的，最新的要最新的，没有流程取旧的，配置信息全空。~~

    讲道理，没必要，如果需要新功能，那就直接修改配置文件就行。如果有需求，以后再说。

- [x] 优化点的坐标颜色信息：20210208

  ~~配置文件优化，增加识别目标点颜色后，可以点击其他位置的功能，现在是检验到目标点之后就要点击目标点。~~

  - 封装成一个类
  - 该类实现：根据多个点的颜色 **定位状态**
  - 然后点击某个点
  - 所以，这就需要优化每个流程，每个流程块要重复录入多个点信息，来判断是否处于某种状态，如果是则点击。这样用多点信息来定义一个状态，增加了准确性。
  - pro_color：状态颜色点位
  - pro_click：状态颜色对应后，点击的点位
  - pro_cc：既是颜色点位，又是识别后的点击点位

- [x] 实现暂停功能：20210208

- [x] 第一次打开软件时弹框警告，显示以下信息：20210208
  
  ```
  致软件使用者：
      本软件作者：李英俊小朋友。（给点尊重，认真读一下，就弹这一次）
      1. 本软件不是无脑使用的软件，有学习门槛，不是基于图片识别而是基于自己想法的软件，
         不保证以后不使用图片识别、人工智能等技术。本软件注重于学习编程，而不是鼓励大家
         去用脚本来打破游戏平衡，降低自己和他人的游戏体验。
      2. 本软件仅供学习参考，不允许用于任何商业用途。使用该脚本造成任何后果与本人无关。
      3. 本软件不收取任何费用，如果你是付钱获取的，那么你可真的憨批。
      4. 发现任何bug可以通过github或者csdn留言给我。
         https://github.com/TinyHandsome/FxxkOnmyoji
      5. 献给所有为了梦想的人们/阴阳师们。
  ```
  
- [x] 使用新的环境（虚拟）：20210212

  更新requirements.txt
  
- [x] 同一种情况（点击一处多次），算作超时，自动暂停脚本。：20210217

  1. ~~10次/10秒，也就是，10秒中之内触发了十次以上算作超时~~

     这里10次/10秒也太慢了，因为现在设置的检查间隔是1-2秒，所以这个频率不对，改为了5次/10秒 ，这样点击5次的时间是5s-10s，不会超过10s，所以检查：

     - 如果点击5次的时间超过了10秒，即正在正常运行，没问题
     - 如果小于10秒，则是一个流程在一直点，所以算作超时

  2. 比如体力刷完了，次数到上限了，就会一直点屏幕，但是刷不了，避免这样的情况出现。

- [x] 新建功能，融合载入配置：20210223
  
  1. 同名配置（func_name）：取交集；导入没有的，采用初始化的，并需要更新初始化的数据；初始化没有的，~~删除导入的数据~~
  
     ~~更新后，需要配置的流程名-点名，给出提示~~
  
  2. 不同名配置（func_name）：加上初始化的功能信息
  
  3. ~~运行时，若功能多出流程，或者流程中点信息不全，给出警报~~
  
- [x] 修改配置融合的逻辑：20210224
  1. 从 *同名function替换* ，改为 *同名function的同名step替换*
  2. 需要注意的是，如果step中部分点或者没有点是有效的，则不进行替换（这与function有效性检测逻辑不同，function是只要不是所有点无效，就能运行）

- [x] 新增上次打开功能，放在update_config.ini中：20210225

  1. 每次导入配置的时候，根据是否有值，自动定位功能
  2. 没有值，或者功能列表中没有对应的值，则设置第一个
  3. 暂时先做保存最后打开的功能叭，因为有了功能文件合并之后，按不同文件名存储对应的最后打开的功能没有什么意义
  
- [x] logs文件夹自动创建：20210227


- [x] 修改funtions.ini配置逻辑：20210308

  现在直接在section中命名即可
  
- [x] Step步骤参数重制：20210308

  也就是说，-后面跟操作，比如说点击，比如某个其他的step，前面只有识别，后面只有操作。这里不大改，只是添加一项流程操作。

  1. 各个点信息用`-`连接
  2. 一个step中只能有一个c（点击）或m（流程，多位置点击）事件
  3. l和n代表识别的点位

  ```ini
  step1 = 名字@l-n-c_1
  step2 = 名字@l-n-m_1_1_1
  step3 = 名字@lc_1
  ```
  
- [x] 新建菜单功能：20210308

  优化部分按钮位置，移到菜单中去
  
- [x] 界面更新：20210310

  1. 将部分功能放入菜单栏中
  
  2. 过去界面
  
     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210310093920231.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
  
  3. 更新后界面
  
     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210310095547971.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
  
- [x] 绑定文件和功能名，实现导入文件时，自动指定功能名：20210310

  1. 根据文件名绑定该文件最后运行的功能
  2. 若没有，则选默认最后运行的功能
  3. 若没有找到该功能名，选第一个功能

- [x] 修正function实现方式为：20210310

  1. 场景识别
  2. 识别后操作：点击流程、~~滚动~~后点击等
  3. 暂时不搞滚动了，滚动之后再实现

- [x] 修改步骤逻辑：20210310

  1. 步骤变量为step的是线程，识别到了就处理
  2. 步骤变量为proc的是步骤，识别到了就执行，需要关联到对应的step
     要求对应的step里没有点击事件，只有识别事件
  3. 现在这个问题通过新增m点击模式来解决步骤的问题，即流水线点击

- [x] 在最右侧建一个Text，每一行显示步骤：20210311

  1. 步骤没配置完成时，fg=red
  2. 执行到步骤的时候，点亮该步骤，bg=yellow
  3. ~~添加滚动条，显示不全的，通过滚动条查看~~（没必要）
  4. ~~步骤超过边界的时候，定义滚动条到步骤位置~~（暂时没必要）

- [x] 更换功能或载入配置的时候，停止所有正在运行的线程：20210311

- [x] 最新界面更新，加入step状态显示：20210311

  1. 普通：黑色fg
  2. 未配置：红色fg
  3. 正在运行：黄色bg
  
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210312103817902.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)
  
- [x] 优化update_config.ini的执行逻辑：20210312

  1. 运行时检测文件是否存在，不在就创建
  2. 运行时检测section是否都存在，不在就创建
  3. 运行时检测option是否都存在，不在就创建

- [x] 增加重载功能：20210314
  1. 无论是载入还是新的写入，更新了function.ini后，界面中加入更新的点信息
  2. 实现通过修改配置文件的方式，实时添加功能的step信息


### 现有问题 | Problems

-  现有问题：

  1. 无法进行图像识别，需要人工加点

  2. 调整阴阳师位置的时候，可能出现异常，不准确，忽大忽小

     这是因为，阴阳师会自动调整比例，但是设置的时候，长和宽都要设置，所以造成缩放和移动的时候会出现：**一会儿按长调整大小，一会儿按宽调整大小** 的情况。
     
  3. 如果存在快捷键冲突的情况，比如微信的截图快捷键是`ALT + A`，会导致脚本的全局快捷键映射出错，从而所有的快捷键都失效。
  
     如果存在快捷键不能用的情况，请注意查看是否存在快捷键冲突。
  
- **问题跟进：**

  1. `win32gui.MoveWindow`拒绝访问的情况：这是因为你的电脑中阴阳师窗口的权限比代码的权限高，[参考链接](https://www.zhihu.com/question/68342805)，建议直接用cmd的管理员权限运行：
     1. 先进入cmd的管理员打开
     2. cd进入脚本的根目录
     3. `python tk_app.pyw`
  2. 关于设置`python.exe`或者`pythonw.exe`兼容性-以管理员身份运行后，各种报错问题
     1. 基本报错有：双击`.pyw`结尾的会报错，`pip`也会报错。
     2. 这是因为windows无法加载UAC表单来升级特权，[参考链接](https://www.pythonheidong.com/blog/article/464486/f383227e304162f244bb/)


## 联系方式 | Contact Me

<a id='contact'>主要还是留言给我吧，暂时不留电话、QQ、微信啥的。</a>

- :cloud: 我的CSDN：https://blog.csdn.net/qq_21579045
- :snowflake: 我的博客园：https://www.cnblogs.com/lyjun/
- :sunny: 我的Github：https://github.com/TinyHandsome

碌碌谋生，谋其所爱。:ocean:
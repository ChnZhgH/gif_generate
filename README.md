# GIF转换工具

这是一个视频转gif的小工具，基于python实现，无论是Windows还是Mac都能用哦

不过不管是Windows还是Mac，都需要装个anaconda

效果图如下：

![image-20200426175354454](image/README.asset/image-20200426175354454.png)

转换完成后，便可直接下载

![image-20200426175509987](image/README.asset/image-20200426175509987.png)

继续拖拽图片到上传框或点击上传框，可重新上传视频文件。







## 工具使用方法(三种方式)

* 方法1：docker部署(推荐)：

     A. 拷贝源代码至本地：

     ```bash
     git clone https://github.com/ChnZhgH/gif_generate
     cd gif_generate
     ```

     B. 构建docker镜像：

     ```bash
     docker build -t gif:v1 .
     ```
    
     C. 运行docker镜像：
  
     ```bash
     docker run -d --name gif_web -p 8000:8000 gif:v1
     ```
    
     D. 打开浏览器，地址栏输入: localhost:8000，然后尽情使用
  
     E. 后续使用：

     ```bash
     # 不想用了，停止即可：
     docker container stop gif_web
     # 想继续用了，开始即可：
     docker container start gif_web
     # 想删除了，删掉即可：
     docker container rm gif_web
     docker image rm gif:v1
     ```
    
* 方法2：使用conda环境

     A. 拷贝源码至本地：

     ```bash
     git clone https://github.com/ChnZhgH/gif_generate
     cd gif_generate
     ```

     B. 安装项目依赖，并切换conda环境：

     ```bash
     conda env create -f env.yml
     conda activate gif_generate
     ```

     C. 运行该工具

     ```bash
     python manage.py runserver
     ```

     D. 打开浏览器，地址栏输入: localhost:8000，然后尽情使用
     <br/>
     E. 后续要使用都很简单，打开终端输入一下两行命令，然后尽情玩耍：

     ```bash
     conda activate gif_generate
     python manage.py runserver
     ```

    

* 方法三：pip安装(Mac和Linux自带了pip了，Windows需要自行安装python3)

     A. 打开终端，拷贝源码至本地：

     ```bash
     git clone ...
     cd gif_generate
     ```

     B. 使用pip安装项目依赖，不过直接怎么操作，没有虚拟环境了呢

     ```bash
     pip install -r requirements.txt
     ```

     C. 运行该工具

     ```bash
     python manage.py runserver
     ```

     D. 打开浏览器，地址栏输入: localhost:8000，然后尽情使用
     <br/>
     E. 后续只需要运行步骤3的命令即可





## 使用问题汇总：

* 如果你使用命令创建环境失败：

    ```bash
    conda env create -f env.yml
    ```

    那么可执行以下命令去完成环境构建：

    ```bash
    # 创建并进入环境，若显示环境已存在，则直接进入即可
    conda env -n fig_generate
    conda activate fig_generate
    
    # 在环境中安装依赖
    pip install -r requirements.txt
    conda install --channel https://conda.anaconda.org/menpo opencv
    ```
















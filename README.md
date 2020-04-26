# GIF转换工具

这是一个视频转gif的小工具，基于python实现，无论是Windows还是Mac都能用哦

不过不管是Windows还是Mac，都需要装个anaconda

效果图如下：

![image-20200426175354454](image/README.asset/image-20200426175354454.png)

转换完成后，便可直接下载

![image-20200426175509987](image/README.asset/image-20200426175509987.png)

继续拖拽图片到上传框或点击上传框，可重新上传视频文件。







## 工具使用方法

* 拷贝源码至本地：

    ```bash
    git clone ...
    cd gif_generate
    ```

* 安装项目依赖，并切换conda环境：

    ```bash
    conda env create -f env.yml
    conda activate gif_generate
    ```

* 运行该工具

    ```bash
    python manager.py runserver
    ```

* 打开浏览器，地址栏输入: localhost:8000，然后尽情使用











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
    
    # 安装依赖
    pip install -r requirements.txt
    conda install --channel https://conda.anaconda.org/menpo opencv
    ```

    
















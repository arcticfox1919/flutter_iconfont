# flutter_iconfont
> Generate flutter icon from [https://www.iconfont.cn/](https://www.iconfont.cn/)


**文中图片若不显示，请查看[原始链接](https://arcticfox.blog.csdn.net/article/details/90485919)**


[https://www.iconfont.cn/](https://www.iconfont.cn/) 为我们提供了海量的矢量图标资源，在Flutter中使用这些资源也还方便，但是在下载大量资源后，仍然需要手动做一些事情，这不符合程序员能偷懒就偷懒的精神，所以我做了这个简单工具，希望对大家有所帮助。


**使用说明**

1. 使用`git clone git@github.com:arcticfox1919/flutter_iconfont.git` 或者直接download zip文件到本地
2. 进入[iconfont](https://www.iconfont.cn/)网站，选取想要的icon到购物车，最后【下载代码】
![](https://github.com/arcticfox1919/ImageHosting/blob/master/Snipaste_2019-05-23_16-57-40.jpg?raw=true)

3. 将下载的压缩包解压到任意目录，或者解压到`flutter_iconfont`工程的tool目录下，如下图所示。注意，如解压到其他任意目录下，在第4步运行生成工具时，需要传入解压路径
![](https://github.com/arcticfox1919/ImageHosting/blob/master/Snipaste_2019-05-23_18-20-19.jpg?raw=true)

4. 进入tool目录，执行`python generate.py`，生成dart文件。注意，如解压到其他目录，执行时需带上解压的目录 `python generate.py "dir path"`。
  关于Python环境的问题，`generate.py`同时兼容py2和py3，通常Mac os都自带有Python环境，但可能未安装`BeautifulSoup`库，在运行脚本前，可以通过以下命令安装`python -m pip install beautifulsoup4`; Windows用户如从未安装过Python环境，建议直接使用我编译好的[**exe程序**](https://github.com/arcticfox1919/flutter_iconfont/releases)，下载解压后将`generate.exe`拷贝至`tool`目录下点击即可执行。如需要指定资源目录，在tool目录下打开cmd命令行，执行`generate "dir path"`指定下载的icon资源目录

5. 进入lib目录下查看`flutter_iconfont.dart`文件，如下例子所示，将变量修改为适当的名字，这一步很重要，如果在[iconfont](https://www.iconfont.cn/)中搜索的icon资源都是中文名，则生成的变量也是中文名，应修改为英文字母，还应当检查是否存在变量同名情况，确认`IconFonts`类无误即可。建议打开解压资源包中的html文件，对照图标进行变量命名

  ```dart
  class IconFonts{
    IconFonts._();

    static const IconData arrow_down = const IconDataEx(0xe623);
    static const IconData arrow_down = const IconDataEx(0xe61a);
    static const IconData arrow_down = const IconDataEx(0xe776);
    static const IconData Arrow_down = const IconDataEx(0xe62e);
    static const IconData Arrow_down_1 = const IconDataEx(0xe6bd);
    static const IconData Arrow_down_4 = const IconDataEx(0xe6be);
    static const IconData Arrow_down_3 = const IconDataEx(0xe6bf);
    static const IconData Arrow_down_2 = const IconDataEx(0xe6c1);
  }
 
  ```

6. 本地离线库已准备妥当，在项目工程的`pubspec.yaml`中添加本地库即可使用。将 `path` 指向你下载的flutter_iconfont库的实际路径，更新一下yaml配置文件

  ```
  dependencies:
    flutter_iconfont:
      path: F:\git_code\flutter_iconfont
  ```

7. 代码使用
  ```dart
  import 'package:flutter_iconfont/flutter_iconfont.dart';
  
  return Center(child:Icon(IconFonts.Arrow_down))
  ```
  

# flutter_iconfont
> Generate flutter icon from [https://www.iconfont.cn/](https://www.iconfont.cn/)


[https://www.iconfont.cn/](https://www.iconfont.cn/) 为我们提供了海量的矢量图标资源，Flutter中使用的时候也还方便，但是在下载大量资源后，仍然需要手动做一些事情，这不符合程序员能偷懒就偷懒的精神，所以我做了这个简单工具，希望对大家有所帮助。


**使用说明**

1. 使用`git clone` 或者直接download zip文件到本地
2. 进入[iconfont](https://www.iconfont.cn/)网站，选取想要的icon到购物车，最后【下载代码】
3. 将下载的压缩包解压到任意目录，或者解压到`flutter_iconfont`工程的tool目录下
4. 进入tool目录，执行`python generate.py`，生成dart文件，进入lib目录下查看`flutter_iconfont.dart`文件，如下例子所示，将变量修改为适当的名字，这一步很重要，如果在[iconfont](https://www.iconfont.cn/)中搜索的icon资源都是中文名，则生成的变量也是中文名，应修改为英文字母，还应当检查是否存在变量同名情况，确认`IconFonts`类无误即可。建议打开解压资源包中的html文件，对照图标进行变量命名

  ```
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

5. 本地离线库已准备妥当，在项目工程的`pubspec.yaml`中添加本地库即可使用。将 `path` 指向你下载的flutter_iconfont库的实际路径，更新一下yaml配置文件

  ```
  dependencies:
    flutter_iconfont:
      path: F:\git_code\flutter_iconfont
  ```

6. 代码使用
  ```
  import 'package:flutter_iconfont/flutter_iconfont.dart';
  
  return Center(child:Icon(IconFonts.Arrow_down))
  ```

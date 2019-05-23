library flutter_iconfont;

import 'package:flutter/widgets.dart';

class IconDataEx extends IconData {
  const IconDataEx(int codePoint)
      : super(
    codePoint,
    fontFamily: 'IconFont',
    fontPackage: 'flutter_iconfont',
  );
}

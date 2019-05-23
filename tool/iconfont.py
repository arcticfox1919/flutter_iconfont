from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import open
from builtins import str
from future import standard_library
standard_library.install_aliases()
from bs4 import BeautifulSoup
from pathlib import Path,PurePath
import shutil, sys

template= '''
library flutter_iconfont;

import 'package:flutter/widgets.dart';
import 'flutter_icon_data.dart';

class IconFonts{{
    IconFonts._();

{code}
}}
'''


def get_filepath(res_path, pattern):
    tmp = list(res_path.rglob(pattern))
    if tmp:
        return tmp[0]
    else:
        raise Exception("There are no %s files in the directory %s" % (pattern, str(res_path)))


def html_parse(html_path):
    with Path.open(html_path,encoding='utf-8') as f:
        bs = BeautifulSoup(f.read(),'html.parser')
        icon_list = bs.select("div[class='content unicode'] > ul > li[class='dib']")
        r = []
        if icon_list:
            for el in icon_list:
                name = el.select("div[class='name']")[0].string
                code = el.select("div[class='code-name']")[0].string[:-1].replace('&#','0')
                r.append('''    static const IconData {0} = const IconDataEx({1});'''.format(name, code))
        else:
            raise Exception("%s file parsing failed" % html_path)
        return r



if __name__ == "__main__":
    if len(sys.argv) > 1:
        res_path = Path(sys.argv[1])
        if not res_path.exists():
            raise Exception("%s path does not exist" % res_path)
    else:
        res_path = Path().cwd()

    print(res_path)
    root = Path().cwd().parent
    dart_path = root.joinpath('lib')
    

    ttf_path = get_filepath(res_path, '*.ttf')
    shutil.copy2(ttf_path, root.joinpath('fonts'))

    html_path = get_filepath(res_path, '*.html')
    data = html_parse(html_path)

    with open(dart_path.joinpath("flutter_iconfont.dart"), "w", encoding='utf-8') as f:
        f.write(template.format(code='\n'.join(data)))

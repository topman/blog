# coding: utf-8
"""
Script to create a skeleton for the new blog post, which includes the following parts:

1. summary
2. body
3. reference
"""

SKELETON = \
"""%(title)s

.. TAGS:

摘要
======

正文
======

总结
=========

下载原文
===========
可从 `此处 <%(download_url)s>`_ 查看或者下载。 

参考资料
===========


"""

import os
PATH = os.path.abspath(os.path.dirname(__file__))

class Helper(object):
    def __init__(self, path):
        self.input = path
        self.path = os.path.join(PATH, path)
        self.title = path.split("/")[-1]
        self.infile = self.path + ".rst"

    @classmethod
    def is_already_existing(self, path):
        import os
        return os.path.exists(path + ".rst")

    def write_file(self):
        fh = open(self.infile, "w")
        t = "=" * len(self.title)
        title = "%s\n%s\n%s" % (t, self.title, t)
        data = {
            "title" : title,
            "download_url" : "https://github.com/topman/blog/tree/master/%s" % self.title + ".rst",
        }
        cont = SKELETON % data
        fh.write(cont)
        fh.close()
        print "The generated new post is %s" % self.path + ".rst"


    @classmethod
    def handle_arg(cls):
        import optparse
        usage = """\
        python make_skeleton.py [infile]
        """
        parser = optparse.OptionParser(usage=usage)
        (options, args) = parser.parse_args()
        if len(args) != 1:
            parser.print_help()
            parser.exit(msg="\nNeed ONE argument as the path of the new post(No .rst append)\n")
        _path = args[0]
        path = os.path.join(PATH, _path)
        if cls.is_already_existing(path):
            parser.exit(msg="\nThe path provided already exists. Try another one!\n")
        return _path

if __name__ == "__main__":
    path = Helper.handle_arg()
    a = Helper(path)
    a.write_file()


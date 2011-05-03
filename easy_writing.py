# coding: utf-8
"""
Script to ease the writing of blogs using restructuredText format.
It will:

1. extract the link with `link`_ style and append the link to the end of the file
   e.g. I'm reading a `book`_. And the script will append .. _book: to the end of the file
2. build the links database by adding a new link(i.e if a link not in the links database, 
   will be added to the database)
3. when appending the link to the end of the file in step 1, the script will try to find the
   corresponding link in the step 2's links database
"""

class Helper(object):
    EXTRACT_MARKS_RE = r"`([^`<]+)`_"

    def __init__(self):
        pass

    def get_content(self, infile):
        fh = open(infile)
        cont = fh.read()
        fh.close()
        return cont

    def extract(self, infile):
        """Extract the marks and return a list with the
        catched words
        """
        out = []
        import re
        cont = self.get_content(infile)
        matches = re.findall(self.EXTRACT_MARKS_RE, cont)
        return list(set(matches))

    def extract_links(self, infile):
        MARKS_RE = r".. _([^:]+):[ ]+([^\s]+)"
        import re
        cont = self.get_content(infile)
        matches = re.findall(MARKS_RE, cont)
        return list(set(matches))

    def write_content(self, outfile, cont):
        fh = open(outfile, "w")
        fh.write(cont)
        fh.close()

    def handle_links(self, infile):
        links = self.extract(infile)
        try:
            from links_database import LINKS
        except ImportError:
            LINKS = {}
        out = {}
        for link in links:
            value = ""
            if link in LINKS:
                value = LINKS.get(link)
            out.update({ link : value })
        cont = ""
        tpl = "\n.. _%s: %s"
        for k, v in out.iteritems():
            cont += tpl % (k, v)
        content = self.get_content(infile)
        content += cont
        self.write_content(infile, content)

    def build_database(self, dirname=None, suffix="rst"):
        """Build the links database by searching all the files
        with the specified suffix recursively.

        if dirname is None, then find the current directory
        """
        DB_NAME = "links_database.py"
        import os
        dirname = os.getcwd() if dirname is None else dirname

        for obj in os.listdir(dirname):
            curobj = os.path.join(dirname, obj)
            if os.path.isdir(curobj):
                self.build_database(curobj, suffix)
            elif curobj.split(".")[-1] == suffix:
                # update the database
                try:
                    fh = open(DB_NAME)
                    old = fh.read()
                    fh.close()
                    exec(old)
                except IOError:
                    LINKS = {}
                matches = self.extract_links(curobj)
                for m in matches:
                    link_name = m[0]
                    link = m[1]
                    if link in ["http://", "https://"]:
                        continue
                    if link_name not in LINKS:
                        key = u"%s" % link_name.decode("utf-8")
                        LINKS.update({ key : link })
                from django.utils import simplejson
                tpl = """# coding: utf-8\nLINKS = %s"""
                new = tpl % simplejson.dumps(LINKS, indent=4, ensure_ascii=False)
                new = new.encode("utf-8")
                fh = open(DB_NAME, "w")
                fh.write(new)
                fh.close()

    def handle_arg(self):
        import optparse
        usage = """\
        python easy_writing.py [infile]

        if infile is a string equals to "build" exactly,
        the script will rebuild the links database instead.
        """
        parser = optparse.OptionParser(usage=usage)
        (options, args) = parser.parse_args()
        if len(args) != 1:
            parser.print_help()
            parser.exit(msg="\nNeed ONE argument as the infile\n")
        return args[0]


if __name__ == "__main__":
    a = Helper()
    infile = a.handle_arg()
    if infile == "build":
        a.build_database()
    else:
        a.handle_links(infile)

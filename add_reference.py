#coding: utf-8
"""
Script to add reference which are extracted from the infile
and will append to the bottom of the rst file.
"""

class Reference(object):
    def __init__(self, infile):
        self.infile = infile

    def add_reference(self):
        from easy_writing import Helper as LinkHelper
        a = LinkHelper()
        links = a.extract(self.infile)
        append = "\n\n"
        i = 1
        for link in links:
            append += "%s. `%s`_ \n" % (str(i), link)
            i += 1
        fh = open(self.infile, "r")
        cont = fh.read()
        fh.close()
        cont += append
        fh = open(self.infile, "w")
        fh.write(cont)
        fh.close()
        print "Done."

    @classmethod
    def handle_arg(cls):
        import optparse
        usage = """\
        python add_reference.py [infile]
        """
        parser = optparse.OptionParser(usage=usage)
        (options, args) = parser.parse_args()
        if len(args) != 1:
            parser.print_help()
            parser.exit(msg="\nNeed ONE argument as the path to handle\n")
        return args[0]

if __name__ == "__main__":
    # add reference
    path = Reference.handle_arg()
    a = Reference(path)
    a.add_reference()

    # add links
    from easy_writing import Helper 
    b = Helper()
    b.handle_links(path)

    

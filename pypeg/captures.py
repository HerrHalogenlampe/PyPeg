

class Capture(object):
#possible refactor: inherit by kind, may or may not be useful

    SIMPLEKIND = 0
    POSITIONKIND = 1
    OPENSTATUS = 0
    FULLSTATUS = 1

    def __init__(self, status=-1, kind=-1, size=-1, index=-1):
        self.status = status  # "open" or "full"
        self.kind = kind  # "simple" or "position" (more in the future)
        self.size = size
        self.index = index

    def __repr__(self):
        return str(self)

    def __str__(self):
        return(self.status + "capture " + self.kind
               + " size:"+str(self.size) + "index: " + str(self.index))

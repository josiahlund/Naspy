from BULKDATA.BulkDataEntry import BulkDataEntry


class Ctria3(BulkDataEntry):
    instances = []
    def __init__(self, EID, PID, G1, G2, G3, THETA, ZOFFS, blank, *args):
        self.EID = int(EID)
        self.PID = int(PID)
        self.G = [G1, G2, G3]
        try:
            self.THETA = float(THETA)
        except ValueError:
            self.THETA = 0.0

        try:
            self.ZOFFS = float(ZOFFS)
        except ValueError:
            self.ZOFFS = 0.0

        try:
            self.TFLAG = int(args[0])
        except IndexError:
            self.TFLAG = 0

        self.T = [t for t in args[1:3]]
        if not self.T:
            self.T = [-1.0, -1.0, -1.0]

        try:
            self.MCID = int(THETA)
        except ValueError:
            self.MCID = -1

        self.entry_count = 8
        self.h5_path = "/NASTRAN/INPUT/ELEMENT/CTRIA3"
        self.dtype = [("EID", int),
                      ("PID", int),
                      ("G", float, 3),
                      ("THETA", float),
                      ("ZOFFS", float),
                      ("TFLAG", int),
                      ("T", float, 3),
                      ("MCID", int)]
        Ctria3.instances.append(self)

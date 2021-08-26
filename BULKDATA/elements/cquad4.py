from BULKDATA.BulkDataEntry import BulkDataEntry


class Cquad4(BulkDataEntry):
    instances = []
    def __init__(self, EID, PID, G1, G2, G3, G4, THETA, ZOFFS, *args):
        self.EID = int(EID)
        self.PID = int(PID)
        self.G = [G1, G2, G3, G4]
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

        self.T = [t for t in args[1:4]]
        if not self.T:
            self.T = [-1.0, -1.0, -1.0, -1.0]

        try:
            self.MCID = int(THETA)
        except ValueError:
            self.MCID = -1

        self.entry_count = 8
        self.h5_path = "/NASTRAN/INPUT/ELEMENT/CQUAD4"
        self.dtype = [("EID", int),
                      ("PID", int),
                      ("G", float, 4),
                      ("THETA", float),
                      ("ZOFFS", float),
                      ("TFLAG", int),
                      ("T", float, 4),
                      ("MCID", int)]
        Cquad4.instances.append(self)

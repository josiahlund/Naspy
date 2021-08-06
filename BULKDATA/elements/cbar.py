from BULKDATA.BulkDataEntry import BulkDataEntry


class Cbar(BulkDataEntry):
    def __init__(self, EID, PID, GA, GB, X1, X2, X3, OFFT, *args):
        self.EID = int(EID)
        self.PID = int(PID)
        self.GA = int(GA)
        self.GB = int(GB)
        self.FLAG = 1
        try:
            self.X1 = float(X1)
            self.X2 = float(X2)
            self.X3 = float(X3)
            self.G0 = 0
        except ValueError:
            self.X1 = 0.0
            self.X2 = 0.0
            self.X3 = 0.0
            self.G0 = int(X1)

        try:
            self.PA = int(args[0])
            self.PB = int(args[1])
        except ValueError:
            self.PA = 0
            self.PB = 0

        self.W1A, self.W2A, self.W3A, self.W1B, self.W2B, self.W3B = args[2:]
        self.entry_count = 17
        self.h5_path = "/NASTRAN/INPUT/ELEMENT/CBAR"
        self.dtype = [("EID", int),
                      ("PID", int),
                      ("GA", int),
                      ("GB", int),
                      ("FLAG", int),
                      ("X1", float),
                      ("X2", float),
                      ("X3", float),
                      ("G0", int),
                      ("PA", int),
                      ("PB", int),
                      ("W1A", float),
                      ("W2A", float),
                      ("W3A", float),
                      ("W1B", float),
                      ("W2B", float),
                      ("W3B", float)]

registry = {}


def register(cls):
    registry[cls.__name__.upper()] = cls
    return cls


@register
class Cbar:
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
            self.PA, self.PB = int(args[0]), int(args[1])
        except (IndexError, ValueError):
            self.PA, self.PB = 0, 0

        try:
            self.W1A, self.W2A, self.W3A, self.W1B, self.W2B, self.W3B = args[2:]
        except ValueError:
            self.W1A, self.W2A, self.W3A, self.W1B, self.W2B, self.W3B = [0.0] * 6
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


@register
class Cquad4:
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


@register
class Ctria3:
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


@register
class Grid:
    def __init__(self, ID, CP, X1, X2, X3, CD, PS, SEID):
        self.ID = int(ID)
        self.CP = int(CP) if CP != "" else 0
        self.X = [float(X1), float(X2), float(X3)]
        self.CD = int(CD) if CD != "" else 0
        self.PS = int(PS) if PS != "" else 0
        self.SEID = int(SEID) if SEID != "" else 0
        self.entry_count = 6
        self.h5_path = "/NASTRAN/INPUT/NODE/GRID"
        self.dtype = [("ID", int),
                      ("CP", int),
                      ("X", float, 3),
                      ("CD", int),
                      ("PS", int),
                      ("SEID", int)]


"""
@register
class Eigrl:
    def __init__(self, SID, V1, V2, ND, MSGLVL, MAXSET, SHFSCL, NORM, *args):
        self.SID = int(SID)
        self.V1 = float(V1) if V1 else 0.0
        self.V2 = float(V2) if V2 else 0.0
        try:
            self.ND = int(ND)
        except ValueError:
            self.ND = 0
        self.MSGLVL = int(MSGLVL) if MSGLVL else 0
        self.MAXSET = int(MAXSET) if MAXSET else 0
        self.SHFCSL = float(SHFSCL) if SHFSCL else 0.0
        self.FLAG1 = 0
        self.FLAG2 = 0
        self.NORM = NORM if NORM else "MASS"
        self.entry_count = 10
        self.h5_path = "/NASTRAN/INPUT/DYNAMIC/EIGRL/IDENTITY"
        self.dtype = [("SID", int),
                      ("V1", float),
                      ("V2", float),
                      ("ND", int),
                      ("MSGLVL", int),
                      ("MAXSET", int),
                      ("SHFCSL", float),
                      ("FLAG1", int),
                      ("FLAG2", int),
                      ("NORM", "S8")]
"""

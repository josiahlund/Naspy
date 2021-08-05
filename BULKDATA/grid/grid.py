from BULKDATA.BulkDataEntry import BulkDataEntry


class Grid(BulkDataEntry):
    def __init__(self, ID, CP, X1, X2, X3, CD, PS, SEID):
        self.ID = int(ID)
        self.CP = int(CP) if CP != "" else 0
        self.X1 = X1
        self.X2 = X2
        self.X3 = X3
        self.CD = int(CD) if CD != "" else 0
        self.PS = PS
        self.SEID = int(SEID) if SEID != "" else 0
        self.h5_path = "/NASTRAN/INPUT/NODE/GRID"
        self.dtype = [("ID", "int"),
                      ("CP", "int"),
                      ("X1", "float"),
                      ("X2", "float"),
                      ("X3", "float"),
                      ("CD", "int"),
                      ("PS", "S8"),
                      ("SEID", "int")]

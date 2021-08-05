from BULKDATA.BulkDataEntry import BulkDataEntry


class Grid(BulkDataEntry):
    def __init__(self, ID, CP, X1, X2, X3, CD, PS, SEID):
        self.ID = int(ID)
        self.CP = int(CP) if CP != "" else 0
        self.X = [X1, X2, X3]
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

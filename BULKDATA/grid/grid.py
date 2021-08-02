from BULKDATA.BulkDataEntry import BulkDataEntry


class Grid(BulkDataEntry):
    def __init__(self, ID, CP, X1, X2, X3, CD, PS, SEID):
        self.ID = ID
        self.CP = CP
        self.X1 = X1
        self.X2 = X2
        self.X3 = X3
        self.CD = CD
        self.PS = PS
        self.SEID = SEID

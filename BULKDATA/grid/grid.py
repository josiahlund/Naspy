from BULKDATA.BulkDataEntry import BulkDataEntry


class Grid(BulkDataEntry):
    # Tracking instances as shown in https://stackoverflow.com/questions/12101958/how-to-keep-track-of-class-instances
    # Use of weakref/WeakSet is another option which may be necessary as things evolve.
    instances = []

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
        Grid.instances.append(self)

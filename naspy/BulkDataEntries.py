# class Eigrl:
#     def __init__(self, SID, V1, V2, ND, MSGLVL, MAXSET, SHFSCL, NORM, *args):
#         self.SID = int(SID)
#         self.V1 = float(V1) if V1 else 0.0
#         self.V2 = float(V2) if V2 else 0.0
#         try:
#             self.ND = int(ND)
#         except ValueError:
#             self.ND = 0
#         self.MSGLVL = int(MSGLVL) if MSGLVL else 0
#         self.MAXSET = int(MAXSET) if MAXSET else 0
#         self.SHFCSL = float(SHFSCL) if SHFSCL else 0.0
#         self.FLAG1 = 0
#         self.FLAG2 = 0
#         self.NORM = NORM if NORM else "MASS"
#         self.entry_count = 10
#         self.h5_path = "/NASTRAN/INPUT/DYNAMIC/EIGRL/IDENTITY"
#         self.dtype = [("SID", int),
#                       ("V1", float),
#                       ("V2", float),
#                       ("ND", int),
#                       ("MSGLVL", int),
#                       ("MAXSET", int),
#                       ("SHFCSL", float),
#                       ("FLAG1", int),
#                       ("FLAG2", int),
#                       ("NORM", "S8")]

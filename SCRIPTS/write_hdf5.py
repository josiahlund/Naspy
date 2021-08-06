import h5py
import numpy as np


def write_hdf5(path: str, bulk_data_entries: dict):
    hdf5 = h5py.File(path, mode="w")
    # SCHEMA is the Nastran version.
    schema_value = 1
    hdf5.attrs.create("SCHEMA", [schema_value], dtype="int64")
    for key, value in bulk_data_entries.items():
        where = value[0].h5_path
        dtype = value[0].dtype + [("DOMAIN_ID", int)]
        count = value[0].entry_count
        sort_by = list(value[0].__dict__.keys())[0]
        data = [(tuple(card.__dict__.values())[:count] + (1,)) for card in bulk_data_entries[key]]
        cards = np.sort(np.array(data, dtype=dtype), order=sort_by)
        table = hdf5.create_dataset(where, data=cards, dtype=dtype)
        table.attrs.create("version", [0], dtype="int64")
    hdf5.close()

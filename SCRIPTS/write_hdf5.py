import tables
import numpy as np


def write_hdf5(path: str, bulk_data_entries: dict):
    hdf5 = tables.open_file(filename=path, mode="w", driver="H5FD_CORE")
    for key, value in bulk_data_entries.items():
        where = value[0].h5_path
        make_nodes(hdf5, where)
        dtype = value[0].dtype
        data = [(tuple(card.__dict__.values())[:8]) for card in bulk_data_entries[key]]
        cards = np.array(data, dtype=dtype)
        hdf5.create_table(where=where, name=key.upper(), obj=cards)
    hdf5.close()


def make_nodes(hdf5, where):
    nodes = where.split('/')
    node_paths = ["/".join(nodes[0:i + 1]) for i in range(len(nodes))][1:]
    for node in node_paths:
        if node not in hdf5:
            node_name = [n for n in nodes if n and node.endswith(n)][0]
            node_path = node[:len(node) - len(node_name)]
            hdf5.create_group(where=node_path, name=node_name)

from cassandra.cluster import Cluster

if __name__ == "__main__":
    cluster = Cluster(['104.197.222.72 '])
    session = cluster.connect('nano',wait_for_all_pools=True)
    session.execute('USE nano')
    rows = session.execute('SELECT * FROM measures')
    for row in rows:
        print(row.measures)
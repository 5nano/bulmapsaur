from cassandra.cluster import Cluster

def insert(idTest, idPlant, measures): #example of use insert(2,2,'{"leadArea":9.75}')
    cluster = Cluster(['104.197.222.72'])
    session = cluster.connect('nano',wait_for_all_pools=True)
    session.execute('USE nano')
    session.execute('insert into measures(id_test,id_plant,time,measures) values(%s,%s,dateOf(now()),%s)', (idTest,idPlant,measures))

from cassandra.cluster import Cluster

def insert(idTest, idPlant, measures, image):
    cluster = Cluster(['104.197.222.72'])
    session = cluster.connect('nano',wait_for_all_pools=True)
    session.execute('USE nano')
    id_test = int(idTest)
    id_plant = int(idPlant)
    session.execute('insert into measures(id_test,id_plant,time,measures,image) values(%s,%s,dateOf(now()),%s,%s)', (id_test,id_plant,str(measures),str(image)))

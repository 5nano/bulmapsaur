from cassandra.cluster import Cluster
from datetime import datetime

def insert(idTest, idPlant, measures, image):
    cluster = Cluster(['104.197.222.72'])
    session = cluster.connect('nano',wait_for_all_pools=True)
    session.execute('USE nano')
    timeNow = datetime.now()
    id_assay = int(idTest)
    id_experiment = int(idPlant)
    try:
        session.execute('insert into measures(id_assay,id_experiment,time,measures) values(%s,%s,%s,%s)', (id_assay,id_experiment,timeNow,str(measures)))
    except:
        print("could not insert measures")
    else:
        session.execute_async('insert into images(id_assay,id_experiment,time,image) values(%s,%s,%s,%s)',(id_assay, id_experiment, timeNow, str(image)))


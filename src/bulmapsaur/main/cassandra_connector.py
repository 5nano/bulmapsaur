from cassandra.cluster import Cluster
from datetime import datetime

def insert(idAssay, idExperiment, measures, image, optionalTime):
    cluster = Cluster(['104.197.222.72'])
    session = cluster.connect('nano',wait_for_all_pools=True)
    session.execute('USE nano')
    if optionalTime is None:
        timeNow = datetime.now()
    else:
        timeNow = datetime.strptime(optionalTime, '%Y-%m-%d %H:%M:%S.%f')
        print(timeNow)
    id_assay = int(idAssay)
    id_experiment = int(idExperiment)
    session.execute('insert into measures(id_assay,id_experiment,time,measures,image) values(%s,%s,%s,%s,%s)', (id_assay,id_experiment,timeNow,str(measures), str(image)))
    #session.execute_async('insert into images(id_assay,id_experiment,time,image) values(%s,%s,%s,%s)',(id_assay, id_experiment, timeNow, str(image)))

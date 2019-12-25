from .models import Data
from datetime import datetime, timezone

from django.utils.timezone import utc

def get_time_diff(data):
    if data.updated_at:
        now = datetime.utcnow().replace(tzinfo=utc)
        timediff = now - data.updated_at
        return timediff.total_seconds()/60

def background_process():
    import time
    while True:
        
        dataset = Data.objects.all()

        for data in dataset:
            if(get_time_diff(data)>=5.0):
                data.delete()
                print('Data Deleted')
        #print(get_time_diff(data))

        time.sleep(3)
        print('Process Finished')



def update_ttl(data):
    data.uploaded_at = datetime.now()
    data.save()







''' Demo Code to run it 
def task():
            import threading
            t = threading.Thread(target=background_process, args=(), kwargs={})
            t.setDaemon(True)
            t.start()
        task()


'''
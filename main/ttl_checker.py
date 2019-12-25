from .models import Data
from datetime import datetime, timezone
import time
from django.utils.timezone import utc

MAX_TIME_OUT = 5.0


def get_time_diff(data):
    if data.updated_at:
        now = datetime.utcnow().replace(tzinfo=utc)
        timediff = now - data.updated_at
        return timediff.total_seconds()/60

def background_process():
    while True:
        dataset = Data.objects.all()

        for data in dataset:
            print(get_time_diff(data))
            if(get_time_diff(data)>=MAX_TIME_OUT):
                data.delete()
                print('Data Deleted')

        time.sleep(5)
        print('Background iteration completed')



def update_ttl(data):
    data.uploaded_at = datetime.now()
    data.save()


def update_all_ttl():
    Data.objects.all().update(updated_at = datetime.utcnow().replace(tzinfo=utc))





''' Demo Code to run it 
def task():
            import threading
            t = threading.Thread(target=background_process, args=(), kwargs={})
            t.setDaemon(True)
            t.start()
        task()


'''
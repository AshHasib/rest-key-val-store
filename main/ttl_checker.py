from .models import Data
from datetime import datetime, timezone
import time
from django.utils.timezone import utc


MAX_TIME_OUT = 5.0

def background_process():
    print('Background TTL process running...')
    
    while True:
        dataset = Data.objects.all()
        if not dataset.count() == 0:
            for data in dataset:
                print('Time elapsed for {} = {}'.format(data,get_time_diff(data)))
                if(get_time_diff(data)>=MAX_TIME_OUT):
                    print('{} Deleted'.format(data))
                    data.delete()
            print('--------------------------------------------------')
        time.sleep(5)



def update_ttl(data):
    data.uploaded_at = datetime.now()
    data.save()


def update_all_ttl():
    Data.objects.all().update(updated_at = datetime.utcnow().replace(tzinfo=utc))


def get_time_diff(data):
    if data.updated_at:
        now = datetime.utcnow().replace(tzinfo=utc)
        timediff = now - data.updated_at
        return timediff.total_seconds()/60


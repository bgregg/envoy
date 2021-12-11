import redis
import shutil
import yaml

r = redis.Redis(host='localhost', port=6379)
stats = shutil.disk_usage("/")
percentage = stats.used / stats.total

with open('/code/front-envoy.yaml') as f:
    dict = yaml.full_load(f)
    print(dict)

key = '79'

r.set(key, round(percentage * 100, 2))

import redis
conn = redis.Redis()
print('Washer is starting')
dishes = ['salad', 'bread', 'entree', 'dessert']
for dish in dishes:
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    print('Washed', dish)
conn.rpush('dishes', 'quit')
while True:
    dish = conn.rpop('dishes')
    print('In Queue', dish)
    if dish is None:
        break
print('Washer is done')

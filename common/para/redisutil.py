import redis


class redisdata:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def setred(self,key,value):
        self.r.set(key,value)


    def getred(self,key):
        return self.r.get(key)

    def delred(self,key):

        self.r.delete(key)
if __name__ == '__main__':
    redi = redisdata()
    print(redi.getred("Authorization"))
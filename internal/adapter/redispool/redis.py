import redis 


class RedisPool:

    def __init__(self, config: dict):
        self.host = config.get("host", "localhost")
        self.port = config.get("port", 6379)
        self.password = config.get("password",None)
        self.db = config.get("database",0)
        self.user = config.get("user")
        self.idleTimeout = self._parseTimeout(config.get("idleTimemout","200s"))
    
    def _parseTimeout(self, time: str) -> float:
        if time.endswith("s"):
            return float(time[:-1])
        elif time.endswith("m"):
            return float(time[:-1])*60
        elif time.endswith("h"):
            return float(time[:-1])*3600
    
    def Client(self) -> redis.Redis:
        pool = redis.ConnectionPool(
            host=self.host,
            port=self.port,
            password= self.password,
            socket_timeout= self.idleTimeout,
            db=self.db,
            decode_responses= True
        )

        return redis.Redis(connection_pool=pool)
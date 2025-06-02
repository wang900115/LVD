import yaml
from dataclasses import dataclass
from typing import Any

@dataclass
class AppSettings:
    run_mode: str
    cancel_timeout: str

@dataclass
class ServerSettings:
    host: str
    http_port: int
    read_header_timeout: str

@dataclass
class MySQLSettings:
    host: str
    port: int
    user: str
    password: str
    name: str
    debug: bool

@dataclass
class RedisSettings:
    host: str
    port: int
    user: str
    password: str
    database: int
    idleTimeout: str

@dataclass
class LogSettings:
    log_path: str
    application_name: str
    debug: bool
    level: str

@dataclass
class JwtSettings:
    expiration: str

class AppConfig:

    def __init__(self, path: str):
        with open(path, 'r') as f:
            raw: dict[str, Any] = yaml.safe_load(f)

        self.app = AppSettings(**raw.get("app",{})).__dict__
        self.server = ServerSettings(**raw.get("server",{})).__dict__
        self.mysql = MySQLSettings(**raw.get("mysql",{})).__dict__
        self.redis = RedisSettings(**raw.get("redis",{})).__dict__
        self.log = LogSettings(**raw.get("log",{})).__dict__
        self.jwt = JwtSettings(**raw.get("jwt",{})).__dict__
        



import logging
import os

import redis

# redcli = redis.Redis(unix_socket_path='redis.sock', password='spiir')
# sub = redcli.pubsub()
# sub.subscribe('trigger_control')
# for message in sub.listen(): \
#     print(message.get('data'))"

logger = logging.getLogger(__name__)


def read_redis_conf(conf_path, delimiter: str = " "):
    """Function to read a basic redis.conf file.

    This function can handle comments but will fail to parse quoted "#" characters.
    Duplicate keys will be overwritten with the latest key value pair.

    Parameters
    ----------
        conf_path: str
            The path to a given redis configuration file (e.g. "redis.conf")
        delimiter: str
            The str character used to delimit key value pairs.

    Returns
    -------
        dict
            The redis configuration data as a dictionary.
    """
    try:
        config = {}
        logging.debug(f"Reading redis.conf from {conf_path}")
        with open(conf_path, mode="r") as file:
            for line in file:
                line = line.partition("#")[0].rstrip()
                if len(line) != 0:
                    key, value = line.split(delimiter, 1)
                    config[key] = value
        return config
    except IOError as exc:
        raise exc


def connect_to_redis_unixsocket(conf_path):
    """Constructs a Redis unixsocket connection client given a redis.conf file path.

    Parameters
    ----------
        conf_path: str
            The path to the redis.conf file

    Returns
    -------
        redis.client.Redis
            A Redis client via unixsocket as defined in the redis.conf file.

    """
    # get redis configuration as dictionary
    redis_conf = read_redis_conf(conf_path)

    # build unix socket path
    if redis_conf["unixsocket"].startswith("/"):
        unix_socket_path = redis_conf["unixsocket"]
    else:
        # assume redis.conf and unixsocket files are stored together
        unix_socket_path = os.path.abspath(os.path.join(os.path.dirname(conf_path), redis_conf["unixsocket"]))
    logger.debug(f"Reading Redis unixsocket file from {unix_socket_path}")
    if not os.path.exists(unix_socket_path):
        raise IOError("Redis unix socket file at %s does not exist." % unix_socket_path)

    # build redis connection arguments
    redis_args = {}
    redis_args["unix_socket_path"] = unix_socket_path
    if "requirepass" in redis_conf:
        redis_args["password"] = redis_conf["requirepass"]

    # logging.info(redis_args)
    return redis.Redis(**redis_args)

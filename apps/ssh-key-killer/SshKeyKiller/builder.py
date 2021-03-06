# -*- coding: utf-8 -*-
from datetime import datetime

from .authorized_keys import AuthorizedKeys
from .logger import logger
from .utils import load_config, scan_authorized_keys


class :
    """
    Killer remove the expired authorized pub keys.
    """
    def __init__(self, configfile):
        self.config = load_config(configfile)

    def get_invalid_hosts(self):
        """
        return the expired pub keys.
        """
        invalid_pub_key = []
        for host in self.config.get("hosts"):
            if datetime.strptime(str(host.get("expire_date")), "%Y%m%d") < datetime.now():
                invalid_pub_key.append(host.get("pub_key"))
        return invalid_pub_key

    def invalid(self):
        """
        remove invalid pub keys from authorized_keys.
        """
        authorized_keys_files = scan_authorized_keys()
        invalid_pub_key = self.get_invalid_hosts()
        for file in authorized_keys_files:
            ak = AuthorizedKeys(file)
            for pub_key in ak.data:
                if pub_key in invalid_pub_key:
                    ak.invalid(pub_key)
                    logger.info("invalid host {}".format(pub_key))
            ak.save()

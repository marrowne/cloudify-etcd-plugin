# Standard imports
from uuid import uuid4

# Third party imports
import etcd3

# Py2/3 compatibility
# from etcd_sdk._compat import text_type


class ExampleException(Exception):
    pass


class EtcdResource(object):
    resource_type = None

    def __init__(self, client_config, resource_config=None, logger=None):
        self.client_config = client_config
        self.logger = logger
        self.connection = etcd3.client(**client_config)
        self.config = resource_config or {}
        self.name = self.config.get('name', None)
        self.resource_id = self.config.get('id', None) or uuid4()

    def __str__(self):
        return self.name or self.resource_id

    def create(self):
        raise NotImplementedError()

    def list(self):
        raise NotImplementedError()

    def get(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()

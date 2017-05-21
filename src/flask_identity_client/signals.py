# coding: UTF-8

from flask.signals import Namespace

__all__ = ['update_service_account']


ns = Namespace()
update_service_account = ns.signal('update-service-account')

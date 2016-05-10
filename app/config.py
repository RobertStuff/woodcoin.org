import os

class BaseConfig(object):
    DEBUG = False
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
   
   	
class DevelopmentConfig(BaseConfig):
	DEBUG = True
	WTF_CSRF_ENABLED = False

class ProductionConfig(BaseConfig):
    DEBUG = False
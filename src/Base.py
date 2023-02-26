from requests import requests
from abc import ABC

class BaseClient(ABC):
    
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
      
    def _get_auth_header(self):
        pass
    
    
    
    
    def get(self):
        pass
    
    def post(self):
        pass 
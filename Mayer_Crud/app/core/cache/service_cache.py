from django.core.cache import cache
import json

        
class ServiceCache:
    def __init__(self, page=1, timeout=None) -> None:
        self.key = f'service.page.{page}'
        
        service_list = cache.get(self.key)
        
        if service_list is None or service_list == 'null':
            empty_array = json.dumps([])
            
            cache.set(self.key, empty_array, timeout=timeout)
            
            self.service_list = []
            
        else:
            self.service_list = json.loads(service_list)
            
    
    def set_data(self, service_list, timeout=None):
        json_service_list = json.dumps(service_list)
        self.service_list = service_list
        cache.set(self.key, json_service_list, timeout=timeout)

        
    def get_data(self):
        return self.service_list
    

    def clear(self):
        key = '.'.join(self.key.split('.')[:-1]) + '.*'
        
        cache.delete_pattern(key)

from django.core.cache import cache
import json

        
class ProvidersCache:
    def __init__(self, page=1, timeout=None) -> None:
        self.key = f'providers.page.{page}'
        
        providers_list = cache.get(self.key)
        
        if providers_list is None or providers_list == 'null':
            empty_array = json.dumps([])
            
            cache.set(self.key, empty_array, timeout=timeout)
            
            self.providers_list = []
            
        else:
            self.providers_list = json.loads(providers_list)
            
    
    def set_data(self, providers_list, timeout=None):
        json_providers_list = json.dumps(providers_list)
        self.providers_list = providers_list
        cache.set(self.key, json_providers_list, timeout=timeout)

        
    def get_data(self):
        return self.providers_list
    

    def clear(self):
        key = '.'.join(self.key.split('.')[:-1]) + '.*'
        
        cache.delete_pattern(key)

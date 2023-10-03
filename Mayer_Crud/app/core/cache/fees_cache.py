from django.core.cache import cache
import json


        
class FeesCache:
    def __init__(self, page=1, timeout=None) -> None:
        self.key = f'fees.page.{page}'
        
        fees_list = cache.get(self.key)
        
        if fees_list is None or fees_list == 'null':
            empty_array = json.dumps([])
            
            cache.set(self.key, empty_array, timeout=timeout)
            
            self.fees_list = []
            
        else:
            self.fees_list = json.loads(fees_list)
            
    
    def set_data(self, fees_list, timeout=None):
        json_fees_list = json.dumps(fees_list)
        self.fees_list = fees_list
        cache.set(self.key, json_fees_list, timeout=timeout)

        
    def get_data(self):
        return self.fees_list
    

    def clear(self):
        key = '.'.join(self.key.split('.')[:-1]) + '.*'
        
        cache.delete_pattern(key)

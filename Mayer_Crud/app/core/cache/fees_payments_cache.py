from django.core.cache import cache
import json

        
class FeesPaymentCache:
    def __init__(self, page=1, timeout=None) -> None:
        self.key = f'fees_payments.page.{page}'
        
        fees_payments_list = cache.get(self.key)
        
        if fees_payments_list is None or fees_payments_list == 'null':
            empty_array = json.dumps([])
            
            cache.set(self.key, empty_array, timeout=timeout)
            
            self.fees_payments_list = []
            
        else:
            self.fees_payments_list = json.loads(fees_payments_list)
            
    
    def set_data(self, fees_payments_list, timeout=None):
        json_fees_payments_list = json.dumps(fees_payments_list)
        self.fees_payments_list = fees_payments_list
        cache.set(self.key, json_fees_payments_list, timeout=timeout)

        
    def get_data(self):
        return self.fees_payments_list
    

    def clear(self):
        key = '.'.join(self.key.split('.')[:-1]) + '.*'
        
        cache.delete_pattern(key)


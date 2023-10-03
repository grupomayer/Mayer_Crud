from django.core.cache import cache
import json

        
class ExpenseRecordCache:
    def __init__(self, page=1, timeout=None) -> None:
        self.key = f'expense_record.page.{page}'
        
        expense_record_list = cache.get(self.key)
        
        if expense_record_list is None or expense_record_list == 'null':
            empty_array = json.dumps([])
            
            cache.set(self.key, empty_array, timeout=timeout)
            
            self.expense_record_list = []
            
        else:
            self.expense_record_list = json.loads(expense_record_list)
            
    
    def set_data(self, expense_record_list, timeout=None):
        json_expense_record_list = json.dumps(expense_record_list)
        self.expense_record_list = expense_record_list
        cache.set(self.key, json_expense_record_list, timeout=timeout)

        
    def get_data(self):
        return self.expense_record_list
    

    def clear(self):
        key = '.'.join(self.key.split('.')[:-1]) + '.*'
        
        cache.delete_pattern(key)

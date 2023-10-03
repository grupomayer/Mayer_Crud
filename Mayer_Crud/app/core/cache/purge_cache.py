from django.core.cache import cache


class PurgeCache:
    def __init__(self, page) -> None:
        self.page = page


    def purge(self):
        cache.clear()
        print(f"Cache from page{self.page} cleared.")
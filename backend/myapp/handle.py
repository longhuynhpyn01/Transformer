class Transformer():
    def __init__(self, query):
        self.query = query
        self.urls_details = []

    def get_urls_text(self):
        print('self query:', self.query)
        self.urls_details = ["kq1", "kq2", "kq3", "kq4", "kq5"]

    def get_results(self):
        self.get_urls_text()
        return self.urls_details
    
    def get_query(self):
        return self.query
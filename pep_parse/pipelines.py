import csv
import os
from collections import defaultdict
from datetime import datetime


class PepParsePipeline:
    def __init__(self):
        self.status_dict = defaultdict(int)

        time_str = datetime.now().strftime('%Y-%m-%dT%H-%M-%S+00-00')

        file_path = os.path.join(
            os.path.dirname(__file__), '..', f'status_summary_{time_str}.csv'
        )
        
        self.file = open(
            file_path,
            mode='w',
            newline='',
            encoding='utf-8'
        )
        self.writer = csv.writer(self.file)
        self.writer.writerow(['Status', 'Count'])
 
    def process_item(self, item, spider):
        self.status_dict[item["status"]] += 1
        return item

    def close_spider(self, spider):
        for status, count in self.status_dict.items():
            self.writer.writerow([status, count])

        self.file.close()

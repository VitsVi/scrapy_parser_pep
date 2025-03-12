import csv
import os
from collections import defaultdict
from datetime import datetime
from constants import BASE_DIR


class PepParsePipeline:
    def __init__(self):
        self.status_dict = defaultdict(int)

    def open_spider(self, spider):
        results_dir = BASE_DIR / 'results'

        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        time_str = datetime.now().strftime('%Y-%m-%dT%H-%M-%S+00-00')
        file_path = os.path.join(
            results_dir,
            f'status_summary_{time_str}.csv'
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

        self.file.close()

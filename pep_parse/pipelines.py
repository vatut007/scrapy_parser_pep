import csv
import datetime as dt


from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = dict()
        self.result_final = [('Статус', 'Количество')]

    def process_item(self, item, spider):
        self.statuses[item['status']] = self.statuses.get(
            item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        self.result_final.extend(self.statuses.items())
        self.result_final.append(('Total', sum(self.statuses.values())))
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(self.result_final)

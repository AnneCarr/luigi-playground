import csv
import luigi
import datetime
from hello_world import HelloWorld

class Analysis(luigi.Task):
    date = luigi.DateParameter(default=datetime.date.today())

    def requires(self):
        return HelloWorld(date=self.date)

    def run(self):
        with open('outputs/hello-world-%s.txt' % self.date, 'r') as f:
            numwords = 0
            for line in f:
                words = line.split()
                numwords += len(words)

        with self.output().open('w') as csvfile:
            outfile = csv.writer(csvfile, delimiter=',')
            outfile.writerow([numwords])

    def output(self):
        return luigi.LocalTarget('data/report-%s.csv' % self.date)

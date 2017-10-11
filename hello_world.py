import luigi
import datetime

class HelloWorld(luigi.Task):
    date = luigi.DateParameter(default=datetime.date.today())

    def run(self):
        with self.output().open('w') as f:
            f.write("Hello World!\n")

    def output(self):
        return luigi.LocalTarget('outputs/hello-world-%s.txt' % self.date)

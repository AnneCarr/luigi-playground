# How To Run

Run the luigi schedule on the commandline
`luigid`
Then, in another tab, run the luigi command referencing the report and the timeframe
`PYTHONPATH=. luigi --module analysis Analysis --date 2000-01-01`

# View Pipeline

Go to `http://localhost:8082/`
In the task list, find the final report task for the time of the last run, click the blue pipeline icon under actions.
On the new page you want to unselect the "Hide Done" option to view the full pipeline

# Data
Once the pipeline has run successfully you should have a report in your data folder that tells you the number of words in the hello world output file. Tada!

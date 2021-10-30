This is a tool which will help you find slow pages. Currently this only works with HTTP GET requests.

PreReq
* Python
* wget
* sqlite3 - `sudo apt install sqlite3`

Here is a basic workflow
1. wget --spider --force-html -r -l1 https://example.com/ 2>&1 | grep -o 'http.*' > urls.txt
1. ./getTimes.py
1. sqlite3 -header -csv urls.sqlite < stats.sql > stats.csv

```
$ ./getTimes.py --help
usage: getTimes.py [-h] [-i INPUT_FILE] [-o SQLITE_DB] [-n REPEATS]

This script time the time it takes to download a set of URLs X times

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input INPUT_FILE, -u INPUT_FILE, --urls INPUT_FILE
                        A file containing one URL per line. Default: urls.txt.
  -o SQLITE_DB, --output SQLITE_DB, --sqlite SQLITE_DB
                        This the name of the sqlite file to write the results to. Default: urls.sqlite.
  -n REPEATS, --iterations REPEATS, -r REPEATS, --repeats REPEATS
                        This the name of the sqlite file to write the results to. Default: 10.
```

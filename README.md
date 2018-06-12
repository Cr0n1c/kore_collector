# kore_collector
The module collects common data sets from an environment and pushes them into the Kore Aggregator.

Each collector plugin should implement a `collect()` menthod which...
* reads either entities of events from an upstream datasource
* stores them on disk in compressed json format using the `save()` method inherited from the main `KoreCollector` class
* then returns a `CollectorResult` describing the path to each event and/or entity file

## `CollectorResult`
* `is_error()` - boolean - indicates an error when reading from the 
* `error_msq` - boolean - error message to log
* `entites` - list<str> - paths to stored entity files
* `events` - list<str> - paths to stored event files


## Usage
Collector should be run on a cron-job to push data into the Kore backend. Specify the the sources to collect from as arguments.

```
usage: kore_collector.py [-h] [-c CONFIG_YAML] [--all] [--persist] [source [source ...]]

positional arguments:
  source                Sources to collects

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_YAML, --config CONFIG_YAML
                        path to config file
  --all                 dump all configured sources
  --persist             Persiste tmp data after completion
```
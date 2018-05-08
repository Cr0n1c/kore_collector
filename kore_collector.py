import datetime

import schedule

import collectors
import kore

CONFIG_YAML = "configuration.yaml"


def print_stdout(string):
    print("{}: {}".format(datetime.datetime.now(), string))


def run_collectors():
    # Statically assigning scheduler.  Will hook yaml in at a later date.
    schedule.every(1).days.do(collectors.ldap.run_collector, setup_conf)
    schedule.every(1).days.do(collectors.sccm.run_collector, setup_conf)
    schedule.every(1).days.do(collectors.nessus.run_collector, setup_conf)

    schedule.run_pending()


if __name__ == "__main__":
    while True:

        # Reading in YAML after each schedule to check for changes.  I will update the rest of the code to be
        # dynamic off of this at a later time.

        print_stdout("Reading Configuration YAML for changes")
        setup_conf = kore.Configuration(CONFIG_YAML)

        print_stdout("Running Collectors")
        run_collectors()


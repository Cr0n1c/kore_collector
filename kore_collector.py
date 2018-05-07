import schedule

import kore

CONFIG_YAML = "configuration.yaml"

def start_scheduler():

def run_collectors():
    pass


if __name__ == "__main__":
    print("[+] Loading Configuration YAML")
    setup_conf = kore.Configuration(CONFIG_YAML)

    print("[+] Starting up Scheduler")
    start_scheduler()

    print("[+] Starting up Collector")
    run_collectors()


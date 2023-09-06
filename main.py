# Imports all projects
import scratchattach as s3
import scratchFrontPage as sfp
import time, os

# Runs projects
sfp.run()

print('All scripts have been run.')
time.sleep(1800)
print('30 mins have passed. Stopping script...')
pgid = os.getpgid(os.getpid())
os.killpg(pgid, signal.SIGINT)

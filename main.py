# Imports all projects
import scratchattach as s3
import scratchFrontPage as sfp
import time, sys

# Runs projects
sfp.run()

print('All scripts have been run.')
time.sleep(60*30)
print('30 mins have passed. Stopping script...')
sys.exit(0)

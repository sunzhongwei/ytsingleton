# ytsingleton

If you want to prevent your script from running in parallel just instantiate SingleInstance() class. 

Usage:

```
from ytsingleton import SingleInstance 
lockfile = "/tmp/<app>.lock"
instance = SingleInstance(lockfile)
```

will sys.exit(-1) if other instance is running

[ ]: handle invalid B values (currently goes over 250 still) - validator could spot any that are over 250 and just replace with 250
[ ]: paramaterize tests for all string letters items - this should **pass**
[ ]: show color live, updating with default when no user input. Have default state of updating every 0.5 seconds.
[ ]: write a test for showing color live, and default values

# tests to write:
    # check display falls back gracefully if invalid rgb
    # how does RGB class handle losing contact with display?
    # how does display handle different tuple feed regularities? eg every 0.5 seconds, every 0.1s, every minute, series of repeats, does that break?


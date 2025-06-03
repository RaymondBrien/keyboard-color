Try quick hash lookup with quick_dict instead.
 - nb. Can this be done with CPython for faster parsing? Currently slower than a snail.

# tests to write:
    # check display falls back gracefully if invalid rgb
    # how does RGB class handle losing contact with display?
    # how does display handle different tuple feed regularities? eg every 0.5 seconds, every 0.1s, every minute, series of repeats, does that break?
    # load testing - how many inputs before it times out?


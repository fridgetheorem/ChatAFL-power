# Detect Response
# using the digitizer libraries.

# We need a way to analyze a trace in real time to determine whether or not there exists an interesting response within it.

# Olha recommended the following algorithm
#   Acquire 10 traces
#   compute:
#       ED
#       ED on normalized samples
#       CP
#       CID
#       Pearson
#   Store array, mean, and std
#   Acquire the next command
#   Compute (against the previous traces):
#       ED
#       ED on normalized
#       CP
#       CID
#       Pearson
#   Store array, mean and std of new data
#   Is it statistically different?
#       If so, add the new traces to data
#       If not, increment the plateau counter 
#   Repeat.
#   If a plateau is reached, stop

import numpy as np
import pandas as pd

def analyze_last_trace():
    # Get location of previous trace
    # First and second trace
    first = np.load()
    second = np.load()
    data = (first, np.mean(first), np.std(first))

    # Compute the distance between the new command and the previous data
    # outlier method?

    new_command = (second, np.mean(second), np.std(second))
    # Get distance metrics
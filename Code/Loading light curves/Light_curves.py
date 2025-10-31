import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset
from astropy.timeseries import LombScargle
import warnings


#Load the data set
tess_data = load_dataset(
    "MultimodalUniverse/tess",
    split="train",
    streaming=True
)

import pandas as pd
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz

from cemrg_wearable.common import get_subject_dataset, get_subject_dataset_from_df

def plot_data(filein, subject, timestr, ycol, ax1, remove_zero=True, fig1=None):
    
    casedf = get_subject_dataset(filein, subject, timestr, ycol, remove_zero)
    plot_from_case_df(casedf, ycol, ax1, fig1)


def plot_from_df(df, subject, timestr, ycol, ax1, remove_zero=True, fig1=None):
    
    casedf = get_subject_dataset_from_df(df, subject, timestr, ycol, remove_zero)
    plot_from_case_df(casedf, ycol, ax1, fig1)

def plot_from_case_df(casedf, ycol, ax1, fig1=None):

    ax1.plot(casedf['days'].values, casedf[ycol].values, '*')
    ax1.set_xlabel('Time(days)')
    ax1.set_ylabel(ycol)
    if fig1 is not None:
        fig1.autofmt_xdate(rotation=45)
    ax1.grid(True)

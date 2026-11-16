# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:14:27 2026

@author: jburj
"""
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

folder_path = Path("C:\\Users\\jburj\\R6Impact\\Data\\MatchData\\OsakaMajor")

df = pd.concat(
    (pd.read_csv(file) for file in folder_path.glob("*.csv")), ignore_index = True)

df.to_csv("concatData.csv", index=False)
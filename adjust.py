#!/usr/bin/env python3

import sys

import numpy as np
import pandas as pd

damage_scale = 0.5

df = pd.read_csv(sys.argv[1], dtype = str)

# df['BaseDamage'] = np.ceil(df['BaseDamage'].astype(float) * damage_scale).astype(int)
# df['ArmourDamage'] = np.ceil(df['ArmourDamage'].astype(float) * damage_scale).astype(int)
# df['ArmourPenetration'] = np.ceil(df['ArmourPenetration'].astype(float) * damage_scale).astype(int)
# df['HelmetDamage'] = np.ceil(df['HelmetDamage'].astype(float) * damage_scale).astype(int)
# df['HelmetBleed'] = np.ceil(df['HelmetBleed'].astype(float) * damage_scale).astype(int)

df['FalloffModifier'] = '0'
df['MinFalloffDist'] = '0'
df['MaxFalloffDist'] = '0'

df.to_csv('out.csv', index = False, line_terminator = '\r\n')

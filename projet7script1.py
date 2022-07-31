#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
#import seaborn as sns #not working
import matplotlib as plt


aster = pd.read_csv('/Users/davidpitoun/All_Ironhack/TeamProjects/project7-models_asteroids/neo.csv')

aster.info()
aster['orbiting_body'].unique()

#it is all the same orbiting object
aster = aster.drop(columns=['orbiting_body'], axis=1)

corr = aster.corr()
#heatmap = sns.heatmap(corr, vmin=-1, vmax=1, annot=True)

aster['sentry_object'].nunique()
aster.columns
aster = aster.drop(columns=['sentry_object'], axis=1)
aster = aster.drop(columns=['est_diameter_min'], axis=1)

aster.info()

astercols = aster.columns
astercols

aster['est_diameter_max'].sort_values(ascending=False).head(50)
aster['est_diameter_max'].sort_values(ascending=True).head(50)
aster['est_diameter_max'].mean()
aster['est_diameter_max'].median()
aster['est_diameter_max'].mode()
aster['est_diameter_max'].min()

aster['relative_velocity'].sort_values(ascending=True).head(50)
aster['relative_velocity'].min()
aster['relative_velocity'].mean()
aster['relative_velocity'].median()


aster['id'].value_counts()

astid2469219 = aster.loc[aster['id'] == 2469219]

ids= aster['id']

for x in ids:
    filters = aster[aster['id']==x]
    meanv = filters['relative_velocity'].mean()
    meand = filters['miss_distance'].mean()
    aster.loc[aster[aster['id']==x].index, 'relative_velocity'] = meanv
    aster.loc[aster[aster['id']==x].index, 'miss_distance'] = meand


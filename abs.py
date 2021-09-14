#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import  control as ctrl
from time import sleep
 
obstacledis = ctrl.Antecedent(np.arange(0,130,1),'obstacledis')
brakeforce=ctrl.Antecedent(np.arange(0,110,1),'brakeforce')
slip=ctrl.Antecedent(np.arange(0,101,1),'slip')
obstacledis['very close']=fuzz.trimf(obstacledis.universe,[0,5,21])
obstacledis['close']=fuzz.trimf(obstacledis.universe,[20,40,76])
obstacledis['away']=fuzz.trimf(obstacledis.universe,[75,105,130])
brakeforce['low'] = fuzz.trimf(brakeforce.universe,[0,20,40])
brakeforce['mid'] = fuzz.trimf(brakeforce.universe,[35,50,62])
brakeforce['high'] = fuzz.trimf(brakeforce.universe,[60,80,100])
slip['safe'] = fuzz.trimf(slip.universe, [0,15,30])
slip['midd'] =fuzz.trimf(slip.universe, [25,50,65])
slip['unsafe']=fuzz.trimf(slip.universe,[60,80,100])
ab=ctrl.Consequent(np.arange(0,101,1),'ab')
ab['low brake'] = fuzz.trimf(ab.universe, [0,15,26])
ab['mid brake'] = fuzz.trimf(ab.universe, [25,50,65])
ab['high brake'] = fuzz.trimf(ab.universe, [60,80,100])
obstacledis.view()
brakeforce.view()
slip.view()

rule1 = ctrl.Rule(obstacledis['very close'] & brakeforce['low'] & slip['unsafe'], ab['low brake'])
rule2 = ctrl.Rule(obstacledis['very close'] & brakeforce['low'] & slip['midd'], ab['low brake'])
rule3 = ctrl.Rule(obstacledis['very close'] & brakeforce['low'] & slip['safe'], ab['low brake'])
rule4 = ctrl.Rule(obstacledis['very close'] & brakeforce['mid'] & slip['unsafe'], ab['mid brake'])
rule5 = ctrl.Rule(obstacledis['very close'] & brakeforce['mid'] & slip['midd'], ab['low brake'])
rule6 = ctrl.Rule(obstacledis['very close'] & brakeforce['mid'] & slip['safe'], ab['mid brake'])
rule7 = ctrl.Rule(obstacledis['very close'] & brakeforce['high'] & slip['unsafe'], ab['low brake'])
rule8 = ctrl.Rule(obstacledis['very close'] & brakeforce['high'] & slip['midd'], ab['mid brake'])
rule9 = ctrl.Rule(obstacledis['very close'] & brakeforce['high'] & slip['safe'], ab['high brake'])
rule10 = ctrl.Rule(obstacledis['close'] & brakeforce['low'] & slip['unsafe'], ab['low brake'])
rule11 = ctrl.Rule(obstacledis['close'] & brakeforce['low'] & slip['midd'], ab['mid brake'])
rule12 = ctrl.Rule(obstacledis['close'] & brakeforce['low'] & slip['safe'], ab['high brake'])
rule13 = ctrl.Rule(obstacledis['close'] & brakeforce['mid'] & slip['unsafe'], ab['low brake'])
rule14 = ctrl.Rule(obstacledis['close'] & brakeforce['mid'] & slip['midd'], ab['mid brake'])
rule15= ctrl.Rule(obstacledis['close'] & brakeforce['mid'] & slip['safe'], ab['high brake'])
rule16 = ctrl.Rule(obstacledis['close'] & brakeforce['high'] & slip['unsafe'], ab['low brake'])
rule17 = ctrl.Rule(obstacledis['close'] & brakeforce['high'] & slip['midd'], ab['mid brake'])
rule18= ctrl.Rule(obstacledis['close'] & brakeforce['high'] & slip['safe'], ab['high brake'])
rule19 = ctrl.Rule(obstacledis['away'] & brakeforce['low'] & slip['unsafe'], ab['low brake'])
rule20 = ctrl.Rule(obstacledis['away'] & brakeforce['low'] & slip['midd'], ab['mid brake'])
rule21 = ctrl.Rule(obstacledis['away'] & brakeforce['low'] & slip['safe'], ab['high brake'])
rule22 = ctrl.Rule(obstacledis['away'] & brakeforce['mid'] & slip['unsafe'], ab['low brake'])
rule23 = ctrl.Rule(obstacledis['away'] & brakeforce['mid'] & slip['midd'], ab['mid brake'])
rule24 = ctrl.Rule(obstacledis['away'] & brakeforce['mid'] & slip['safe'], ab['high brake'])
rule25 = ctrl.Rule(obstacledis['away'] & brakeforce['high'] & slip['unsafe'], ab['low brake'])
rule26 = ctrl.Rule(obstacledis['away'] & brakeforce['high'] & slip['midd'], ab['mid brake'])
rule27 = ctrl.Rule(obstacledis['away'] & brakeforce['high'] & slip['safe'], ab['high brake'])
mn = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
mng = ctrl.ControlSystemSimulation(mn)
mng.input['obstacledis'] = int(input("Enter the obstacle distance =  "))
mng.input['slip'] = int(input("Enter the slip rate =  "))
mng.input['brakeforce'] = int(input("Enter the brakeforce = "))
mng.compute()
s=mng.output['ab']
print(s)
ab.view(sim=mng)


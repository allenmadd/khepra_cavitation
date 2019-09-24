#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Khepra Cavitation Simulation
Goal: Produce Graphs for bubble radius and energy transfer of bubble to solvent over time
Created on Mon Sep 23 18:09:02 2019

@author: mallen
"""

#following the guidelines outlined in "Heat transfer during cavitation bubble collapse"
#Zongyi Qin a , Habib Alehossein b,


#libraries
import numpy as np
import matplotlib.pyplot as plt


"""Constants"""

#bubble diameter
bubbleDiameter = 1 #mm
#boundary diameter 
boundartDiameter = 8 #mm
#boundary pressure
boundaryPressure = 0 #Pa
#boundary temperature
boundaryTemperature = 300 #K
#initial oil pressure
initialOilPressure = 0 #Pa
#Initial Bubble Diameter
initialBubbleDiameter = 1 #mm
#initial temperature of oil / bubble
initialTemperature = 300 #K
#initial bubble pressure
initialBubblePressure = -70000 #Pa
#air in bubble
airInBubble = 6.33*10**-9 #moles



#bubble area
bubbleArea = 4*np.pi*((bubbleDiameter/2)**2)
#specific heat of castor oil
specificHeat = 1.8 #(kJ/(kg K))
#emissivity of hot surface (using water)
emissivity = .96
#layer thickness (for estimation)
d = .01 #mm
#thermal conductivity (for castor oil)
thermalConductivity = .180 #(W/m K)
#viscosity (for castor oil)
viscosity = .650 #(N s/m2, Pa s)
#density 
density = 0.918 #g/cm^3
#steffon's constant
steffon = 5.67 * 10**-8 #W/m^2K^4
#surface tension of corn oil
surfaceTension = 31.6 #mN/m
#number of moles
moles = 1

"""arrays"""
#time (i believe thiis can just be a constant, it is infinitessimal,)


#pressure in the bubble?

#change in volume (should this be constant? should this change as the bubble oscillates?)

#need to figure out what Tb and Tinfinity are . maybe Tinfinity is the boundary temperature but idk what Tb is 

"""determine the temperature (pseudocode because I am sleepy)"""
#T(0) = 300
#for i=1:length(temperature):
#   T(i) = T(i-1) + (1/(moles*specificHeat))*(bubblePressure*deltaV - thermalConductivity*bubbleArea*(Tb-Tinfinity)deltaTime/d 
#- emissivity*steffon*bubbleArea*(Tb^4 - Tinfinity^4)*deltaTime)

"""plot T(i)"""









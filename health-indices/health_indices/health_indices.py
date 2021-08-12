# -*- coding: utf-8-*-

###### Health IndeX #######
## Version 0.1 ##

# ---- List of Indices -----
# Body adiposity index
# Body Shape Index
# Body volume index
# Body water
# Corpulence index
# Pignet Index
from __future__ import division
import math


# Body Mass Index
def bmi(mass, height):
    """BMI: Body Mass Index

    Params:
    ------
    mass: int/float : mass of the person in kg
    height:int/float: height of the person in m

    Usage:
    -----
    >>> from health_indices import bmi
    >>> bmi(mass=65,height=1.70)
    >>>

    """
    bmi_formula = mass // height ** 2
    if bmi_formula < 18.5:
        print("Body Mass Index is => ", bmi_formula)
        print("BMI Category => Underweight ")
    elif bmi_formula > 23:
        print("Body Mass Index is => ", bmi_formula)
        print("BMI Category => Overweight ")
    elif bmi_formula > 30:
        print("Body Mass Index is => ", bmi_formula)
        print("BMI Category => Obese ")
    else:
        print("Body Mass Index is => ", bmi_formula)

    print("Body Mass Index is => ", bmi_formula)
    return bmi_formula


def bodymassindex(mass, height):
    """BMI: Body Mass Index

    Params:
    ------
    mass: int/float : mass of the person
    height:int/float: height of the person in cm

    Usage:
    -----
    >>> from health_indices import bodymassindex
    >>> bodymassindex(mass=65,height=170)
    >>>

    """
    bmi_formula = float(mass) / height ** 2
    if bmi_formula < 18.5:
        print("Body Mass Index is => ", bmi_formula)
        print("BMI Category => Underweight ")
    elif bmi_formula > 23:
        print("Body Mass Index is => ", bmi_formula)
        print("BMI Category => Overweight ")
    elif bmi_formula > 30:
        print("Body Mass Index is => ", bmi_formula)
        print("BMI Category => Obese ")
    else:
        print("Body Mass Index is => ", bmi_formula)

    print("Body Mass Index is => ", bmi_formula)


# Body Adipose Index
# Measuring the amount of body fat in humans
def bai(hip_circumference, height):
    bai_formula = (100 * hip_circumference / height * math.sqrt(height)) - 18
    print("Body Adipose Index =>", bai_formula)


def bodyadiposeindex(hip_circumference, height):
    bai_formula = (100 * hip_circumference / height * math.sqrt(height)) - 18
    print("Body Adipose Index =>", bai_formula)


# Body Shape Index
def bsi(wc, mass, height):
    bsi_formula = wc / (cbrt((mass / height ** 2) ** 2)) * math.sqrt(height)
    print("Body Shape Index =>", bsi_formula)


# def bodyshapeindex(wc,mass,height):
# 	bsi_formula = wc/(cbrt((mass/height**2)**2))*math.sqrt(height)
#     print("Body Shape Index =>",bsi_formula)
#     return bsi_formula


# Body water
# C is a coefficient for the expected percentage of weight made up of free water.
# 	For adult, non-elderly males, C = 0.6.
# 	For adult elderly males, malnourished males, or females, C = 0.5.
# 	For adult elderly or malnourished females C = 0.45.

#
def tbw(weight, age):
    adult_elderly = range(61, 100)
    adult_nonelderly = range(18, 60)
    children = range(1, 7)
    if age in adult_nonelderly:
        C = 0.6
        tbw_formula = weight * C
        print("Total Body Water =>", tbw_formula)
    elif age in adult_elderly:
        C = 0.5
        tbw_formula = weight * C
        print("Total Body Water =>", tbw_formula)
    else:
        C = 0.45
        tbw_formula = weight * C
        print("Total Body Water =>", tbw_formula)


def totalbodywater(weight, age):
    adult_elderly = range(61, 100)
    adult_nonelderly = range(18, 60)
    children = range(1, 7)
    if age in adult_nonelderly:
        C = 0.6
        tbw_formula = weight * C
        print("Total Body Water =>", tbw_formula)
    elif age in adult_elderly:
        C = 0.5
        tbw_formula = weight * C
        print("Total Body Water =>", tbw_formula)
    else:
        C = 0.45
        tbw_formula = weight * C
        print("Total Body Water =>", tbw_formula)


# Corpulence
# The Corpulence Index (CI) or Ponderal Index (PI) is a measure of leanness (corpulence) of a person


def corpulence_index(mass, height):
    corpulence_formula = mass / height ** 3
    print("Corpulence Index =>", corpulence_formula)


# waist to hip ratio
# that abdominal obesity is defined as a waist–hip ratio above 0.90 for males and above 0.85 for females, or a body mass index (BMI) above 30.0
def waist_to_hip(waist_size, hip_size):
    waist_to_hip_formula = waist_size / hip_size
    print("Waist To Hip Ratio=>", waist_to_hip_formula)


# Pignet
# Pignet Index or Body Build Index is an index used for evaluation of body build.
# Stature in cm - (weight in kg + chest circumference in cm)
def pignetindex(height, weight, chest_circumference):
    pignetindex_formula = height - (weight + chest_circumference)
    print("Pignet Index=>", pignetindex_formula)


def bodybuildindex(height, weight, chest_circumference):
    pignetindex_formula = height - (weight + chest_circumference)
    print("Pignet Index=>", pignetindex_formula)


def bbi(height, weight, chest_circumference):
    pignetindex_formula = height - (weight + chest_circumference)
    print("Pignet Index=>", pignetindex_formula)


## Perinatal mortality rate – the sum of neonatal deaths and fetal deaths (stillbirths) per 1,000 births.
# Maternal mortality ratio – the number of maternal deaths per 100,000 live births in same time period.
# Maternal mortality rate – the number of maternal deaths per 1,000 women of reproductive age in the population (generally defined as 15–44 years of age).
# Infant mortality rate – the number of deaths of children less than 1 year old per 1,000 live births.
# Child mortality rate: the number of deaths of children less than 5 years old per 1,000 live births.


# Mortality rate
# Perinatal the sum of neonatal deaths and fetal deaths (stillbirths) per 1,000 births.
def perinatal_mortality(neonatal_deaths):
    perinatal_mortality_formula = sum(neonatal_deaths) / 1000 * 100
    print("Perinatal Mortality=>", perinatal_mortality_formula, "%")


# Maternal mortality ratio
def maternal_mortality_ratio(num_maternal_deaths):
    maternal_mortality_formula = num_maternal_deaths / 100000
    print("Maternal Mortality Ratio=>", maternal_mortality_formula)


# Maternal mortality rate
# Maternal mortality rate – the number of maternal deaths per 1,000 women of reproductive age in the population (generally defined as 15–44 years of age).
def maternal_mortality(num_maternal_deaths):
    maternal_mortality_formula = num_maternal_deaths / 1000 * 100
    print("Maternal Mortality Rate=>", maternal_mortality_formula, "%")


# Infant mortality rate
# Infant mortality rate – the number of deaths of children less than 1 year old per 1,000 live births.
def infant_mortality(num_infant_deaths):
    infant_mortality_formula = num_infant_deaths / 100000 * 100
    print("Infant Mortality Rate=>", infant_mortality_formula, "%")


# Child mortality rate
# # Child mortality rate: the number of deaths of children less than 5 years old per 1,000 live births.
def child_mortality(num_child_deaths):
    infant_mortality_formula = num_child_deaths / 100000 * 100
    print("Infant Mortality Rate=>", infant_mortality_formula, "%")


# For Heel-Ball Index:(Breadth at heel x 100/Breadth at ball)
def heelballindex(heel_breadth, ball_breadth):
    heelIndex = heel_breadth * 100 / ball_breadth
    return heelIndex


# Health Indicators For General Population
# For BirthRate
def birthrate(number_of_live_births, population):
    birthRate = number_of_live_births / population * 1000
    return birthRate


# For Crude Birth Rate
def crudebirthrate(number_of_live_births, population_at_mid_year):
    crudeBirth = number_of_live_births / population_at_mid_year * 1000
    return crudeBirth


# For Mortality Rate
def mortalityrate(number_of_deaths, population):
    mortality = number_of_deaths / population * 1000
    return mortality


# For Natural Population Growth
def populationgrowth(number_of_births, number_of_death):
    naturalPopGrowth = number_of_births - number_of_death * 1000
    return naturalPopGrowth


# Fertility Rate
def fertilityrate(number_of_births, population_of_women_in_fertilityage):
    fertilityRate = number_of_births / population_of_women_in_fertilityage * 1000
    return fertilityRate

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damcon(damage):
  updated_Damages = []
  for dam in damage:
    if 'M' in dam:
      updated_Damages.append(float(dam[:-1]) * 1000000)
    elif 'B' in dam:
      updated_Damages.append(float(dam[:-1]) * 1000000000)
    else:
      updated_Damages.append(dam)
  return updated_Damages
updated_damages = damcon(damages) 
print(updated_damages, '\n')

# write your construct hurricane dictionary function here:
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  for i in range(len(names)):
    hurricanes[names[i]] = ({'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Death': deaths[i]})
  return (hurricanes)
  
hurricanes = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes, '\n')
print(len(hurricanes))

# write your construct hurricane by year dictionary function here:
def hurricane_year(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricane_Year = []
  for na, mo, ye, ma, ar, up, de in zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    yd = {ye: {'Name': na, 'Month': mo, 'Year': ye, 'Max Sustained Wind': ma, 'Areas Affected': ar, 'Damage': up, 'Death': de}}
    hurricane_Year.append(yd)
  return hurricane_Year 
year_dictionary = hurricane_year(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)  
print (year_dictionary, '\n') 
    
# write your count affected areas function here:
def hurricane_count(areas_affected):
  occurrence_count = {}
  for occurrences in areas_affected:
    for state in occurrences:
      if state in occurrence_count:  
        occurrence_count[state] += 1
      elif state not in occurrence_count:
        occurrence_count[state] = 1
  return occurrence_count
occurrence_dictionary = hurricane_count(areas_affected)
print(occurrence_dictionary, '\n')  


# write your find most affected area function here:
def max_occurrence(occurrence_dictionary):
  most_hurricanes = {}
  max = 0
  area = ''
  for areas in occurrence_dictionary:
    if occurrence_dictionary[areas] >= max:
      max = occurrence_dictionary[areas]
      area = areas
  most_hurricanes[area] = max
  return most_hurricanes

Max_Occurrence = max_occurrence(occurrence_dictionary)
print(Max_Occurrence)  

# write your greatest number of deaths function here:
def max_death(deaths):
  maximum_death = 0
  for cases in deaths:
    if cases >= maximum_death:
      maximum_death = cases
  return maximum_death
Maximum_Death = max_death(deaths)
print(Maximum_Death, '\n')    


# write your catgeorize by mortality function here:
def hurricane_rating(hurricanes):
  mortality_rates = {0: [], 1: [], 2: [], 3: [], 4: [], 5:[]}
  rate = 0
  for hurricane in hurricanes:
    deaths = hurricanes[hurricane]['Death']
    if deaths == 0:
      rate = 0
    elif deaths > 0 and deaths <= 100:
      rate = 1
    elif deaths > 100 and deaths <= 500:
      rate =  2
    elif deaths > 500 and deaths <= 1000:
      rate = 3
    elif deaths > 1000 and deaths <= 10000:
      rate = 4

    if rate not in mortality_rates:
      mortality_rates[rate] = hurricanes[hurricane]
    else:
      mortality_rates[rate].append(hurricanes[hurricane])

  return mortality_rates

mortality_rates = hurricane_rating(hurricanes)
print(mortality_rates, '\n')


# write your greatest damage function here:
def greatest_damage(hurricanes):
  max_damage = 0
  country_with_max = ''
  for hurricane in hurricanes:
    if hurricanes[hurricane]['Damage'] == 'Damages not recorded':
      continue
    elif hurricanes[hurricane]['Damage'] > max_damage:
      max_damage = hurricanes[hurricane]['Damage']
      country_with_max = hurricanes[hurricane]['Name']
    
   
  maximum = {country_with_max: max_damage}
  return maximum

greatest_damage = greatest_damage(hurricanes)
print(greatest_damage, '\n')  



# write your catgeorize by damage function here:
def damage_rating(hurricanes):
  damage_scale = {0: [], 1: [], 2: [], 3: [], 4: []}
  
  for hurricane in hurricanes:
    damage = hurricanes[hurricane]['Damage']
    rating = 0
    if damage == 'Damages not recorded':
     continue
    elif damage == 0:
      rating = 0
    elif damage > 0 and damage <= 100000000:
      rating = 1
    elif damage > 100000000 and damage <= 1000000000:
      rating = 2
    elif damage > 1000000000 and damage <= 10000000000:
      rating = 3
    elif damage > 10000000000 and damage <= 50000000000:  
      rating = 4
    
    if rating in damage_scale:
      damage_scale[rating].append(hurricanes[hurricane])
  return damage_scale

damage_rating = damage_rating(hurricanes)
print(damage_rating)

    







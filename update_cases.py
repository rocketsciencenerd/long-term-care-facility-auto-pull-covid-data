import requests  
import csv
import datetime
import json

#get data from source
url = "https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/Maryland_Congregate_Living_COVID19_Cases_Assisted/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Facility_Name%20asc&resultOffset=0&resultRecordCount=200&resultType=standard&cacheHint=true"
headers = {}
response = requests.get(url, headers)
respObj = json.loads(response.content)
facilitiesData = respObj["features"]

facilitiesObj = {}

for facility in facilitiesData:
	facName = facility["attributes"]["Facility_Name"].replace(" ", "")
	facilitiesObj[facName] = {}
	facilitiesObj[facName]["name"] = facility["attributes"]["Facility_Name"]
	facilitiesObj[facName]["county"] = facility["attributes"]["County"]
	facilitiesObj[facName]["staffCases"] = facility["attributes"]["Number_of_Staff_Cases"]
	facilitiesObj[facName]["staffDeaths"] = facility["attributes"]["Number_of_Staff_Deaths"]
	facilitiesObj[facName]["residentCases"] = facility["attributes"]["Number_of_Resident_Cases"]
	facilitiesObj[facName]["residentDeaths"] = facility["attributes"]["Number_of_Staff_Deaths"]

#generate csv file
today = str(datetime.date.today())
csvName = "ltcFacilityData" + today + ".csv"
outputFile = csv.writer(open(csvName, "w"))

with open(csvName, "w", newline='') as outputFile:
	wr = csv.writer(outputFile, quoting=csv.QUOTE_ALL)

	# snf's
	wr.writerow(['Status of Concerning SNFs in Hopkins Catchment Area'])
	wr.writerow(['Only includes SNFs with at least 100 bed capacity'])
	wr.writerow(['Date Updated: ' + today])
	wr.writerow([''])
	wr.writerow(['License_Capacity', 'Facility_Name', 'County', 'Closest Hopkins Hospital', 'Distance', 'Staff Cases', 'Staff Deaths', 'Resident Cases', 'Resident Deaths', 'Changes in Cases Since Yesterday', 'Changes in Deaths Since Yesterday'])

	wr.writerow(['170', 'ADELPHI NURSING AND REHABILITATION CENTER', 'PRINCE GEORGE\'S COUNTY', 'Suburban', '11.9 miles', facilitiesObj['AdelphiNursingandRehabilitation']["staffCases"], facilitiesObj['AdelphiNursingandRehabilitation']["staffDeaths"], facilitiesObj['AdelphiNursingandRehabilitation']["residentCases"], facilitiesObj['AdelphiNursingandRehabilitation']["residentDeaths"],'', ''])
	wr.writerow(['151', 'ARCOLA HEALTH AND REHABILITATION CENTER', 'MONTGOMERY COUNTY', 'Suburban', '10.3 miles', facilitiesObj['ArcolaHealthandRehabilitationCenter']["staffCases"], facilitiesObj['ArcolaHealthandRehabilitationCenter']["staffDeaths"], facilitiesObj['ArcolaHealthandRehabilitationCenter']["residentCases"], facilitiesObj['ArcolaHealthandRehabilitationCenter']["residentDeaths"],'', ''])
	wr.writerow(['138', 'AUTUMN LAKE HEALTHCARE AT OAKVIEW', 'MONTGOMERY COUNTY', 'Suburban', '4.9 miles', facilitiesObj['AutumnLakeHealthcareatOakview']["staffCases"], facilitiesObj['AutumnLakeHealthcareatOakview']["staffDeaths"], facilitiesObj['AutumnLakeHealthcareatOakview']["residentCases"], facilitiesObj['AutumnLakeHealthcareatOakview']["residentDeaths"],'', ''])
	wr.writerow(['140', 'AUTUMN LAKE HEALTHCARE AT PIKESVILLE', 'BALTIMORE COUNTY', 'JHH', '14.8 miles', facilitiesObj['AutumnLakePikesville']["staffCases"], facilitiesObj['AutumnLakePikesville']["staffDeaths"], facilitiesObj['AutumnLakePikesville']["residentCases"], facilitiesObj['AutumnLakePikesville']["residentDeaths"],'', ''])
	wr.writerow(['238', 'AUTUMN LAKE HEALTHCARE AT RIVERVIEW ', 'BALTIMORE COUNTY', 'Bayview', '3.8 miles', facilitiesObj['AutumnLakeHealthcareatRiverview']["staffCases"], facilitiesObj['AutumnLakeHealthcareatRiverview']["staffDeaths"], facilitiesObj['AutumnLakeHealthcareatRiverview']["residentCases"], facilitiesObj['AutumnLakeHealthcareatRiverview']["residentDeaths"],'', ''])
	wr.writerow(['195', 'BETHESDA HEALTH AND REHABILITATION', 'MONTGOMERY COUNTY', 'Suburban', '2.4 miles', facilitiesObj['BethesdaHealthandRehab']["staffCases"], facilitiesObj['BethesdaHealthandRehab']["staffDeaths"], facilitiesObj['BethesdaHealthandRehab']["residentCases"], facilitiesObj['BethesdaHealthandRehab']["residentDeaths"],'', ''])
	wr.writerow(['118', 'BIRCH MANOR CENTER FOR REHABILITATION & HEALTHCARE', 'CARROLL COUNTY', 'Howard County', '19.2 miles', facilitiesObj['BirchManorHealthcareCenter']["staffCases"], facilitiesObj['BirchManorHealthcareCenter']["staffDeaths"], facilitiesObj['BirchManorHealthcareCenter']["residentCases"], facilitiesObj['BirchManorHealthcareCenter']["residentDeaths"],'', ''])
	wr.writerow(['270', 'CADIA HEALTHCARE - HYATTSVILLE','PRINCE GEORGE\'S COUNTY', 'Sibley', '9.0 miles', facilitiesObj['CadiaHyattsville']["staffCases"], facilitiesObj['CadiaHyattsville']["staffDeaths"], facilitiesObj['CadiaHyattsville']["residentCases"], facilitiesObj['CadiaHyattsville']["residentDeaths"],'', ''])
	wr.writerow(['116', 'CADIA HEALTHCARE - WHEATON', 'MONTGOMERY COUNTY', 'Suburban', '6.2 miles', facilitiesObj['CadiaHealthcareWheaton']["staffCases"], facilitiesObj['CadiaHealthcareWheaton']["staffDeaths"], facilitiesObj['CadiaHealthcareWheaton']["residentCases"], facilitiesObj['CadiaHealthcareWheaton']["residentDeaths"],'', ''])
	wr.writerow(['108', 'CARRIAGE HILL BETHESDA', 'MONTGOMERY COUNTY', 'Suburban', '1.0 miles', facilitiesObj['CarriageHill']["staffCases"], facilitiesObj['CarriageHill']["staffDeaths"], facilitiesObj['CarriageHill']["residentCases"], facilitiesObj['CarriageHill']["residentDeaths"],'', ''])
	wr.writerow(['160', 'COLLINGSWOOD REHABILITATION AND HEALTHCARE CENTER', 'MONTGOMERY COUNTY', 'Suburban', '8.0 miles', facilitiesObj['CollingswoodRehabilitationandHealthcareCenter']["staffCases"], facilitiesObj['CollingswoodRehabilitationandHealthcareCenter']["staffDeaths"], facilitiesObj['CollingswoodRehabilitationandHealthcareCenter']["residentCases"], facilitiesObj['CollingswoodRehabilitationandHealthcareCenter']["residentDeaths"],'', ''])
	wr.writerow(['140', 'CRESCENT CITIES NURSING & REHABILITATION CENTER', 'PRINCE GEORGE\'S COUNTY', 'Sibley', '11.2 miles', facilitiesObj['CrescentCities']["staffCases"], facilitiesObj['CrescentCities']["staffDeaths"], facilitiesObj['CrescentCities']["residentCases"], facilitiesObj['CrescentCities']["residentDeaths"],'', ''])
	wr.writerow(['135', 'CROMWELL CENTER', 'BALTIMORE COUNTY', 'Bayview', '11.8 miles', facilitiesObj['GenesisCromwellCenter']["staffCases"], facilitiesObj['GenesisCromwellCenter']["staffDeaths"], facilitiesObj['GenesisCromwellCenter']["residentCases"], facilitiesObj['GenesisCromwellCenter']["residentDeaths"],'', ''])
	wr.writerow(['182', 'ELLICOTT CITY HEALTHCARE CENTER', 'HOWARD COUNTY', 'Howard County', '7.9 miles', facilitiesObj['EllicottCityHealthcareCenter']["staffCases"], facilitiesObj['EllicottCityHealthcareCenter']["staffDeaths"], facilitiesObj['EllicottCityHealthcareCenter']["residentCases"], facilitiesObj['EllicottCityHealthcareCenter']["residentDeaths"],'', ''])
	wr.writerow(['156', 'FAYETTE HEALTH AND REHABILITATION CENTER', 'BALTIMORE CITY', 'JHH', '2.8 miles', facilitiesObj['FayetteNursingandRehabilitation']["staffCases"], facilitiesObj['FayetteNursingandRehabilitation']["staffDeaths"], facilitiesObj['FayetteNursingandRehabilitation']["residentCases"], facilitiesObj['FayetteNursingandRehabilitation']["residentDeaths"],'', ''])
	wr.writerow(['155', 'FUTURE CARE NORTHPOINT', 'BALTIMORE COUNTY', 'Bayview', '2.6 miles', facilitiesObj['FutureCareNorthpoint']["staffCases"], facilitiesObj['FutureCareNorthpoint']["staffDeaths"], facilitiesObj['FutureCareNorthpoint']["residentCases"], facilitiesObj['FutureCareNorthpoint']["residentDeaths"],'', ''])
	wr.writerow(['556', 'HEBREW HOME OF GREATER WASHINGTON', 'MONTGOMERY COUNTY', 'Suburban', '5.0 miles', facilitiesObj['HebrewHomeofGreaterWashington']["staffCases"], facilitiesObj['HebrewHomeofGreaterWashington']["staffDeaths"], facilitiesObj['HebrewHomeofGreaterWashington']["residentCases"], facilitiesObj['HebrewHomeofGreaterWashington']["residentDeaths"],'', ''])
	wr.writerow(['177', 'HERITAGE CENTER', 'BALTIMORE COUNTY', 'Bayview', '2.0 miles', facilitiesObj['HeritageCenterGenesisEldercare']["staffCases"], facilitiesObj['HeritageCenterGenesisEldercare']["staffDeaths"], facilitiesObj['HeritageCenterGenesisEldercare']["residentCases"], facilitiesObj['HeritageCenterGenesisEldercare']["residentDeaths"],'', ''])
	wr.writerow(['140', 'KENSINGTON HEALTHCARE CENTER', 'MONTGOMERY COUNTY', 'Suburban', '4.8 miles', facilitiesObj['KensingtonHealthcareCenter']["staffCases"], facilitiesObj['KensingtonHealthcareCenter']["staffDeaths"], facilitiesObj['KensingtonHealthcareCenter']["residentCases"], facilitiesObj['KensingtonHealthcareCenter']["residentDeaths"],'', ''])
	wr.writerow(['242', 'KESWICK MULTI-CARE CENTER', 'BALTIMORE CITY', 'JHH', '5.2 miles', facilitiesObj['KeswickMulti-CareCenter']["staffCases"], facilitiesObj['KeswickMulti-CareCenter']["staffDeaths"], facilitiesObj['KeswickMulti-CareCenter']["residentCases"], facilitiesObj['KeswickMulti-CareCenter']["residentDeaths"],'', ''])
	wr.writerow(['118', 'LAYHILL NURSING AND REHABILITATION CENTER', 'MONTGOMERY COUNTY', 'Suburban', '8.5 miles', facilitiesObj['LayhillCenter']["staffCases"], facilitiesObj['LayhillCenter']["staffDeaths"], facilitiesObj['LayhillCenter']["residentCases"], facilitiesObj['LayhillCenter']["residentDeaths"],'', ''])
	wr.writerow(['205', 'LORIEN HEALTH SYSTEMS - COLUMBIA', 'HOWARD COUNTY', 'Howard County', '1.4 miles', facilitiesObj['LorienColumbia']["staffCases"], facilitiesObj['LorienColumbia']["staffDeaths"], facilitiesObj['LorienColumbia']["residentCases"], facilitiesObj['LorienColumbia']["residentDeaths"],'', ''])
	wr.writerow(['148', 'MANOR CARE HEALTH SERVICES - SILVER SPRING', 'MONTGOMERY COUNTY', 'Suburban', '13.0 miles', facilitiesObj['ManorCareSilverSpring']["staffCases"], facilitiesObj['ManorCareSilverSpring']["staffDeaths"], facilitiesObj['ManorCareSilverSpring']["residentCases"], facilitiesObj['ManorCareSilverSpring']["residentDeaths"],'', ''])
	wr.writerow(['110', 'MANOR CARE HEALTH SERVICES - BETHESDA', 'MONTGOMERY COUNTY', 'Suburban', '2.8 miles', facilitiesObj['ManorCareHealthServicesBethesda']["staffCases"], facilitiesObj['ManorCareHealthServicesBethesda']["staffDeaths"], facilitiesObj['ManorCareHealthServicesBethesda']["residentCases"], facilitiesObj['ManorCareHealthServicesBethesda']["residentDeaths"],'', ''])
	wr.writerow(['172', 'MANOR CARE HEALTH SERVICES - CHEVY CHASE', 'MONTGOMERY COUNTY', 'Suburban', '3.2 miles', facilitiesObj['ManorCareHealthServices-ChevyChase']["staffCases"], facilitiesObj['ManorCareHealthServices-ChevyChase']["staffDeaths"], facilitiesObj['ManorCareHealthServices-ChevyChase']["residentCases"], facilitiesObj['ManorCareHealthServices-ChevyChase']["residentDeaths"],'', ''])
	wr.writerow(['158', 'MANOR CARE HEALTH SERVICES - POTOMAC', 'MONTGOMERY COUNTY', 'Suburban', '7.1 miles', facilitiesObj['ManorCarePotomac']["staffCases"], facilitiesObj['ManorCarePotomac']["staffDeaths"], facilitiesObj['ManorCarePotomac']["residentCases"], facilitiesObj['ManorCarePotomac']["residentDeaths"],'', ''])
	wr.writerow(['172', 'MANOR CARE HEALTH SERVICES - ROSSVILLE', 'BALTIMORE COUNTY', 'JHH', '7.5 miles', facilitiesObj['ManorCareHealthServices-Rossville']["staffCases"], facilitiesObj['ManorCareHealthServices-Rossville']["staffDeaths"], facilitiesObj['ManorCareHealthServices-Rossville']["residentCases"], facilitiesObj['ManorCareHealthServices-Rossville']["residentDeaths"],'', ''])
	wr.writerow(['147', 'MONTGOMERY VILLAGE HEALTH CARE CENTER', 'MONTGOMERY COUNTY', 'Suburban', '15.1 miles', facilitiesObj['MontgomeryVillageHealthCareCenter']["staffCases"], facilitiesObj['MontgomeryVillageHealthCareCenter']["staffDeaths"], facilitiesObj['MontgomeryVillageHealthCareCenter']["residentCases"], facilitiesObj['MontgomeryVillageHealthCareCenter']["residentDeaths"],'', ''])
	wr.writerow(['150', 'OAK MANOR CENTER FOR REHABILITATION AND HEALTHCARE', 'MONTGOMERY COUNTY', 'Howard County', '11.0 miles', facilitiesObj['OakManorCenter']["staffCases"], facilitiesObj['OakManorCenter']["staffDeaths"], facilitiesObj['OakManorCenter']["residentCases"], facilitiesObj['OakManorCenter']["residentDeaths"],'', ''])
	wr.writerow(['150', 'OVERLEA HEALTH AND REHABILITATION CENTER', 'BALTIMORE CITY', 'JHH', '5.1 miles']) #,'', '','', '','', ''])
	wr.writerow(['153', 'PATUXENT RIVER HEALTH AND REHABILITATION CENTER', 'PRINCE GEORGE\'S COUNTY', 'Howard County', '14.8 miles', facilitiesObj['PatuxentRiverHealthandRehabilitationCenter']["staffCases"], facilitiesObj['PatuxentRiverHealthandRehabilitationCenter']["staffDeaths"], facilitiesObj['PatuxentRiverHealthandRehabilitationCenter']["residentCases"], facilitiesObj['PatuxentRiverHealthandRehabilitationCenter']["residentDeaths"],'', ''])
	wr.writerow(['225', 'POST-ACUTE CARE CENTER', 'BALTIMORE CITY', 'Bayview', '3.9 miles', facilitiesObj['PostAcuteCareCenter']["staffCases"], facilitiesObj['PostAcuteCareCenter']["staffDeaths"], facilitiesObj['PostAcuteCareCenter']["residentCases"], facilitiesObj['PostAcuteCareCenter']["residentDeaths"],'', ''])
	wr.writerow(['175', 'POTOMAC VALLEY REHABILITATION AND HEALTHCARE', 'MONTGOMERY COUNTY', 'Suburban', '7.0 miles', facilitiesObj['PotomacValleyRehabilitationandHealthcareCenter']["staffCases"], facilitiesObj['PotomacValleyRehabilitationandHealthcareCenter']["staffDeaths"], facilitiesObj['PotomacValleyRehabilitationandHealthcareCenter']["residentCases"], facilitiesObj['PotomacValleyRehabilitationandHealthcareCenter']["residentDeaths"],'', ''])
	wr.writerow(['100', 'ROCKVILLE NURSING HOME', 'MONTGOMERY COUNTY', 'Suburban', '8.4 miles', facilitiesObj['RockvilleNursingHome']["staffCases"], facilitiesObj['RockvilleNursingHome']["staffDeaths"], facilitiesObj['RockvilleNursingHome']["residentCases"], facilitiesObj['RockvilleNursingHome']["residentDeaths"],'', ''])
	wr.writerow(['134', 'SHADY GROVE NURSING AND REHABILITATION CENTER', 'MONTGOMERY COUNTY', 'Suburban', '9.6 miles', facilitiesObj['ShadyGroveCenterforNursing&Rehabilitation']["staffCases"], facilitiesObj['ShadyGroveCenterforNursing&Rehabilitation']["staffDeaths"], facilitiesObj['ShadyGroveCenterforNursing&Rehabilitation']["residentCases"], facilitiesObj['ShadyGroveCenterforNursing&Rehabilitation']["residentDeaths"],'', ''])
	wr.writerow(['160', 'THE VILLAGE AT ROCKVILLE', 'MONTGOMERY COUNTY', 'Suburban', '8.5 miles', facilitiesObj['VillageatRockville']["staffCases"], facilitiesObj['VillageatRockville']["staffDeaths"], facilitiesObj['VillageatRockville']["residentCases"], facilitiesObj['VillageatRockville']["residentDeaths"],'', ''])
	wr.writerow(['285', 'WILSON HEALTH CARE CENTER', 'MONTGOMERY COUNTY', 'Suburban', '13.4 miles']) #, facilitiesObj['WilsonHealthCareCenteratAsburyMethodistVillage']["staffCases"], facilitiesObj['WilsonHealthCareCenteratAsburyMethodistVillage']["staffDeaths"], facilitiesObj['WilsonHealthCareCenteratAsburyMethodistVillage']["residentCases"], facilitiesObj['WilsonHealthCareCenteratAsburyMethodistVillage']["residentDeaths"],'', ''])

	# alfs 
	wr.writerow([''])
	wr.writerow([''])
	wr.writerow(['Status of concerning ALFs, Retirement Communities, etc in Hopkins Catchment Area'])
	wr.writerow(['Date Updated: ' + today])
	wr.writerow([''])
	wr.writerow(['License_Capacity', 'Facility_Name', 'County', 'Closest Hopkins Hospital', 'Distance', 'Staff Cases', 'Staff Deaths', 'Resident Cases', 'Resident Deaths', 'Changes in Cases Since Yesterday', 'Changes in Deaths Since Yesterday'])
	wr.writerow(['100', 'BRIGHTVIEW FALLSGROVE', 'MONTGOMERY COUNTY', 'Suburban', '8.7 miles', facilitiesObj['BrightviewFallsgrove-RockvilleSeniorAssistedLivingandMemoryCare']["staffCases"], facilitiesObj['BrightviewFallsgrove-RockvilleSeniorAssistedLivingandMemoryCare']["staffDeaths"], facilitiesObj['BrightviewFallsgrove-RockvilleSeniorAssistedLivingandMemoryCare']["residentCases"], facilitiesObj['BrightviewFallsgrove-RockvilleSeniorAssistedLivingandMemoryCare']["residentDeaths"],'', ''])
	wr.writerow(['98', 'BRIGHTVIEW WEST END', 'MONTGOMERY COUNTY', 'Suburban', '7.9 miles', facilitiesObj['BrightviewWestEnd-BrightviewSeniorLiving']["staffCases"], facilitiesObj['BrightviewWestEnd-BrightviewSeniorLiving']["staffDeaths"], facilitiesObj['BrightviewWestEnd-BrightviewSeniorLiving']["residentCases"], facilitiesObj['BrightviewWestEnd-BrightviewSeniorLiving']["residentDeaths"],'', ''])
	wr.writerow(['', 'Cedar Creek Memory Care Homes - Maple Ridge', 'MONTGOMERY COUNTY', 'Suburban', '11.2 miles', facilitiesObj['CedarCreekMemoryCareHomes-MapleRidge']["staffCases"], facilitiesObj['CedarCreekMemoryCareHomes-MapleRidge']["staffDeaths"], facilitiesObj['CedarCreekMemoryCareHomes-MapleRidge']["residentCases"], facilitiesObj['CedarCreekMemoryCareHomes-MapleRidge']["residentDeaths"],'', ''])
	wr.writerow(['', 'Friends House Retirement Community','MONTGOMERY COUNTY','Howard County','12.1 miles', facilitiesObj['FriendsHouseRetirementCommunity']["staffCases"], facilitiesObj['FriendsHouseRetirementCommunity']["staffDeaths"], facilitiesObj['FriendsHouseRetirementCommunity']["residentCases"], facilitiesObj['FriendsHouseRetirementCommunity']["residentDeaths"],'', ''])
	wr.writerow(['', 'Inspirations Assisted Living and Memory Care of Linthicum', 'ANNE ARUNDEL', 'JHH', '9.8 miles', facilitiesObj['InspirationMemoryCareLinthicum']["staffCases"], facilitiesObj['InspirationMemoryCareLinthicum']["staffDeaths"], facilitiesObj['InspirationMemoryCareLinthicum']["residentCases"], facilitiesObj['InspirationMemoryCareLinthicum']["residentDeaths"],'', ''])
	wr.writerow(['', 'Maplewood Park Place', 'MONTGOMERY COUNTY', 'Suburban', '1.6 miles', facilitiesObj['MaplewoodofParkPlace,SunriseSeniorLiving']["staffCases"], facilitiesObj['MaplewoodofParkPlace,SunriseSeniorLiving']["staffDeaths"], facilitiesObj['MaplewoodofParkPlace,SunriseSeniorLiving']["residentCases"], facilitiesObj['MaplewoodofParkPlace,SunriseSeniorLiving']["residentDeaths"],'', ''])
	wr.writerow(['', 'New Life Healthy Living',	'BALTIMORE', 'JHH',	'11.4 miles', facilitiesObj['NewLifeHealthLiving']["staffCases"], facilitiesObj['NewLifeHealthLiving']["staffDeaths"], facilitiesObj['NewLifeHealthLiving']["residentCases"], facilitiesObj['NewLifeHealthLiving']["residentDeaths"],'', ''])
	wr.writerow(['', 'Oak Crest Senior Living Community', 'BALTIMORE', 'Bayview', '9.4 miles', facilitiesObj['OakCrest']["staffCases"], facilitiesObj['OakCrest']["staffDeaths"], facilitiesObj['OakCrest']["residentCases"], facilitiesObj['OakCrest']["residentDeaths"],'', ''])
	wr.writerow(['', 'Oakwood Care Center',	'BALTIMORE', 'Bayview',	'7.7 miles', facilitiesObj['OakwoodCareCenter']["staffCases"], facilitiesObj['OakwoodCareCenter']["staffDeaths"], facilitiesObj['OakwoodCareCenter']["residentCases"], facilitiesObj['OakwoodCareCenter']["residentDeaths"],'', ''])
	wr.writerow(['64', 'Olney Memory Care',	'MONTGOMERY COUNTY', 'Suburban', '11.1 miles', facilitiesObj['OlneyMemoryCare']["staffCases"], facilitiesObj['OlneyMemoryCare']["staffDeaths"], facilitiesObj['OlneyMemoryCare']["residentCases"], facilitiesObj['OlneyMemoryCare']["residentDeaths"],'', ''])
	wr.writerow(['', 'Residences at Vantage Point',	'HOWARD', 'Howard County', '3.3 miles', facilitiesObj['ResidencesatVantagePoint']["staffCases"], facilitiesObj['ResidencesatVantagePoint']["staffDeaths"], facilitiesObj['ResidencesatVantagePoint']["residentCases"], facilitiesObj['ResidencesatVantagePoint']["residentDeaths"],'', ''])
	wr.writerow(['', 'Riderwood Village - Arbor Ridge',	'MONTGOMERY COUNTY', 'Suburban', '14.1 miles', facilitiesObj['Riderwood-ArborRidge']["staffCases"], facilitiesObj['Riderwood-ArborRidge']["staffDeaths"], facilitiesObj['Riderwood-ArborRidge']["residentCases"], facilitiesObj['Riderwood-ArborRidge']["residentDeaths"],'', ''])
	wr.writerow(['', 'Roland Park Place', 'BALTIMORE CITY', 'JHH', '5.8 miles', facilitiesObj['RolandParkPlace']["staffCases"], facilitiesObj['RolandParkPlace']["staffDeaths"], facilitiesObj['RolandParkPlace']["residentCases"], facilitiesObj['RolandParkPlace']["residentDeaths"],'', ''])


csvNameRaw = "ltcFacilityData_raw" + today + ".csv"
outputFileRaw = csv.writer(open(csvNameRaw, "w"))

with open(csvNameRaw, "w", newline='') as outputFileRaw:
	wr = csv.writer(outputFileRaw, quoting=csv.QUOTE_ALL)
	wr.writerow(['License_Capacity', 'Facility_Name', 'County', 'Closest Hopkins Hospital', 'Distance', 'Staff Cases', 'Staff Deaths', 'Resident Cases', 'Resident Deaths', 'Changes in Cases Since Yesterday', 'Changes in Deaths Since Yesterday'])
	for facName in facilitiesObj:
		wr.writerow(['', facilitiesObj[facName]["name"], facilitiesObj[facName]["county"], '', '', facilitiesObj[facName]["staffCases"], facilitiesObj[facName]["staffDeaths"], facilitiesObj[facName]["residentCases"], facilitiesObj[facName]["residentDeaths"] ])

#todo: add in script that auto updates changes in cases / deaths since yesterday
















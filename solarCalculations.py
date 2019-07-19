import numpy as np
from datetime import datetime as DT
from pytz import timezone
from solartime import SolarTime
import time
import matplotlib
import math



class earth(object):
		def __init__(self, dayofyear , longitude = -116.35 , latitude = np.deg2rad(41.0)):
			self.Gsc = 1367
			self.latitude = latitude	# Barrick's latitude
			self.longitude = longitude # [Should be in Radians? 2-20-19]
			self.dayofyear = dayofyear
			self.today = DT.now()
			self.localtz = timezone('US/Pacific')
			self.LST = 120
			self.hourMin = DT.time(self.today).hour + (DT.time(self.today).minute / 60 )
			self.Radiation = None
			self.B = np.deg2rad((((self.dayofyear-1)*360)/365))		# working
			self.E = 229.2* (0.000075 + (0.001868 * np.cos(self.B)) - (0.032077 * np.sin(self.B)) - (0.014615 * np.cos(2*self.B)) - (0.04089 * np.sin(2*self.B)) )	 # working do not change
			
		# Confirmed functions	
		def declinationCalc(self):	# Verified between -23.45 and 23.45
			declination = 23.45* np.sin(np.deg2rad((360*(284+self.dayofyear)/float(365))))
			return np.deg2rad(declination)	# in radians now. Does not actually return between -23.5 and 23.5 anymore!!	
			
		def solarTime(self):		# confirmed in hours between 13 hr and 13.6 hr
			return  self.hourMin +(((4*(self.LST - self.longitude))+ self.E) / 60)
			
		def hourAngle(self):		# degrees 15 to 21
			h = 15 * (self.solarTime()-12)
			return np.deg2rad(h)	# changed to radians 0.26 - 0.41
		
		def zenith(self):		#Psi						#delta							        #omega					#psi						#delta
			return np.cos(self.latitude)* np.cos(self.declinationCalc())* np.cos(np.deg2rad(self.hourAngle()))   +   np.sin(self.latitude)* np.sin(self.declinationCalc())		# degree
		
		def zenithAngle(self):
			z = np.arccos(self.zenith())
			return np.rad2deg(z)		# comes out as degree
			
		def radiance_time(self):			#G_on			# Verified
			return self.Gsc *(1+0.033*np.cos(np.deg2rad((360*self.dayofyear)/365)))			# W/m2

		def sunsetHour(self):		# Verified (ws)
			sunset = (np.arccos(   -np.tan(   self.latitude   )*np.tan(self.declinationCalc())   ))
			return np.rad2deg(sunset)			# This answer comes out in degree
			
		def hoursintheday(self):		# Verified (N)
			sunrise = 2*(self.sunsetHour()) / 15
			#sunrise = 24*.31
			return sunrise			# This answer comes out in radians			
			

			
			
		# Unconfirmed	
		
		def groundRadiation(self , units = 'W/m2 or J/s.m2'):
			self.Radiation = (self.tauB()+self.tauD()) * self.radiance_time() * self.zenith()		#W/m2   ---> J/s.m2 
			return self.Radiation 

		def tauB(self):
			r0 , r1 , rk = [0.97 , 0.99 , 1.02] # midatlantic summer
			#r0 , r1 , rk = [1.03 , 1.01 , 1.00] # midatlantic Winter
			A = np.rad2deg(self.sunAltitude())		# degrees
			a0 = r0*(0.4237 - 0.00821*((6-A)**2))
			a1 = r1*(0.5055 - 0.00595*((6.5-A)**2))
			k = rk*(0.2711 - 0.01858*((2.5-A)**2))
			a0 , a1 , k = np.deg2rad(np.array([a0 , a1 , k]))
			return np.rad2deg(a0 + a1 * np.exp(-k/np.cos(np.deg2rad(self.zenithAngle())))) 			# 
			
		def sunAltitude(self):
			hs = np.arcsin(self.zenith())
			return np.deg2rad(hs)
			
		def azimuth(self):
			gamma = np.arcsin(np.cos(self.declinationCalc())* np.sin(np.deg2rad(self.hourAngle())) / np.cos(self.sunAltitude()))
			return np.rad2deg(gamma)			# degrees
			
		def tauD(self):
			return 0.271 - 0.294 * self.tauB()
			
		def hourlyRadiation(self, w2, w1):
			hourRad = ((12*3600)/np.pi) * self.Gsc * self.radiance_time() * np.cos(self.latitude)* np.cos(self.declinationCalc())* (np.sin(np.deg2rad(w2)) - np.sin(np.deg2rad(w1))) * ((np.pi*(w2-w1))/180) * np.sin(self.latitude)*np.sin(self.declinationCalc())
			return hourRad
			
		def dailyRadiation(self):
			dailyRad = ((24*3600)/np.pi) * self.radiance_time() * np.cos((self.latitude)*np.cos(self.declinationCalc()) * np.sin(np.deg2rad(self.sunsetHour())) * ((np.pi*np.deg2rad(self.sunsetHour()))/180) * np.sin(self.latitude)*np.sin(self.declinationCalc()))
			return dailyRad

		def recieve(self):
			print(np.array(["Hourly Radiation:" +str(self.hourlyRadiation()) , "Daily Radiation:" +str(self.dailyRadiation()) , "Zenith Angle:" +str(self.zenithAngle())]))

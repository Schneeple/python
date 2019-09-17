import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as DT
from pytz import timezone
from solartime import SolarTime
try:
    import pitools.pull as Pi
except:
    print('Do not have pitools library. Will not be able to save to OSIsoft Pi Server.')
import time
import matplotlib
import math



class earth(object):
        def __init__(self , year = 2019 ,dayofyear= np.linspace(1,365,365) ,  longitude = -116.35 , latitude = np.deg2rad(41.0)):
            self.year = year
            self.Gsc = 1367
            self.latitude = latitude
            self.longitude = longitude # [Should be in Radians? 2-20-19]
            self.dayofyear = np.array(dayofyear)
            self.today = DT.datetime.now()
            self.localtz = timezone('US/Pacific')
            self.LST = 120
            self.hourMin = DT.datetime.time(self.today).hour + (DT.datetime.time(self.today).minute / 60 )
            self.Radiation = None
            self.B = np.deg2rad((((self.dayofyear-1)*360)/365))            # working
            self.E = 229.2* (0.000075 + (0.001868 * np.cos(self.B)) - (0.032077 * np.sin(self.B)) - (0.014615 * np.cos(2*self.B)) - (0.04089 * np.sin(2*self.B)) )	 # working do not change
            self.runCalc()
            # Confirmed functions
        def declinationCalc (self):            # Verified between -23.45 and 23.45
            self.declination = 23.45* np.sin(np.deg2rad((360*(284+self.dayofyear)/float(365))))
            return np.deg2rad(self.declination)	# in radians now. Does not actually return between -23.5 and 23.5 anymore!!

        def solarTime(self):            # confirmed in hours between 13 hr and 13.6 hr
            return  self.hourMin +(((4*(self.LST - self.longitude))+ self.E) / 60)

        def hourAngle(self):            # degrees 15 to 21
            self.hourAng = 15 * (self.solarTime()-12)
            return np.deg2rad(self.hourAng)            # changed to radians 0.26 - 0.41

        def zenith(self):              #Psi                     #delta                                    #omega                             #psi                 #delta
            zenith = np.cos(self.latitude)* np.cos(self.declinationCalc())* np.cos(np.deg2rad(self.hourAngle()))   +   np.sin(self.latitude)* np.sin(self.declinationCalc())            # degree
            return zenith

        def zenithAngle(self):
            z = np.arccos(self.zenith())
            return np.rad2deg(z)            # comes out as degree

        def radiance_time(self):            #G_on            # Verified
            self.radTime = self.Gsc *(1+0.033*np.cos(np.deg2rad((360*self.dayofyear)/365)))            # W/m2
            return self.radTime

        def sunsetHour(self):            # Verified (ws)
            self.hourSunset = (np.arccos(   -np.tan(   self.latitude   )*np.tan(self.declinationCalc())   ))
            return np.rad2deg(self.hourSunset)            # This answer comes out in degree

        def hoursintheday(self):            # Verified (N)
            self.hoursintheDay = 2*(self.sunsetHour()) / 15
            #sunrise = 24*.31
            return self.hoursintheDay            # This answer comes out in radians

        def dailyRadiation(self):
            self.dailyRad = ((24*3600)/np.pi) * self.radiance_time() * np.cos((self.latitude)*np.cos(self.declinationCalc()) * np.sin(np.deg2rad(self.sunsetHour())) * ((np.pi*np.deg2rad(self.sunsetHour()))/180) * np.sin(self.latitude)*np.sin(self.declinationCalc()))
            return self.dailyRad

        # Unconfirmed

        def groundRadiation(self , units = 'W/m2 or J/s.m2'):
            self.Radiation = (self.tauB()+self.tauD()) * self.radiance_time() * self.zenith()            #W/m2   ---> J/s.m2
            return self.Radiation

        def tauB(self):
            r0 , r1 , rk = [0.97 , 0.99 , 1.02] # midatlantic summer
            #r0 , r1 , rk = [1.03 , 1.01 , 1.00] # midatlantic Winter
            A = np.rad2deg(self.sunAltitude())		# degrees
            a0 = r0*(0.4237 - 0.00821*((6-A)**2))
            a1 = r1*(0.5055 - 0.00595*((6.5-A)**2))
            k = rk*(0.2711 - 0.01858*((2.5-A)**2))
            a0 , a1 , k = np.deg2rad(np.array([a0 , a1 , k]))
            tauB = np.rad2deg(a0 + a1 * np.exp(-k/np.cos(np.deg2rad(self.zenithAngle()))))
            return tauB            #

        def sunAltitude(self):
            sunAltitude = np.arcsin(self.zenith())
            return np.deg2rad(sunAltitude)

        def azimuth(self): # gamma
            Azimuth = np.arcsin(np.cos(self.declinationCalc())* np.sin(np.deg2rad(self.hourAngle())) / np.cos(self.sunAltitude()))
            return np.rad2deg(Azimuth)            # degrees

        def tauD(self):
            tauD = 0.271 - 0.294 * self.tauB()
            return tauD

        def hourlyRadiation(self, w2, w1):
            hourRad = ((12*3600)/np.pi) * self.Gsc * self.radiance_time() * np.cos(self.latitude)* np.cos(self.declinationCalc())* (np.sin(np.deg2rad(w2)) - np.sin(np.deg2rad(w1))) * ((np.pi*(w2-w1))/180) * np.sin(self.latitude)*np.sin(self.declinationCalc())
            return hourRad



        def recieve(self):
            print(np.array(["Hourly Radiation:" +str(self.hourlyRadiation()) , "Daily Radiation:" +str(self.dailyRadiation()) , "Zenith Angle:" +str(self.zenithAngle())]))

        def dayToDate(self):
            d = self.dayofyear
            year = self.year
            try:
                vals = []
                for i in d:
                    days = i
                    dt = DT.datetime(year, 1, 1) + DT.timedelta(days - 1)
                    vals.append(dt)
            except:
                days = int(d)
                dt = DT.datetime(year, 1, 1) + DT.timedelta(days - 1)
                vals.append(dt)
            datetimes = np.array(vals)
            return datetimes

        def runCalc(self):
            ind = self.dayToDate()
            self.dic = {
                'Daily Radiation':self.dailyRadiation(),
                'Hours in the Day':self.hoursintheday(),
                'Azimuth':self.azimuth(),
                'Zenith':self.zenith(),
                'Declination Angle':self.declinationCalc(),
                'Sun Altitude':self.sunAltitude(),
                'Sunset Hour':self.sunsetHour(),
                'tau D':self.tauD(),
                'tau B':self.tauB(),
                'Radiance Time':self.radiance_time(),
                #'Hour Angle':self.hourAng,

            }
            self.df = pd.DataFrame(self.dic , index = ind)
            return self.df
            

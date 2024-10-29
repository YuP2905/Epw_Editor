# coding=utf-8
import math
import pandas as pd
from ladybug.epw import EPW
from ladybug.wea import Wea
from ladybug.datacollection import HourlyContinuousCollection, MonthlyCollection
from ladybug.sunpath import Sunpath
from ladybug.datatype.fraction import RelativeHumidity
from ladybug.psychrometrics import rel_humid_from_db_dpt

class Epwdata(object):
    def __init__(self, epw_path):
        self.epw = EPW(epw_path)
        # EPW_Data_Attribute_Name Based on Ladybug
        self.__attribute_name = [
            "dry_bulb_temperature",
            "dew_point_temperature",
            "relative_humidity",
            "wind_speed",
            "wind_direction",
            "direct_normal_radiation",
            "diffuse_horizontal_radiation",
            "global_horizontal_radiation",
            "horizontal_infrared_radiation_intensity",
            "direct_normal_illuminance",
            "diffuse_horizontal_illuminance",
            "global_horizontal_illuminance",
            "total_sky_cover",
            "atmospheric_station_pressure",
            "visibility",
            "ceiling_height",
            "years",
            "monthly_ground_temperature",
        ]
        self.__epw_df_1 = pd.DataFrame() # Void DataFrame for Translate the data of hours(8760) from Epw
        self.__epw_df_2 = pd.DataFrame() # Void DataFrame for Translate the data of month from Epw
        pass
    def __str__(self):
        return str(self.epw)

    def df_from_epw(self):
        for name in self.__attribute_name:
            if hasattr(self.epw, name):
                if name != "monthly_ground_temperature":
                    _values = getattr(self.epw, name).values # 8760h data of Epw(len 8760)
                    self.__epw_df_1[name] = _values 
                    pass

                else:
                    g_temp = getattr(self.epw, name) # monthly_ground_temperature(12month) data of Epw(len 12)
                    for j, key in  enumerate(sorted(g_temp.keys())):
                        _values = g_temp[key].values
                        self.__epw_df_2[name + str(j+1)] = _values
                    pass
                pass
            pass

        epw_df = pd.concat([self.__epw_df_1, self.__epw_df_2], axis=1) # Stack 2 dataframes with different len
        epw_df.fillna(0)
        return epw_df

    def rewrite_epw_from_df(self, epw_df):
        if len(epw_df) != 8760:
            print("This is not a EPW DataFrame File")
            pass
        
        if "dry_bulb_temperature" in epw_df.columns and "dew_point_temperature" in epw_df.columns:
            dry_temp = HourlyContinuousCollection(self.epw.dry_bulb_temperature.header, epw_df["dry_bulb_temperature"].to_list())
            dew_temp = HourlyContinuousCollection(self.epw.dew_point_temperature.header, epw_df["dew_point_temperature"].to_list())
            rel_humid = HourlyContinuousCollection.compute_function_aligned(rel_humid_from_db_dpt, 
                                                                            [dry_temp, dew_temp],
                                                                            RelativeHumidity(), "%")
            self.epw.relative_humidity.values = rel_humid.values
            pass

        if "direct_normal_radiation" in epw_df.columns and "diffuse_horizontal_radiation" in epw_df.columns:
            direct_normal_rad = HourlyContinuousCollection(self.epw.direct_normal_radiation.header, epw_df["direct_normal_radiation"].to_list())
            diffuse_horiz_rad = HourlyContinuousCollection(self.epw.diffuse_horizontal_radiation.header, epw_df["diffuse_horizontal_radiation"].to_list())
            wea = Wea(self.epw.location, direct_normal_rad, diffuse_horiz_rad)
            self.epw.global_horizontal_radiation.values = wea.global_horizontal_irradiance.values
            pass

        if "direct_normal_illuminance" in epw_df.columns and "diffuse_horizontal_illuminance" in epw_df.columns:
            glob_horiz = []
            sp = Sunpath.from_location(self.epw.location)
            sp.is_leap_year = self.epw.is_leap_year
            direct_normal_ill = HourlyContinuousCollection(self.epw.direct_normal_illuminance.header, epw_df["direct_normal_illuminance"].to_list())
            diffuse_horiz_ill = HourlyContinuousCollection(self.epw.diffuse_horizontal_illuminance.header, epw_df["diffuse_horizontal_illuminance"].to_list())
            for dt, dni, dhi in zip(direct_normal_ill.datetimes, direct_normal_ill, diffuse_horiz_ill):
                sun = sp.calculate_sun_from_date_time(dt)
                glob_horiz.append(dhi + dni*math.sin(math.radians(sun.altitude)))
                pass
            self.epw.global_horizontal_illuminance.values = glob_horiz
            pass
           
        if set(epw_df.columns).issubset(set(self.df_from_epw().columns)):
            for column in epw_df.columns:
                if hasattr(self.epw, column):
                    _values = epw_df[column].to_list()
                    _header = getattr(self.epw, column).header
                    getattr(self.epw, column).values = HourlyContinuousCollection(_header, _values)
                    pass

                if self.__attribute_name[-1] in column:
                    _values = [x for x in epw_df[column].to_list() if not math.isnan(x)]
                    g_temp = getattr(self.epw, self.__attribute_name[-1])
                    for key in sorted(g_temp.keys()):
                        _header = g_temp[key].header
                        g_temp[key].values = MonthlyCollection(_header, _values, _header.analysis_period.months_int)
            return self.epw
        
        else:
            print("The Columns of EPW DataFrame is not right, please Check")
            pass
        pass
    pass

if __name__ == "__main__":
    print(1)
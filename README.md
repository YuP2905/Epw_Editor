After decompressing this program, run the exe file directly to run it.


This program has two functions:

+ Based on the uploaded EPW file, you can export a CSV file that combines the data of the EPW file.

   The data type of EPW contained in its CSV file is as follows:

   + dry_bulb_temperature

   + dew_point_temperature

   + relative_humidity

   +wind_speed

   +wind_direction

   + direct_normal_radiation

   + diffuse_horizontal_radiation

   + global_horizontal_radiation

   + horizontal_infrared_radiation_intensity",

   + direct_normal_illuminance

   + diffuse_horizontal_illuminance

   + global_horizontal_illuminance

   + total_sky_cover

   + atmospheric_station_pressure

   + visibility

   + ceiling_height

   + years

   + monthly_ground_temperature_1

   + monthly_ground_temperature_2

   + monthly_ground_temperature_.....

    


+ Based on the changed CSV file, a new EPW file that conforms to the CSV file data can be generated. *(Note: The EPW file to be changed needs to be uploaded)*

   *Note: CSV cannot change the above data types. Changing meteorological data must comply with the calculation rules of Ladybug model (for details, refer to the source code or instructions of epw model on lladybug tools github).*



This program refers to part of the code of Dragonfly's DF creat epw battery in Grasshopper's Ladybug Tools plug-in.

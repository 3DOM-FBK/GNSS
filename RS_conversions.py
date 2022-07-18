# >conda create --name pyproj_env
# >conda activate pyproj_env
# >conda install -c conda-forge pyproj
# >conda install -c conda-forge pymap3d
# >conda deactivate pyproj_env

import pyproj
import pymap3d as pm

INPUT_COORD_FILE = r"C:\Users\Luscias\Desktop\Dottorato\05_Meeting\2022_03_25_FBK\PROCESSING\parcheggio_smartphone2\pos2_smartph_coombined.txt"
OUTPUT_FILE = r"C:\Users\Luscias\Desktop\Dottorato\05_Meeting\2022_03_25_FBK\PROCESSING\parcheggio_smartphone2\pos2_smartph_coombined_6704to6707.txt"

INPUT_EPSG   =   "epsg:6704"
OUTPUT_EPSG  =   "epsg:6707"

# REFERENCE SYSTEMS ID
# IGS14     geocentric      EPSG:9018
# RDN2008   geocentric      EPSG:6704


with open(INPUT_COORD_FILE, "r") as file:
    for line in file:
        line = line.strip()
        ID, X, Y, Z = line.split(",", 3)
        X_CRS_1 = X
        Y_CRS_1 = Y
        Z_CRS_1 = Z
        print(X, Y, Z)

        # ETRS89 UTM 32N to ECEF
        CRS_1 = pyproj.Proj(init='{}'.format(INPUT_EPSG))
        CRS_2 = pyproj.Proj(init='{}'.format(OUTPUT_EPSG))
        
        X_CRS_2, Y_CRS_2, Z_CRS_2 = pyproj.transform(CRS_1, CRS_2, X_CRS_1, Y_CRS_1, Z_CRS_1)
        print(X_CRS_2, Y_CRS_2, Z_CRS_2)
        new_file = open(OUTPUT_FILE, "a")
        new_file.write("{},{},{},{}\n".format(ID,X_CRS_2,Y_CRS_2,Z_CRS_2))
        new_file.close()
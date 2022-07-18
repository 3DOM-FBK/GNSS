# >conda create --name pyproj_env
# >conda activate pyproj_env
# >conda install -c conda-forge pyproj
# >conda install -c conda-forge pymap3d
# >conda deactivate pyproj_env

import pyproj
import pymap3d as pm

INPUT_COORD_FILE = r"C:\Users\Luscias\Desktop\Dottorato\05_Meeting\2022_03_25_FBK\PROCESSING\StationCoordinates.txt"   # ETRS89 UTM32N
OUTPUT_FILE = r"C:\Users\Luscias\Desktop\Dottorato\05_Meeting\2022_03_25_FBK\PROCESSING\StationCoordinates_epsg6704to6707.txt"


with open(INPUT_COORD_FILE, "r") as file:
    for line in file:
        line = line.strip()
        ID, X, Y, Z = line.split(",", 3)
        X_CRS_1 = X
        Y_CRS_1 = Y
        Z_CRS_1 = Z
        print(X, Y, Z)

        # ETRS89 UTM 32N to ECEF
        CRS_1 = pyproj.Proj(init='epsg:6704')
        CRS_2 = pyproj.Proj(init='epsg:6707')
        
        X_CRS_2, Y_CRS_2, Z_CRS_2 = pyproj.transform(CRS_1, CRS_2, X_CRS_1, Y_CRS_1, Z_CRS_1)
        print(X_CRS_2, Y_CRS_2, Z_CRS_2)
        new_file = open(OUTPUT_FILE, "a")
        new_file.write("{},{},{},{}\n".format(ID,X_CRS_2,Y_CRS_2,Z_CRS_2))
        new_file.close()
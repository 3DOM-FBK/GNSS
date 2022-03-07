# >conda create --name pyproj_env
# >conda activate pyproj_env
# >conda install -c conda-forge pyproj
# >conda install -c conda-forge pymap3d
# >conda deactivate pyproj_env

import pyproj
import pymap3d as pm

INPUT_COORD_FILE = r"G:\3DOM\13_Imgs_aeree\aerial_trento\Equal_coordinates\GCPs_ETRS89_UTMzone32N.txt"   # ETRS89 UTM32N
OUTPUT_FILE = r"G:\3DOM\13_Imgs_aeree\aerial_trento\Equal_coordinates\GT_ETRS89_ECEF.txt"


with open(INPUT_COORD_FILE, "r") as file:
    for line in file:
        line = line.strip()
        ID, X, Y, Z = line.split(",", 3)
        X_utm_etrs89_32N = X
        Y_utm_etrs89_32N = Y
        Z = Z
        print(X, Y, Z)

        # ETRS89 UTM 32N to ECEF
        etrs89_utm_32N = pyproj.Proj(init='epsg:25832')
        ecef = pyproj.Proj(init='epsg:4936')   #IGNF:ETRS89 epsg:4936 both og them are ECEF ETRS89
        Xc, Yc, Zc = pyproj.transform(etrs89_utm_32N, ecef, X_utm_etrs89_32N, Y_utm_etrs89_32N, Z)
        print(Xc, Yc, Zc)
        new_file = open(OUTPUT_FILE, "a")
        new_file.write("{},{},{},{}\n".format(ID,Xc,Yc,Zc))
        new_file.close()
        
quit()








# The local coordinate origin (Zermatt, Switzerland)
lat0 = 46.138834 # deg
lon0 = 11.101691  # deg
h0 = 220.900000     # meters

with open(INPUT_COORD_FILE, "r") as file:
    for line in file:
        line = line.strip()
        ID, lat, lon, h = line.split(",", 3)
        lat = float(lat)
        lon = float(lon)
        h = float(h)

        E,N,U = pm.geodetic2enu(lat, lon, h, lat0, lon0, h0, grs80, deg='deg')
        new_file = open(OUTPUT_FILE, "a")
        new_file.write("{},{},{},{}\n".format(ID,E,N,U))
        new_file.close()

quit()
with open(INPUT_COORD_FILE, "r") as file:
    for line in file:
        line = line.strip()
        ID, X, Y, Z = line.split(",", 3)
        X_utm_etrs89_32N = X
        Y_utm_etrs89_32N = Y
        Z = Z
        print(X, Y, Z)

        # ETRS89 UTM 32N to ECEF
        etrs89_utm_32N = pyproj.Proj('+proj=utm +zone=32 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
        ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
        #etrs89_utm_32N = pyproj.Proj('+proj=utm +zone=32 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
        #ecef = pyproj.Proj('+proj=geocent +zone=32 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
        #ecef = pyproj.Proj(proj='geocent', ellps='GRS80', towgs84='0,0,0,0,0,0,0', units='m')
        Xc, Yc, Zc = pyproj.transform(etrs89_utm_32N, ecef, X_utm_etrs89_32N, Y_utm_etrs89_32N, Z)
        print(Xc, Yc, Z)
        new_file = open(OUTPUT_FILE, "a")
        new_file.write("{},{},{},{}\n".format(ID,Xc,Yc,Z))
        new_file.close()
        
        quit()


quit()
lat = 46.04201332532064
lon = 11.130928248982503
hight = 300

etrs89_utm_32N = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')

x, y, z = pyproj.transform(lla, ecef, lat, lon, hight, radians=False)

print(lat, lon, hight)
print(x, y, z)




quit()
# Example position data, should be somewhere in Germany
x = 652954.1006
y = 4774619.7919
z = -2217647.7937

ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
lon, lat, alt = pyproj.transform(ecef, lla, x, y, z, radians=True)

print(lat, lon, alt)
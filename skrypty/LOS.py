import sys
import time
import datetime
import subprocess
from qgis.core import *
WORKSPACE = "C:\\QGIS\\"
#WORKSPACE = "C:/QGIS/"
#print WORKSPACE

# Initialize QGIS Application
QgsApplication.setPrefixPath("C:\\Program Files\\QGIS 2.18\\apps\\qgis-ltr", True)
app = QgsApplication([], True)
QgsApplication.initQgis()

# Add the path to Processing framework
sys.path.append('C:\\Program Files\\QGIS 2.18\\apps\\qgis-ltr\\python\\plugins')
# Add time utils


CZAS = datetime.datetime.now().strftime("%H:%M:%S")
print CZAS, '[Python] Importowanie algorytmow...'
print
# Import and initialize Processing framework
from processing.core.Processing import Processing
Processing.initialize()
import processing

CZAS = datetime.datetime.now().strftime("%H:%M:%S")
print CZAS, '[Python] Wczytywanie danych...'
print
#print sys.argv
NR_LINII=sys.argv[1]
NR=sys.argv[2]
NAZWA=sys.argv[3]
LAT=sys.argv[4]
LON=sys.argv[5]
ANT=sys.argv[6]
CEL=sys.argv[7]
print ('##### %s. lokalizacja - %s #####' % (NR_LINII, NAZWA))
print ('LAT = %s' % LAT)
print ('LON = %s' % LON)
print ('Wysokosc posadow. anteny [mAGL] = %s' % ANT)
print ('Wysokosc celu obserwacji [mAGL] = %s' % CEL)
print ('Numer nadany = %s' % NR)
print

CZAS = datetime.datetime.now().strftime("%H:%M:%S")
print CZAS, '[GRASS] WYKONYWANIE OBLICZEN WIDOCZNOSCI (viewshed)...'
print
# zasieg - CALA POLSKA
processing.runalg("grass7:r.viewshed","%s\\dane\\NMT.tif" % WORKSPACE,"%s,%s" % (LON, LAT),"%s" % ANT,"%s" % CEL,"148160",0.14286,500,True,False,False,False,"14.11666667,24.13333333,49.000000,54.83333333",0,"%s\\temp\\viewshed_%s.tif" % (WORKSPACE, NR))
# zasieg - MOLOPOLSKA
#processing.runalg("grass7:r.viewshed","%s\\dane\\NMT.tif" % WORKSPACE,"%s,%s" % (LON, LAT),"%s" % ANT,"%s" % CEL,"148160",0.14286,500,True,False,False,False,"19.0816733054,21.4718440971,49.1587317039,50.5242906951",0,"%s\\temp\\viewshed_%s.tif" % (WORKSPACE, NR))

time.sleep(2)
CZAS = datetime.datetime.now().strftime("%H:%M:%S")
print CZAS, '[SAGA] REKLASYFIKOWANIE RASTRA...'
print
processing.runalg("saga:changegridvalues","%s\\temp\\viewshed_%s.tif" % (WORKSPACE, NR),2,"0,2000,1",3,"%s\\temp\\viewshed_reclass_%s.tif" % (WORKSPACE, NR))

time.sleep(2)
CZAS = datetime.datetime.now().strftime("%H:%M:%S")
print CZAS, '[QGIS] KONWERSJA RASTRA NA WEKTOR (polygon)...'
wej = '%s\\temp\\viewshed_reclass_%s.tif' % (WORKSPACE, NR)
wyj = '%s\\temp\\viewshed_reclass_poly_%s.shp' % (WORKSPACE, NR)
#print wej
#print wyj
subprocess.Popen(["polygonize.bat", wej, wyj], shell=True)
print

time.sleep(2)
CZAS = datetime.datetime.now().strftime("%H:%M:%S")
print CZAS, '[SAGA] DISSOLVE...'
print
#processing.runalg("saga:polygondissolveallpolygons","C:/QGIS/temp/out.dbf",False,"C:/QGIS/temp/viewshed_reclass_poly_disso_1.shp")
#processing.runalg("saga:polygondissolveallpolygons","C:/QGIS/temp/out.dbf",False,"%s\\temp\\viewshed_reclass_poly_disso_%s.shp" % (WORKSPACE, NR))
#processing.runalg("saga:polygondissolveallpolygons","%s\\temp\\viewshed_reclass_poly_%s.shp" % (WORKSPACE, NR),False,"%s\\temp\\viewshed_reclass_poly_disso_%s.shp" % (WORKSPACE, NR))
processing.runalg("saga:polygondissolveallpolygons","%s\\temp\\viewshed_reclass_poly_%s.shp" % (WORKSPACE, NR),False,"%s\\temp\\%s_%s_%s-%smAGL.shp" % (WORKSPACE, NR, NAZWA, ANT, CEL))

CZAS = datetime.datetime.now().strftime("%H:%M:%S")
print CZAS, ('[Python] Koniec obliczen dla lokalizacji %s.' % NR_LINII)
print

#raw_input("[Python] Press Enter to continue ...")
#exit()
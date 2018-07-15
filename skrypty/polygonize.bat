@ECHO OFF
::CLS

:START
::skryptowy odpowiednik QGIS-Konwersja-Poligonizuj
::gdal_polygonize.bat C:/Toshi-Z30/GIS/2_Zab_QGIS_CODGIK_100m/viewshed_reclass.tif -f "ESRI Shapefile" C:\Toshi-Z30\GIS\2_Zab_QGIS_CODGIK_100m viewshed_reclass_poly

SET wej=%1
SET wyj=%2
gdal_polygonize.bat %wej% -f "ESRI Shapefile" %wyj% >nul

GOTO :EOF
::zmien nazwy plikow z out.* na nazwa_kartoteki.* i przenies je do kartoteki roboczej
CD %wyj%
FOR %%a in (.) DO SET wyj_plik=%%~na
MOVE  out.dbf ../%wyj_plik%.dbf
MOVE  out.prj ../%wyj_plik%.prj
MOVE  out.shp ../%wyj_plik%.shp
MOVE  out.shx ../%wyj_plik%.shx

:EOF
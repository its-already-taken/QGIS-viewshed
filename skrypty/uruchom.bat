@ECHO OFF
CLS
CALL znacznik_czasu.bat
TITLE WIDOCZNOSC (viewshed) analiza nr %znacznik% 

:INIT_BATCH
SET /a licznik=1
SET /a liczba_linii=0
SET czas=%TIME%
SET czas=%czas: =0%
SET czas=%czas:~0,8%
ECHO.
ECHO %czas% [Windows] Uruchamianie srodowiska Python...
ECHO.

:INIT_PYTHON
:: base install folder Setup
SET OSGEO4W_ROOT=C:\Program Files\QGIS 2.18
SET QGISNAME=qgis-ltr
SET QGIS=%OSGEO4W_ROOT%\apps\%QGISNAME%
SET QGIS_PREFIX_PATH=%QGIS%
:: Gdal Setup
SET GDAL_DATA=%OSGEO4W_ROOT%\share\gdal\
:: Python Setup
SET PATH=%OSGEO4W_ROOT%\bin;%QGIS%\bin;%PATH%
SET PYTHONHOME=%OSGEO4W_ROOT%\apps\Python27
SET PYTHONPATH=%QGIS%\python;%PYTHONPATH%

:LINE_COUNT
FOR /f "tokens=*" %%a IN (lokalizacje.txt) DO SET /a "liczba_linii+=1"
SET /a stop=%liczba_linii%+1

:START
FINDSTR /n . lokalizacje.txt | FINDSTR "^%licznik%:" >linia.tmp
FOR /f "tokens=1,2,3,4,5,6,7* delims=:, " %%a IN (linia.tmp) DO ECHO python LOS.py %%a %%b %%c %%d %%e %%f %%g >py_start.bat
CALL py_start.bat
REM PAUSE
SET /a "licznik+=1"
ECHO.
IF %licznik% == %stop% GOTO :FORMATOR
GOTO :START

:FORMATOR
ECHO Wykonano obliczenia dla %liczba_linii% lokalizacji (linii pliku LOKALIZACJE.TXT). 
ECHO.
REM usun posrednie pliki wynikowe
DEL linia.tmp >NUL
MKDIR ..\%znacznik%
COPY lokalizacje.txt ..\%znacznik%\lokalizacje_%znacznik%.txt >NUL
CD ..\temp
DEL viewshed_*.*
COPY *.* ..\%znacznik% >NUL
DEL /q *.*
CD ..\skrypty
SET czas=%TIME%
SET czas=%czas: =0%
SET czas=%czas:~0,8%
ECHO %czas% [Windows] Zakonczono wykonywanie analizy nr %znacznik%.
ECHO.
ECHO Nacisnij dowolny klawisz aby zakonczyc.
ECHO.
PAUSE >NUL
REM EXIT

:EOF
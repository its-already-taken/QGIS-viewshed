@ECHO OFF

SET znacznik=%DATE:-=%-%TIME::=%
REM skleja date i godzine wstawiac pomiedzy myslnik
REM z daty usuwamy myslniki a z godziny dwukropki

SET znacznik=%znacznik: =0%
REM zamienia spacje na wiodace zero przed godzinami<10
SET znacznik=%znacznik:~0,13%
REM usuwa sekundy, setne sekundy z godziny

REM ECHO %znacznik%
REM ECHO.

:EOF
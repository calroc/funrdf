REM This is a simple script to set up PYTHONPATH and download a db dump.
cd C:\Users\Owner\Desktop\Pete\funrdf

set GOOGLEPATH=C:\Program Files\Google\google_appengine
set GOOGLELIBPATH=%GOOGLEPATH%\lib

set PYTHONPATH=%GOOGLEPATH%\;%GOOGLELIBPATH%\fancy_urllib;%GOOGLELIBPATH%\antlr3;%GOOGLELIBPATH%\ipaddr;%GOOGLELIBPATH%\webob

python "%GOOGLEPATH%\google\appengine\tools\appcfg.py" download_data --application=funrdf --url=http://funrdf.appspot.com/remote_api --filename=down.data




"""
Enumerate installed components of Joomla
Original code: https://github.com/OWASP/joomscan/blob/master/exploit/components.pl
Original version: 0.0.7
Original license: GPL-3
Work:
1. Read all components in a list (text file)
2. Do brute forcing path $target/components/$row/. $target is target's url, $row is line in db which is component name
3. Analysis response of each component requests:
3a. status == 200
3b. Check if server has directory listing
4. Brute force files. Files are list of ('WS_FTP.LOG','README.txt','readme.txt','README.md','readme.md',
'LICENSE.TXT','license.txt','LICENSE.txt','licence.txt','CHANGELOG.txt','changelog.txt','MANIFEST.xml','manifest.xml',
'error_log','error.log');
5. Check version. Version should be in .xml file of components. syntax $target/components/$row/$row.xml
regex /type=\"component\" version=\"(.*?)\" (perl syntax)
6. Compare version with vulnerable versions
"""
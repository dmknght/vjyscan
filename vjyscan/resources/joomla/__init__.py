"""
Database for vulnerabilities of Joomla. All extensions are .jdb, which has json on each line
Reason: To optimize runtime memory, i'd like to read single files and loads to json instead load
everything into json object which eventually loads all data in a list. With loading only line,
the runtime memory is expected to be very small.
Jdb stands for Json database, which has multiple json on single line.
Version standard: Custom version or version range.
    - Exact version: 2.3.4
    - Range: 1.1.1<=2.2.2 (which means patched version is 2.2.3)
    - Range: 1.1.1<2.2.2 (which means patched version is 2.2.2)
    - Multiple version: 2.3.4|3.3.4 which means vulnerable versions are 2.3.4 and 3.3.4
    - Range: 1.1.1<2.2.2|3.3.3<=4.4.4.4|5.5.5 which means
        1. Version range is 1.1.1 to versions before 2.2.2
        2. 3.3.3 to 4.4.4
        3. 5.5.5
core.jdb: Vulnerabilities of core CMS, https://developer.joomla.org/security-centre.html
plugins.jdb: Vulnerabilites of plugin CMS, https://extensions.joomla.org/index.php?option=com_vel&format=json
"""
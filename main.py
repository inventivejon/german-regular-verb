import requests
import re
import sqlite3

db = sqlite3.connect('local.db')

db.execute('CREATE TABLE IF NOT EXISTS RegelmäßigeVerben (id INTEGER PRIMARY KEY AUTOINCREMENT, Infinitiv VARCHAR(250), Typ VARCHAR(250), Wortform VARCHAR(250))')

def getAllWithoutLink(singleSearchResult):
    if "(Seite nicht vorhanden)" in singleSearchResult:
        return singleSearchResult
    else:
        return None

def getAllWithLink(singleSearchResult):
    if "(Seite nicht vorhanden)" not in singleSearchResult:
        return singleSearchResult
    else:
        return None

r = requests.get('https://de.m.wiktionary.org/wiki/Verzeichnis:Deutsch/Regelm%C3%A4%C3%9Fige_Verben')
r.encoding = 'UTF-8'
# print("{}".format(r.content))
x = re.findall("<li>.*?</li>", r.text)
# Get all entries without link, strip all None entries
resultsWithoutLink = [i for i in list(map(getAllWithoutLink, x)) if i is not None]
# Strip all irrelevant code
resultsWithoutLink = [(re.search("\">(.*?)</a></li>",i).group(1), None) for i in resultsWithoutLink]

# Get all entries with link, strip all None entries
resultsWithLink = [i for i in list(map(getAllWithLink, x)) if i is not None]
# Strip all irrelevant code
resultsWithLink = [(re.search("\">(.*?)</a",i).group(1),re.search("href=\"(.*?)\"",i).group(1)) for i in resultsWithLink]

mergedResults = resultsWithoutLink + resultsWithLink

rootAddressForVerbDetails = 'https://de.m.wiktionary.org'

finalVerbList = []

for singleVerb in mergedResults:
    newEntry = {
        'Infinitiv': singleVerb[0]
    }

    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'Infinitiv', newEntry['Infinitiv']))

    if singleVerb[1] is not None:
        try:
            fetchUrl = rootAddressForVerbDetails + singleVerb[1]
            r = requests.get(fetchUrl)
            r.encoding = 'UTF-8'
            content = r.text.replace('\n','').replace('\t','')
            try:
                x = re.findall("<table.*?</table>", content)

                # Verbform - einfach
                verbTable = x[0]

                for singleTable in x:
                    if 'Wortform' in singleTable:
                        verbTable = singleTable
                        break
                
                try:
                    newEntry['Praesens1PersonSingular'] = re.search("Präsens.*?>ich<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'Praesens1PersonSingular', newEntry['Praesens1PersonSingular']))
                except:
                    newEntry['Praesens1PersonSingular'] = None
                
                try:
                    newEntry['Praesens2PersonSingular'] = re.search("Präsens.*?>du<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'Praesens2PersonSingular', newEntry['Praesens2PersonSingular']))
                except:
                    newEntry['Praesens2PersonSingular'] = None

                try:
                    newEntry['Praesens3PersonSingular'] = re.search("Präsens.*?>er, sie, es<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'Praesens3PersonSingular', newEntry['Praesens3PersonSingular']))
                except:
                    newEntry['Praesens3PersonSingular'] = None

                try:
                    newEntry['Praeteritum1PersonSingular'] = re.search("Präteritum.*?>ich<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'Praeteritum1PersonSingular', newEntry['Praeteritum1PersonSingular']))
                except:
                    newEntry['Praeteritum1PersonSingular'] = None
                
                try:
                    newEntry['Praeteritum2PersonSingular'] = re.search("Präteritum.*?>du<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'Praeteritum2PersonSingular', newEntry['Praeteritum2PersonSingular']))
                except:
                    newEntry['Praeteritum2PersonSingular'] = None
                
                try:
                    newEntry['Praeteritum3PersonSingular'] = re.search("Präteritum.*?>er, sie, es<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'Praeteritum3PersonSingular', newEntry['Praeteritum3PersonSingular']))
                except:
                    newEntry['Praeteritum3PersonSingular'] = None

                try:
                    newEntry['KonjunktivII1PersonSingular'] = re.search("Konjunktiv.*?>ich<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'KonjunktivII1PersonSingular', newEntry['KonjunktivII1PersonSingular']))
                except:
                    newEntry['KonjunktivII1PersonSingular'] = None
                
                try:
                    newEntry['KonjunktivII2PersonSingular'] = re.search("Konjunktiv.*?>du<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'KonjunktivII2PersonSingular', newEntry['KonjunktivII2PersonSingular']))
                except:
                    newEntry['KonjunktivII2PersonSingular'] = None
                
                try:
                    newEntry['KonjunktivII3PersonSingular'] = re.search("Konjunktiv.*?>er, sie, es<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'KonjunktivII3PersonSingular', newEntry['KonjunktivII3PersonSingular']))
                except:
                    newEntry['KonjunktivII3PersonSingular'] = None

                try:
                    newEntry['ImperativSingular'] = re.search("Imperativ.*?>Singular<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'ImperativSingular', newEntry['ImperativSingular']))
                except:
                    newEntry['ImperativSingular'] = None
                
                try:
                    newEntry['ImperativPlural'] = re.search("Imperativ.*?>Plural<.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'ImperativPlural', newEntry['ImperativPlural']))
                except:
                    newEntry['ImperativPlural'] = None
                
                try:
                    newEntry['PerfektPartizip2'] = re.search("Perfekt.*?>Hilfsverb<.*?title.*?>(.*?)</a>.*?title.*?>(.*?)</a>", verbTable).group(1)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'PerfektPartizip2', newEntry['PerfektPartizip2']))
                except:
                    newEntry['PerfektPartizip2'] = None
                
                try:
                    newEntry['PerfektHilfsverb'] = re.search("Perfekt.*?>Hilfsverb<.*?title.*?>(.*?)</a>.*?title.*?>(.*?)</a>", verbTable).group(2)
                    db.execute('INSERT INTO RegelmäßigeVerben VALUES(NULL,\'{}\',\'{}\',\'{}\')'.format(newEntry['Infinitiv'], 'PerfektHilfsverb', newEntry['PerfektHilfsverb']))
                except:
                    newEntry['PerfektHilfsverb'] = None

                print("{}".format(newEntry))
                
                db.commit()

            except Exception as e:
                print(str(e.args))
                newEntry['failed'] = content
                print("{}".format(fetchUrl))
        except Exception as e:
            print(str(e.args))

    finalVerbList.append(newEntry)

# print("{}".format(finalVerbList))

db.close()
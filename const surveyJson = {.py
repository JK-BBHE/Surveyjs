const surveyJson = {
    {
  "title": "25XXX – Projektname – Erfassungsbogen für ein potenzielles Nahwärmenetz",
  "description": "erstellt von: BBH Engineering GmbH\r\nAdresse: BBH Engineering GmbH, Agrippinawerft 26-30, 50678 Köln\r\n\r\nim Auftrag von: \r\nXX\r\n\r\nDatenschutzerklärung\r\nIn den nachfolgenden Fragen soll das Potenzial für eine mögliche Nahwärmeversorgung in ihrer Ortschaft ermittelt werden.  \r\nIn diesem Zuge werden die Adressen sowie die Eckpunkte der jeweiligen aktuellen Wärme- und Stromerzeugung je Haushalt abgefragt. Ihre Personendaten (Name) sind für die Umfrage nicht erforderlich. Lediglich die Adresse des Haushaltes wird zur geographischen Bewertung im Zusammenhang mit einem möglichen Nahwärmesystem abgefragt.\r\n\r\nDie erhobenen Daten werden ausschließlich zum Zwecke der Auslegung der Anlagen und des Wärmenetzes innerhalb des benannten Projektes genutzt. Eine anderweitige Nutzung oder Weitergabe der Daten an Dritte ist ausgeschlossen.\r\nAuch bei einer Umfrage haben Sie gemäß Datenschutz gegenüber dem Informationsträger das Recht auf Auskunft sowie Löschung Ihrer personenbezogenen Daten. Sie können diese Einwilligungserklärung jederzeit unter info@bbh-engineering.de widerrufen. Nach erfolgtem Widerruf werden Ihre Daten gelöscht und unzugänglich aufbewahrt.\r\n\r\nDiese Umfrage wird durch folgenden Auftragnehmer ausgewertet: BBH Engineering GmbH.",
  "logo": "https://api.surveyjs.io/private/Surveys/files?name=b14885fc-366d-456e-bf63-2be99364d672",
  "pages": [
    {
      "name": "datenschutz_und_datum",
      "elements": [
        {
          "type": "radiogroup",
          "name": "datenschutz",
          "title": "Zustimmung zur Datenschutzerklärung\n\nIch habe die Datenschutzerklärung von BBH Engineering GmbH gelesen und bin mit der Verarbeitung meiner Daten einverstanden.",
          "isRequired": true,
          "choices": [
            {
              "value": "ja",
              "text": "Ja, ich stimme zu"
            },
            {
              "value": "nein",
              "text": "Nein, ich stimme nicht zu"
            }
          ]
        },
        {
          "type": "text",
          "name": "datum",
          "title": "Datum",
          "defaultValueExpression": "today()",
          "isRequired": true,
          "inputType": "date"
        }
      ]
    },
    {
      "name": "person",
      "elements": [
        {
          "type": "panel",
          "name": "person_panel",
          "title": "Persönliche Angaben (Anschrift des Anschlussobjekts)",
          "elements": [
            {
              "type": "text",
              "name": "vorname",
              "title": "Vorname"
            },
            {
              "type": "text",
              "name": "nachname",
              "title": "Nachname"
            },
            {
              "type": "text",
              "name": "adresse",
              "title": "Adresse (Straße)",
              "isRequired": true
            },
            {
              "type": "text",
              "name": "question2",
              "title": " Adresse (Hausnummer)",
              "isRequired": true
            },
            {
              "type": "text",
              "name": "question1",
              "title": "Adresse (PLZ)",
              "isRequired": true,
              "inputType": "number",
              "min": 9999,
              "max": 100000
            },
            {
              "type": "text",
              "name": "question3",
              "title": "Adresse (Ort)",
              "isRequired": true
            }
          ]
        },
        {
          "type": "panel",
          "name": "anschluss_panel",
          "title": "Frage der Anschlussbereitschaft",
          "elements": [
            {
              "type": "radiogroup",
              "name": "anschluss_bereitschaft",
              "title": "Für den Fall, dass das Projekt umgesetzt wird und sich ein für Sie attraktiver Wärmepreis realisieren lässt: Würden Sie sich an das Nahwärmenetz der Zentralheizung anschließen?",
              "isRequired": true,
              "choices": [
                {
                  "value": "ja",
                  "text": "Ja"
                },
                {
                  "value": "nein",
                  "text": "Nein"
                }
              ]
            },
            {
              "type": "comment",
              "name": "anschluss_nein_begruendung",
              "visibleIf": "{anschluss_bereitschaft} = 'nein'",
              "title": "Wenn „Nein“, warum nicht:"
            }
          ]
        }
      ]
    },
    {
      "name": "gebaeudetyp",
      "elements": [
        {
          "type": "radiogroup",
          "name": "Gebaeudetyp",
          "title": "Angaben zum Gebäudetyp:",
          "isRequired": true,
          "choices": [
            {
              "value": "einfamilienhaus",
              "text": "Einfamilienhaus"
            },
            {
              "value": "mehrfamilienhaus",
              "text": "Mehrfamilienhaus"
            },
            {
              "value": "apartmentblock",
              "text": "Apartmentblock"
            },
            {
              "value": "nicht_wohnen",
              "text": "Nicht-Wohngebäude"
            }
          ]
        }
      ]
    },
    {
      "name": "einfamilienhaus",
      "visibleIf": "{gebaeudetyp} = 'einfamilienhaus'",
      "title": "Spezifikation Einfamilienhaus",
      "elements": [
        {
          "type": "radiogroup",
          "name": "efh_baujahrklasse",
          "title": "9. Angaben zum Gebäudetyp:",
          "choices": [
            "Einfamilienhaus (bis 1918)",
            "Einfamilienhaus (1919–1948)",
            "Einfamilienhaus (1949–1957)",
            "Einfamilienhaus (1958–1968)",
            "Einfamilienhaus (1969–1978)",
            "Einfamilienhaus (1979–1983)",
            "Einfamilienhaus (1984–1994)",
            "Einfamilienhaus (1995–2001)",
            "Einfamilienhaus (ab 2002)",
            "Einfamilienhaus (KfW 40)",
            "Einfamilienhaus (KfW 55)",
            "Einfamilienhaus (KfW 70)",
            "Einfamilienhaus (KfW 85)",
            "Einfamilienhaus (Passivhaus)"
          ],
          "colCount": 2
        },
        {
          "type": "text",
          "name": "efh_personen",
          "title": "10. Wie viele Personen wohnen im Haus? [Anzahl] (für die Abschätzung des Trinkwarmwasserbedarfs)",
          "inputType": "number"
        },
        {
          "type": "text",
          "name": "question4",
          "title": "Gesamte zu beheizende Fläche des Gebäudes [m²]",
          "isRequired": true,
          "inputType": "number",
          "min": 30,
          "max": 15000
        },
        {
          "type": "boolean",
          "name": "SM -EFH",
          "title": "11. Wurden schon oder sind Sanierungsmaßnahmen am Gebäude durchgeführt oder geplant?"
        },
        {
          "type": "matrixdynamic",
          "name": "efh_sanierung",
          "visible": false,
          "visibleIf": "{SM -EFH} = true",
          "title": "Welche sanierungsmaßnahmen am Gebäude durchgeführt oder geplant?",
          "columns": [
            {
              "name": "Art der Maßnahe",
              "cellType": "dropdown",
              "choices": [
                "Dachsanierung",
                "Außenwanddämmung",
                "Innendämmung",
                "Fenstersanierung",
                "Heizungserneuerung",
                "Sonstiges"
              ],
              "storeOthersAsComment": true
            },
            {
              "name": "Durchführungsjahr",
              "cellType": "text",
              "inputType": "number",
              "min": 1900,
              "max": 2030,
              "step": 1
            },
            {
              "name": "Column 3",
              "visible": false
            }
          ],
          "choices": [
            "Dachsanierung",
            "Außenwanddämmung",
            "Innendämmung",
            "Fenstersanierung",
            "Heizungserneuerung",
            "Sonstiges"
          ],
          "placeholder": "auswählen"
        }
      ]
    },
    {
      "name": "mehrfamilienhaus",
      "visibleIf": "{gebaeudetyp} = 'mehrfamilienhaus'",
      "title": "Spezifikation Mehrfamilienhaus",
      "elements": [
        {
          "type": "radiogroup",
          "name": "mfh_baujahrklasse",
          "title": "13. Angaben zum Gebäudetyp:",
          "isRequired": true,
          "choices": [
            "Mehrfamilienhaus (bis 1918)",
            "Mehrfamilienhaus (1919–1948)",
            "Mehrfamilienhaus (1949–1957)",
            "Mehrfamilienhaus (1958–1968)",
            "Mehrfamilienhaus (1969–1978)",
            "Mehrfamilienhaus (1979–1983)",
            "Mehrfamilienhaus (1984–1994)",
            "Mehrfamilienhaus (1995–2001)",
            "Mehrfamilienhaus (ab 2002)",
            "Mehrfamilienhaus (KfW 40)",
            "Mehrfamilienhaus (KfW 55)",
            "Mehrfamilienhaus (KfW 70)",
            "Mehrfamilienhaus (KfW 85)",
            "Mehrfamilienhaus (Passivhaus)"
          ],
          "colCount": 2
        },
        {
          "type": "text",
          "name": "question7",
          "title": "Gesamte zu beheizende Fläche des Gebäudes [m²]",
          "isRequired": true,
          "inputType": "number",
          "min": 30,
          "max": 15000
        },
        {
          "type": "text",
          "name": "ap_wohneinheiten",
          "title": "19. Bitte geben Sie die Anzahl der Wohneinheiten an [Anzahl WE]",
          "inputType": "number"
        },
        {
          "type": "text",
          "name": "mfh_personen",
          "title": "15. Wie viele Personen wohnen im Haus? [Anzahl] (für die Abschätzung des Trinkwarmwasserbedarfs)",
          "inputType": "number"
        },
        {
          "type": "boolean",
          "name": "SM-MFH",
          "title": "11. Wurden schon oder sind Sanierungsmaßnahmen am Gebäude durchgeführt oder geplant?"
        },
        {
          "type": "matrixdynamic",
          "name": "MFH_sanierung",
          "visible": false,
          "visibleIf": "{SM-MFH} = true",
          "title": "Welche sanierungsmaßnahmen am Gebäude durchgeführt oder geplant?",
          "columns": [
            {
              "name": "Art der Maßnahe",
              "cellType": "dropdown",
              "choices": [
                "Dachsanierung",
                "Außenwanddämmung",
                "Innendämmung",
                "Fenstersanierung",
                "Heizungserneuerung",
                "Sonstiges"
              ],
              "storeOthersAsComment": true
            },
            {
              "name": "Durchführungsjahr",
              "cellType": "text",
              "inputType": "number",
              "min": 1900,
              "max": 2030,
              "step": 1
            },
            {
              "name": "Column 3",
              "visible": false
            }
          ],
          "choices": [
            "Dachsanierung",
            "Außenwanddämmung",
            "Innendämmung",
            "Fenstersanierung",
            "Heizungserneuerung",
            "Sonstiges"
          ],
          "placeholder": "auswählen"
        }
      ]
    },
    {
      "name": "apartmentblock",
      "visibleIf": "{gebaeudetyp} = 'apartmentblock'",
      "title": "Spezifikation Apartmentblock",
      "elements": [
        {
          "type": "radiogroup",
          "name": "ap_baujahrklasse",
          "title": "18. Angaben zum Gebäudetyp:",
          "isRequired": true,
          "choices": [
            "Apartmentblock (bis 1918)",
            "Apartmentblock (1919–1948)",
            "Apartmentblock (1949–1957)",
            "Apartmentblock (1958–1968)",
            "Apartmentblock (1969–1978)",
            "Apartmentblock (1979–1983)",
            "Apartmentblock (1984–1994)",
            "Apartmentblock (1995–2001)",
            "Apartmentblock (ab 2002)",
            "Apartmentblock (KfW 40)",
            "Apartmentblock (KfW 55)",
            "Apartmentblock (KfW 70)",
            "Apartmentblock (KfW 85)",
            "Apartmentblock (Passivhaus)"
          ],
          "colCount": 2
        },
        {
          "type": "text",
          "name": "question9",
          "title": "Gesamte zu beheizende Fläche des Gebäudes [m²]",
          "isRequired": true,
          "inputType": "number",
          "min": 30,
          "max": 15000
        },
        {
          "type": "text",
          "name": "question10",
          "title": "Bitte geben Sie die Anzahl der Wohneinheiten an [Anzahl WE]",
          "inputType": "number"
        },
        {
          "type": "text",
          "name": "ap_personen",
          "title": "20. Wie viele Personen wohnen im Haus? [Anzahl] (für die Abschätzung des Trinkwarmwasserbedarfs)",
          "inputType": "number"
        },
        {
          "type": "boolean",
          "name": "SM-AP",
          "title": "11. Wurden schon oder sind Sanierungsmaßnahmen am Gebäude durchgeführt oder geplant?"
        },
        {
          "type": "matrixdynamic",
          "name": "AP_sanierung",
          "visible": false,
          "visibleIf": "{SM-AP} = true",
          "title": "Welche sanierungsmaßnahmen am Gebäude durchgeführt oder geplant?",
          "columns": [
            {
              "name": "Art der Maßnahe",
              "cellType": "dropdown",
              "choices": [
                "Dachsanierung",
                "Außenwanddämmung",
                "Innendämmung",
                "Fenstersanierung",
                "Heizungserneuerung",
                "Sonstiges"
              ],
              "storeOthersAsComment": true
            },
            {
              "name": "Durchführungsjahr",
              "cellType": "text",
              "inputType": "number",
              "min": 1900,
              "max": 2030,
              "step": 1
            },
            {
              "name": "Column 3",
              "visible": false
            }
          ],
          "choices": [
            "Dachsanierung",
            "Außenwanddämmung",
            "Innendämmung",
            "Fenstersanierung",
            "Heizungserneuerung",
            "Sonstiges"
          ],
          "placeholder": "auswählen"
        }
      ]
    },
    {
      "name": "nichtwohn",
      "visibleIf": "{gebaeudetyp} = 'nicht_wohnen'",
      "title": "Spezifikation Nicht-Wohngebäude",
      "elements": [
        {
          "type": "radiogroup",
          "name": "nw_gebaeudetyp",
          "title": "23. Angaben zum Nicht-Wohngebäudetyp:",
          "isRequired": true,
          "choices": [
            "Alten-/Pflegeheim",
            "Büro",
            "Einkaufszentrum",
            "Einzelhandel",
            "Fitnesscenter",
            "Hotel",
            "Kantine",
            "Kindergarten",
            "Krankenhaus",
            "Museum",
            "Restaurant",
            "Gewerbe",
            "Sonstiges"
          ],
          "colCount": 2
        },
        {
          "type": "text",
          "name": "question11",
          "title": "Gesamte zu beheizende Fläche des Gebäudes [m²]",
          "isRequired": true,
          "inputType": "number",
          "min": 30,
          "max": 15000
        },
        {
          "type": "radiogroup",
          "name": "nw_trinkwarmwasser",
          "title": "24. Wird in dem Nicht-Wohngebäude Trinkwarmwasser bereitgestellt?",
          "choices": [
            "Ja, über die Heizung",
            "Ja, über eine separate TWWB",
            "Nein",
            "Sonstiges"
          ]
        }
      ]
    },
    {
      "name": "waermeerzeugung",
      "title": "Angaben zur Wärmeerzeugung",
      "elements": [
        {
          "type": "checkbox",
          "name": "heizungssysteme",
          "visible": false,
          "title": "25. Ihr derzeitiges Heizungssystem (Mehrfachauswahl möglich). Falls Sie ein nicht aufgeführtes System installiert haben, geben Sie dies bitte unter Sonstiges an.",
          "isRequired": true,
          "choices": [
            "Heizöl Zentralheizung",
            "Erdgas Zentralheizung",
            "Flüssiggas Zentralheizung",
            "Holz Zentralheizung",
            "Stromnachtspeicher",
            "Wärmepumpe",
            "Kamin als Ergänzung",
            "Sonstiges"
          ]
        },
        {
          "type": "text",
          "name": "heizung_baujahr",
          "visible": false,
          "title": "26. Baujahr der Heizungsanlage [Jahr]",
          "inputType": "number"
        },
        {
          "type": "text",
          "name": "heizung_leistung",
          "visible": false,
          "title": "27. Nennheizleistung der Heizungsanlage [kW]",
          "inputType": "number"
        },
        {
          "type": "radiogroup",
          "name": "holzofen_kamin",
          "visible": false,
          "title": "28. Ist ein Holzofen / Kamin vorhanden? (ggf. mit direkter Verbindung in das Heizsystem)",
          "choices": [
            "Ja, ohne Verbindung zum Heizsystem",
            "Ja, mit Verbindung zum Heizsystem",
            "Nein"
          ]
        },
        {
          "type": "checkbox",
          "name": "heatingSystems",
          "title": "Ihr derzeitiges Heizungssystem (Mehrfachauswahl möglich).",
          "choices": [
            {
              "value": "oil",
              "text": "Heizöl Zentralheizung"
            },
            {
              "value": "gas",
              "text": "Erdgas Zentralheizung"
            },
            {
              "value": "lpg",
              "text": "Flüssiggas Zentralheizung"
            },
            {
              "value": "wood",
              "text": "Holz Zentralheizung"
            },
            {
              "value": "night",
              "text": "Stromnachtspeicher"
            },
            {
              "value": "hp",
              "text": "Wärmepumpe"
            },
            {
              "value": "fireplace",
              "text": "Kamin als Ergänzung"
            },
            {
              "value": "other",
              "text": "Sonstiges"
            }
          ]
        },
        {
          "type": "matrixdropdown",
          "name": "heatingTechDetails",
          "visibleIf": "{heatingSystems.length} > 0",
          "title": "Bitte geben Sie Baujahr und Heizlast für die ausgewählten Systeme an.",
          "isRequired": true,
          "columns": [
            {
              "name": "baujahr",
              "title": "Baujahr",
              "cellType": "text",
              "inputType": "number",
              "min": 1900,
              "max": 2026
            },
            {
              "name": "heizlast",
              "title": "Heizlast [kW]",
              "cellType": "text",
              "inputType": "number",
              "min": 3,
              "max": 1500
            }
          ],
          "rows": [
            {
              "value": "oil",
              "text": "Heizöl Zentralheizung",
              "visibleIf": "{heatingSystems} contains 'oil'"
            },
            {
              "value": "gas",
              "text": "Erdgas Zentralheizung",
              "visibleIf": "{heatingSystems} contains 'gas'"
            },
            {
              "value": "lpg",
              "text": "Flüssiggas Zentralheizung",
              "visibleIf": "{heatingSystems} contains 'lpg'"
            },
            {
              "value": "wood",
              "text": "Holz Zentralheizung",
              "visibleIf": "{heatingSystems} contains 'wood'"
            },
            {
              "value": "night",
              "text": "Stromnachtspeicher",
              "visibleIf": "{heatingSystems} contains 'night'"
            },
            {
              "value": "hp",
              "text": "Wärmepumpe",
              "visibleIf": "{heatingSystems} contains 'hp'"
            },
            {
              "value": "fireplace",
              "text": "Kamin als Ergänzung",
              "visibleIf": "{heatingSystems} contains 'fireplace'"
            },
            {
              "value": "other",
              "text": "Sonstiges",
              "visibleIf": "{heatingSystems} contains 'other'"
            }
          ]
        },
        {
          "type": "matrixdropdown",
          "name": "heatingConsumption",
          "visibleIf": "{heatingSystems.length} > 0",
          "title": "Bitte geben Sie den Energieverbrauch der letzten 3 Jahre an.",
          "defaultValue": {
            "oil": {
              "fuel": "oil"
            },
            "gas": {
              "fuel": "gas"
            },
            "lpg": {
              "fuel": "lpg"
            },
            "wood": {
              "fuel": "wood"
            },
            "night": {
              "fuel": "night"
            },
            "hp": {
              "fuel": "hp"
            },
            "fireplace": {
              "fuel": "fireplace"
            },
            "other": {
              "fuel": "other"
            }
          },
          "isRequired": true,
          "columns": [
            {
              "name": "year1",
              "title": "Verbrauch von 2022",
              "cellType": "text",
              "inputType": "number",
              "min": 0,
              "placeholder": "Wert"
            },
            {
              "name": "year2",
              "title": "Verbrauch  von 2023",
              "cellType": "text",
              "inputType": "number",
              "min": 0,
              "placeholder": "Wert"
            },
            {
              "name": "year3",
              "title": "Verbrauch im von 2024",
              "cellType": "text",
              "inputType": "number",
              "min": 0,
              "placeholder": "Wert"
            },
            {
              "name": "unit",
              "title": "Einheit",
              "cellType": "dropdown",
              "choices": [
                {
                  "value": "kwh",
                  "text": "kWh"
                },
                {
                  "value": "l",
                  "text": "Liter"
                },
                {
                  "value": "m3",
                  "text": "m³"
                },
                {
                  "value": "rm",
                  "text": "Rm"
                },
                {
                  "value": "tonne",
                  "text": "Tonne"
                },
                {
                  "value": "srm",
                  "text": "Srm"
                }
              ],
              "choicesVisibleIf": "(({row.fuel} = 'oil' and ({item} = 'l' or {item} = 'm3' or {item} = 'kwh')) or ({row.fuel} = 'gas' and ({item} = 'm3' or {item} = 'kwh')) or ({row.fuel} = 'lpg' and ({item} = 'm3' or {item} = 'kwh')) or ({row.fuel} = 'night' and {item} = 'kwh') or ({row.fuel} = 'wood' and ({item} = 'rm' or {item} = 'kwh')) or ({row.fuel} = 'pellets' and ({item} = 'tonne' or {item} = 'kwh')) or ({row.fuel} = 'chips' and ({item} = 'srm' or {item} = 'kwh')))"
            },
            {
              "name": "fuel",
              "cellType": "text",
              "visible": false
            }
          ],
          "rows": [
            {
              "value": "oil",
              "text": "Heizöl Zentralheizung",
              "visibleIf": "{heatingSystems} contains 'oil'"
            },
            {
              "value": "gas",
              "text": "Erdgas Zentralheizung",
              "visibleIf": "{heatingSystems} contains 'gas'"
            },
            {
              "value": "lpg",
              "text": "Flüssiggas Zentralheizung",
              "visibleIf": "{heatingSystems} contains 'lpg'"
            },
            {
              "value": "wood",
              "text": "Holz Zentralheizung",
              "visibleIf": "{heatingSystems} contains 'wood'"
            },
            {
              "value": "night",
              "text": "Stromnachtspeicher",
              "visibleIf": "{heatingSystems} contains 'night'"
            },
            {
              "value": "hp",
              "text": "Wärmepumpe",
              "visibleIf": "{heatingSystems} contains 'hp'"
            },
            {
              "value": "fireplace",
              "text": "Kamin als Ergänzung",
              "visibleIf": "{heatingSystems} contains 'fireplace'"
            },
            {
              "value": "other",
              "text": "Sonstiges",
              "visibleIf": "{heatingSystems} contains 'other'"
            }
          ]
        },
        {
          "type": "radiogroup",
          "name": "solaranlage",
          "title": "29. Ist eine Solaranlage zur Heizungsunterstützung oder Warmwassererzeugung vorhanden?",
          "choices": [
            "Ja",
            "Nein"
          ]
        }
      ]
    },
    {
      "name": "brennstoff_verbrauch",
      "visible": false,
      "elements": [
        {
          "type": "checkbox",
          "name": "brennstoffe",
          "visible": false,
          "title": "30. Ihr aktueller und vergangener Brennstoffverbrauch (hier nur angeben, was durch die Nahwärme ersetzt wird). Welche Brennstoffe nutzen Sie?",
          "choices": [
            "Heizöl [l/Jahr]",
            "Erdgas [m³/Jahr]",
            "Flüssiggas [l/Jahr]",
            "Strom [kWh/Jahr]",
            "Scheitholz [Raummeter/Jahr]",
            "Holz-Pellets [t/Jahr]",
            "Hackschnitzel [Srm/Jahr]"
          ]
        },
        {
          "type": "comment",
          "name": "verbrauch_2024",
          "visible": false,
          "title": "31. Angabe des Verbrauchs – Jahr 2024\n\nHinweis: Bitte die in „30“ angekreuzte Brennstoff-Einheit berücksichtigen. Sollten keine Daten zum Brennstoffverbrauch vorliegen, können Sie auch die Wärmemenge in kWh angeben."
        },
        {
          "type": "comment",
          "name": "verbrauch_2023",
          "visible": false,
          "title": "32. Angabe des Verbrauchs – Jahr 2023\n\nHinweis: Bitte die in „30“ angekreuzte Brennstoff-Einheit berücksichtigen. Sollten keine Daten zum Brennstoffverbrauch vorliegen, können Sie auch die Wärmemenge in kWh angeben."
        },
        {
          "type": "comment",
          "name": "verbrauch_2022",
          "visible": false,
          "title": "33. Angabe des Verbrauchs – Jahr 2022\n\nHinweis: Bitte die in „30“ angekreuzte Brennstoff-Einheit berücksichtigen. Sollten keine Daten zum Brennstoffverbrauch vorliegen, können Sie auch die Wärmemenge in kWh angeben."
        },
        {
          "type": "comment",
          "name": "verbrauch_ergaenzende_systeme",
          "visible": false,
          "title": "34. Falls ein ergänzendes System vorliegt (Kamin, Solaranlage) – Angabe des dort eingesetzten Brennstoffs und Verbrauchs."
        }
      ]
    },
    {
      "name": "bemerkungen",
      "elements": [
        {
          "type": "comment",
          "name": "hinweise_bemerkungen",
          "title": "35. Hinweise / Bemerkungen"
        }
      ]
    }
  ],
  "triggers": [
    {
      "type": "complete",
      "expression": "{anschluss_bereitschaft} <> 'ja'"
    },
    {
      "type": "complete",
      "expression": "{datenschutz} = 'nein'"
    }
  ],
  "showQuestionNumbers": "on"
}
}
const surveyJson = {
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
              "name": "strasse",
              "title": "Adresse (Straße)",
              "isRequired": true
            },
            {
              "type": "text",
              "name": "hausnummer",
              "title": " Adresse (Hausnummer)",
              "isRequired": true
            },
            {
              "type": "text",
              "name": "plz",
              "title": "Adresse (PLZ)",
              "isRequired": true,
              "inputType": "number",
              "min": 9999,
              "max": 100000
            },
            {
              "type": "text",
              "name": "ort",
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
              "name": "anschlussbereitschaft",
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
              "visibleIf": "{anschlussbereitschaft} = 'nein'",
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
          "title": "Angaben zum Gebäudetyp:",
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
          "name": "efh_m2",
          "title": "Gesamte zu beheizende Fläche des Gebäudes [m²]",
          "isRequired": true,
          "inputType": "number",
          "min": 30,
          "max": 15000
        },
        {
          "type": "text",
          "name": "efh_personen",
          "title": "Wie viele Personen wohnen im Haus? [Anzahl] (für die Abschätzung des Trinkwarmwasserbedarfs)",
          "inputType": "number"
        },
        {
          "type": "boolean",
          "name": "efh_sm",
          "title": "Wurden schon oder sind Sanierungsmaßnahmen am Gebäude durchgeführt oder geplant?"
        },
        {
          "type": "matrixdynamic",
          "name": "efh_sanierung",
          "visible": false,
          "visibleIf": "{efh_sm} = true",
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
          "title": "Angaben zum Gebäudetyp:",
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
          "name": "mfh_m2",
          "title": "Gesamte zu beheizende Fläche des Gebäudes [m²]",
          "isRequired": true,
          "inputType": "number",
          "min": 30,
          "max": 15000
        },
        {
          "type": "text",
          "name": "mfh_WE",
          "title": "Bitte geben Sie die Anzahl der Wohneinheiten an [Anzahl WE]",
          "inputType": "number"
        },
        {
          "type": "text",
          "name": "mfh_personen",
          "title": " Wie viele Personen wohnen im Haus? [Anzahl] (für die Abschätzung des Trinkwarmwasserbedarfs)",
          "inputType": "number"
        },
        {
          "type": "boolean",
          "name": "mfh_sm",
          "title": "Wurden schon oder sind Sanierungsmaßnahmen am Gebäude durchgeführt oder geplant?"
        },
        {
          "type": "matrixdynamic",
          "name": "mfh_sanierung",
          "visible": false,
          "visibleIf": "{mfh_sm} = true",
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
          "title": "Angaben zum Gebäudetyp:",
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
          "name": "ap_m2",
          "title": "Gesamte zu beheizende Fläche des Gebäudes [m²]",
          "isRequired": true,
          "inputType": "number",
          "min": 30,
          "max": 15000
        },
        {
          "type": "text",
          "name": "ap_WE",
          "title": "Bitte geben Sie die Anzahl der Wohneinheiten an [Anzahl WE]",
          "inputType": "number"
        },
        {
          "type": "text",
          "name": "ap_personen",
          "title": "Wie viele Personen wohnen im Haus? [Anzahl] (für die Abschätzung des Trinkwarmwasserbedarfs)",
          "inputType": "number"
        },
        {
          "type": "boolean",
          "name": "ap_sm",
          "title": "Wurden schon oder sind Sanierungsmaßnahmen am Gebäude durchgeführt oder geplant?"
        },
        {
          "type": "matrixdynamic",
          "name": "ap_sanierung",
          "visible": false,
          "visibleIf": "{ap_sm} = true",
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
          "title": "Angaben zum Nicht-Wohngebäudetyp:",
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
          "name": "nw_m2",
          "title": "Gesamte zu beheizende Fläche des Gebäudes [m²]",
          "isRequired": true,
          "inputType": "number",
          "min": 30,
          "max": 15000
        },
        {
          "type": "radiogroup",
          "name": "nw_trinkwarmwasser",
          "title": "Wird in dem Nicht-Wohngebäude Trinkwarmwasser bereitgestellt?",
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
          "name": "heizung_typ",
          "title": "Ihr derzeitiges Heizungssystem (Mehrfachauswahl möglich).",
          "isRequired": true,
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
          "name": "heizung_bj_hl",
          "visibleIf": "{heizung_typ.length} > 0",
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
              "visibleIf": "{heizung_typ} contains 'oil'"
            },
            {
              "value": "gas",
              "text": "Erdgas Zentralheizung",
              "visibleIf": "{heizung_typ} contains 'gas'"
            },
            {
              "value": "lpg",
              "text": "Flüssiggas Zentralheizung",
              "visibleIf": "{heizung_typ} contains 'lpg'"
            },
            {
              "value": "wood",
              "text": "Holz Zentralheizung",
              "visibleIf": "{heizung_typ} contains 'wood'"
            },
            {
              "value": "night",
              "text": "Stromnachtspeicher",
              "visibleIf": "{heizung_typ} contains 'night'"
            },
            {
              "value": "hp",
              "text": "Wärmepumpe",
              "visibleIf": "{heizung_typ} contains 'hp'"
            },
            {
              "value": "fireplace",
              "text": "Kamin als Ergänzung",
              "visibleIf": "{heizung_typ} contains 'fireplace'"
            },
            {
              "value": "other",
              "text": "Sonstiges",
              "visibleIf": "{heizung_typ} contains 'other'"
            }
          ]
        },
        {
          "type": "matrixdropdown",
          "name": "heizung_verbrauch",
          "visibleIf": "{heizung_typ.length} > 0",
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
              "visibleIf": "{heizung_typ} contains 'oil'"
            },
            {
              "value": "gas",
              "text": "Erdgas Zentralheizung",
              "visibleIf": "{heizung_typ} contains 'gas'"
            },
            {
              "value": "lpg",
              "text": "Flüssiggas Zentralheizung",
              "visibleIf": "{heizung_typ} contains 'lpg'"
            },
            {
              "value": "wood",
              "text": "Holz Zentralheizung",
              "visibleIf": "{heizung_typ} contains 'wood'"
            },
            {
              "value": "night",
              "text": "Stromnachtspeicher",
              "visibleIf": "{heizung_typ} contains 'night'"
            },
            {
              "value": "hp",
              "text": "Wärmepumpe",
              "visibleIf": "{heizung_typ} contains 'hp'"
            },
            {
              "value": "fireplace",
              "text": "Kamin als Ergänzung",
              "visibleIf": "{heizung_typ} contains 'fireplace'"
            },
            {
              "value": "other",
              "text": "Sonstiges",
              "visibleIf": "{heizung_typ} contains 'other'"
            }
          ]
        },
        {
          "type": "radiogroup",
          "name": "frage_solaranlage",
          "title": "Ist eine Solaranlage zur Heizungsunterstützung oder Warmwassererzeugung vorhanden?",
          "choices": [
            "Ja",
            "Nein"
          ]
        }
      ]
    },
    {
      "name": "bemerkungen",
      "elements": [
        {
          "type": "comment",
          "name": "hinweise_bemerkungen",
          "title": "Hinweise / Bemerkungen"
        }
      ]
    }
  ],
  "triggers": [
    {
      "type": "complete",
      "expression": "{anschlussbereitschaft} <> 'ja'"
    },
    {
      "type": "complete",
      "expression": "{datenschutz} = 'nein'"
    }
  ],
  "showQuestionNumbers": "on"
}

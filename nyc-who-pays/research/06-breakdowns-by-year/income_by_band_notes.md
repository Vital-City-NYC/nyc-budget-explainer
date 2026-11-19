# IBO NYC personal income tax liability before credits, by income band, tax years 2006-2023

All values: IBO workbook sheet "8. Tax Liability", nominal NYAGI rows 19-38 plus "All Filers" row 39. Column B = "Number of Filers"; column F = "NYC Personal Income Tax Liability Before Credits" ($ millions). Cell values below are exactly as stored in the file (full precision). Sheet "2. Summary" column B filer counts and row labels were checked against sheet 8 for every row of every year and match.

Base folder: the working folder where the files were downloaded and read (not kept in the repository); file names below are relative to it.

## Tax year 2006

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2006pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20221201182815id_/https://www.ibo.nyc.ny.us/RevenueSpending/2006pitdata.xlsx
- File: 2006pitdata.xlsx (196228 bytes), MD5 78ca37e51e097623013c668c8f38403d
- Local copy: src/2006pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2006"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,380,500; liability before credits 809.370707 -> 809.4
    row 19  "Under $0"  B=40013  F=0
    row 20  "$0 - $9,999"  B=656176  F=2.823297
    row 21  "$10,000 - $19,999"  B=575363  F=67.680817
    row 22  "$20,000 - $29,999"  B=447579  F=179.149504
    row 23  "$30,000 - $39,999"  B=379255  F=269.64586
    row 24  "$40,000 - $49,999"  B=282114  F=290.071229
i2 $50,000 to $99,999: returns 595,969; liability before credits 1081.383524 -> 1081.4
    row 25  "$50,000 - $59,999"  B=194640  F=261.183267
    row 26  "$60,000 - $74,999"  B=202800  F=353.76324
    row 27  "$75,000 - $99,999"  B=198529  F=466.437017
i3 $100,000 to $199,999: returns 220,390; liability before credits 870.238282 -> 870.2
    row 28  "$100,000 - $124,999"  B=103137  F=324.399023
    row 29  "$125,000 - $149,999"  B=55755  F=223.266426
    row 30  "$150,000 - $199,999"  B=61498  F=322.572833
i4 $200,000 to $499,999: returns 78,035; liability before credits 743.67752 -> 743.7
    row 31  "$200,000 - $349,999"  B=59169  F=484.613099
    row 32  "$350,000 - $499,999"  B=18866  F=259.064421
i5 $500,000 to $999,999: returns 20,723; liability before credits 485.426351 -> 485.4
    row 33  "$500,000 - $749,999"  B=14155  F=290.870135
    row 34  "$750,000 - $999,999"  B=6568  F=194.556216
i6 $1 million and over: returns 18,662; liability before credits 2885.349066 -> 2885.3
    row 35  "$1,000,000 - $1,999,999"  B=9872  F=472.455897
    row 36  "$2,000,000 - $4,999,999"  B=5755  F=606.192134
    row 37  "$5,000,000 - $9,999,999"  B=1743  F=414.797026
    row 38  "$10,000,000 and Over"  B=1292  F=1391.904009
All Filers (row 39): B=3314279  F=6875.44545
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = 0.0 ($M); rounded bands sum minus rounded total = 0.0

## Tax year 2007

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2007pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20221201205202id_/https://www.ibo.nyc.ny.us/RevenueSpending/2007pitdata.xlsx
- File: 2007pitdata.xlsx (198652 bytes), MD5 0b393a14ea6bf86b84ce8118a932cc53
- Local copy: src/2007pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2007"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,437,997; liability before credits 825.766815 -> 825.8
    row 19  "Under $0"  B=40987  F=4.7e-05
    row 20  "$0 - $9,999"  B=693861  F=2.968924
    row 21  "$10,000 - $19,999"  B=586168  F=70.368738
    row 22  "$20,000 - $29,999"  B=442165  F=175.404829
    row 23  "$30,000 - $39,999"  B=383419  F=275.84379
    row 24  "$40,000 - $49,999"  B=291397  F=301.180487
i2 $50,000 to $99,999: returns 628,549; liability before credits 1151.030913 -> 1151.0
    row 25  "$50,000 - $59,999"  B=202573  F=275.902064
    row 26  "$60,000 - $74,999"  B=212886  F=373.133688
    row 27  "$75,000 - $99,999"  B=213090  F=501.995161
i3 $100,000 to $199,999: returns 243,539; liability before credits 967.704811 -> 967.7
    row 28  "$100,000 - $124,999"  B=110640  F=351.628391
    row 29  "$125,000 - $149,999"  B=64838  F=258.483859
    row 30  "$150,000 - $199,999"  B=68061  F=357.592561
i4 $200,000 to $499,999: returns 88,471; liability before credits 863.034924 -> 863.0
    row 31  "$200,000 - $349,999"  B=65545  F=545.375631
    row 32  "$350,000 - $499,999"  B=22926  F=317.659293
i5 $500,000 to $999,999: returns 23,523; liability before credits 559.984773 -> 560.0
    row 33  "$500,000 - $749,999"  B=15773  F=328.237047
    row 34  "$750,000 - $999,999"  B=7750  F=231.747726
i6 $1 million and over: returns 22,124; liability before credits 4244.443577 -> 4244.4
    row 35  "$1,000,000 - $1,999,999"  B=11483  F=553.847977
    row 36  "$2,000,000 - $4,999,999"  B=6887  F=738.883183
    row 37  "$5,000,000 - $9,999,999"  B=2073  F=504.681725
    row 38  "$10,000,000 and Over"  B=1681  F=2447.030692
All Filers (row 39): B=3444202  F=8611.965812
Checks: band returns sum minus All Filers = 1; band liability sum minus All Filers = 1e-06 ($M); rounded bands sum minus rounded total = -0.1

## Tax year 2008

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2008pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20221201193115id_/https://www.ibo.nyc.ny.us/RevenueSpending/2008pitdata.xlsx
- File: 2008pitdata.xlsx (195005 bytes), MD5 9b625781023812c734b6c20f3311bcf9
- Local copy: src/2008pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2008"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,362,960; liability before credits 813.905307 -> 813.9
    row 19  "Under $0"  B=56767  F=0
    row 20  "$0 - $9,999"  B=656360  F=2.936495
    row 21  "$10,000 - $19,999"  B=546143  F=66.671372
    row 22  "$20,000 - $29,999"  B=446040  F=180.034734
    row 23  "$30,000 - $39,999"  B=369432  F=264.157462
    row 24  "$40,000 - $49,999"  B=288218  F=300.105244
i2 $50,000 to $99,999: returns 648,723; liability before credits 1197.307965 -> 1197.3
    row 25  "$50,000 - $59,999"  B=207209  F=284.941453
    row 26  "$60,000 - $74,999"  B=218231  F=385.910156
    row 27  "$75,000 - $99,999"  B=223283  F=526.456356
i3 $100,000 to $199,999: returns 260,596; liability before credits 1033.587315 -> 1033.6
    row 28  "$100,000 - $124,999"  B=121908  F=387.971251
    row 29  "$125,000 - $149,999"  B=65402  F=261.304108
    row 30  "$150,000 - $199,999"  B=73286  F=384.311956
i4 $200,000 to $499,999: returns 89,758; liability before credits 862.995333 -> 863.0
    row 31  "$200,000 - $349,999"  B=67804  F=562.182246
    row 32  "$350,000 - $499,999"  B=21954  F=300.813087
i5 $500,000 to $999,999: returns 22,707; liability before credits 539.070598 -> 539.1
    row 33  "$500,000 - $749,999"  B=15131  F=313.794193
    row 34  "$750,000 - $999,999"  B=7576  F=225.276405
i6 $1 million and over: returns 18,935; liability before credits 3045.663973 -> 3045.7
    row 35  "$1,000,000 - $1,999,999"  B=10557  F=508.569691
    row 36  "$2,000,000 - $4,999,999"  B=5695  F=602.159828
    row 37  "$5,000,000 - $9,999,999"  B=1498  F=359.283118
    row 38  "$10,000,000 and Over"  B=1185  F=1575.651336
All Filers (row 39): B=3403680  F=7492.530491
Checks: band returns sum minus All Filers = -1; band liability sum minus All Filers = -0.0 ($M); rounded bands sum minus rounded total = 0.1

## Tax year 2009

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2009pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20221201203716id_/https://www.ibo.nyc.ny.us/RevenueSpending/2009pitdata.xlsx
- File: 2009pitdata.xlsx (123573 bytes), MD5 0c90050ff545fb37c0ebe3891ce222ea
- Local copy: src/2009pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2009"
- Header row 3 (non-empty cells): "Income Groups" | "Number of filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,434,455; liability before credits 801.701652 -> 801.7
    row 19  "Under $0"  B=54831  F=0
    row 20  "$0 - $9,999"  B=710766  F=3.29913
    row 21  "$10,000 - $19,999"  B=592134  F=71.531181
    row 22  "$20,000 - $29,999"  B=446857  F=178.68837
    row 23  "$30,000 - $39,999"  B=345495  F=250.513039
    row 24  "$40,000 - $49,999"  B=284372  F=297.669932
i2 $50,000 to $99,999: returns 650,292; liability before credits 1207.235655 -> 1207.2
    row 25  "$50,000 - $59,999"  B=209127  F=286.996899
    row 26  "$60,000 - $74,999"  B=217809  F=385.93919
    row 27  "$75,000 - $99,999"  B=223356  F=534.299566
i3 $100,000 to $199,999: returns 258,335; liability before credits 1028.953964 -> 1029.0
    row 28  "$100,000 - $124,999"  B=116776  F=370.445171
    row 29  "$125,000 - $149,999"  B=68648  F=276.346859
    row 30  "$150,000 - $199,999"  B=72911  F=382.161934
i4 $200,000 to $499,999: returns 84,501; liability before credits 802.922527 -> 802.9
    row 31  "$200,000 - $349,999"  B=64937  F=536.10841
    row 32  "$350,000 - $499,999"  B=19564  F=266.814117
i5 $500,000 to $999,999: returns 19,144; liability before credits 450.656822 -> 450.7
    row 33  "$500,000 - $749,999"  B=13142  F=272.314485
    row 34  "$750,000 - $999,999"  B=6002  F=178.342337
i6 $1 million and over: returns 14,795; liability before credits 2254.621135 -> 2254.6
    row 35  "$1,000,000 - $1,999,999"  B=8381  F=408.97151
    row 36  "$2,000,000 - $4,999,999"  B=4512  F=486.012881
    row 37  "$5,000,000 - $9,999,999"  B=1085  F=265.420547
    row 38  "$10,000,000 and Over"  B=817  F=1094.216197
All Filers (row 39): B=3461521  F=6546.091756
Checks: band returns sum minus All Filers = 1; band liability sum minus All Filers = -1e-06 ($M); rounded bands sum minus rounded total = 0.0

## Tax year 2010

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2010pitdata.xls
- Retrieved from: https://web.archive.org/web/20221203235010id_/https://www.ibo.nyc.ny.us/RevenueSpending/2010pitdata.xls
- File: 2010pitdata.xls (225792 bytes), MD5 4e1f59387b71d5cf13e37637bc0ef2f7
- Local copy: src/2010pitdata.xls
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2010"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,441,336; liability before credits 798.580856 -> 798.6
    row 19  "Under $0"  B=54316  F=0.0
    row 20  "$0 - $9,999"  B=707089  F=3.452488
    row 21  "$10,000 - $19,999"  B=609800  F=74.694774
    row 22  "$20,000 - $29,999"  B=428303  F=167.99851
    row 23  "$30,000 - $39,999"  B=363296  F=260.425998
    row 24  "$40,000 - $49,999"  B=278532  F=292.009086
i2 $50,000 to $99,999: returns 646,201; liability before credits 1206.577688 -> 1206.6
    row 25  "$50,000 - $59,999"  B=207296  F=283.729787
    row 26  "$60,000 - $74,999"  B=214719  F=385.472892
    row 27  "$75,000 - $99,999"  B=224186  F=537.375009
i3 $100,000 to $199,999: returns 263,769; liability before credits 1063.392643 -> 1063.4
    row 28  "$100,000 - $124,999"  B=117878  F=381.438089
    row 29  "$125,000 - $149,999"  B=70031  F=282.763746
    row 30  "$150,000 - $199,999"  B=75860  F=399.190808
i4 $200,000 to $499,999: returns 91,877; liability before credits 879.980703 -> 880.0
    row 31  "$200,000 - $349,999"  B=70995  F=592.502653
    row 32  "$350,000 - $499,999"  B=20882  F=287.47805
i5 $500,000 to $999,999: returns 21,691; liability before credits 523.757937 -> 523.8
    row 33  "$500,000 - $749,999"  B=14367  F=300.41918
    row 34  "$750,000 - $999,999"  B=7324  F=223.338757
i6 $1 million and over: returns 18,355; liability before credits 2956.183511 -> 2956.2
    row 35  "$1,000,000 - $1,999,999"  B=10234  F=521.468227
    row 36  "$2,000,000 - $4,999,999"  B=5535  F=627.080973
    row 37  "$5,000,000 - $9,999,999"  B=1474  F=380.762731
    row 38  "$10,000,000 and Over"  B=1112  F=1426.87158
All Filers (row 39): B=3483229.0  F=7428.47334
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = -2e-06 ($M); rounded bands sum minus rounded total = 0.1

## Tax year 2011

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2011pitdata.xls
- Retrieved from: https://web.archive.org/web/20221202065808id_/https://www.ibo.nyc.ny.us/RevenueSpending/2011pitdata.xls
- File: 2011pitdata.xls (230912 bytes), MD5 d1efa43d77cc6fc8ffd0cc130c98b366
- Local copy: src/2011pitdata.xls
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2011"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,455,767; liability before credits 802.470382 -> 802.5
    row 19  "Under $0"  B=57274  F=0.0
    row 20  "$0 - $9,999"  B=716014  F=3.530038
    row 21  "$10,000 - $19,999"  B=612177  F=74.649197
    row 22  "$20,000 - $29,999"  B=443544  F=175.438284
    row 23  "$30,000 - $39,999"  B=351982  F=256.658212
    row 24  "$40,000 - $49,999"  B=274776  F=292.194651
i2 $50,000 to $99,999: returns 665,051; liability before credits 1256.564897 -> 1256.6
    row 25  "$50,000 - $59,999"  B=207822  F=288.950195
    row 26  "$60,000 - $74,999"  B=222940  F=399.73441
    row 27  "$75,000 - $99,999"  B=234289  F=567.880292
i3 $100,000 to $199,999: returns 280,560; liability before credits 1139.553484 -> 1139.6
    row 28  "$100,000 - $124,999"  B=123562  F=399.373852
    row 29  "$125,000 - $149,999"  B=75092  F=307.157246
    row 30  "$150,000 - $199,999"  B=81906  F=433.022386
i4 $200,000 to $499,999: returns 100,763; liability before credits 965.497154 -> 965.5
    row 31  "$200,000 - $349,999"  B=77146  F=641.047808
    row 32  "$350,000 - $499,999"  B=23617  F=324.449346
i5 $500,000 to $999,999: returns 23,994; liability before credits 576.718655 -> 576.7
    row 33  "$500,000 - $749,999"  B=16250  F=340.825405
    row 34  "$750,000 - $999,999"  B=7744  F=235.89325
i6 $1 million and over: returns 19,675; liability before credits 2971.961345 -> 2972.0
    row 35  "$1,000,000 - $1,999,999"  B=10987  F=560.395316
    row 36  "$2,000,000 - $4,999,999"  B=5960  F=677.391643
    row 37  "$5,000,000 - $9,999,999"  B=1568  F=405.209364
    row 38  "$10,000,000 and Over"  B=1160  F=1328.965022
All Filers (row 39): B=3545808.0  F=7712.765917
Checks: band returns sum minus All Filers = 2; band liability sum minus All Filers = -0.0 ($M); rounded bands sum minus rounded total = 0.1

## Tax year 2012

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2012pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20221014112349id_/https://www.ibo.nyc.ny.us/RevenueSpending/2012pitdata.xlsx
- File: 2012pitdata.xlsx (195994 bytes), MD5 a0904fc977c37616045bc90cb62e9fde
- Local copy: src/2012pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2012"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,446,304; liability before credits 803.146416 -> 803.1
    row 19  "Under $0"  B=59808  F=0
    row 20  "$0 - $9,999"  B=699983  F=3.515124
    row 21  "$10,000 - $19,999"  B=616334  F=76.591329
    row 22  "$20,000 - $29,999"  B=438115  F=173.672107
    row 23  "$30,000 - $39,999"  B=353483  F=252.517142
    row 24  "$40,000 - $49,999"  B=278581  F=296.850714
i2 $50,000 to $99,999: returns 680,224; liability before credits 1291.660093 -> 1291.7
    row 25  "$50,000 - $59,999"  B=214292  F=299.023852
    row 26  "$60,000 - $74,999"  B=224892  F=406.855689
    row 27  "$75,000 - $99,999"  B=241040  F=585.780552
i3 $100,000 to $199,999: returns 295,887; liability before credits 1196.845001 -> 1196.8
    row 28  "$100,000 - $124,999"  B=133815  F=434.805143
    row 29  "$125,000 - $149,999"  B=76539  F=313.361511
    row 30  "$150,000 - $199,999"  B=85533  F=448.678347
i4 $200,000 to $499,999: returns 106,521; liability before credits 1024.997467 -> 1025.0
    row 31  "$200,000 - $349,999"  B=80814  F=670.414645
    row 32  "$350,000 - $499,999"  B=25707  F=354.582822
i5 $500,000 to $999,999: returns 25,781; liability before credits 621.336627 -> 621.3
    row 33  "$500,000 - $749,999"  B=17410  F=364.441722
    row 34  "$750,000 - $999,999"  B=8371  F=256.894905
i6 $1 million and over: returns 22,135; liability before credits 3866.869476 -> 3866.9
    row 35  "$1,000,000 - $1,999,999"  B=12071  F=617.050894
    row 36  "$2,000,000 - $4,999,999"  B=6627  F=756.352505
    row 37  "$5,000,000 - $9,999,999"  B=1944  F=500.678087
    row 38  "$10,000,000 and Over"  B=1493  F=1992.78799
All Filers (row 39): B=3576851  F=8804.855079
Checks: band returns sum minus All Filers = 1; band liability sum minus All Filers = 1e-06 ($M); rounded bands sum minus rounded total = -0.1

## Tax year 2013

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2013pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20221014112434id_/https://www.ibo.nyc.ny.us/RevenueSpending/2013pitdata.xlsx
- File: 2013pitdata.xlsx (198938 bytes), MD5 34b818440528b7e8d7218948e404cc35
- Local copy: src/2013pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2013"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,511,249; liability before credits 803.874349 -> 803.9
    row 19  "Under $0"  B=54348  F=0
    row 20  "$0 - $9,999"  B=755255  F=3.066719
    row 21  "$10,000 - $19,999"  B=617387  F=73.663257
    row 22  "$20,000 - $29,999"  B=448845  F=175.695091
    row 23  "$30,000 - $39,999"  B=355458  F=255.345819
    row 24  "$40,000 - $49,999"  B=279956  F=296.103463
i2 $50,000 to $99,999: returns 699,008; liability before credits 1335.681484 -> 1335.7
    row 25  "$50,000 - $59,999"  B=217528  F=304.917542
    row 26  "$60,000 - $74,999"  B=229814  F=417.074128
    row 27  "$75,000 - $99,999"  B=251666  F=613.689814
i3 $100,000 to $199,999: returns 310,500; liability before credits 1275.531305 -> 1275.5
    row 28  "$100,000 - $124,999"  B=134758  F=441.26798
    row 29  "$125,000 - $149,999"  B=84438  F=348.495258
    row 30  "$150,000 - $199,999"  B=91304  F=485.768067
i4 $200,000 to $499,999: returns 115,379; liability before credits 1119.994505 -> 1120.0
    row 31  "$200,000 - $349,999"  B=87866  F=737.71445
    row 32  "$350,000 - $499,999"  B=27513  F=382.280055
i5 $500,000 to $999,999: returns 28,019; liability before credits 671.121173 -> 671.1
    row 33  "$500,000 - $749,999"  B=19426  F=407.560599
    row 34  "$750,000 - $999,999"  B=8593  F=263.560574
i6 $1 million and over: returns 21,764; liability before credits 3582.742196 -> 3582.7
    row 35  "$1,000,000 - $1,999,999"  B=11996  F=611.014853
    row 36  "$2,000,000 - $4,999,999"  B=6601  F=750.225783
    row 37  "$5,000,000 - $9,999,999"  B=1852  F=478.889093
    row 38  "$10,000,000 and Over"  B=1315  F=1742.612467
All Filers (row 39): B=3685919  F=8788.945011
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = 1e-06 ($M); rounded bands sum minus rounded total = 0.0

## Tax year 2014

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2014pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20221202051312id_/https://www.ibo.nyc.ny.us/RevenueSpending/2014pitdata.xlsx
- File: 2014pitdata.xlsx (179169 bytes), MD5 eaf49f3e4ce1bac4a16530d6038f06ef
- Local copy: src/2014pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2014"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,486,710; liability before credits 813.35998 -> 813.4
    row 19  "Under $0"  B=55340  F=0
    row 20  "$0 - $9,999"  B=718849  F=2.881726
    row 21  "$10,000 - $19,999"  B=623871  F=73.803572
    row 22  "$20,000 - $29,999"  B=449193  F=174.111462
    row 23  "$30,000 - $39,999"  B=355448  F=257.374222
    row 24  "$40,000 - $49,999"  B=284009  F=305.188998
i2 $50,000 to $99,999: returns 722,682; liability before credits 1388.777358 -> 1388.8
    row 25  "$50,000 - $59,999"  B=224376  F=315.134399
    row 26  "$60,000 - $74,999"  B=238683  F=433.292959
    row 27  "$75,000 - $99,999"  B=259623  F=640.35
i3 $100,000 to $199,999: returns 334,912; liability before credits 1382.38322 -> 1382.4
    row 28  "$100,000 - $124,999"  B=146856  F=482.346786
    row 29  "$125,000 - $149,999"  B=88553  F=366.485127
    row 30  "$150,000 - $199,999"  B=99503  F=533.551307
i4 $200,000 to $499,999: returns 126,937; liability before credits 1230.326781 -> 1230.3
    row 31  "$200,000 - $349,999"  B=96461  F=807.41952
    row 32  "$350,000 - $499,999"  B=30476  F=422.907261
i5 $500,000 to $999,999: returns 31,078; liability before credits 749.059346 -> 749.1
    row 33  "$500,000 - $749,999"  B=21320  F=447.120517
    row 34  "$750,000 - $999,999"  B=9758  F=301.938829
i6 $1 million and over: returns 25,085; liability before credits 4396.279178 -> 4396.3
    row 35  "$1,000,000 - $1,999,999"  B=13470  F=684.271471
    row 36  "$2,000,000 - $4,999,999"  B=7746  F=883.523635
    row 37  "$5,000,000 - $9,999,999"  B=2169  F=564.810161
    row 38  "$10,000,000 and Over"  B=1700  F=2263.673911
All Filers (row 39): B=3727404  F=9960.185863
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = -0.0 ($M); rounded bands sum minus rounded total = 0.1; NOTE row 17 All Filers F = 9960.19 vs row 39 F = 9960.185863

## Tax year 2015

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2015pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20221201212823id_/https://www.ibo.nyc.ny.us/RevenueSpending/2015pitdata.xlsx
- File: 2015pitdata.xlsx (183698 bytes), MD5 c9a87012ffbd033df6ddc003921de147
- Local copy: src/2015pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2015"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,463,754; liability before credits 817.18675 -> 817.2
    row 19  "Under $0"  B=52279  F=0
    row 20  "$0 - $9,999"  B=690239  F=2.576107
    row 21  "$10,000 - $19,999"  B=616138  F=73.042903
    row 22  "$20,000 - $29,999"  B=461506  F=177.448545
    row 23  "$30,000 - $39,999"  B=357342  F=258.626921
    row 24  "$40,000 - $49,999"  B=286250  F=305.492274
i2 $50,000 to $99,999: returns 751,853; liability before credits 1450.414744 -> 1450.4
    row 25  "$50,000 - $59,999"  B=233958  F=330.174975
    row 26  "$60,000 - $74,999"  B=248264  F=453.542191
    row 27  "$75,000 - $99,999"  B=269631  F=666.697578
i3 $100,000 to $199,999: returns 361,148; liability before credits 1498.266649 -> 1498.3
    row 28  "$100,000 - $124,999"  B=158444  F=524.01191
    row 29  "$125,000 - $149,999"  B=94504  F=393.133208
    row 30  "$150,000 - $199,999"  B=108200  F=581.121531
i4 $200,000 to $499,999: returns 138,063; liability before credits 1338.74813 -> 1338.7
    row 31  "$200,000 - $349,999"  B=105160  F=881.114336
    row 32  "$350,000 - $499,999"  B=32903  F=457.633794
i5 $500,000 to $999,999: returns 33,032; liability before credits 832.057798 -> 832.1
    row 33  "$500,000 - $749,999"  B=22521  F=497.260906
    row 34  "$750,000 - $999,999"  B=10511  F=334.796892
i6 $1 million and over: returns 25,934; liability before credits 4430.777598 -> 4430.8
    row 35  "$1,000,000 - $1,999,999"  B=14114  F=734.521969
    row 36  "$2,000,000 - $4,999,999"  B=7872  F=907.259982
    row 37  "$5,000,000 - $9,999,999"  B=2269  F=586.668993
    row 38  "$10,000,000 and Over"  B=1679  F=2202.326654
All Filers (row 39): B=3773784  F=10367.451669
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = -0.0 ($M); rounded bands sum minus rounded total = 0.0

## Tax year 2016

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2016pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20221202011046id_/https://www.ibo.nyc.ny.us/RevenueSpending/2016pitdata.xlsx
- File: 2016pitdata.xlsx (197626 bytes), MD5 b9041ee7ae1793800e4ba1869f1ac6d1
- Local copy: src/2016pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2016"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,448,750; liability before credits 831.56074 -> 831.6
    row 19  "Under $0"  B=54553  F=0
    row 20  "$0 - $9,999"  B=662094  F=2.438171
    row 21  "$10,000 - $19,999"  B=609208  F=72.796629
    row 22  "$20,000 - $29,999"  B=466954  F=179.334343
    row 23  "$30,000 - $39,999"  B=362620  F=262.703532
    row 24  "$40,000 - $49,999"  B=293321  F=314.288065
i2 $50,000 to $99,999: returns 776,052; liability before credits 1503.136951 -> 1503.1
    row 25  "$50,000 - $59,999"  B=241385  F=342.31492
    row 26  "$60,000 - $74,999"  B=256690  F=470.724703
    row 27  "$75,000 - $99,999"  B=277977  F=690.097328
i3 $100,000 to $199,999: returns 371,101; liability before credits 1547.553559 -> 1547.6
    row 28  "$100,000 - $124,999"  B=161106  F=534.890034
    row 29  "$125,000 - $149,999"  B=97677  F=407.80583
    row 30  "$150,000 - $199,999"  B=112318  F=604.857695
i4 $200,000 to $499,999: returns 145,300; liability before credits 1409.95097 -> 1410.0
    row 31  "$200,000 - $349,999"  B=110308  F=924.668512
    row 32  "$350,000 - $499,999"  B=34992  F=485.282458
i5 $500,000 to $999,999: returns 33,776; liability before credits 846.401577 -> 846.4
    row 33  "$500,000 - $749,999"  B=23314  F=513.580595
    row 34  "$750,000 - $999,999"  B=10462  F=332.820982
i6 $1 million and over: returns 25,230; liability before credits 3784.425737 -> 3784.4
    row 35  "$1,000,000 - $1,999,999"  B=13997  F=725.019288
    row 36  "$2,000,000 - $4,999,999"  B=7705  F=887.406303
    row 37  "$5,000,000 - $9,999,999"  B=2116  F=542.72585
    row 38  "$10,000,000 and Over"  B=1412  F=1629.274296
All Filers (row 39): B=3800209  F=9923.029534
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = 0.0 ($M); rounded bands sum minus rounded total = 0.1

## Tax year 2017

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2017pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20240613183108id_/https://www.ibo.nyc.ny.us/RevenueSpending/2017pitdata.xlsx
- File: 2017pitdata.xlsx (185369 bytes), MD5 a399a5f94963b719330b61d75b170e0c
- Local copy: src/2017pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2017"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,424,880; liability before credits 897.79421 -> 897.8
    row 19  "Under $0"  B=51839  F=0
    row 20  "$0 - $9,999"  B=633763  F=2.344329
    row 21  "$10,000 - $19,999"  B=582587  F=74.07638
    row 22  "$20,000 - $29,999"  B=489547  F=198.801635
    row 23  "$30,000 - $39,999"  B=366651  F=280.874695
    row 24  "$40,000 - $49,999"  B=300493  F=341.697171
i2 $50,000 to $99,999: returns 802,190; liability before credits 1658.543933 -> 1658.5
    row 25  "$50,000 - $59,999"  B=246845  F=372.471681
    row 26  "$60,000 - $74,999"  B=266336  F=519.974925
    row 27  "$75,000 - $99,999"  B=289009  F=766.097327
i3 $100,000 to $199,999: returns 399,477; liability before credits 1773.003415 -> 1773.0
    row 28  "$100,000 - $124,999"  B=173315  F=613.259227
    row 29  "$125,000 - $149,999"  B=105609  F=469.198378
    row 30  "$150,000 - $199,999"  B=120553  F=690.54581
i4 $200,000 to $499,999: returns 158,583; liability before credits 1634.039636 -> 1634.0
    row 31  "$200,000 - $349,999"  B=120748  F=1076.203361
    row 32  "$350,000 - $499,999"  B=37835  F=557.836275
i5 $500,000 to $999,999: returns 36,732; liability before credits 924.237366 -> 924.2
    row 33  "$500,000 - $749,999"  B=25219  F=558.399247
    row 34  "$750,000 - $999,999"  B=11513  F=365.838119
i6 $1 million and over: returns 28,321; liability before credits 5288.966815 -> 5289.0
    row 35  "$1,000,000 - $1,999,999"  B=15595  F=808.481795
    row 36  "$2,000,000 - $4,999,999"  B=8390  F=970.243633
    row 37  "$5,000,000 - $9,999,999"  B=2518  F=655.868672
    row 38  "$10,000,000 and Over"  B=1818  F=2854.372715
All Filers (row 39): B=3850183  F=12176.585375
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = -0.0 ($M); rounded bands sum minus rounded total = -0.1

## Tax year 2018

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/2018pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20210731161051id_/https://www.ibo.nyc.ny.us/RevenueSpending/2018pitdata.xlsx
- File: 2018pitdata.xlsx (185812 bytes), MD5 a5cc3bf9521077993763d2b0b19856e3
- Local copy: src/2018pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2018"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,364,862; liability before credits 933.269658 -> 933.3
    row 19  "Under $0"  B=47299  F=0.001931
    row 20  "$0 - $9,999"  B=594908  F=2.229704
    row 21  "$10,000 - $19,999"  B=533916  F=71.855947
    row 22  "$20,000 - $29,999"  B=495230  F=207.994999
    row 23  "$30,000 - $39,999"  B=383704  F=295.935083
    row 24  "$40,000 - $49,999"  B=309805  F=355.251994
i2 $50,000 to $99,999: returns 838,188; liability before credits 1749.164388 -> 1749.2
    row 25  "$50,000 - $59,999"  B=256844  F=391.13458
    row 26  "$60,000 - $74,999"  B=280132  F=551.563641
    row 27  "$75,000 - $99,999"  B=301212  F=806.466167
i3 $100,000 to $199,999: returns 425,300; liability before credits 1900.82128 -> 1900.8
    row 28  "$100,000 - $124,999"  B=186794  F=667.200548
    row 29  "$125,000 - $149,999"  B=111284  F=498.62718
    row 30  "$150,000 - $199,999"  B=127222  F=734.993552
i4 $200,000 to $499,999: returns 172,746; liability before credits 1796.669905 -> 1796.7
    row 31  "$200,000 - $349,999"  B=130601  F=1171.768367
    row 32  "$350,000 - $499,999"  B=42145  F=624.901538
i5 $500,000 to $999,999: returns 40,345; liability before credits 1017.940337 -> 1017.9
    row 33  "$500,000 - $749,999"  B=27716  F=615.697335
    row 34  "$750,000 - $999,999"  B=12629  F=402.243002
i6 $1 million and over: returns 30,012; liability before credits 4750.582781 -> 4750.6
    row 35  "$1,000,000 - $1,999,999"  B=16798  F=869.402191
    row 36  "$2,000,000 - $4,999,999"  B=8802  F=1011.152838
    row 37  "$5,000,000 - $9,999,999"  B=2626  F=682.268038
    row 38  "$10,000,000 and Over"  B=1786  F=2187.759714
All Filers (row 39): B=3871453  F=12148.448349
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = -0.0 ($M); rounded bands sum minus rounded total = 0.1

## Tax year 2019

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/december2019pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20230327173039id_/https://www.ibo.nyc.ny.us/RevenueSpending/december2019pitdata.xlsx
- File: december2019pitdata.xlsx (175002 bytes), MD5 aac898b4f5936a61d54abbce802e6cf3
- Local copy: src/december2019pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "Major Components of Adjusted Gross Income / Tax Year 2019"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,404,224; liability before credits 975.185493 -> 975.2
    row 19  "Under $0"  B=50167  F=0
    row 20  "$0 - $9,999"  B=611946  F=2.155751
    row 21  "$10,000 - $19,999"  B=522246  F=71.89181
    row 22  "$20,000 - $29,999"  B=473983  F=202.085608
    row 23  "$30,000 - $39,999"  B=421268  F=326.383263
    row 24  "$40,000 - $49,999"  B=324614  F=372.669061
i2 $50,000 to $99,999: returns 884,200; liability before credits 1847.52976 -> 1847.5
    row 25  "$50,000 - $59,999"  B=269146  F=411.643254
    row 26  "$60,000 - $74,999"  B=300339  F=592.58691
    row 27  "$75,000 - $99,999"  B=314715  F=843.299596
i3 $100,000 to $199,999: returns 449,257; liability before credits 2013.969007 -> 2014.0
    row 28  "$100,000 - $124,999"  B=195928  F=701.631939
    row 29  "$125,000 - $149,999"  B=118677  F=532.930415
    row 30  "$150,000 - $199,999"  B=134652  F=779.406653
i4 $200,000 to $499,999: returns 184,866; liability before credits 1929.237678 -> 1929.2
    row 31  "$200,000 - $349,999"  B=139203  F=1251.75328
    row 32  "$350,000 - $499,999"  B=45663  F=677.484398
i5 $500,000 to $999,999: returns 42,599; liability before credits 1071.562214 -> 1071.6
    row 33  "$500,000 - $749,999"  B=29488  F=653.8914
    row 34  "$750,000 - $999,999"  B=13111  F=417.670814
i6 $1 million and over: returns 30,460; liability before credits 4771.74216 -> 4771.7
    row 35  "$1,000,000 - $1,999,999"  B=17084  F=884.861696
    row 36  "$2,000,000 - $4,999,999"  B=8952  F=1025.52893
    row 37  "$5,000,000 - $9,999,999"  B=2658  F=695.594684
    row 38  "$10,000,000 and Over"  B=1766  F=2165.75685
All Filers (row 39): B=3995606  F=12609.226312
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = -0.0 ($M); rounded bands sum minus rounded total = 0.0

## Tax year 2020

- IBO URL: https://www.ibo.nyc.ny.us/RevenueSpending/december2020pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20250117235856id_/https://www.ibo.nyc.ny.us/RevenueSpending/december2020pitdata.xlsx
- File: december2020pitdata.xlsx (176645 bytes), MD5 c7c0d556ae7666cb18c8cf83d3236fe5
- Local copy: src/december2020pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "Major Components of Adjusted Gross Income / Tax Year 2020"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,547,920; liability before credits 1118.595322 -> 1118.6
    row 19  "Under $0"  B=68968  F=0
    row 20  "$0 - $9,999"  B=625693  F=1.589448
    row 21  "$10,000 - $19,999"  B=474863  F=84.547315
    row 22  "$20,000 - $29,999"  B=542526  F=243.758432
    row 23  "$30,000 - $39,999"  B=472217  F=371.628825
    row 24  "$40,000 - $49,999"  B=363653  F=417.071302
i2 $50,000 to $99,999: returns 893,634; liability before credits 1858.169397 -> 1858.2
    row 25  "$50,000 - $59,999"  B=277802  F=423.028149
    row 26  "$60,000 - $74,999"  B=304016  F=599.093197
    row 27  "$75,000 - $99,999"  B=311816  F=836.048051
i3 $100,000 to $199,999: returns 435,981; liability before credits 1959.745882 -> 1959.7
    row 28  "$100,000 - $124,999"  B=190357  F=683.118204
    row 29  "$125,000 - $149,999"  B=115612  F=521.170385
    row 30  "$150,000 - $199,999"  B=130012  F=755.457293
i4 $200,000 to $499,999: returns 173,747; liability before credits 1815.008356 -> 1815.0
    row 31  "$200,000 - $349,999"  B=131262  F=1182.617546
    row 32  "$350,000 - $499,999"  B=42485  F=632.39081
i5 $500,000 to $999,999: returns 39,020; liability before credits 982.626962 -> 982.6
    row 33  "$500,000 - $749,999"  B=27181  F=604.357464
    row 34  "$750,000 - $999,999"  B=11839  F=378.269498
i6 $1 million and over: returns 27,598; liability before credits 5284.25563 -> 5284.3
    row 35  "$1,000,000 - $1,999,999"  B=15217  F=789.518083
    row 36  "$2,000,000 - $4,999,999"  B=7940  F=908.263696
    row 37  "$5,000,000 - $9,999,999"  B=2543  F=671.464028
    row 38  "$10,000,000 and Over"  B=1898  F=2915.009823
All Filers (row 39): B=4117900  F=13018.401549
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = 0.0 ($M); rounded bands sum minus rounded total = 0.0

## Tax year 2021

- IBO URL: https://a860-gpp.nyc.gov/downloads/g158bm69j
- File: november2023pittable.xlsx (175148 bytes), MD5 f6f1119eba5c0688a71b096321fcbdd8
- Local copy: not saved (bytes held in browser only); cell values saved in src/browser_extract_gpp.json
- How read: fetched in the in-app browser from a860-gpp.nyc.gov (curl gets HTTP 403); MD5 computed and xlsx unzipped/parsed in the browser
- Sheet: "8. Tax Liability" ; title cell A1: "Major Components of Adjusted Gross Income / Tax Year 2021"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,340,089; liability before credits 1029.659245 -> 1029.7
    row 19  "Under $0"  B=46209  F=0.0
    row 20  "$0 - $9,999"  B=524373  F=1.550988
    row 21  "$10,000 - $19,999"  B=509517  F=91.31399
    row 22  "$20,000 - $29,999"  B=503564  F=226.238948
    row 23  "$30,000 - $39,999"  B=427587  F=333.767684
    row 24  "$40,000 - $49,999"  B=328839  F=376.787635
i2 $50,000 to $99,999: returns 864,771; liability before credits 1815.823233 -> 1815.8
    row 25  "$50,000 - $59,999"  B=258936  F=394.642224
    row 26  "$60,000 - $74,999"  B=293370  F=580.218582
    row 27  "$75,000 - $99,999"  B=312465  F=840.962427
i3 $100,000 to $199,999: returns 449,711; liability before credits 2035.839094 -> 2035.8
    row 28  "$100,000 - $124,999"  B=193011  F=696.073908
    row 29  "$125,000 - $149,999"  B=120110  F=543.342363
    row 30  "$150,000 - $199,999"  B=136590  F=796.422823
i4 $200,000 to $499,999: returns 194,270; liability before credits 2046.237328 -> 2046.2
    row 31  "$200,000 - $349,999"  B=146022  F=1324.833189
    row 32  "$350,000 - $499,999"  B=48248  F=721.404139
i5 $500,000 to $999,999: returns 47,478; liability before credits 1201.901069 -> 1201.9
    row 33  "$500,000 - $749,999"  B=32780  F=731.797347
    row 34  "$750,000 - $999,999"  B=14698  F=470.103722
i6 $1 million and over: returns 35,192; liability before credits 7455.781288 -> 7455.8
    row 35  "$1,000,000 - $1,999,999"  B=18851  F=981.720137
    row 36  "$2,000,000 - $4,999,999"  B=10176  F=1178.207767
    row 37  "$5,000,000 - $9,999,999"  B=3389  F=885.142243
    row 38  "$10,000,000 and Over"  B=2776  F=4410.711141
All Filers (row 39): B=3931511  F=15585.241257
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = 0.0 ($M); rounded bands sum minus rounded total = 0.0

## Tax year 2022

- IBO URL: https://ibo.nyc.ny.us/RevenueSpending/2022pitdata.xlsx
- Retrieved from: https://web.archive.org/web/20241213202511id_/https://ibo.nyc.ny.us/RevenueSpending/2022pitdata.xlsx
- File: 2022pitdata.xlsx (178446 bytes), MD5 7bbc39db9422f61ac43d179c4e59cf7f
- Local copy: src/2022pitdata.xlsx
- How read: downloaded with curl from the Internet Archive capture; read locally with openpyxl/xlrd
- Sheet: "8. Tax Liability" ; title cell A1: "Major Components of Adjusted Gross Income / Tax Year 2022"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC Personal Income Tax Liability After Credits" | "Average Effective NYC PIT Rate" | "NYS Personal Income Tax Liability After Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,187,133; liability before credits 852.085876 -> 852.1
    row 19  "Under $0"  B=54571  F=0
    row 20  "$0 - $9,999"  B=602171  F=1.919005
    row 21  "$10,000 - $19,999"  B=490476  F=66.595752
    row 22  "$20,000 - $29,999"  B=393230  F=167.929637
    row 23  "$30,000 - $39,999"  B=352677  F=275.305581
    row 24  "$40,000 - $49,999"  B=294008  F=340.335901
i2 $50,000 to $99,999: returns 872,987; liability before credits 1861.991831 -> 1862.0
    row 25  "$50,000 - $59,999"  B=244394  F=375.365918
    row 26  "$60,000 - $74,999"  B=300511  F=598.658169
    row 27  "$75,000 - $99,999"  B=328082  F=887.967744
i3 $100,000 to $199,999: returns 490,171; liability before credits 2242.800429 -> 2242.8
    row 28  "$100,000 - $124,999"  B=205346  F=744.067915
    row 29  "$125,000 - $149,999"  B=130423  F=593.063628
    row 30  "$150,000 - $199,999"  B=154402  F=905.668886
i4 $200,000 to $499,999: returns 219,564; liability before credits 2301.312872 -> 2301.3
    row 31  "$200,000 - $349,999"  B=166442  F=1508.437461
    row 32  "$350,000 - $499,999"  B=53122  F=792.875411
i5 $500,000 to $999,999: returns 50,396; liability before credits 1269.68635 -> 1269.7
    row 33  "$500,000 - $749,999"  B=35091  F=780.684638
    row 34  "$750,000 - $999,999"  B=15305  F=489.001712
i6 $1 million and over: returns 33,765; liability before credits 5550.839883 -> 5550.8
    row 35  "$1,000,000 - $1,999,999"  B=19037  F=982.241519
    row 36  "$2,000,000 - $4,999,999"  B=9718  F=1111.861042
    row 37  "$5,000,000 - $9,999,999"  B=2989  F=774.281628
    row 38  "$10,000,000 and Over"  B=2021  F=2682.455694
All Filers (row 39): B=3854016  F=14078.717241
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = -0.0 ($M); rounded bands sum minus rounded total = 0.0

## Tax year 2023

- IBO URL: https://a860-gpp.nyc.gov/downloads/2227mv671
- File: 2023-pit-data.xlsx (180968 bytes), MD5 4db3713423d59a5627224ca038929f08
- Local copy: not saved (bytes held in browser only); cell values saved in src/browser_extract_gpp.json
- How read: fetched in the in-app browser from a860-gpp.nyc.gov (curl gets HTTP 403); MD5 computed and xlsx unzipped/parsed in the browser
- Sheet: "8. Tax Liability" ; title cell A1: "New York City and New York State Tax Liability and Tax Rates / Tax Year 2023"
- Header row 3 (non-empty cells): "Income Groups" | "Number of Filers" | "New York Taxable Income" | "NYC Personal Income Tax Liability Before Credits" | "Average Marginal NYC PIT Rate" | "NYC PIT Liability After Non-Refundable Credits" | "NYC Net PIT Liability After Refundable Credits " | "Average Effective NYC PIT Rate" | "NYS Net PIT Liability After Refundable Credits" | "Average Marginal NYS PIT Rate" | "Average Effective NYS PIT Rate"
- Rows used: 19-38 (bands), 39 (All Filers)

i1 Under $50,000: returns 2,121,623; liability before credits 841.964965 -> 842.0
    row 19  "Under $0"  B=51536  F=0.0
    row 20  "$0 - $9,999"  B=578044  F=1.834351
    row 21  "$10,000 - $19,999"  B=464107  F=64.943863
    row 22  "$20,000 - $29,999"  B=385637  F=164.090015
    row 23  "$30,000 - $39,999"  B=348707  F=271.627737
    row 24  "$40,000 - $49,999"  B=293592  F=339.468999
i2 $50,000 to $99,999: returns 915,979; liability before credits 1964.215183 -> 1964.2
    row 25  "$50,000 - $59,999"  B=253334  F=389.493602
    row 26  "$60,000 - $74,999"  B=313794  F=626.998493
    row 27  "$75,000 - $99,999"  B=348851  F=947.723088
i3 $100,000 to $199,999: returns 533,424; liability before credits 2452.653535 -> 2452.7
    row 28  "$100,000 - $124,999"  B=220456  F=802.434226
    row 29  "$125,000 - $149,999"  B=142984  F=651.627724
    row 30  "$150,000 - $199,999"  B=169984  F=998.591585
i4 $200,000 to $499,999: returns 245,497; liability before credits 2572.960962 -> 2573.0
    row 31  "$200,000 - $349,999"  B=186452  F=1691.913296
    row 32  "$350,000 - $499,999"  B=59045  F=881.047666
i5 $500,000 to $999,999: returns 54,404; liability before credits 1366.787869 -> 1366.8
    row 33  "$500,000 - $749,999"  B=38128  F=848.058905
    row 34  "$750,000 - $999,999"  B=16276  F=518.728964
i6 $1 million and over: returns 34,307; liability before credits 5432.010802 -> 5432.0
    row 35  "$1,000,000 - $1,999,999"  B=19897  F=1029.756258
    row 36  "$2,000,000 - $4,999,999"  B=9660  F=1112.431415
    row 37  "$5,000,000 - $9,999,999"  B=2814  F=739.422257
    row 38  "$10,000,000 and Over"  B=1936  F=2550.400872
All Filers (row 39): B=3905234  F=14630.593316
Checks: band returns sum minus All Filers = 0; band liability sum minus All Filers = -0.0 ($M); rounded bands sum minus rounded total = 0.1

## How the series is published

- One workbook per tax year; no workbook holds more than one year. Each has the same layout: sheets 1-8 ("1. Income Categories" ... "8. Tax Liability"; 2019 onward and the GPP copies also have "9. Tax Credits"), with deciles/percentiles on rows 4-17 and 20 nominal NYAGI groups on rows 19-38, "All Filers" on row 39.
- IBO's overview page (archived copy, Wayback 20260601091703, saved as src/html/wb_overview_20260601.html, MD5 17c8eec03bfea66ad2e0d51518de4dcf, dated "December 2024" on the page) links one file per year: 2006pitdata.xlsx ... 2018pitdata.xlsx (2010 and 2011 as .xls), december2019pitdata.xlsx, december2020pitdata.xlsx, 2021pitdata.xlsx / november2023pittable.xlsx, 2022pitdata.xlsx. The live ibo.nyc.ny.us URLs now redirect to IBO's new site and no longer serve the files, so 2006-2020 and 2022 came from Internet Archive captures of those exact URLs (latest 200-status capture for each).
- 2021 and 2023 are not in the Internet Archive. They came from the NYC Government Publications Portal: 2021 = november2023pittable.xlsx, record 12579w78g (published 2023-11-08); 2023 = 2023-pit-data.xlsx, record pv63g542d (published 2026-02-10). The portal returns HTTP 403 to curl, so each file was fetched in the in-app browser, its MD5 computed there (MD5 routine verified on "abc"), and the xlsx unzipped and parsed in the page. No local copy of these two workbooks exists. The cells read were saved as src/browser_extract_gpp.json (8,352 bytes, MD5 8d57fa7c33272a01b579a0dcb0629857; the same MD5 was computed in the browser on the string before it was written, so the transcription is exact).

## Cross-checks between copies

- 2017pitdata.xlsx, 2018pitdata.xlsx and 2022pitdata.xlsx on the Publications Portal (file sets n870zs93h, 3197xp03p, m613n2342) have the same MD5 as the archived IBO-site copies used here.
- 2019 and 2020: the Portal copies (december2019pitdata.xlsx 6682x6599, MD5 5ec22724f7f1d3ee73c2cce3bab06a4d; december2020pitdata.xlsx sx61dq12m, MD5 67be501b4cc607a6ef851543aa043823) are different files from the archived IBO-site copies (MD5 aac898b4... and c7c0d556...), but every label, filer count and before-credits value in sheet 8 rows 17 and 19-39 is identical. The original November 2021 release for 2019 (2019pitdata.xlsx: archived copy MD5 ead5edf2a7135754be63623601920ab7 in src/; Portal copy m039k727z MD5 35ab4ea21ce835c8ab7d011650cdbebb) also has identical sheet-8 values to the December 2022 update, so the "update" did not change these figures.
- Older archived versions checked for revisions: 2006 (Feb 2017 capture), 2014 (Feb 2017), 2015 and 2016 (Aug 2019) are in src/superseded/; their sheet-8 rows 17 and 19-39 are identical to the versions used.

## Checks

- Every year: the 20 nominal rows map one-to-one onto the six bands (cut points at $50k, $100k, $200k, $500k and $1M exist in every year, with identical row labels 2006-2023). No year needed splitting; every year is groupable.
- Liability: band sums equal the row 39 All Filers value to within 0.000002 ($M) in every year. Rounded to $0.1M, the six bands can differ from the rounded total by 0.1 (2007, 2008, 2010, 2011, 2012, 2014, 2016, 2017, 2018, 2023); this is rounding only.
- Returns: band sums equal All Filers exactly except 2007 (+1), 2008 (-1), 2009 (+1), 2011 (+2), 2012 (+1). These are sample years (weighted counts rounded to whole returns); flagged but within rounding.
- 2014: row 17 (decile-section All Filers) shows F = 9960.19, while row 39 shows 9960.185863; the row 39 value was used.
- 2023 matches the target check values exactly: 842.0 / 1,964.2 / 2,452.7 / 2,573.0 / 1,366.8 / 5,432.0 (total 14,630.6) and 2,121,623 / 915,979 / 533,424 / 245,497 / 54,404 / 34,307 (total 3,905,234).

## Definition changes and caveats

- Sample vs. population (the biggest break). Per IBO's overview: "For 2015 through 2021, OTPA provided population files containing all returns"; for 2014 and earlier "the files are large samples containing between 643,000 and 776,000 returns", which "should therefore be considered estimates." IBO says the samples include every return with more than $1 million of income or loss, and that comparisons between sample years and population years "should be made with caution." 2022 and 2023 are also full files (2022/2023 overview text not seen for those years specifically; the 2023 workbook totals 3.9 million filers, consistent with a population file).
- Who is counted: full-year New York City residents only; returns of filers claimed as dependents on someone else's return are excluded (overview text).
- "Liability before credits": the column header is the same in every year ("NYC Personal Income Tax Liability Before Credits", sheet 8 column F). No footnote in any workbook defines it differently by year. In 2023 the after-credits columns were split into "NYC PIT Liability After Non-Refundable Credits" and "NYC Net PIT Liability After Refundable Credits"; the before-credits column is unchanged.
- Trap in sheet "2. Summary": through 2022, Summary column J is "New York City Personal Income Tax", which is after credits (it is negative in the lowest bands, e.g. 2021 row 20 J = -4.713036, and matches sheet 8's after-credits column). In the 2023 workbook Summary column J became "NYC Personal Income Tax Liability Before Credits". Taking Summary J for every year would mix after-credits figures (2006-2022) with before-credits (2023). This file uses sheet 8 column F for all years; for 2023 it is identical to Summary J.
- Sheet-8 title text changed from "New York City and New York State Tax Liability and Tax Rates" (2006-2018, 2023) to "Major Components of Adjusted Gross Income" (2019-2022 files). This looks like a copied title; the column headers are unchanged.
- Income bands are nominal New York AGI; neither dollars nor band edges are adjusted for inflation, so band membership shifts with wage growth over the 18 years.

## Gaps and things not confirmed

- No tax years left out: 2006 through 2023 are all present.
- Could not confirm that IBO did not replace any 2006-2016 file after the last archived capture (December 2022); the files' new home on ibo.nyc.gov does not list them, and the Publications Portal has no xlsx for 2006-2016 (only 2012 and 2013 PDFs, not checked).
- 2021 and 2023 rest on the browser read of the Portal files (MD5 recorded, bytes not saved locally). Their bands add to their own All Filers rows, and 2023 matches the expected values.
- The overview's statement about population files covers 2015-2021; I did not find IBO text stating the file type for 2022 and 2023.

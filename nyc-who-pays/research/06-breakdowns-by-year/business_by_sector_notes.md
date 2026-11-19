# NYC business income tax liability by sector: source notes
Source series: NYC Department of Finance, "Statistical Profiles of New York City Business Income Taxes." Listing page: https://www.nyc.gov/site/finance/business/business-reports-statistical-profiles.page (fetched 2026-11-19, saved as src/listing.html). nyc.gov needs a browser User-Agent.
Text was pulled with PyMuPDF (scripts/dump.py). Row text below is the extracted text for each table row, with line breaks replaced by spaces. Values are $ thousands as printed. Pages for 1999 and 2008 were also rendered and checked by eye. For 2013-2022 every sector value was also checked against DOF's own .xlsx copy of the same table. The xlsx stores whole dollars; rounded to thousands it matches the PDF, with at most $1K difference in s6 from rounding two rows.
## Sector mapping (the same in every year)
DOF's combined table has seven rows in every year from 1999 to 2022. 2022 Table 1 footnote, verbatim: "Industry classification for the combined business income taxes differs from that of the individual taxes." The per-tax tables' footnote, verbatim: "The services sector in the combined table (Table 1) includes professional/technical/managerial and other services sectors." In the UBT tables the services sector also includes legal and arts/entertainment/accommodation/food. Services is one DOF row in the combined table; I summed nothing inside it.
- s1 Finance and insurance = "FINANCIAL" (1999-2008), relabeled "FINANCE & INSURANCE" / "Finance & Insurance" (2009-2022). In every year this row equals the BCT total (COR finance & insurance from 2015) plus the GCT, UBT partnership and UBT proprietorship finance & insurance rows, to within $1K (scripts/fin_check.py). The relabel is therefore not a change in content, and insurance is included before 2009 too. Example, 2008: 733,968 (BCT Table 7 total) + 517,697 (GCT) + 790,424 (UBT-P) + 23,782 (UBT-S) = 2,065,871.
- s2 Services = "SERVICES". 2008 check: GCT 346,721 + 301,781; UBT-P 411,637 + 195,400 + 30,226 + 48,694; UBT-S 20,349 + 33,125 + 22,450 + 58,799; total 1,469,182 = combined row.
- s3 Trade = "TRADE"
- s4 Information = "INFORMATION"
- s5 Real estate = "REAL ESTATE"
- s6 All other = "MANUFACTURING" + "OTHER" (summed by me; arithmetic shown under each year)
## Years in the series (1999-2022, 24 tax years)
### Tax year 1999
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/02pdf/taxpol_btax_99.pdf
- Local file: src/taxpol_btax_99.pdf
- MD5: 660ad4e89fb49881e7c9d7223429b874
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 3
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 13,584 5.0 % $972,426 35.8 %"
  - "REAL ESTATE 43,360 15.8 190,715 7.0"
  - "SERVICES 99,590 36.3 847,417 31.2"
  - "INFORMATION 8,008 2.9 165,048 6.1"
  - "TRADE 51,708 18.9 257,682 9.5"
  - "MANUFACTURING 12,826 4.7 132,617 4.9"
  - "OTHER 44,907 16.4 149,676 5.5"
  - "TOTAL 273,983 100.0 % $2,715,581 100.0 %"
- s6 = 132,617 + 149,676 = 282,293
- Check: the six groups sum to 2,715,581 against the printed total of 2,715,581, a difference of +0K (rounding, within $3K).
### Tax year 2000
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/03pdf/taxpol_btax_00.pdf
- Local file: src/taxpol_btax_00.pdf
- MD5: 2ba7d6f22d582f8e3cdf4105510f34a2
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 10, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 14,071 5.0 % $1,055,702 35.7 %"
  - "REAL ESTATE 44,249 15.8 221,067 7.5"
  - "SERVICES 104,229 37.1 937,761 31.8"
  - "INFORMATION 8,310 3.0 173,716 5.9"
  - "TRADE 53,091 18.9 268,496 9.1"
  - "MANUFACTURING 12,329 4.4 130,448 4.4"
  - "OTHER 44,522 15.9 165,971 5.6"
  - "TOTAL 280,801 100.0 % $2,953,161 100.0 %"
- s6 = 130,448 + 165,971 = 296,419
- Check: the six groups sum to 2,953,161 against the printed total of 2,953,161, a difference of +0K (rounding, within $3K).
### Tax year 2001
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/04pdf/taxpol_bustax_01.pdf
- Local file: src/taxpol_bustax_01.pdf
- MD5: 24988c2d6a4d50889dc20deb7752676c
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 12, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 14,014 4.9 % $889,579 33.5 %"
  - "REAL ESTATE 45,307 15.9 230,210 8.7"
  - "SERVICES 107,096 37.6 852,420 32.1"
  - "INFORMATION 8,310 2.9 155,326 5.9"
  - "TRADE 55,038 19.3 242,202 9.1"
  - "MANUFACTURING 11,949 4.2 132,111 5.0"
  - "OTHER 43,021 15.1 152,954 5.8"
  - "TOTAL 284,735 100.0 % $2,654,802 100.0 %"
- s6 = 132,111 + 152,954 = 285,065
- Check: the six groups sum to 2,654,802 against the printed total of 2,654,802, a difference of +0K (rounding, within $3K).
### Tax year 2002
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/05pdf/taxpol_bustax_02.pdf
- Local file: src/taxpol_bustax_02.pdf
- MD5: 749c1f0e5765e53824d4b32187d35a0f
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 12, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 13,765 4.8 % $791,361 31.2 %"
  - "REAL ESTATE 45,314 15.6 213,848 8.4"
  - "SERVICES 107,117 37.0 854,325 33.7"
  - "INFORMATION 7,986 2.8 172,652 6.8"
  - "TRADE 56,706 19.6 247,496 9.8"
  - "MANUFACTURING 11,327 3.9 109,103 4.3"
  - "OTHER 47,384 16.4 147,737 5.8"
  - "TOTAL 289,599 100.0 % $2,536,522 100.0 %"
- s6 = 109,103 + 147,737 = 256,840
- Check: the six groups sum to 2,536,522 against the printed total of 2,536,522, a difference of +0K (rounding, within $3K).
### Tax year 2003
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/07pdf/stat_prof_nyc_bus_tax1.pdf
- Local file: src/stat_prof_nyc_bus_tax1.pdf
- MD5: 9c196148516bab26524062b6650bad48
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 12, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 14,051 4.8 % $853,804 30.2 %"
  - "REAL ESTATE 46,238 15.8 254,254 9.0"
  - "SERVICES 110,107 37.5 942,997 33.3"
  - "INFORMATION 8,168 2.8 246,113 8.7"
  - "TRADE 56,896 19.4 278,846 9.9"
  - "MANUFACTURING 10,825 3.7 116,714 4.1"
  - "OTHER 47,210 16.1 136,495 4.8"
  - "TOTAL 293,495 100.0 % $2,829,223 100.0 %"
- s6 = 116,714 + 136,495 = 253,209
- Check: the six groups sum to 2,829,223 against the printed total of 2,829,223, a difference of +0K (rounding, within $3K).
### Tax year 2004
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/04pdf/2004_stat_profiles_of_nyc_bus_income_tax.pdf
- Local file: src/2004_stat_profiles_of_nyc_bus_income_tax.pdf
- MD5: 6c776218c65a7340055339857f53fd46
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 12, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 14,380 4.8 % $1,216,484 34.6 %"
  - "REAL ESTATE 46,898 15.7 334,844 9.5"
  - "SERVICES 111,073 37.1 1,079,696 30.7"
  - "INFORMATION 8,122 2.7 237,962 6.8"
  - "TRADE 57,557 19.2 324,886 9.2"
  - "MANUFACTURING 10,347 3.5 168,129 4.8"
  - "OTHER 50,695 17.0 150,613 4.3"
  - "TOTAL 299,072 100.0 % $3,512,614 100.0 %"
- s6 = 168,129 + 150,613 = 318,742
- Check: the six groups sum to 3,512,614 against the printed total of 3,512,614, a difference of +0K (rounding, within $3K).
### Tax year 2005
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/05pdf/bit_report_2005_final.pdf
- Local file: src/bit_report_2005_final.pdf
- MD5: ee482d6b6aeb8621fa5eaa0dc6287816
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 14,901 4.9 % $1,650,538 39.1 %"
  - "REAL ESTATE 47,541 15.7 446,081 10.6"
  - "SERVICES 113,328 37.4 1,187,073 28.1"
  - "INFORMATION 8,083 2.7 266,229 6.3"
  - "TRADE 57,510 19.0 359,527 8.5"
  - "MANUFACTURING 10,026 3.3 145,153 3.4"
  - "OTHER 51,881 17.1 165,596 3.9"
  - "TOTAL 303,270 100.0 % $4,220,197 100.0 %"
- s6 = 145,153 + 165,596 = 310,749
- Check: the six groups sum to 4,220,197 against the printed total of 4,220,197, a difference of +0K (rounding, within $3K).
### Tax year 2006
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/09pdf/bit_report_2006_11_12_09.pdf
- Local file: src/bit_report_2006_11_12_09.pdf
- MD5: cee2080a373d4518fbd6699004e5296e
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 15,725 5.1 % $2,141,844 41.0 %"
  - "REAL ESTATE 48,708 15.8 554,982 10.6"
  - "SERVICES 118,119 38.2 1,375,956 26.3"
  - "INFORMATION 8,318 2.7 316,489 6.1"
  - "TRADE 58,247 18.9 417,372 8.0"
  - "MANUFACTURING 9,904 3.2 204,879 3.9"
  - "OTHER 49,964 16.2 210,907 4.0"
  - "TOTAL 308,985 100.0 % $5,222,429 100.0 %"
- s6 = 204,879 + 210,907 = 415,786
- Check: the six groups sum to 5,222,429 against the printed total of 5,222,429, a difference of +0K (rounding, within $3K).
### Tax year 2007
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/07pdf/bit_report_2007_final.pdf
- Local file: src/bit_report_2007_final.pdf
- MD5: d03a78afffea8c95d8e46d64cb2bde49
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 16,025 5.2 % $2,096,488 39.0 %"
  - "REAL ESTATE 48,753 15.7 650,859 12.1"
  - "SERVICES 120,548 38.8 1,490,307 27.7"
  - "INFORMATION 8,395 2.7 324,312 6.0"
  - "TRADE 58,115 18.7 452,875 8.4"
  - "MANUFACTURING 9,700 3.1 146,927 2.7"
  - "OTHER 49,083 15.8 211,789 3.9"
  - "TOTAL 310,619 100.0 % $5,373,557 100.0 %"
- s6 = 146,927 + 211,789 = 358,716
- Check: the six groups sum to 5,373,557 against the printed total of 5,373,557, a difference of +0K (rounding, within $3K).
### Tax year 2008
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/08pdf/bit_report_%202008.pdf
- Local file: src/bit_report__2008.pdf
- MD5: 0e0bccbd76f63063d615cd61d2249097
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCIAL 16,029 5.2 % $2,065,871 41.2 %"
  - "REAL ESTATE 49,233 15.8 439,243 8.8"
  - "SERVICES 125,669 40.4 1,469,182 29.3"
  - "INFORMATION 8,664 2.8 270,966 5.4"
  - "TRADE 59,044 19.0 356,366 7.1"
  - "MANUFACTURING 9,439 3.0 151,598 3.0"
  - "OTHER 42,908 13.8 263,078 5.2"
  - "TOTAL 310,986 100.0 % $5,016,303 100.0 %"
- s6 = 151,598 + 263,078 = 414,676
- Check: the six groups sum to 5,016,304 against the printed total of 5,016,303, a difference of +1K (rounding, within $3K).
### Tax year 2009
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/09pdf/2009_stat_profiles_of_nyc_bus_income_tax.pdf
- Local file: src/2009_stat_profiles_of_nyc_bus_income_tax.pdf
- MD5: e57d3ec9e971b9e21573135758505ec8
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCE & INSURANCE 15,180 5.0 % $2,081,455 44.6 %"
  - "REAL ESTATE 48,858 16.1 262,778 5.6"
  - "SERVICES 122,409 40.3 1,286,250 27.5"
  - "INFORMATION 8,452 2.8 289,468 6.2"
  - "TRADE 60,214 19.8 366,194 7.8"
  - "MANUFACTURING 9,140 3.0 160,105 3.4"
  - "OTHER 39,210 12.9 224,365 4.8"
  - "TOTAL 303,463 100.0 % $4,670,617 100.0 %"
- s6 = 160,105 + 224,365 = 384,470
- Check: the six groups sum to 4,670,615 against the printed total of 4,670,617, a difference of -2K (rounding, within $3K).
### Tax year 2010
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2010.pdf
- Local file: src/bit_report_2010.pdf
- MD5: 1607a767f723b0d8ddc5afa8a9f8e068
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCE & INSURANCE 15,635 5.0 % $2,416,153 45.5 %"
  - "REAL ESTATE 49,844 15.9 332,576 6.3"
  - "SERVICES 128,710 41.0 1,371,999 25.8"
  - "INFORMATION 8,859 2.8 327,776 6.2"
  - "TRADE 62,152 19.8 430,186 8.1"
  - "MANUFACTURING 9,061 2.9 216,209 4.1"
  - "OTHER 39,287 12.5 220,552 4.1"
  - "TOTAL 313,548 100.0 % $5,315,450 100.0 %"
- s6 = 216,209 + 220,552 = 436,761
- Check: the six groups sum to 5,315,451 against the printed total of 5,315,450, a difference of +1K (rounding, within $3K).
### Tax year 2011
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2011.pdf
- Local file: src/bit_report_2011.pdf
- MD5: 420a7e4c16371ae5592088e7d92c1217
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCE & INSURANCE 16,201 5.0 % $2,380,154 43.6 %"
  - "REAL ESTATE 50,781 15.8 371,480 6.8"
  - "SERVICES 134,556 41.8 1,459,891 26.7"
  - "INFORMATION 9,225 2.9 364,415 6.7"
  - "TRADE 63,457 19.7 474,178 8.7"
  - "MANUFACTURING 9,055 2.8 212,605 3.9"
  - "OTHER 38,974 12.1 201,105 3.7"
  - "TOTAL 322,249 100.0 % $5,463,828 100.0 %"
- s6 = 212,605 + 201,105 = 413,710
- Check: the six groups sum to 5,463,828 against the printed total of 5,463,828, a difference of +0K (rounding, within $3K).
### Tax year 2012
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2012.pdf
- Local file: src/bit_report_2012.pdf
- MD5: b8e8e66c6f2db30a28f74bf90707e3bb
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "FINANCE & INSURANCE 16,534 5.0 % $2,675,441 44.5 %"
  - "REAL ESTATE 51,793 15.7 462,268 7.7"
  - "SERVICES 139,081 42.2 1,586,454 26.4"
  - "INFORMATION 9,737 3.0 364,612 6.1"
  - "TRADE 64,469 19.5 512,120 8.5"
  - "MANUFACTURING 9,089 2.8 196,419 3.3"
  - "OTHER 39,212 11.9 215,431 3.6"
  - "TOTAL 329,915 100.0 % $6,012,745 100.0 %"
- s6 = 196,419 + 215,431 = 411,850
- Check: the six groups sum to 6,012,745 against the printed total of 6,012,745, a difference of +0K (rounding, within $3K).
### Tax year 2013
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2013.pdf
- Local file: src/bit_report_2013.pdf
- MD5: 5370b11541ee2fa265196e494d17db23
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 12, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2013.xlsx (local src/bit_report_2013.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 16,882 4.9 % $2,352,252 41.0 %"
  - "Real Estate 53,382 15.6 426,516 7.4"
  - "Services 145,425 42.4 1,560,484 27.2"
  - "Information 10,118 2.9 479,410 8.4"
  - "Trade 66,649 19.4 501,141 8.7"
  - "Manufacturing 9,271 2.7 186,506 3.3"
  - "Other 41,439 12.1 226,921 4.0"
  - "TOTAL 343,166 100.0 % $5,733,231 100.0 %"
- s6 = 186,506 + 226,921 = 413,427
- Check: the six groups sum to 5,733,230 against the printed total of 5,733,231, a difference of -1K (rounding, within $3K).
### Tax year 2014
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2014.pdf
- Local file: src/bit_report_2014.pdf
- MD5: bfb2645459dc9be707dc6680c99dfc44
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 12, printed page 4
- Taxes in combined table: BCT, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2014.xlsx (local src/bit_report_2014.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 17,607 5.0 % $2,606,164 41.9 %"
  - "Real Estate 54,478 15.5 592,234 9.5"
  - "Services 149,303 42.4 1,685,779 27.1"
  - "Information 10,346 2.9 400,597 6.4"
  - "Trade 67,544 19.2 499,248 8.0"
  - "Manufacturing 9,283 2.6 192,652 3.1"
  - "Other 43,471 12.3 241,445 3.9"
  - "TOTAL 352,032 100.0 % $6,218,119 100.0 %"
- s6 = 192,652 + 241,445 = 434,097
- Check: the six groups sum to 6,218,119 against the printed total of 6,218,119, a difference of +0K (rounding, within $3K).
### Tax year 2015
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2015.pdf
- Local file: src/bit_report_2015.pdf
- MD5: 220e83edfce064dd8c317fe6ab556169
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 12, printed page 4
- Taxes in combined table: COR, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2015.xlsx (local src/bit_report_2015.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 17,681 5.0 % $2,013,463 35.8 %"
  - "Real Estate 55,101 15.5 595,669 10.6"
  - "Services 151,218 42.6 1,699,478 30.2"
  - "Information 10,273 2.9 341,879 6.1"
  - "Trade 67,196 18.9 514,645 9.2"
  - "Manufacturing 9,064 2.6 197,927 3.5"
  - "Other 44,384 12.5 258,902 4.6"
  - "TOTAL 354,917 100.0 % $5,621,961 100.0 %"
- s6 = 197,927 + 258,902 = 456,829
- Check: the six groups sum to 5,621,963 against the printed total of 5,621,961, a difference of +2K (rounding, within $3K).
### Tax year 2016
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2016.pdf
- Local file: src/bit_report_2016.pdf
- MD5: 4a9c880b6825922ebf36e82655c305fb
- Table: Table 3: Distribution by Industry (Business Income Taxes, combined); PDF page 12, printed page 4
- Taxes in combined table: COR, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2016.xlsx (local src/bit_report_2016.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 17,825 5.0 % $1,952,997 35.5 %"
  - "Real Estate 55,820 15.5 570,908 10.4"
  - "Services 153,487 42.7 1,690,188 30.7"
  - "Information 10,460 2.9 311,848 5.7"
  - "Trade 67,425 18.8 479,570 8.7"
  - "Manufacturing 8,993 2.5 195,246 3.5"
  - "Other 45,553 12.7 300,850 5.5"
  - "TOTAL 359,563 100.0 % $5,501,606 100.0 %"
- s6 = 195,246 + 300,850 = 496,096
- Check: the six groups sum to 5,501,607 against the printed total of 5,501,606, a difference of +1K (rounding, within $3K).
### Tax year 2017
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2017.pdf
- Local file: src/bit_report_2017.pdf
- MD5: bfd3aa4a373c494bc2822639cac0fa02
- Table: Table 1: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 5
- Taxes in combined table: COR, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2017.xlsx (local src/bit_report_2017.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 18,123 4.9 % $2,051,132 36.4 %"
  - "Real Estate 56,697 15.5 534,248 9.5"
  - "Services 157,246 42.9 1,816,775 32.3"
  - "Information 10,636 2.9 303,382 5.4"
  - "Trade 67,228 18.3 443,727 7.9"
  - "Manufacturing 8,946 2.4 185,900 3.3"
  - "Other 48,092 13.1 295,762 5.3"
  - "TOTAL 366,968 100.0 % $5,630,926 100.0 %"
- s6 = 185,900 + 295,762 = 481,662
- Check: the six groups sum to 5,630,926 against the printed total of 5,630,926, a difference of +0K (rounding, within $3K).
### Tax year 2018
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2018.pdf
- Local file: src/bit_report_2018.pdf
- MD5: d5433139db56beaa9f17e7f70eccf8a7
- Table: Table 1: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 5
- Taxes in combined table: COR, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2018.xlsx (local src/bit_report_2018.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 18,700 5.0 % $2,275,569 35.1 %"
  - "Real Estate 57,504 15.2 559,840 8.6"
  - "Services 162,995 43.2 2,037,213 31.4"
  - "Information 10,970 2.9 488,684 7.5"
  - "Trade 67,221 17.8 543,279 8.4"
  - "Manufacturing 8,927 2.4 228,241 3.5"
  - "Other 51,003 13.5 352,747 5.4"
  - "TOTAL 377,320 100.0 % $6,485,573 100.0 %"
- s6 = 228,241 + 352,747 = 580,988
- Check: the six groups sum to 6,485,573 against the printed total of 6,485,573, a difference of +0K (rounding, within $3K).
### Tax year 2019
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2019.pdf
- Local file: src/bit_report_2019.pdf
- MD5: 13b799177ea7cb99e1ed20921aa1f569
- Table: Table 1: Distribution by Industry (Business Income Taxes, combined); PDF page 12, printed page 5
- Taxes in combined table: COR, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2019.xlsx (local src/bit_report_2019.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 19,039 5.0 % $2,301,455 34.2 %"
  - "Real Estate 58,062 15.1 519,193 7.7"
  - "Services 167,927 43.8 2,129,142 31.6"
  - "Information 11,242 2.9 610,978 9.1"
  - "Trade 66,808 17.4 548,894 8.2"
  - "Manufacturing 8,908 2.3 253,404 3.8"
  - "Other 51,727 13.5 365,828 5.4"
  - "TOTAL 383,713 100.0 % $6,728,894 100.0 %"
- s6 = 253,404 + 365,828 = 619,232
- Check: the six groups sum to 6,728,894 against the printed total of 6,728,894, a difference of +0K (rounding, within $3K).
### Tax year 2020
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2020.pdf
- Local file: src/bit_report_2020.pdf
- MD5: 54417abeb78a1dd4a8412f395ace4833
- Table: Table 1: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 5
- Taxes in combined table: COR, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2020.xlsx (local src/bit_report_2020.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 19,384 5.1 % $2,530,109 39.8 %"
  - "Real Estate 57,197 15.1 401,808 6.3"
  - "Services 164,857 43.6 1,843,293 29.0"
  - "Information 10,647 2.8 412,376 6.5"
  - "Trade 65,005 17.2 527,842 8.3"
  - "Manufacturing 8,915 2.4 286,227 4.5"
  - "Other 52,044 13.8 361,360 5.7"
  - "TOTAL 378,049 100.0 % $6,363,015 100.0 %"
- s6 = 286,227 + 361,360 = 647,587
- Check: the six groups sum to 6,363,015 against the printed total of 6,363,015, a difference of +0K (rounding, within $3K).
### Tax year 2021
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2021.pdf
- Local file: src/bit_report_2021.pdf
- MD5: 38587a59270ddc39ad8236978dc331e5
- Table: Table 1: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 5
- Taxes in combined table: COR, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2021.xlsx (local src/bit_report_2021.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 21,125 5.5 % $3,175,181 40.3 %"
  - "Real Estate 57,904 15.0 554,424 7.0"
  - "Services 168,953 43.7 2,243,406 28.5"
  - "Information 10,722 2.8 560,772 7.1"
  - "Trade 65,117 16.9 709,684 9.0"
  - "Manufacturing 8,885 2.3 278,553 3.5"
  - "Other 53,476 13.8 360,450 4.6"
  - "TOTAL 386,182 100.0 % $7,882,470 100.0 %"
- s6 = 278,553 + 360,450 = 639,003
- Check: the six groups sum to 7,882,470 against the printed total of 7,882,470, a difference of +0K (rounding, within $3K).
### Tax year 2022
- URL: https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2022.pdf
- Local file: src/bit_report_2022.pdf
- MD5: 284019ad8f82cce40159782e6f2609fb
- Table: Table 1: Distribution by Industry (Business Income Taxes, combined); PDF page 11, printed page 5
- Taxes in combined table: COR, GCT, UBT
- Cross-checked against https://www.nyc.gov/assets/finance/downloads/pdf/reports/business_income_tax_liability/bit_report_2022.xlsx (local src/bit_report_2022.xlsx)
- Rows (Industry, Number, % of total, Liability $K, % of total):
  - "Finance & Insurance 21,308 5.4 % $3,319,281 38.7 %"
  - "Real Estate 57,544 14.7 516,266 6.0"
  - "Services 171,675 43.8 2,462,933 28.7"
  - "Information 10,703 2.7 734,710 8.6"
  - "Trade 64,143 16.4 793,889 9.2"
  - "Manufacturing 8,855 2.3 376,735 4.4"
  - "Other 57,550 14.7 383,260 4.5"
  - "TOTAL 391,778 100.0 % $8,587,075 100.0 %"
- s6 = 376,735 + 383,260 = 759,995
- Check: the six groups sum to 8,587,074 against the printed total of 8,587,075, a difference of -1K (rounding, within $3K).

## Tax years found and not found

Found on the DOF listing page, one report per tax year: 1997 through 2022 (26 reports). Tax years 1994-1996 also appear as per-tax back tables inside the 1997 report.

In the series: 1999-2022.

Left out:
- 1998 (src/gctubt98.pdf, https://www.nyc.gov/assets/finance/downloads/pdf/gctubt98.pdf). The report covers only the GCT and UBT, with no Banking Corporation Tax, and has no combined industry table. It gives only a combined total: "For tax year 1998, these taxpayers generated $2.152 billion in liability." Its industry codes are NAICS, so the per-tax tables could be mapped, but any sum would leave out all bank liability (the BCT was $377M in 1999) and would not be comparable with 1999 onward. The per-tax tables are recorded in biz_by_sector.json under excluded_years and are not summed. The per-tax totals match the report's figure: GCT 1,502,550 + UBT-P 547,094 + UBT-S 102,067 = 2,151,711 ($2.152 billion).
- 1997 (and the 1994-1996 back tables). GCT and UBT only, with no combined table. Industries use IRS Principal Business Activity codes. Report text, verbatim: "The PBA system is similar to the Standard Industrial Classification (SIC) code system and was used by the IRS through 1997." The GCT Table 3 rows are FINANCE & INSURANCE, REAL ESTATE, MANUFACTURING, SERVICES, TRADE and OTHER. There is no Information row and holding companies sit inside Finance, so the mapping is not unambiguous.
- 2023 onward. Not on the listing page; bit_report_2023.pdf and .xlsx (and 2024) return 404. The city publications archive a860-gpp.nyc.gov returned HTTP 403 (Akamai "Access Denied") to curl and to WebFetch, so I could not check whether it holds any other edition. Pre-1997 editions were not found either.

## Basis breaks

1. Tax year 2015, corporate tax reform. 1999-2014 = BCT + GCT + UBT. 2015-2022 = Business Corporation Tax (COR) + GCT + UBT. 2015 report, verbatim: "The Business Corporation Tax, however, applies only to C corporations and does not apply to S corporations". GCT after 2015 covers S corporations only. The BCT is dropped from the report from 2015, footnote verbatim: "to protect taxpayer confidentiality, this report no longer includes the Banking Corporation Tax" and "Banking Corporation Tax liability was less than $5 million in 2015." So 2015+ totals leave out a small amount of BCT. Bank liability formerly under the BCT now sits in COR finance & insurance.
2. 1999 and 2008/2009 labels. The sector row was "FINANCIAL" through 2008 and "FINANCE & INSURANCE" from 2009. The content is the same (see the check above).
3. Liability definition wording. Through the 2013 report: "Liability excludes penalty and interest charges." From the 2014 report: "Liability excludes penalty and interest charges and is net of all refundable credits." I could not confirm whether this is a real method change or a clarification. Small negative liability cells appear after it (e.g. 2016 "$300 or Less" -$810K). Also, in 2009 the UBT business tax credit was expanded (2009 report footnote), which reduced the number of UBT filers with liability.
4. Table numbering. The combined industry table is Table 3 in the 1999-2016 reports and Table 1 in 2017-2022.
5. 2021 NAICS subsector reclassification. It affects Information subsectors only (broadcasting/telecom split; news syndicates moved). The combined Information row is not split, so the series is unaffected beyond that reclassification.
6. 1998 NAICS switch. From the 1999-2003 reports, verbatim: "This system for classifying taxpayers by sector was implemented by the Federal government beginning in tax year 1998." This is one reason 1997 is excluded.

## Not confirmed

- Whether DOF later revised any year's figures. Each value comes from that year's own report, and later reports do not reprint earlier combined tables.
- a860-gpp archive contents (blocked).
- Industry is the taxpayer's national NAICS code, which DOF says may not reflect New York City activity.

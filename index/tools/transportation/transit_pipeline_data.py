# Transit delivery pipeline dataset. One source for the doc, the grid and the map.
# Capital rows: [name, sponsor, cat, PD, ENG, grant, construction start, service, scope, cost $B, CIG $B, lon, lat, mode]
#   cat: F = federal agreement signed, building | N = New Starts / Core Capacity in the pipeline
#        S = Small (Streamlined) Starts in the pipeline | L = not in the federal pipeline
#   0 = not reached / not applicable.  Years are fiscal years.
# Dashboard rows: FTA CIG Dashboard, Sept 11 2026 (cost, CIG request, phase, estimated grant date).
# Grant years for pipeline rows are the dashboard estimate plus a slip: +2 for New Starts over $1B,
# +1 otherwise, reflecting FY2027-28 (divided government, FTA at 552 staff). Service = grant + build time.
# F and L rows were checked against sponsor and press sources on Oct 4 2026. Years are fiscal years, so a
# late-calendar-2027 opening is FY2028. Still unverified: Red Line Extension opening (2030, press only), Honolulu opening
# (Mar 2031 official, Apr 2032 per FTA's consultant; cost is the $10.08B official budget), IndyGo cost (2023 figure), Red-Blue Connector cost
# (2021 concept estimate), Red and Purple Modernization cost (no official estimate; placeholder).
# L-row costs: West Seattle and Ballard are Sound Transit midpoints in 2025 dollars; Sepulveda in 2023 dollars.
# L-row grant, construction and service years are my assumptions, later than sponsor targets where one exists.
CAP = [
 # ---- F: federal agreement signed, under construction
 ["Second Avenue Subway Phase 2","MTA","F",2016,2020,2023,2024,2032,"1.8 miles and three stations to 125th Street, East Harlem. Federal payments held Oct 2025, restored Apr 2026",6.97,3.40,-73.94,40.80,"HR"],
 ["Red Line Extension","Chicago Transit Authority","F",2014,2020,2025,2026,2030,"5.6 miles and four stations from 95th Street to 130th Street",5.75,1.97,-87.62,41.69,"HR"],
 ["D Line Subway Extension, Sections 2 and 3","LA Metro","F",2014,2016,2017,2018,2027,"Wilshire subway from Beverly Hills to Westwood/VA Hospital. Section 1 opened May 2026",6.90,2.50,-118.42,34.06,"HR"],
 ["East San Fernando Valley Light Rail","LA Metro","F",2018,2022,2024,2026,2032,"6.7 miles on Van Nuys Boulevard, 11 stations",3.57,0.89,-118.45,34.21,"LRT"],
 ["Purple Line","Maryland Transit Administration","F",2011,2014,2017,2017,2028,"16 miles of light rail, Bethesda to New Carrollton, 21 stations",9.50,0.90,-77.00,38.99,"LRT"],
 ["METRO Green Line Extension","Metropolitan Council","F",2011,2016,2020,2019,2027,"14.5 miles, Minneapolis to Eden Prairie, 16 stations",2.86,0.93,-93.40,44.90,"LRT"],
 ["Skyline to Civic Center","Honolulu Authority for Rapid Transportation","F",2009,2011,2012,2011,2031,"Final segment of the 18.9-mile automated line into downtown; FTA's consultant projects April 2032",10.08,1.55,-157.86,21.31,"HR"],
 ["Blue Line Bus Rapid Transit","IndyGo","F",2018,0,2024,2025,2029,"24 miles on Washington Street to the airport",0.39,0.15,-86.16,39.77,"BRT"],
 # ---- N: New Starts and Core Capacity in the pipeline (dashboard)
 ["FrontRunner 2X","Utah DOT","N",2022,2026,2028,2028,2031,"Double-tracking the 82-mile commuter line for 15-minute service",3.22,1.29,-111.89,40.76,"CR"],
 ["Red Line Modernization (core capacity)","WMATA","N",2026,2028,2030,2030,2034,"Signals, power and stations on 32 miles and 27 stations",1.60,0.96,-77.03,38.90,"HR"],
 ["Green Line Transformation (core capacity)","MBTA","N",2022,2025,2029,2029,2034,"Longer trains, power and accessible stations on 26.7 miles",4.08,2.04,-71.08,42.35,"LRT"],
 ["Transbay Downtown Rail Extension (The Portal)","Transbay Joint Powers Authority","N",2021,2024,2029,2029,2036,"2.2-mile tunnel bringing Caltrain and high-speed rail to Salesforce Transit Center",8.25,3.38,-122.40,37.79,"CR"],
 ["BART Silicon Valley Phase II","Santa Clara VTA","N",2022,2024,2029,2029,2038,"Six miles and four stations through downtown San Jose to Santa Clara",12.75,5.10,-121.89,37.34,"HR"],
 ["Northeast Corridor Rapid Transit","Miami-Dade DTPW","N",2021,2024,2028,2028,2032,"13.5 miles of commuter rail on the FEC corridor, seven stations",0.93,0.39,-80.19,25.85,"CR"],
 ["METRO Blue Line Extension","Metropolitan Council","N",2014,2017,2028,2028,2031,"13.4 miles, Minneapolis to Brooklyn Park, 13 stations",3.58,0.75,-93.33,45.05,"LRT"],
 ["Lowcountry Rapid Transit","Berkeley-Charleston-Dorchester COG","N",2019,2022,2028,2028,2030,"21.3 miles of bus rapid transit, 20 stations",0.63,0.37,-79.99,32.85,"BRT"],
 ["Richmond Highway Bus Rapid Transit","Fairfax County","N",2020,2024,2028,2028,2032,"7.4 miles, nine stations, Huntington to Fort Belvoir",0.94,0.35,-77.10,38.76,"BRT"],
 ["Eastside Transit Corridor Phase 2","LA Metro","N",2026,2029,2032,2032,2037,"4.7 miles of light rail from East Los Angeles toward Whittier",8.16,0.00,-118.10,34.01,"LRT"],
 ["Southeast Gateway Line","LA Metro","N",2022,2024,2029,2029,2036,"14.5 miles of light rail, nine stations, Slauson to Artesia",10.55,5.19,-118.15,33.90,"LRT"],
 ["Broward Commuter Rail South","Broward County","N",2022,2027,2028,2028,2031,"10.5 miles and three stations on the FEC corridor",0.71,0.35,-80.14,26.05,"CR"],
 ["MD 355 Central Flash Bus Rapid Transit","Montgomery County DOT","N",2024,0,2029,2029,2031,"15.6 miles, 14 stations, Rockville to Germantown",0.50,0.25,-77.18,39.12,"BRT"],
 ["Green Line Bus Rapid Transit","Bi-State Development","N",2024,0,2030,2030,2032,"11.5 miles north-south through St. Louis",0.48,0.00,-90.20,38.63,"BRT"],
 ["Austin Light Rail Phase 1","Austin Transit Partnership","N",2024,2027,2029,2029,2034,"9.8 miles and 15 stations",8.23,4.07,-97.74,30.27,"LRT"],
 ["Interstate Bridge Replacement, light rail","Washington State DOT","N",2023,2027,2030,2030,2035,"1.9-mile MAX extension across the Columbia to Vancouver",1.83,1.00,-122.67,45.62,"LRT"],
 ["Tacoma Dome Link Extension","Sound Transit","N",2026,2028,2031,2031,2036,"8.5 miles and four stations, Federal Way to Tacoma",5.75,0.00,-122.42,47.24,"LRT"],
 # ---- S: Small Starts in the pipeline (dashboard)
 ["Stone Avenue BRT","City of Tucson","S",2023,0,2029,2029,2031,"4.9 miles, 10 stations",0.14,0.08,-110.97,32.24,"BRT"],
 ["Downtown Riverfront Streetcar","Sacramento RT","S",2014,0,2028,2028,2030,"1.5 miles, Sacramento to West Sacramento",0.23,0.00,-121.50,38.58,"SC"],
 ["Federal Boulevard BRT","Colorado DOT","S",2023,0,2028,2028,2030,"18 miles, 38 stations",0.32,0.15,-105.02,39.76,"BRT"],
 ["West Elizabeth BRT","City of Fort Collins","S",2021,0,2029,2029,2031,"3.6 miles to the CSU campus",0.10,0.06,-105.10,40.57,"BRT"],
 ["MARTA Rapid Campbellton","MARTA","S",2022,0,2029,2029,2031,"5.3 miles of center-running bus rapid transit",0.32,0.15,-84.47,33.71,"BRT"],
 ["MARTA Rapid Southlake","MARTA","S",2022,0,2028,2028,2030,"13.3 miles in Clayton County",0.36,0.07,-84.35,33.57,"BRT"],
 ["Blue Hill Avenue Transit Action Plan","MBTA","S",2025,0,2028,2028,2030,"Three miles of center-running bus lanes",0.16,0.08,-71.09,42.29,"BRT"],
 ["Veirs Mill Road Flash BRT","Montgomery County DOT","S",2022,0,2027,2027,2029,"7.6 miles, Wheaton to Rockville",0.19,0.15,-77.08,39.06,"BRT"],
 ["METRO F Line BRT","Metropolitan Council","S",2022,0,2028,2028,2029,"13 miles on Central Avenue",0.10,0.05,-93.25,45.03,"BRT"],
 ["North-South BRT","Chapel Hill Transit","S",2016,0,2027,2027,2030,"8.2 miles, 16 stations",0.20,0.15,-79.05,35.92,"BRT"],
 ["Wake BRT: Southern Corridor","City of Raleigh","S",2021,0,2028,2028,2030,"5.1 miles to Garner",0.17,0.09,-78.64,35.73,"BRT"],
 ["Wake BRT: Western Corridor","City of Raleigh","S",2020,0,2029,2029,2032,"11.3 miles to Cary",0.39,0.15,-78.72,35.79,"BRT"],
 ["Nassau Hub BRT","Nassau County","S",2025,0,2028,2028,2030,"Six miles; cost not yet set",0.04,0.00,-73.60,40.72,"BRT"],
 ["Hamilton Avenue Corridor BRT","SORTA","S",2023,0,2028,2028,2030,"Nine miles, 11 stations",0.17,0.14,-84.54,39.16,"BRT"],
 ["Reading Road Corridor BRT","SORTA","S",2023,0,2028,2028,2030,"9.2 miles, 13 stations",0.17,0.12,-84.48,39.15,"BRT"],
 ["MetroHealth Line BRT","Greater Cleveland RTA","S",2022,0,2028,2028,2029,"3.8 miles on West 25th Street",0.05,0.02,-81.70,41.46,"BRT"],
 ["East Main Street BRT","COTA","S",2021,0,2028,2028,2030,"13.6 miles, 18 stations",0.39,0.15,-82.93,39.96,"BRT"],
 ["Northwest Corridor BRT","COTA","S",2025,0,2029,2029,2031,"8.5 miles, 14 stations",0.36,0.15,-83.04,40.03,"BRT"],
 ["West Broad Street BRT","COTA","S",2021,0,2027,2027,2029,"9.3 miles, 17 stations",0.38,0.15,-83.07,39.96,"BRT"],
 ["MAPS 4 BRT","COPTA, Oklahoma City","S",2025,0,2029,2029,2031,"17 miles on two corridors",0.10,0.03,-97.52,35.47,"BRT"],
 ["Montgomery Park Transit Project","TriMet and City of Portland","S",2024,0,2029,2029,2031,"0.7-mile streetcar extension",0.18,0.00,-122.71,45.54,"SC"],
 ["82nd Avenue Transit Project","TriMet","S",2024,0,2028,2028,2030,"10.1 miles, 35 stations",0.32,0.15,-122.58,45.50,"BRT"],
 ["TV Highway Transit and Safety Project","TriMet","S",2025,0,2029,2029,2031,"16.2 miles, Beaverton to Forest Grove",0.30,0.15,-122.95,45.50,"BRT"],
 ["METRORapid Gulfton","Houston METRO","S",2023,0,2028,2028,2030,"4.1 miles, eight stations",0.22,0.00,-95.48,29.72,"BRT"],
 ["Advanced Rapid Transit East-West","VIA Metropolitan Transit","S",2022,0,2028,2028,2030,"7.3 miles through downtown San Antonio",0.32,0.15,-98.49,29.42,"BRT"],
 ["Davis-Salt Lake City Community Connector","Utah Transit Authority","S",2024,0,2028,2028,2030,"26.6 miles, 20 stations",0.07,0.04,-111.89,40.89,"BRT"],
 ["Swift Gold Line BRT","Community Transit","S",2025,0,2030,2030,2032,"15 miles, Everett to Arlington",0.19,0.00,-122.20,48.05,"BRT"],
 ["RapidRide K Line","King County Metro","S",2019,0,2028,2028,2030,"15.7 miles, Kirkland to Bellevue",0.11,0.05,-122.19,47.64,"BRT"],
 ["Division Street BRT","Spokane Transit","S",2023,0,2027,2027,2030,"Nine miles, 22 stations",0.17,0.08,-117.41,47.70,"BRT"],
 ["Madison North-South BRT","City of Madison","S",2023,0,2027,2027,2029,"12.5 miles, 24 stations",0.18,0.12,-89.39,43.07,"BRT"],
 # ---- L: not in the federal pipeline today; enters under the Act
 ["Interborough Express","MTA","L",2031,2032,2033,2033,2038,"14 miles and 18 stations of light rail on a freight corridor, Brooklyn to Queens",5.50,0.00,-73.90,40.68,"LRT"],
 ["Sepulveda Transit Corridor","LA Metro","L",2031,2033,2035,2035,2043,"About 13 miles of automated heavy rail, seven stations, Van Nuys to the E Line under the Sepulveda Pass",24.20,0.00,-118.47,34.12,"HR"],
 ["West Seattle Link Extension","Sound Transit","L",2031,2031,2032,2032,2037,"3.9 miles and three stations across the Duwamish",5.10,0.00,-122.38,47.56,"LRT"],
 ["Ballard Link Extension","Sound Transit","L",2031,2033,2035,2035,2042,"7.7 miles with a second downtown tunnel; funded only as far as Seattle Center",21.40,0.00,-122.38,47.67,"LRT"],
 ["Baltimore Red Line","Maryland Transit Administration","L",2031,2033,2034,2034,2040,"14 miles east-west; light rail or bus rapid transit, state decision due early 2027",7.00,0.00,-76.61,39.29,"LRT"],
 ["Red-Blue Connector","MBTA","L",2031,2032,2033,2033,2037,"0.4-mile Blue Line extension to Charles/MGH",0.85,0.00,-71.07,42.36,"HR"],
 ["Red and Purple Modernization Phase 2","Chicago Transit Authority","L",2031,2032,2033,2033,2039,"Addison to Sheridan, Thorndale to Howard and the Evanston branch; no published estimate",4.00,0.00,-87.66,41.97,"HR"],
 ["Charlotte Red Line commuter rail","Charlotte Area Transit System","L",2031,2032,2034,2034,2038,"25 miles and 10 stations to Mount Mourne on the Norfolk Southern O-Line",1.26,0.00,-80.84,35.40,"CR"],
 ["Link21 new transbay rail crossing","BART and Capitol Corridor JPA","L",2032,2036,2040,2040,2050,"Standard-gauge transbay crossing shared by regional and intercity rail; $18-30B in 2023 dollars",29.00,0.00,-122.33,37.80,"CR"],
]

# Systems: [name, region, lon, lat, gap text, stage by year function inputs]
#   stage: 1 = gap open, cuts on the table | 2 = stopgap (state one-time money, capital funds or reserves)
#          3 = state or local fix enacted | 4 = federal transition grants (FY2029-30) | 5 = Title II tier (FY2031+)
#   fields: stopgap_from, stopgap_to (inclusive), fixed_from (0 if none), note
SYS = [
 ["MTA New York","New York",-73.99,40.75,2026,2028,0,"Balanced through 2026; reported gaps of $160M, $243M and $306M in 2027-29, with $700M a year of one-time money ending in 2029"],
 ["NJ Transit","New Jersey",-74.17,40.73,2026,2030,0,"$3.5B budget leans on a $765.6M corporate transit fee and a $302M state subsidy"],
 ["WMATA","Washington",-77.03,38.90,2026,2027,2028,"DMVMoves: $460M a year of new capital funding from FY2028, endorsed by Virginia and Maryland leaders"],
 ["SEPTA","Philadelphia",-75.16,39.95,2026,2027,0,"$213M structural deficit; $394M of state capital funds covers operations for two years"],
 ["Pittsburgh Regional Transit","Pittsburgh",-79.99,40.44,2026,2027,0,"$100M-plus deficit deferred to 2027; FY2027 uses $44.8M of capital funds and $15.4M of reserves"],
 ["MBTA","Boston",-71.06,42.36,2026,2028,0,"Gaps closed year to year with state surtax revenue"],
 ["CTA, Metra and Pace","Chicago",-87.63,41.88,2026,2026,2027,"$1.5B state package enacted October 2025"],
 ["BART","San Francisco Bay Area",-122.27,37.80,2026,2027,0,"$350-400M a year; regional sales tax measure on the November 2026 ballot"],
 ["SFMTA (Muni)","San Francisco",-122.42,37.77,2026,2027,0,"$307M, growing to $430M by 2030; cuts from FY2027-28 without new funding"],
 ["TriMet","Portland",-122.68,45.52,2026,2028,0,"Service cuts and layoffs announced May 2026"],
 ["Greater Cleveland RTA","Cleveland",-81.69,41.50,2026,2028,0,"Service cuts in 2026; no long-term source identified"],
 ["Milwaukee County Transit","Milwaukee",-87.91,43.04,2026,2028,0,"County stopgap of $4.8M; 2027 gap unresolved"],
 ["Caltrain and AC Transit","San Francisco Bay Area",-122.20,37.55,2026,2027,0,"Dependent on the same November 2026 regional measure as BART"],
]

def sys_stage(row, y):
    name, reg, lon, lat, s0, s1, fixed, note = row
    if y >= 2031: return 5
    if y >= 2029: return 4
    if fixed and y >= fixed: return 3
    if s0 <= y <= s1: return 2
    return 1

if __name__ == "__main__":
    import json, collections
    cats = collections.Counter(r[2] for r in CAP); print(cats, len(CAP), len(SYS))
    for c in "FNSL":
        rows = [r for r in CAP if r[2] == c]
        print(c, len(rows), "cost", round(sum(r[9] for r in rows), 2), "cig", round(sum(r[10] for r in rows), 2))
    dash = [r for r in CAP if r[2] in "NS"]; print("dashboard rows", len(dash), "cost", round(sum(r[9] for r in dash), 1), "cig", round(sum(r[10] for r in dash), 1), "with cig est", sum(1 for r in dash if r[10] > 0))
    for yr in (2028, 2031, 2036, 2041, 2046):
        print(yr, "in service", sum(1 for r in CAP if r[7] and r[7] <= yr), "building", sum(1 for r in CAP if r[6] and r[6] <= yr and r[7] > yr),
              "big (>$1B) in service", sum(1 for r in CAP if r[7] <= yr and r[9] >= 1))
    # sensitivity: no slip (dashboard dates) -> service by 2031?
    json.dump({"cap": CAP, "sys": SYS}, open("pipeline.json", "w"))

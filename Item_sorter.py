import re

data = """
$Merle Hay Mall    $ Address: 3800 Merle Hay Rd., Des Moines, IA, 50310 1267   $ Phone: (515) 276 8551
$Eastwood Mall    $ Address: 5555 Youngstown Warren Rd., Niles, OH, 44446 4801   $ Phone: (330) 652 6980
$Great Mall of the Bay Area    $ Address: 447 Great Mall Dr., Milpitas, CA, 95035 8041   $ Phone: (408) 956 2033
$Laguna Gateway    $ Address: 9650 Bruceville Rd., Elk Grove, CA, 95757 6117   $ Phone: (916) 683 3005
$Elk Grove Commons    $ Address: 5101 Laguna Blvd., Elk Grove, CA, 95758 7207   $ Phone: (916) 684 1114
$The Highlands    $ Address: 1032 Springdale Rd., Cherry Hill, NJ, 08003 2042   $ Phone: (856) 665 5188
$The Plaza at Cherry Hill    $ Address: 2139 Rt. 38, Cherry Hill, NJ, 08002 2042   $ Phone: (856) 317 1990
$Holmdel Commons    $ Address: 2130 Rt. 35 & Union Ave., Holmdel, NJ, 07733 3038   $ Phone: (732) 335 3700
$Colonial Commons    $ Address: 5084 Jonestown Rd., Harrisburg, PA, 17112 2904   $ Phone: (717) 901 8336
$Boulevard at Box Hill    $ Address: 3412 Merchants Blvd., Abingdon, MD, 21009 1715   $ Phone: (410) 569 0934
$Brandywine Crossing    $ Address: 15902 E. Crain Hwy., Brandywine, MD, 20613 3013   $ Phone: (301) 782 4730
$Marketplace at Inverness Corners    $ Address: 1030 Inverness Corners, Hoover, AL, 35242 5104   $ Phone: (205) 582 0716
$Brandywine Town Center    $ Address: 3334 Brandywine Pkwy., Wilmington, DE, 19803 1481   $ Phone: (302) 478 1462
$Nittany Mall    $ Address: 2901 E. College Ave., State College, PA, 16801 7563   $ Phone: (814) 861 0200
$Eagle Commons    $ Address: 4711 Village Plaza Loop, Eugene, OR, 97401 6692   $ Phone: (541) 357 2288
$Dartmouth Mall    $ Address: 200 N. Dartmouth Mall, Dartmouth, MA, 02747 2300   $ Phone: (508) 994 4777
$Mill Creek Mall    $ Address: 2350 N.W. 9th St., Corvallis, OR, 97330 5883   $ Phone: (541) 738 1327
$Lincoln Plaza    $ Address: 622 George Washington Hwy., Lincoln, RI, 02865 4216   $ Phone: (401) 333 4877
$Clocktower Plaza    $ Address: 15560 W. High St., Middlefield, OH, 44062 8505   $ Phone: (440) 632 1582
$North Hanover Mall    $ Address: 1155 Carlisle St., Hanover, PA, 17331 1226   $ Phone: (717) 632 4880
$Ontario Plaza    $ Address: 2000 N. Rt. 741, Lebanon, OH, 45036 7570   $ Phone: (513) 932 4461
$Triangle Town Center    $ Address: 5959 Triangle Town Blvd., Raleigh, NC, 27616 2786   $ Phone: (919) 792 2222
$University Commons    $ Address: 1815 E. Arbors Dr., Charlotte, NC, 28262 8474   $ Phone: (704) 972 2011
$Providence Marketplace    $ Address: 401 S. Mt. Juliet Rd., Mt. Juliet, TN, 37122 6359   $ Phone: (615) 773 0264
$Goodyear Centerpointe    $ Address: 1005 N. Pebble Creek Pkwy., Goodyear, AZ, 85395 1744   $ Phone: (623) 935 6000
$Laveen Village Marketplace    $ Address: 5035 W. Baseline Rd., Laveen, AZ, 85339 9721   $ Phone: (602) 323 5100
$Valley Vista Crossing    $ Address: 2675 N. 44th St., Phoenix, AZ, 85008 2420   $ Phone: (602) 522 8645
$Maryvale Village    $ Address: 5005 W. Indian School Rd., Phoenix, AZ, 85031 7714   $ Phone: (623) 245 6030
$Westgate Marketplace    $ Address: 2160 E. Baseline Rd., Phoenix, AZ, 85042 6830   $ Phone: (602) 268 9940
$SanTan Village Marketplace    $ Address: 2755 S. Market St., Gilbert, AZ, 85295 1343   $ Phone: (480) 821 2022
$Southgate Plaza    $ Address: 3212 S. 27th St., Milwaukee, WI, 53215 1101   $ Phone: (414) 645 7888
$Brookfield Fashion Center    $ Address: 605 Main St., Brookfield, WI, 53005 4304   $ Phone: (262) 782 1770
$Germantown Plaza    $ Address: W190 N9855 Appleton Ave., Germantown, WI, 53022 5305   $ Phone: (262) 253 0120
$Oak Creek Parkway Plaza    $ Address: 8780 S. Howell Ave., Oak Creek, WI, 53154 7803   $ Phone: (414) 764 2690
$Greenway Station    $ Address: 1650 Deming Way, Middleton, WI, 53562 4732   $ Phone: (608) 824 9111
$The Shoppes at Grand Prairie    $ Address: 5201 W. War Memorial Dr., Peoria, IL, 61615 7107   $ Phone: (309) 692 2200
$Dawley Farm Village    $ Address: 2400 W. 41st St., Sioux Falls, SD, 57105 6051   $ Phone: (605) 361 0806
$Shoppes at Walnut Grove    $ Address: 1025 Washington Pike, Bridgeville, PA, 15017 2833   $ Phone: (412) 257 8780
$Towne Place at Garden State Park    $ Address: 951 Haddonfield Rd., Cherry Hill, NJ, 08002 2011   $ Phone: (856) 910 7901
$Colony Crossing    $ Address: 6360 Ridgewood Ct. Dr., Jackson, MS, 39211 2311   $ Phone: (601) 206 1560
$Traditions Square    $ Address: 3720 Hardy St., Hattiesburg, MS, 39402 1210   $ Phone: (601) 579 0821
$The Forum at Grandview    $ Address: 7071 S. Clinton St., Englewood, CO, 80112 3602   $ Phone: (303) 708 8530
$Westminster Promenade    $ Address: 10649 Westminster Blvd., Westminster, CO, 80020 3902   $ Phone: (303) 439 5228
$Southlands    $ Address: 6155 S. Main St., Aurora, CO, 80016 5315   $ Phone: (303) 662 5305
$Coralville Strip Center    $ Address: 1431 Coral Ridge Ave., Coralville, IA, 52241 2837   $ Phone: (319) 625 0200
$Sierra Center North    $ Address: 1850 Douglas Blvd., Roseville, CA, 95661 3663   $ Phone: (916) 782 2841
$Red Hawk Plaza    $ Address: 2050 Blue Oaks Blvd., Roseville, CA, 95747 7215   $ Phone: (916) 788 2023
$Fountains at Roseville    $ Address: 1182 Roseville Pkwy., Roseville, CA, 95678 1354   $ Phone: (916) 789 2001
$Woodbridge Center    $ Address: 101 Woodbridge Center Dr., Woodbridge, NJ, 07095 1181   $ Phone: (732) 634 0003
$Valley View Mall    $ Address: 4200 W. Valley View Rd., Roanoke, VA, 24012 2037   $ Phone: (540) 563 3600
$The Shops at Valley Square    $ Address: 1501 Main St., Warrington, PA, 18976 2423   $ Phone: (215) 343 7150
$Concordville Town Center    $ Address: 853 E. Baltimore Pike, Kennett Square, PA, 19348 3301   $ Phone: (610) 558 5300
$Presidential Plaza    $ Address: 5150 City Ave., Philadelphia, PA, 19131 1413   $ Phone: (215) 877 0200
$Plymouth Meeting Mall   $ Address: 500 W. Germantown Pike, Plymouth Meeting, PA, 19462 1307   $ Phone: (610) 825 9265
$Montgomery Mall    $ Address: 230 Montgomery Mall, North Wales, PA, 19454 3904   $ Phone: (215) 362 1600
$Willow Grove Park Mall    $ Address: 2500 W. Moreland Rd., Willow Grove, PA, 19090 4116   $ Phone: (215) 657 6000
$Neshaminy Mall    $ Address: 707 Neshaminy Mall, Bensalem, PA, 19020 1609   $ Phone: (215) 357 6100
$Plaza Del Caribe    $ Address: 2050 Ponce Bypass, Ponce, PR, 00717 1439   $ Phone: (787) 844 4760
$Plaza Carolina    $ Address: 525 F.D. Roosevelt Ave., Carolina, PR, 00988 1403   $ Phone: (787) 776 3000
$Aguadilla Mall    $ Address: 1 Ave. Aguadilla Oeste, Aguadilla, PR, 00603 2746   $ Phone: (787) 882 7575
$Las Catalinas Mall    $ Address: 4000 Calle Betances, Caguas, PR, 00726 4283   $ Phone: (787) 653 0480
$Mayagüez Mall    $ Address: 9750 Shopping Dr., Mayagüez, PR, 00680 6314   $ Phone: (787) 834 1616
$Plaza Fajardo    $ Address: 4246 Carretera #3, Fajardo, PR, 00738 7532   $ Phone: (787) 863 1818
$Plaza Isabela    $ Address: Carr. #2 Int. 4495, Isabela, PR, 00662 0418   $ Phone: (787) 830 0900
$Vega Alta Shopping Center    $ Address: 15 Calle Matienzo Cintrón, Vega Alta, PR, 00692 2623   $ Phone: (787) 883 2626
$Plaza Del Norte   $ Address: 725 W. Main Rd., Hatillo, PR, 00659 2285   $ Phone: (787) 898 5100
$Plaza Palma Real    $ Address: 350 Carr. 3, Humacao, PR, 00791 5102   $ Phone: (787) 850 7444
$Arecibo Towne Center    $ Address: 3016 Ave. San Cristobal, Arecibo, PR, 00612 2045   $ Phone: (787) 880 0000
$San Patricio Plaza    $ Address: 100 Ave. San Patricio, Guaynabo, PR, 00968 1408   $ Phone: (787) 781 5353
$Plaza Guayama    $ Address: Carr. 3 KM 134.8, Guayama, PR, 00784 3024   $ Phone: (787) 864 7878
$Western Plaza    $ Address: 67 Ave. Betances, Mayagüez, PR, 00680 4701   $ Phone: (787) 834 2929
$Plaza Cayey    $ Address: 104 Ave. Jesus T. Piñero, Cayey, PR, 00736 2122   $ Phone: (787) 738 2828
$Plaza Río Hondo    $ Address: 60 Ave. Comandante, Bayamon, PR, 00961 5403   $ Phone: (787) 279 8888
$Plaza Caparra    $ Address: 1492 Ave. Américo Miranda, San Juan, PR, 00921 1051   $ Phone: (787) 792 8888
$Plaza Escorial    $ Address: 65 Infanteria Ave., San Juan, PR, 00924 1853   $ Phone: (787) 781 7171
$Plaza Del Sol    $ Address: 725 West Main St., Hatillo, PR, 00659 2285   $ Phone: (787) 898 5100
$Rexville Town Center    $ Address: 166 Ave. Hostos, Bayamón, PR, 00959 7130   $ Phone: (787) 995 7800
$Mayagüez Town Center   $ Address: 9750 Shopping Dr., Mayagüez, PR, 00680 6314   $ Phone: (787) 834 1616
$Plaza Degetau    $ Address: 201 Carr. #3, Humacao, PR, 00791 4540   $ Phone: (787) 285 4747
$Centro Gran Caribe    $ Address: 1445 Ave. Jesús T. Piñero, San Juan, PR, 00921 1916   $ Phone: (787) 767 8484
$Plaza Centro 2    $ Address: Carr. #3 KM 82.6, Lares, PR, 00669 2973   $ Phone: (787) 897 9999
$The Outlet 66 Mall    $ Address: Carr. 666, Canóvanas, PR, 00729 7004   $ Phone: (787) 256 1532
$The Outlets at Montehiedra    $ Address: 950 Ave. Los Romero, San Juan, PR, 00926 2903   $ Phone: (787) 720 3777
$The Mall of San Juan    $ Address: 1000 The Mall of San Juan Blvd., San Juan, PR, 00924 2459   $ Phone: (787) 759 6310
$Plaza del Norte    $ Address: Carr. 2 KM 42.4, Hatillo, PR, 00659 2285   $ Phone: (787) 898 5100
$Calle Loíza Shopping District    $ Address: Calle Loíza, San Juan, PR, 00911
$Centro Comercial Plaza Carolina    $ Address: Ave. Jesús T. Piñero, Carolina, PR, 00987 3304   $ Phone: (787) 776 1111
$Plaza Pradera    $ Address: Carr. 3, Guayama, PR, 00784   $ Phone: (787) 864 7878
$Plaza Monte Verde    $ Address: 5750 Ave. Isla Verde, Carolina, PR, 00979 5805   $ Phone: (787) 257 0053
$Plaza Las Américas    $ Address: 525 F.D. Roosevelt Ave., San Juan, PR, 00918 1907   $ Phone: (787) 767 5202
$Plaza Guaynabo    $ Address: 100 Carr. 165, Guaynabo, PR, 00966 2705   $ Phone: (787) 781 7171
$Rexville Town Center    $ Address: 166 Ave. Hostos, Bayamón, PR, 00959 7130   $ Phone: (787) 995 7800
$Mayagüez Town Center    $ Address: 9750 Shopping Dr., Mayagüez, PR, 00680 6314   $ Phone: (787) 834 1616
$Plaza Degetau    $ Address: 201 Carr. #3, Humacao, PR, 00791 4540   $ Phone: (787) 285 4747
$Centro Gran Caribe    $ Address: 1445 Ave. Jesús T. Piñero, San Juan, PR, 00921 1916   $ Phone: (787) 767 8484
$Plaza Centro 2    $ Address: Carr. #3 KM 82.6, Lares, PR, 00669 2973   $ Phone: (787) 897 9999
$The Outlet 66 Mall    $ Address: Carr. 666, Canóvanas, PR, 00729 7004   $ Phone: (787) 256 1532
$The Outlets at Montehiedra    $ Address: 950 Ave. Los Romero, San Juan, PR, 00926 2903   $ Phone: (787) 720 3777
$The Mall of San Juan    $ Address: 1000 The Mall of San Juan Blvd., San Juan, PR, 00924 2459   $ Phone: (787) 759 6310
$Plaza del Norte   $ Address: Carr. 2 KM 42.4, Hatillo, PR, 00659 2285   $ Phone: (787) 898 5100
$Calle Loíza Shopping District    $ Address: Calle Loíza, San Juan, PR, 00911
$Centro Comercial Plaza Carolina    $ Address: Ave. Jesús T. Piñero, Carolina, PR, 00987 3304   $ Phone: (787) 776 1111
$Plaza Pradera    $ Address: Carr. 3, Guayama, PR, 00784   $ Phone: (787) 864 7878
$Plaza Monte Verde    $ Address: 5750 Ave. Isla Verde, Carolina, PR, 00979 5805   $ Phone: (787) 257 0053
$Plaza Las Américas    $ Address: 525 F.D. Roosevelt Ave., San Juan, PR, 00918 1907   $ Phone: (787) 767 5202
$Plaza Guaynabo     $ Address: 100 Carr. 165, Guaynabo, PR, 00966 2705   $ Phone: (787) 781 7171
$Las Catalinas Mall     $ Address: Carr. 52 KM 2.7, Caguas, PR, 00725 0000   $ Phone: (787) 653 4472
$Centro Comercial Arboleda     $ Address: Carr. 2 KM 85.4, Bo. Palmas, Cataño, PR, 00962   $ Phone: (787) 783 4676
$Centro Gran Caribe     $ Address: 601 Ave. Jesús T. Piñero, San Juan, PR, 00921   $ Phone: (787) 767 8484
$Plaza El Jardín     $ Address: Carr. 1 KM 6.9, Caguas, PR, 00725 3110   $ Phone: (787) 745 2800
$Plaza del Caribe     $ Address: 2050 Ponce By Pass, Ponce, PR, 00717 1500   $ Phone: (787) 259 8989
$Ponce Town Center     $ Address: 1050 Carr. 2, Ponce, PR, 00728 3913   $ Phone: (787) 259 7745
$Plaza Caparra Shopping Center     $ Address: Carr. 2 KM 7.1, Guaynabo, PR, 00966   $ Phone: (787) 286 2610
$Plaza Palma Real     $ Address: Carr. 3, Humacao, PR, 00791   $ Phone: (787) 852 0000
$The Mall of San Juan     $ Address: 1000 The Mall of San Juan Blvd., San Juan, PR, 00924 2459   $ Phone: (787) 759 6310
$The Outlet 66 Mall     $ Address: Carr. 666, Canóvanas, PR, 00729 7004   $ Phone: (787) 256 1532
$The Outlets at Montehiedra     $ Address: 950 Ave. Los Romero, San Juan, PR, 00926 2903   $ Phone: (787) 720 3777
$Plaza del Norte     $ Address: Carr. 2 KM 42.4, Hatillo, PR, 00659 2285   $ Phone: (787) 898 5100
$Centro Comercial Plaza Carolina     $ Address: Ave. Jesús T. Piñero, Carolina, PR, 00987 3304   $ Phone: (787) 776 1111
$Plaza Pradera     $ Address: Carr. 3, Guayama, PR, 00784   $ Phone: (787) 864 7878
$Plaza Monte Verde     $ Address: 5750 Ave. Isla Verde, Carolina, PR, 00979 5805   $ Phone: (787) 257 0053
$Plaza Las Américas     $ Address: 525 F.D. Roosevelt Ave., San Juan, PR, 00918 1907   $ Phone: (787) 767 5202
$Plaza Guaynabo     $ Address: 100 Carr. 165, Guaynabo, PR, 00966 2705   $ Phone: (787) 781 7171
$Las Catalinas Mall     $ Address: Carr. 52 KM 2.7, Caguas, PR, 00725 0000   $ Phone: (787) 653 4472
$Centro Comercial Arboleda     $ Address: Carr. 2 KM 85.4, Bo. Palmas, Cataño, PR, 00962   $ Phone: (787) 783 4676
$Centro Gran Caribe     $ Address: 601 Ave. Jesús T. Piñero, San Juan, PR, 00921   $ Phone: (787) 767 8484
$Plaza El Jardín     $ Address: Carr. 1 KM 6.9, Caguas, PR, 00725 3110   $ Phone: (787) 745 2800
$Plaza del Caribe     $ Address: 2050 Ponce By Pass, Ponce, PR, 00717 1500   $ Phone: (787) 259 8989
$Ponce Town Center     $ Address: 1050 Carr. 2, Ponce, PR, 00728 3913   $ Phone: (787) 259 7745
$Plaza Caparra Shopping Center     $ Address: Carr. 2 KM 7.1, Guaynabo, PR, 00966   $ Phone: (787) 286 2610
$Plaza Palma Real     $ Address: Carr. 3, Humacao, PR, 00791   $ Phone: (787) 852 0000
$The Mall of San Juan     $ Address: 1000 The Mall of San Juan Blvd., San Juan, PR, 00924 2459   $ Phone: (787) 759 6310
$The Outlet 66 Mall     $ Address: Carr. 666, Canóvanas, PR, 00729 7004   $ Phone: (787) 256 1532
$The Outlets at Montehiedra     $ Address: 950 Ave. Los Romero, San Juan, PR, 00926 2903   $ Phone: (787) 720 3777
$Plaza del Norte     $ Address: Carr. 2 KM 42.4, Hatillo, PR, 00659 2285   $ Phone: (787) 898 5100
$Centro Comercial Plaza Carolina     $ Address: Ave. Jesús T. Piñero, Carolina, PR, 00987 3304   $ Phone: (787) 776 1111
$Plaza Pradera     $ Address: Carr. 3, Guayama, PR, 00784   $ Phone: (787) 864 7878
$Plaza Monte Verde     $ Address: 5750 Ave. Isla Verde, Carolina, PR, 00979 5805   $ Phone: (787) 257 0053
$Plaza Las Américas     $ Address: 525 F.D. Roosevelt Ave., San Juan, PR, 00918 1907   $ Phone: (787) 767 5202
$Plaza Guaynabo     $ Address: 100 Carr. 165, Guaynabo, PR, 00966 2705   $ Phone: (787) 781 7171
$San Patricio Plaza     $ Address: 100 Carr. 1, Guaynabo, PR, 00968 1407   $ Phone: (787) 782 0231
$Plaza Río Hondo     $ Address: Carr. 2 KM 8.5, Bayamón, PR, 00961   $ Phone: (787) 785 0345
$Centro Comercial Los Colobos     $ Address: F.D. Roosevelt Ave., Carolina, PR, 00983   $ Phone: (787) 776 7474
$Centro Comercial Santa Rosa     $ Address: Carr. 3 KM 14.9, Trujillo Alto, PR, 00976   $ Phone: (787) 748 1810
$Plaza Caparra     $ Address: 100 Carr. 2, Guaynabo, PR, 00966 2705   $ Phone: (787) 781 7171
$Plaza Carolina     $ Address: 75 Carr. 3, Carolina, PR, 00987 8323   $ Phone: (787) 769 3544
$Plaza del Carmen Shopping Center     $ Address: Carr. 2 KM 85.3, Cataño, PR, 00962   $ Phone: (787) 789 2701
$Plaza del Oeste     $ Address: 100 Carr. 2, Mayagüez, PR, 00680 5468   $ Phone: (787) 834 2316
$Plaza del Sol     $ Address: Carr. 2 KM 77.4, Dorado, PR, 00646 9204   $ Phone: (787) 796 5130
$Plaza Escorial     $ Address: Carr. 2 KM 8.7, San Juan, PR, 00924   $ Phone: (787) 782 6434
$Plaza Fajardo     $ Address: 4515 Carr. 3, Fajardo, PR, 00738   $ Phone: (787) 863 4040
$Plaza Ferrán     $ Address: 260 Carr. 1, Guaynabo, PR, 00965 7505   $ Phone: (787) 287 7805
$Plaza Guayama     $ Address: Carr. 3, Guayama, PR, 00784   $ Phone: (787) 864 7878
$Plaza Isabela     $ Address: Carr. 2 KM 117.8, Isabela, PR, 00662   $ Phone: (787) 872 5400
$Plaza La Campiña     $ Address: 2850 Carr. 3, Toa Alta, PR, 00953   $ Phone: (787) 784 2290
$Plaza Las Delicias     $ Address: 113 Cristina St., Ponce, PR, 00730 6719   $ Phone: (787) 843 2532
$Plaza Las Lomas     $ Address: 300 Carr. 159, Toa Alta, PR, 00953 3347   $ Phone: (787) 870 2710
$Plaza Las Vegas     $ Address: Carr. 159, Toa Baja, PR, 00949   $ Phone: (787) 795 8500
$Plaza Las Vistas     $ Address: Carr. 177, Hato Rey, PR, 00919   $ Phone: (787) 282 1112
$Plaza Los Prados     $ Address: Carr. 2 KM 24.0, Caguas, PR, 00725   $ Phone: (787) 286 2610
$Plaza Mayor Shopping Center     $ Address: Carr. 2, Manatí, PR, 00674 9667   $ Phone: (787) 854 8872
$Plaza Mendoza     $ Address: Carr. 173, Caguas, PR, 00725 0467   $ Phone: (787) 286 2610
$Plaza Montehiedra     $ Address: Carr. 177, San Juan, PR, 00926 2605   $ Phone: (787) 282 1112
$Plaza Munoz Marin     $ Address: 2850 Carr. 3, Toa Alta, PR, 00953   $ Phone: (787) 870 2710
$Plaza Palma del Mar     $ Address: Carr. 3, Humacao, PR, 00791   $ Phone: (787) 852 0000
$Plaza Palma Real     $ Address: Carr. 2, Vega Alta, PR, 00692   $ Phone: (787) 260 5050
$Plaza Palma Real     $ Address: Carr. 2 KM 43.2, Vega Alta, PR, 00692   $ Phone: (787) 260 5050
$Plaza Pradera     $ Address: Carr. 3, Guayama, PR, 00784   $ Phone: (787) 864 7878
$Plaza Progreso Shopping Center     $ Address: Carr. 2, Toa Baja, PR, 00949 3308   $ Phone: (787) 251 3303
$Plaza Rio Hondo     $ Address: 100 Carr. 1, Bayamón, PR, 00961   $ Phone: (787) 785 0345
$Plaza San Francisco     $ Address: Carr. 848, San Juan, PR, 00926   $ Phone: (787) 250 7035
$Plaza San Juan     $ Address: 150 Carr. 2, San Juan, PR, 00926   $ Phone: (787) 781 7171
$Plaza San Patricio     $ Address: Carr. 2 KM 85.3, Guaynabo, PR, 00969   $ Phone: (787) 748 1810
$Plaza Santiago Shopping Center     $ Address: Carr. 172, Caguas, PR, 00725   $ Phone: (787) 286 2610
$Plaza Suchville     $ Address: Carr. 2 KM 17.1, Bayamón, PR, 00956   $ Phone: (787) 290 1070
$Plaza Tropical     $ Address: Carr. 115, Rincón, PR, 00677   $ Phone: (787) 823 6666
$Plaza Vega Baja Shopping Center     $ Address: Carr. 2, Vega Baja, PR, 00694   $ Phone: (787) 260 5050
$Plaza Villa Carolina     $ Address: Carr. 853, Carolina, PR, 00987   $ Phone: (787) 776 3110
$Plaza Villa Esperanza     $ Address: Carr. 181, San Juan, PR, 00926   $ Phone: (787) 796 2878
$Plaza Villa Prades     $ Address: Carr. 1, Caguas, PR, 00725   $ Phone: (787) 286 2610
$Plaza Villa Prades     $ Address: Carr. 172, Caguas, PR, 00725   $ Phone: (787) 286 2610
$Plaza Villa Roca     $ Address: Carr. 111, San Juan, PR, 00920   $ Phone: (787) 765 1212
$Plaza Villas de Caney     $ Address: Carr. 158, Bayamón, PR, 00959   $ Phone: (787) 288 9009
$Plaza Vista Canovanas     $ Address: Carr. 185, Canóvanas, PR, 00729   $ Phone: (787) 256 3300
$Ponce Mall     $ Address: 500 Carr. 12, Ponce, PR, 00730   $ Phone: (787) 844 2000
$Pradera Shopping Center     $ Address: Carr. 106, Aguadilla, PR, 00603   $ Phone: (787) 793 3488
$Premium Outlets    $ Address: 1 Premium Outlets Blvd, Barceloneta, PR, 00617   $ Phone: (787) 846 5300
$Prime Outlet Barceloneta    $ Address: Carr. 1, Barceloneta, PR, 00617   $ Phone: (787) 846 5300
$Pueblo Bayamón    $ Address: Carr. 2 KM 16.1, Bayamón, PR, 00959   $ Phone: (787) 787 242 1990
$Pueblo Caguas Norte    $ Address: Carr. 183, Caguas, PR, 00725   $ Phone: (787) 286 2610
$Pueblo Canóvanas    $ Address: Carr. 3, Canóvanas, PR, 00729   $ Phone: (787) 256 3300
$Pueblo Canóvanas    $ Address: Carr. 66, Canóvanas, PR, 00729   $ Phone: (787) 256 3300
$Pueblo Carolina    $ Address: Carr. 853, Carolina, PR, 00987   $ Phone: (787) 776 3110
$Pueblo Dorado    $ Address: Carr. 105, Dorado, PR, 00646   $ Phone: (787) 796 2878
$Pueblo Dorado    $ Address: Carr. 2, Dorado, PR, 00646   $ Phone: (787) 796 2878
$Pueblo Fajardo    $ Address: Carr. 195, Fajardo, PR, 00738   $ Phone: (787) 860 3000
"""

# Split the data into sections for each location
locations = re.split(r'\n(?=\d)', data.strip())

# Process each location and print the results
for location in locations:
    lines = location.strip().split('$')
    name = lines[0]
    Address = ', '.join(lines[1:1])
    Phone_number = lines[1]
    print (f"Name: {name}\n Address: { - Address}\n Phone Number: {- Phone_number}\n")

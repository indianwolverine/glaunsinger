import pandas as pd
import numpy as np

minus = pd.read_excel("read-counts.xlsx", sheet_name="Sheet2")
plus = pd.read_excel("read-counts.xlsx", sheet_name="Sheet3")
minus = minus.sort_values(by=["Name"])
plus = plus.sort_values(by=["Name"])

minus_names = ['1.tRNA1001-LeuCAG', '1.tRNA1002-AspGTC', '1.tRNA1003-GlyTCC',
       '1.tRNA1004-GluCTC', '1.tRNA1005-AspGTC', '1.tRNA1006-GlyTCC',
       '1.tRNA1007-GluCTC', '1.tRNA1008-AspGTC', '1.tRNA1009-GlyTCC',
       '1.tRNA1010-GluCTC', '1.tRNA1012-GlyTCC', '1.tRNA1013-AspGTC',
       '1.tRNA1014-AsnGTT', '1.tRNA1027-Undet???', '1.tRNA1030-ProCGG',
       '1.tRNA111-IleGAT', '1.tRNA1153-Undet???', '1.tRNA1182-SerGCT',
       '1.tRNA1192-LysTTT', '1.tRNA1378-SerGCT', '1.tRNA1400-GlyGCC',
       '1.tRNA1491-AsnGTT', '1.tRNA154-AsnGTT', '1.tRNA1555-GluTTC',
       '1.tRNA1612-Undet???', '1.tRNA167-SerACT', '1.tRNA18-AsnGTT',
       '1.tRNA198-SerGCT', '1.tRNA210-AsnATT', '1.tRNA219-SerACT',
       '1.tRNA485-LysTTT', '1.tRNA631-SerGCT', '1.tRNA672-ProAGG',
       '1.tRNA698-LeuCAG', '1.tRNA699-GlyGCC', '1.tRNA701-LeuCAG',
       '1.tRNA702-GlyGCC', '1.tRNA703-LeuCAG', '1.tRNA704-GlyGCC',
       '1.tRNA705-LeuCAG', '1.tRNA706-GlyGCC', '1.tRNA707-AspGTC',
       '1.tRNA708-GlyTCC', '1.tRNA709-GluCTC', '1.tRNA710-ValCAC',
       '1.tRNA712-IleGAT', '1.tRNA737-SeCTCA', '1.tRNA775-AsnGTT',
       '1.tRNA790-SerGCT', '10.tRNA1105-SerTGA', '10.tRNA1201-SerGCT',
       '10.tRNA1261-SerGCT', '10.tRNA1326-LeuTAA', '10.tRNA270-Undet???',
       '10.tRNA390-AsnGTT', '10.tRNA495-SerGCT', '10.tRNA500-SerACT',
       '10.tRNA502-SerGCT', '10.tRNA503-SerGCT', '10.tRNA698-SerCGA',
       '10.tRNA854-SerGCT', '10.tRNA861-AspGTC', '10.tRNA866-AspGTC',
       '10.tRNA867-TrpCCA', '10.tRNA90-GluCTC', '10.tRNA971-PheGAA',
       '10.tRNA976-ArgGCG', '10.tRNA987-SerGCT', '10.tRNA990-SerGCT',
       '11.tRNA1022-ArgCCT', '11.tRNA1023-ArgTCG', '11.tRNA1027-SerACT',
       '11.tRNA1144-SerGCT', '11.tRNA1234-ArgCCT', '11.tRNA1348-SerGCT',
       '11.tRNA137-SerGCT', '11.tRNA1432-CysGCA', '11.tRNA1433-CysGCA',
       '11.tRNA1442-CysGCA', '11.tRNA1444-CysGCA', '11.tRNA1446-AsnGTT',
       '11.tRNA1493-GlnTTG', '11.tRNA1592-SerGCT', '11.tRNA163-AsnGTT',
       '11.tRNA1631-GlyGCC', '11.tRNA1743-SerGCT', '11.tRNA1816-LysTTT',
       '11.tRNA1817-GlnCTG', '11.tRNA1818-ArgTCT', '11.tRNA1819-GlyGCC',
       '11.tRNA1820-TrpCCA', '11.tRNA1821-SerGCT', '11.tRNA1822-ThrAGT',
       '11.tRNA1823-IleAAT', '11.tRNA1824-GlyTCC', '11.tRNA1849-TrpCCA',
       '11.tRNA1880-TrpCCA', '11.tRNA1911-LeuCAA', '11.tRNA1912-GluCTC',
       '11.tRNA2022-AlaTGC', '11.tRNA204-ValCAC', '11.tRNA205-GlyACC',
       '11.tRNA206-ThrTGT', '11.tRNA207-ProTGG', '11.tRNA208-ValAAC',
       '11.tRNA2092-SerACT', '11.tRNA245-SerGCT', '11.tRNA311-SerGCT',
       '11.tRNA328-Undet???', '11.tRNA393-IleAAT', '11.tRNA394-SerAGA',
       '11.tRNA395-ThrAGT', '11.tRNA396-ProCGG', '11.tRNA397-AspGTC',
       '11.tRNA398-TrpCCA', '11.tRNA399-ThrAGT', '11.tRNA400-SerCGA',
       '11.tRNA401-LeuTAG', '11.tRNA516-SerGCT', '11.tRNA550-ThrCGT',
       '11.tRNA630-GlnTTG', '11.tRNA64-SerGCT', '11.tRNA69-AspGTC',
       '11.tRNA750-SerGCT', '11.tRNA791-CysGCA', '11.tRNA818-IleGAT',
       '11.tRNA87-SerGCT', '11.tRNA884-SerGCT', '11.tRNA945-ArgCCG',
       '11.tRNA961-SerGCT', '12.tRNA22-SerGCT', '12.tRNA275-SerGCT',
       '12.tRNA42-SerGCT', '12.tRNA476-IleAAT', '12.tRNA60-AlaAGC',
       '12.tRNA796-LysCTT', '12.tRNA842-IleGAT', '13.tRNA100-IleAAT',
       '13.tRNA1000-PheGAA', '13.tRNA1001-IleAAT', '13.tRNA1002-IleAAT',
       '13.tRNA1003-LeuTAA', '13.tRNA1006-MetCAT', '13.tRNA1007-GlnTTG',
       '13.tRNA1008-ThrAGT', '13.tRNA1009-ArgCCG', '13.tRNA1010-LeuCAA',
       '13.tRNA1011-MetCAT', '13.tRNA1012-LysTTT', '13.tRNA1013-GluCTC',
       '13.tRNA102-AlaAGC', '13.tRNA103-LysCTT', '13.tRNA104-ThrAGT',
       '13.tRNA105-GluTTC', '13.tRNA106-TyrGTA', '13.tRNA107-TrpCCA',
       '13.tRNA108-MetCAT', '13.tRNA109-TrpCCA', '13.tRNA110-GlyGCC',
       '13.tRNA111-MetCAT', '13.tRNA112-SerTGA', '13.tRNA113-GlnTTG',
       '13.tRNA114-GlnTTG', '13.tRNA115-SerGCT', '13.tRNA226-SerGCT',
       '13.tRNA271-SerGCT', '13.tRNA382-IleGAT', '13.tRNA539-AlaAGC',
       '13.tRNA60-PheGAA', '13.tRNA61-MetCAT', '13.tRNA64-GlnCTG',
       '13.tRNA65-LeuCAA', '13.tRNA66-AlaAGC', '13.tRNA67-AlaAGC',
       '13.tRNA68-AlaTGC', '13.tRNA69-AlaAGC', '13.tRNA70-AlaCGC',
       '13.tRNA71-AlaAGC', '13.tRNA72-ThrCGT', '13.tRNA73-ThrTGT',
       '13.tRNA74-ArgTCG', '13.tRNA75-ThrCGT', '13.tRNA78-MetCAT',
       '13.tRNA79-SupTTA', '13.tRNA81-ThrAGT', '13.tRNA82-MetCAT',
       '13.tRNA83-LysTTT', '13.tRNA84-AspGTC', '13.tRNA85-LeuCAA',
       '13.tRNA86-SerAGA', '13.tRNA863-SerGCT', '13.tRNA87-GlnCTG',
       '13.tRNA88-SerAGA', '13.tRNA89-LysTTT', '13.tRNA90-MetCAT',
       '13.tRNA91-ValCAC', '13.tRNA92-IleAAT', '13.tRNA93-ValAAC',
       '13.tRNA95-ValAAC', '13.tRNA958-ThrAGT', '13.tRNA959-MetCAT',
       '13.tRNA96-AlaAGC', '13.tRNA960-ArgTCG', '13.tRNA961-ArgTCG',
       '13.tRNA962-SerAGA', '13.tRNA963-ArgACG', '13.tRNA964-LeuCAG',
       '13.tRNA965-ArgACG', '13.tRNA966-ValCAC', '13.tRNA967-AlaCGC',
       '13.tRNA968-IleAAT', '13.tRNA969-ProAGG', '13.tRNA97-ValCAC',
       '13.tRNA970-TyrGTA', '13.tRNA972-TyrGTA', '13.tRNA973-TyrGTA',
       '13.tRNA974-ValAAC', '13.tRNA975-AlaAGC', '13.tRNA976-ValCAC',
       '13.tRNA977-ValAAC', '13.tRNA978-AlaAGC', '13.tRNA98-ValCAC',
       '13.tRNA980-IleAAT', '13.tRNA981-IleTAT', '13.tRNA982-SerGCT',
       '13.tRNA983-ThrAGT', '13.tRNA984-SerCGA', '13.tRNA985-ArgACG',
       '13.tRNA986-ValAAC', '13.tRNA987-GlnCTG', '13.tRNA988-SerGCT',
       '13.tRNA99-MetCAT', '13.tRNA990-SerAGA', '13.tRNA991-AspGTC',
       '13.tRNA992-SerAGA', '13.tRNA993-AspGTC', '13.tRNA994-GlnCTG',
       '13.tRNA995-MetCAT', '13.tRNA996-SerTGA', '13.tRNA997-ArgTCT',
       '13.tRNA999-IleTAT', '14.tRNA168-SerGCT', '14.tRNA189-LeuAAG',
       '14.tRNA191-ThrTGT', '14.tRNA192-TyrGTA', '14.tRNA193-ProTGG',
       '14.tRNA202-SerGCT', '14.tRNA210-ArgACG', '14.tRNA238-SerGCT',
       '14.tRNA28-AsnGTT', '14.tRNA286-SerGCT', '14.tRNA352-GluTTC',
       '14.tRNA364-GluTTC', '14.tRNA462-PheGAA', '14.tRNA493-SerGCT',
       '14.tRNA570-AsnGTT', '14.tRNA709-LeuTAG', '14.tRNA710-ThrTGT',
       '14.tRNA711-ProAGG', '14.tRNA823-SerGCT', '15.tRNA1018-SerGCT',
       '15.tRNA1063-Undet???', '15.tRNA11-SerGCT', '15.tRNA183-AsnGTT',
       '15.tRNA238-AsnGTT', '15.tRNA342-SerGCT', '15.tRNA396-SerGCT',
       '15.tRNA602-SerGCT', '15.tRNA736-SerGCT', '15.tRNA755-Undet???',
       '15.tRNA850-SerGCT', '15.tRNA876-MetCAT', '15.tRNA913-MetCAT',
       '15.tRNA975-SerACT', '16.tRNA273-AsnGTT', '16.tRNA300-SerGCT',
       '16.tRNA305-SerGCT', '16.tRNA308-Undet???', '16.tRNA315-IleAAT',
       '16.tRNA50-ThrCGT', '16.tRNA561-Undet???', '16.tRNA630-SerGCT',
       '16.tRNA701-SerACT', '16.tRNA706-GlyGCC', '17.tRNA1021-SerGCT',
       '17.tRNA112-GlyCCC', '17.tRNA418-SerGCT', '17.tRNA457-CysGCA',
       '17.tRNA466-Undet???', '17.tRNA515-IleTAT', '17.tRNA53-SerGCT',
       '17.tRNA613-SerGCT', '17.tRNA717-SerGCT', '17.tRNA772-SerGCT',
       '17.tRNA82-ProCGG', '17.tRNA873-ThrAGT', '17.tRNA993-ArgCCG',
       '17.tRNA994-ArgCCT', '17.tRNA995-ProTGG', '17.tRNA999-LysCTT',
       '18.tRNA323-SerGCT', '18.tRNA54-SerGCT', '19.tRNA106-PheGAA',
       '19.tRNA107-LysTTT', '19.tRNA109-ValTAC', '19.tRNA110-ValTAC',
       '19.tRNA145-SerGCT', '19.tRNA196-SerGCT', '19.tRNA326-SerACT',
       '19.tRNA62-AlaAGC', '19.tRNA630-SerGCT', '19.tRNA639-ArgTCT',
       '19.tRNA640-LeuTAA', '19.tRNA641-LysTTT', '19.tRNA713-SerGCT',
       '19.tRNA8-AlaAGC', '2.tRNA105-Undet???', '2.tRNA1158-SerGCT',
       '2.tRNA1238-SerGCT', '2.tRNA1292-AsnGTT', '2.tRNA1431-HisGTG',
       '2.tRNA1432-HisGTG', '2.tRNA1437-SerGCT', '2.tRNA1506-IleGAT',
       '2.tRNA1509-SerGCT', '2.tRNA1600-SerGCT', '2.tRNA1747-GlyGCC',
       '2.tRNA1832-SerGCT', '2.tRNA1918-SerGCT', '2.tRNA1947-AsnGTT',
       '2.tRNA263-AlaCGC', '2.tRNA277-SerGCT', '2.tRNA28-SerGCT',
       '2.tRNA341-Undet???', '2.tRNA416-ArgTCT', '2.tRNA587-HisGTG',
       '2.tRNA644-ArgTCT', '2.tRNA840-IleGAT', '3.tRNA1026-LeuCAG',
       '3.tRNA1040-ArgACG', '3.tRNA240-TyrGTA', '3.tRNA27-TyrGTA',
       '3.tRNA28-TyrGTA', '3.tRNA283-AsnGTT', '3.tRNA284-ValCAC',
       '3.tRNA286-GluTTC', '3.tRNA287-GlyCCC', '3.tRNA288-GlnTTG',
       '3.tRNA289-AsnGTT', '3.tRNA29-AlaAGC', '3.tRNA291-HisGTG',
       '3.tRNA292-LysCTT', '3.tRNA293-HisGTG', '3.tRNA294-AsnGTT',
       '3.tRNA295-HisGTG', '3.tRNA297-GlnCTG', '3.tRNA298-AsnGTT',
       '3.tRNA303-GluCTC', '3.tRNA309-GlnCTG', '3.tRNA48-ValAAC',
       '3.tRNA584-SerGCT', '3.tRNA628-ArgTCT', '3.tRNA745-GluCTC',
       '3.tRNA746-GlyTCC', '3.tRNA747-HisGTG', '3.tRNA748-LysCTT',
       '3.tRNA749-HisGTG', '3.tRNA750-AsnGTT', '3.tRNA751-HisGTG',
       '3.tRNA752-GlyCCC', '3.tRNA753-GlnCTG', '3.tRNA754-GluTTC',
       '3.tRNA755-GlyCCC', '3.tRNA756-GlnCTG', '3.tRNA757-AsnGTT',
       '3.tRNA792-MetCAT', '3.tRNA849-SerGCT', '3.tRNA878-GlyGCC',
       '3.tRNA92-ProTGG', '3.tRNA93-ProAGG', '3.tRNA964-SerGCT',
       '3.tRNA99-AsnGTT', '4.tRNA1019-SerGCT', '4.tRNA1066-SerGCT',
       '4.tRNA1358-SerGCT', '4.tRNA141-SerGCT', '4.tRNA16-SerAGA',
       '4.tRNA1614-SerGCT', '4.tRNA1622-TyrGTA', '4.tRNA1657-SerGCT',
       '4.tRNA1691-HisGTG', '4.tRNA1813-SerGCT', '4.tRNA1838-SerGCT',
       '4.tRNA1908-SerGCT', '4.tRNA1916-SerGCT', '4.tRNA1952-Undet???',
       '4.tRNA241-SerGCT', '4.tRNA249-SerGCT', '4.tRNA391-SerGCT',
       '4.tRNA434-SerGCT', '4.tRNA62-IleAAT', '4.tRNA697-SerGCT',
       '4.tRNA837-SerGCT', '4.tRNA844-AsnGTT', '4.tRNA847-SerGCT',
       '4.tRNA947-Undet???', '5.tRNA1044-AsnGTT', '5.tRNA109-TyrGTA',
       '5.tRNA110-AlaAGC', '5.tRNA111-SerGCT', '5.tRNA1165-AlaTGC',
       '5.tRNA1315-AspGTC', '5.tRNA1316-PheGAA', '5.tRNA1317-AspGTC',
       '5.tRNA1318-AlaTGC', '5.tRNA1709-AsnGTT', '5.tRNA185-SerGCT',
       '5.tRNA221-SerGCT', '5.tRNA366-AsnGTT', '5.tRNA410-SerGCT',
       '5.tRNA411-SerGCT', '5.tRNA474-SerGCT', '5.tRNA703-AlaTGC',
       '5.tRNA740-SerGCT', '5.tRNA882-AsnGTT', '6.tRNA10-ValCAC',
       '6.tRNA1005-CysGCA', '6.tRNA1006-CysGCA', '6.tRNA1008-CysGCA',
       '6.tRNA1009-CysGCA', '6.tRNA1012-CysGCA', '6.tRNA1013-CysGCA',
       '6.tRNA1016-CysGCA', '6.tRNA1017-CysGCA', '6.tRNA1019-CysGCA',
       '6.tRNA1023-CysGCA', '6.tRNA1024-CysGCA', '6.tRNA1025-CysGCA',
       '6.tRNA1026-CysGCA', '6.tRNA1029-CysGCA', '6.tRNA1030-CysGCA',
       '6.tRNA1031-CysGCA', '6.tRNA1032-CysGCA', '6.tRNA107-ArgCCT',
       '6.tRNA1100-AsnATT', '6.tRNA1115-Undet???', '6.tRNA157-CysGCA',
       '6.tRNA161-CysGCA', '6.tRNA163-CysGCA', '6.tRNA164-CysGCA',
       '6.tRNA166-CysGCA', '6.tRNA168-CysGCA', '6.tRNA172-CysGCA',
       '6.tRNA173-CysGCA', '6.tRNA178-CysGCA', '6.tRNA179-CysGCA',
       '6.tRNA181-CysGCA', '6.tRNA197-SerGCT', '6.tRNA315-ArgTCT',
       '6.tRNA317-GlyCCC', '6.tRNA46-ProAGG', '6.tRNA462-AsnGTT',
       '6.tRNA508-SerGCT', '6.tRNA685-SerGCT', '7.tRNA1036-SerACT',
       '7.tRNA1092-AsnGTT', '7.tRNA1156-AlaGGC', '7.tRNA1208-SerGCT',
       '7.tRNA1217-ThrAGT', '7.tRNA1275-SerGCT', '7.tRNA1280-LysTTT',
       '7.tRNA1299-AsnGTT', '7.tRNA1325-Undet???', '7.tRNA158-IleTAT',
       '7.tRNA211-Undet???', '7.tRNA339-GluTTC', '7.tRNA389-ArgTCG',
       '7.tRNA443-ProTGG', '7.tRNA464-AlaAGC', '7.tRNA561-LeuAAG',
       '7.tRNA644-AsnGTT', '7.tRNA70-SerACT', '7.tRNA799-GlyGCC',
       '7.tRNA833-SerGCT', '7.tRNA863-LeuTAG', '7.tRNA865-SerGCT',
       '7.tRNA88-SeC(e)TCA', '7.tRNA945-SerGCT', '7.tRNA979-ProAGG',
       '8.tRNA1013-LeuCAG', '8.tRNA1262-SerGCT', '8.tRNA1405-Undet???',
       '8.tRNA263-SerACT', '8.tRNA416-LeuCAG', '8.tRNA46-SerGCT',
       '8.tRNA490-SerGCT', '8.tRNA513-SerGCT', '8.tRNA529-Undet???',
       '8.tRNA562-GlyGCC', '8.tRNA648-Undet???', '8.tRNA788-MetCAT',
       '8.tRNA85-AsnGTT', '8.tRNA881-SerGCT', '8.tRNA891-GlyGCC',
       '8.tRNA892-GlyGCC', '9.tRNA1035-LysCTT', '9.tRNA1129-Undet???',
       '9.tRNA1251-SerGCT', '9.tRNA342-GlnCTG', '9.tRNA350-SerGCT',
       '9.tRNA551-SerGCT', '9.tRNA592-CysGCA', '9.tRNA593-CysGCA',
       '9.tRNA596-AlaCGC', '9.tRNA783-ArgACG', '9.tRNA961-GluTTC',
       'GL456239.1.tRNA2-LysCTT', 'GL456350.1.tRNA3-SerGCT',
       'JH584293.1.tRNA3-SerGCT', 'JH584294.1.tRNA1-SerGCT',
       'MT.tRNA1-PheGAA', 'MT.tRNA10-HisGTG', 'MT.tRNA11-LeuTAG',
       'MT.tRNA12-ThrTGT', 'MT.tRNA13-ProTGG', 'MT.tRNA14-GluTTC',
       'MT.tRNA15-SerTGA', 'MT.tRNA16-TyrGTA', 'MT.tRNA17-CysGCA',
       'MT.tRNA18-AsnGTT', 'MT.tRNA19-AlaTGC', 'MT.tRNA2-ValTAC',
       'MT.tRNA20-GlnTTG', 'MT.tRNA3-LeuTAA', 'MT.tRNA4-IleGAT',
       'MT.tRNA5-MetCAT', 'MT.tRNA6-AspGTC', 'MT.tRNA7-LysTTT',
       'MT.tRNA8-GlyTCC', 'MT.tRNA9-ArgTCG', 'X.tRNA121-GlyTCC',
       'X.tRNA304-ThrGGT', 'X.tRNA321-ArgCCT', 'X.tRNA371-AlaTGC',
       'X.tRNA372-AlaTGC', 'X.tRNA375-AlaTGC', 'X.tRNA460-ValTAC',
       'X.tRNA478-Undet???', 'X.tRNA602-SerGCT', 'X.tRNA637-AlaTGC',
       'X.tRNA939-AsnGTT']

plus_names = ['1.tRNA1001-LeuCAG', '1.tRNA1002-AspGTC', '1.tRNA1003-GlyTCC',
       '1.tRNA1004-GluCTC', '1.tRNA1005-AspGTC', '1.tRNA1006-GlyTCC',
       '1.tRNA1007-GluCTC', '1.tRNA1008-AspGTC', '1.tRNA1009-GlyTCC',
       '1.tRNA1010-GluCTC', '1.tRNA1012-GlyTCC', '1.tRNA1013-AspGTC',
       '1.tRNA1014-AsnGTT', '1.tRNA1030-ProCGG', '1.tRNA111-IleGAT',
       '1.tRNA1192-LysTTT', '1.tRNA1378-SerGCT', '1.tRNA1400-GlyGCC',
       '1.tRNA1412-AlaAGC', '1.tRNA1547-SerGCT', '1.tRNA1555-GluTTC',
       '1.tRNA1612-Undet???', '1.tRNA219-SerACT', '1.tRNA225-SerGCT',
       '1.tRNA485-LysTTT', '1.tRNA565-IleGAT', '1.tRNA672-ProAGG',
       '1.tRNA698-LeuCAG', '1.tRNA699-GlyGCC', '1.tRNA701-LeuCAG',
       '1.tRNA702-GlyGCC', '1.tRNA703-LeuCAG', '1.tRNA704-GlyGCC',
       '1.tRNA705-LeuCAG', '1.tRNA706-GlyGCC', '1.tRNA707-AspGTC',
       '1.tRNA708-GlyTCC', '1.tRNA709-GluCTC', '1.tRNA710-ValCAC',
       '1.tRNA712-IleGAT', '1.tRNA730-ArgTCT', '1.tRNA737-SeCTCA',
       '1.tRNA775-AsnGTT', '10.tRNA1105-SerTGA', '10.tRNA1292-TrpCCA',
       '10.tRNA1326-LeuTAA', '10.tRNA390-AsnGTT', '10.tRNA428-SerGCT',
       '10.tRNA649-SerGCT', '10.tRNA698-SerCGA', '10.tRNA861-AspGTC',
       '10.tRNA866-AspGTC', '10.tRNA867-TrpCCA', '10.tRNA90-GluCTC',
       '10.tRNA971-PheGAA', '10.tRNA976-ArgGCG', '10.tRNA987-SerGCT',
       '10.tRNA990-SerGCT', '11.tRNA1022-ArgCCT', '11.tRNA1023-ArgTCG',
       '11.tRNA1234-ArgCCT', '11.tRNA1432-CysGCA', '11.tRNA1433-CysGCA',
       '11.tRNA1442-CysGCA', '11.tRNA1444-CysGCA', '11.tRNA1446-AsnGTT',
       '11.tRNA1493-GlnTTG', '11.tRNA1743-SerGCT', '11.tRNA1785-SerGCT',
       '11.tRNA1816-LysTTT', '11.tRNA1817-GlnCTG', '11.tRNA1818-ArgTCT',
       '11.tRNA1819-GlyGCC', '11.tRNA1820-TrpCCA', '11.tRNA1821-SerGCT',
       '11.tRNA1822-ThrAGT', '11.tRNA1823-IleAAT', '11.tRNA1824-GlyTCC',
       '11.tRNA1849-TrpCCA', '11.tRNA1880-TrpCCA', '11.tRNA1911-LeuCAA',
       '11.tRNA1912-GluCTC', '11.tRNA2021-LeuAAG', '11.tRNA2022-AlaTGC',
       '11.tRNA2023-LysCTT', '11.tRNA204-ValCAC', '11.tRNA205-GlyACC',
       '11.tRNA206-ThrTGT', '11.tRNA207-ProTGG', '11.tRNA208-ValAAC',
       '11.tRNA245-SerGCT', '11.tRNA393-IleAAT', '11.tRNA394-SerAGA',
       '11.tRNA395-ThrAGT', '11.tRNA396-ProCGG', '11.tRNA397-AspGTC',
       '11.tRNA398-TrpCCA', '11.tRNA399-ThrAGT', '11.tRNA400-SerCGA',
       '11.tRNA401-LeuTAG', '11.tRNA516-SerGCT', '11.tRNA550-ThrCGT',
       '11.tRNA630-GlnTTG', '11.tRNA69-AspGTC', '11.tRNA750-SerGCT',
       '11.tRNA791-CysGCA', '11.tRNA832-SerGGA', '11.tRNA884-SerGCT',
       '11.tRNA945-ArgCCG', '12.tRNA1008-SerACT', '12.tRNA275-SerGCT',
       '12.tRNA42-SerGCT', '12.tRNA476-IleAAT', '12.tRNA60-AlaAGC',
       '12.tRNA796-LysCTT', '13.tRNA100-IleAAT', '13.tRNA1000-PheGAA',
       '13.tRNA1001-IleAAT', '13.tRNA1002-IleAAT', '13.tRNA1003-LeuTAA',
       '13.tRNA1004-SerGCT', '13.tRNA1006-MetCAT', '13.tRNA1007-GlnTTG',
       '13.tRNA1008-ThrAGT', '13.tRNA1009-ArgCCG', '13.tRNA101-TyrGTA',
       '13.tRNA1010-LeuCAA', '13.tRNA1011-MetCAT', '13.tRNA1012-LysTTT',
       '13.tRNA1013-GluCTC', '13.tRNA102-AlaAGC', '13.tRNA103-LysCTT',
       '13.tRNA104-ThrAGT', '13.tRNA105-GluTTC', '13.tRNA1053-LysCTT',
       '13.tRNA106-TyrGTA', '13.tRNA107-TrpCCA', '13.tRNA108-MetCAT',
       '13.tRNA109-TrpCCA', '13.tRNA110-GlyGCC', '13.tRNA111-MetCAT',
       '13.tRNA112-SerTGA', '13.tRNA113-GlnTTG', '13.tRNA114-GlnTTG',
       '13.tRNA115-SerGCT', '13.tRNA226-SerGCT', '13.tRNA60-PheGAA',
       '13.tRNA61-MetCAT', '13.tRNA62-LeuAAG', '13.tRNA63-LeuAAG',
       '13.tRNA64-GlnCTG', '13.tRNA65-LeuCAA', '13.tRNA66-AlaAGC',
       '13.tRNA67-AlaAGC', '13.tRNA68-AlaTGC', '13.tRNA69-AlaAGC',
       '13.tRNA70-AlaCGC', '13.tRNA71-AlaAGC', '13.tRNA72-ThrCGT',
       '13.tRNA73-ThrTGT', '13.tRNA74-ArgTCG', '13.tRNA75-ThrCGT',
       '13.tRNA77-GlyGCC', '13.tRNA78-MetCAT', '13.tRNA81-ThrAGT',
       '13.tRNA82-MetCAT', '13.tRNA83-LysTTT', '13.tRNA84-AspGTC',
       '13.tRNA85-LeuCAA', '13.tRNA86-SerAGA', '13.tRNA863-SerGCT',
       '13.tRNA87-GlnCTG', '13.tRNA88-SerAGA', '13.tRNA89-LysTTT',
       '13.tRNA90-MetCAT', '13.tRNA91-ValCAC', '13.tRNA92-IleAAT',
       '13.tRNA93-ValAAC', '13.tRNA94-AlaAGC', '13.tRNA95-ValAAC',
       '13.tRNA958-ThrAGT', '13.tRNA959-MetCAT', '13.tRNA96-AlaAGC',
       '13.tRNA960-ArgTCG', '13.tRNA961-ArgTCG', '13.tRNA962-SerAGA',
       '13.tRNA963-ArgACG', '13.tRNA964-LeuCAG', '13.tRNA965-ArgACG',
       '13.tRNA966-ValCAC', '13.tRNA967-AlaCGC', '13.tRNA968-IleAAT',
       '13.tRNA969-ProAGG', '13.tRNA97-ValCAC', '13.tRNA970-TyrGTA',
       '13.tRNA972-TyrGTA', '13.tRNA973-TyrGTA', '13.tRNA974-ValAAC',
       '13.tRNA975-AlaAGC', '13.tRNA977-ValAAC', '13.tRNA978-AlaAGC',
       '13.tRNA98-ValCAC', '13.tRNA980-IleAAT', '13.tRNA981-IleTAT',
       '13.tRNA982-SerGCT', '13.tRNA983-ThrAGT', '13.tRNA984-SerCGA',
       '13.tRNA985-ArgACG', '13.tRNA986-ValAAC', '13.tRNA987-GlnCTG',
       '13.tRNA988-SerGCT', '13.tRNA99-MetCAT', '13.tRNA990-SerAGA',
       '13.tRNA991-AspGTC', '13.tRNA992-SerAGA', '13.tRNA993-AspGTC',
       '13.tRNA994-GlnCTG', '13.tRNA995-MetCAT', '13.tRNA996-SerTGA',
       '13.tRNA997-ArgTCT', '13.tRNA999-IleTAT', '14.tRNA189-LeuAAG',
       '14.tRNA191-ThrTGT', '14.tRNA192-TyrGTA', '14.tRNA193-ProTGG',
       '14.tRNA202-SerGCT', '14.tRNA210-ArgACG', '14.tRNA286-SerGCT',
       '14.tRNA352-GluTTC', '14.tRNA364-GluTTC', '14.tRNA462-PheGAA',
       '14.tRNA709-LeuTAG', '14.tRNA710-ThrTGT', '14.tRNA711-ProAGG',
       '15.tRNA1018-SerGCT', '15.tRNA11-SerGCT', '15.tRNA342-SerGCT',
       '15.tRNA355-MetCAT', '15.tRNA410-SerGCT', '15.tRNA602-SerGCT',
       '15.tRNA755-Undet???', '15.tRNA876-MetCAT', '15.tRNA913-MetCAT',
       '16.tRNA273-AsnGTT', '16.tRNA305-SerGCT', '16.tRNA315-IleAAT',
       '16.tRNA50-ThrCGT', '16.tRNA561-Undet???', '16.tRNA630-SerGCT',
       '16.tRNA701-SerACT', '16.tRNA706-GlyGCC', '16.tRNA78-Undet???',
       '17.tRNA112-GlyCCC', '17.tRNA457-CysGCA', '17.tRNA515-IleTAT',
       '17.tRNA719-GluCTC', '17.tRNA81-LysCTT', '17.tRNA82-ProCGG',
       '17.tRNA83-LysCTT', '17.tRNA873-ThrAGT', '17.tRNA935-SerGCT',
       '17.tRNA969-SerGCT', '17.tRNA993-ArgCCG', '17.tRNA994-ArgCCT',
       '17.tRNA995-ProTGG', '17.tRNA999-LysCTT', '19.tRNA106-PheGAA',
       '19.tRNA107-LysTTT', '19.tRNA108-PheGAA', '19.tRNA109-ValTAC',
       '19.tRNA110-ValTAC', '19.tRNA326-SerACT', '19.tRNA62-AlaAGC',
       '19.tRNA630-SerGCT', '19.tRNA639-ArgTCT', '19.tRNA640-LeuTAA',
       '19.tRNA641-LysTTT', '19.tRNA713-SerGCT', '19.tRNA8-AlaAGC',
       '2.tRNA105-Undet???', '2.tRNA1238-SerGCT', '2.tRNA1292-AsnGTT',
       '2.tRNA1431-HisGTG', '2.tRNA1432-HisGTG', '2.tRNA1506-IleGAT',
       '2.tRNA1509-SerGCT', '2.tRNA1599-ThrGGT', '2.tRNA1747-GlyGCC',
       '2.tRNA1832-SerGCT', '2.tRNA1918-SerGCT', '2.tRNA1947-AsnGTT',
       '2.tRNA263-AlaCGC', '2.tRNA504-GlnCTG', '2.tRNA587-HisGTG',
       '2.tRNA840-IleGAT', '2.tRNA897-SerGCT', '2.tRNA925-Undet???',
       '3.tRNA1026-LeuCAG', '3.tRNA1040-ArgACG', '3.tRNA240-TyrGTA',
       '3.tRNA27-TyrGTA', '3.tRNA28-TyrGTA', '3.tRNA283-AsnGTT',
       '3.tRNA284-ValCAC', '3.tRNA286-GluTTC', '3.tRNA287-GlyCCC',
       '3.tRNA289-AsnGTT', '3.tRNA29-AlaAGC', '3.tRNA291-HisGTG',
       '3.tRNA292-LysCTT', '3.tRNA293-HisGTG', '3.tRNA294-AsnGTT',
       '3.tRNA295-HisGTG', '3.tRNA297-GlnCTG', '3.tRNA298-AsnGTT',
       '3.tRNA303-GluCTC', '3.tRNA309-GlnCTG', '3.tRNA424-SerGCT',
       '3.tRNA48-ValAAC', '3.tRNA628-ArgTCT', '3.tRNA745-GluCTC',
       '3.tRNA746-GlyTCC', '3.tRNA747-HisGTG', '3.tRNA748-LysCTT',
       '3.tRNA749-HisGTG', '3.tRNA750-AsnGTT', '3.tRNA751-HisGTG',
       '3.tRNA752-GlyCCC', '3.tRNA753-GlnCTG', '3.tRNA754-GluTTC',
       '3.tRNA755-GlyCCC', '3.tRNA756-GlnCTG', '3.tRNA757-AsnGTT',
       '3.tRNA792-MetCAT', '3.tRNA849-SerGCT', '3.tRNA878-GlyGCC',
       '3.tRNA92-ProTGG', '3.tRNA93-ProAGG', '3.tRNA964-SerGCT',
       '3.tRNA968-SerGCT', '3.tRNA99-AsnGTT', '4.tRNA1380-Undet???',
       '4.tRNA16-SerAGA', '4.tRNA1622-TyrGTA', '4.tRNA1691-HisGTG',
       '4.tRNA1820-SerGCT', '4.tRNA249-SerGCT', '4.tRNA322-SerGCT',
       '4.tRNA391-SerGCT', '4.tRNA596-SerGCT', '4.tRNA62-IleAAT',
       '4.tRNA641-AlaAGC', '4.tRNA67-GlyCCC', '4.tRNA837-SerGCT',
       '4.tRNA844-AsnGTT', '4.tRNA861-SerGCT', '5.tRNA1044-AsnGTT',
       '5.tRNA109-TyrGTA', '5.tRNA110-AlaAGC', '5.tRNA111-SerGCT',
       '5.tRNA1154-SerGCT', '5.tRNA1165-AlaTGC', '5.tRNA1315-AspGTC',
       '5.tRNA1316-PheGAA', '5.tRNA1317-AspGTC', '5.tRNA1318-AlaTGC',
       '5.tRNA221-SerGCT', '5.tRNA366-AsnGTT', '5.tRNA410-SerGCT',
       '5.tRNA474-SerGCT', '5.tRNA703-AlaTGC', '6.tRNA10-ValCAC',
       '6.tRNA1005-CysGCA', '6.tRNA1006-CysGCA', '6.tRNA1008-CysGCA',
       '6.tRNA1009-CysGCA', '6.tRNA1010-CysGCA', '6.tRNA1011-CysGCA',
       '6.tRNA1012-CysGCA', '6.tRNA1013-CysGCA', '6.tRNA1015-CysGCA',
       '6.tRNA1016-CysGCA', '6.tRNA1017-CysGCA', '6.tRNA1019-CysGCA',
       '6.tRNA1021-CysGCA', '6.tRNA1024-CysGCA', '6.tRNA1025-CysGCA',
       '6.tRNA1026-CysGCA', '6.tRNA1027-CysGCA', '6.tRNA1029-CysGCA',
       '6.tRNA1030-CysGCA', '6.tRNA1031-CysGCA', '6.tRNA1032-CysGCA',
       '6.tRNA107-ArgCCT', '6.tRNA1115-Undet???', '6.tRNA157-CysGCA',
       '6.tRNA161-CysGCA', '6.tRNA163-CysGCA', '6.tRNA164-CysGCA',
       '6.tRNA166-CysGCA', '6.tRNA168-CysGCA', '6.tRNA171-CysGCA',
       '6.tRNA172-CysGCA', '6.tRNA173-CysGCA', '6.tRNA175-CysGCA',
       '6.tRNA176-CysGCA', '6.tRNA178-CysGCA', '6.tRNA179-CysGCA',
       '6.tRNA180-CysGCA', '6.tRNA181-CysGCA', '6.tRNA197-SerGCT',
       '6.tRNA317-GlyCCC', '6.tRNA46-ProAGG', '6.tRNA916-SerGCT',
       '7.tRNA1036-SerACT', '7.tRNA1156-AlaGGC', '7.tRNA1208-SerGCT',
       '7.tRNA1217-ThrAGT', '7.tRNA1275-SerGCT', '7.tRNA1280-LysTTT',
       '7.tRNA158-IleTAT', '7.tRNA211-Undet???', '7.tRNA339-GluTTC',
       '7.tRNA389-ArgTCG', '7.tRNA407-IleGAT', '7.tRNA443-ProTGG',
       '7.tRNA464-AlaAGC', '7.tRNA554-SerGCT', '7.tRNA561-LeuAAG',
       '7.tRNA794-SerGCT', '7.tRNA833-SerGCT', '7.tRNA863-LeuTAG',
       '7.tRNA877-SerGCT', '7.tRNA88-SeC(e)TCA', '7.tRNA945-SerGCT',
       '7.tRNA979-ProAGG', '8.tRNA1013-LeuCAG', '8.tRNA171-LeuCAG',
       '8.tRNA416-LeuCAG', '8.tRNA513-SerGCT', '8.tRNA529-Undet???',
       '8.tRNA562-GlyGCC', '8.tRNA648-Undet???', '8.tRNA788-MetCAT',
       '8.tRNA891-GlyGCC', '8.tRNA892-GlyGCC', '9.tRNA1035-LysCTT',
       '9.tRNA1129-Undet???', '9.tRNA1251-SerGCT', '9.tRNA342-GlnCTG',
       '9.tRNA571-Undet???', '9.tRNA592-CysGCA', '9.tRNA593-CysGCA',
       '9.tRNA783-ArgACG', '9.tRNA961-GluTTC', 'MT.tRNA1-PheGAA',
       'MT.tRNA10-HisGTG', 'MT.tRNA11-LeuTAG', 'MT.tRNA12-ThrTGT',
       'MT.tRNA13-ProTGG', 'MT.tRNA14-GluTTC', 'MT.tRNA15-SerTGA',
       'MT.tRNA16-TyrGTA', 'MT.tRNA17-CysGCA', 'MT.tRNA18-AsnGTT',
       'MT.tRNA19-AlaTGC', 'MT.tRNA2-ValTAC', 'MT.tRNA20-GlnTTG',
       'MT.tRNA3-LeuTAA', 'MT.tRNA4-IleGAT', 'MT.tRNA5-MetCAT',
       'MT.tRNA6-AspGTC', 'MT.tRNA7-LysTTT', 'MT.tRNA8-GlyTCC',
       'MT.tRNA9-ArgTCG', 'X.tRNA121-GlyTCC', 'X.tRNA321-ArgCCT',
       'X.tRNA371-AlaTGC', 'X.tRNA372-AlaTGC', 'X.tRNA375-AlaTGC',
       'X.tRNA460-ValTAC', 'X.tRNA602-SerGCT', 'X.tRNA636-AlaCGC',
       'X.tRNA637-AlaTGC']

value_dict = {}

value_dict.values()

for name in minus_names:
    value_dict[name] = []

for name in plus_names:
    value_dict[name] = []

for row in minus.iterrows():
    value_dict[row[1]["Name"]].append(row[1]["logFC"])

value_dict.values()

for item in value_dict.values():
    if len(item) == 0:
        item.append(0)

for item in value_dict.values():
    print(len(item))

for row in plus.iterrows():
    value_dict[row[1]["Name"]].append(row[1]["logFC"])

for arr in value_dict.values():
    arr = np.array(arr)

final_values = pd.DataFrame(data=value_dict)

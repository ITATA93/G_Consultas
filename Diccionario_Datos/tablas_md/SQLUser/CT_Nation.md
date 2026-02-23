# SQLUser.CT_Nation

**Schema:** SQLUser
**Columnas:** 162
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTNAT_RowId | bigint | PK |  | NO | - |
| CTNAT_Code | varchar |  |  | NO | Nationality Code |
| CTNAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTNAT_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| CTNAT_CreatedDate | date |  |  | SI | Created Date |
| CTNAT_CreatedTime | time |  |  | SI | Created Time |
| CTNAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTNAT_DateFrom | date |  |  | SI | Date From |
| CTNAT_DateTo | date |  |  | SI | Date To |
| CTNAT_Desc | varchar |  |  | NO | Nationality Description |
| CTNAT_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| CTNAT_Iso3166Alpha2Code | varchar |  |  | SI | ISO-3166 Alpha-2 Code |
| CTNAT_Iso3166Alpha3Code | varchar |  |  | SI | ISO-3166 Alpha-3 Code |
| CTNAT_Iso3166Code | varchar |  |  | SI | ISO-3166 Code |
| CTNAT_NationalCode | varchar |  |  | SI | National Code |
| CTNAT_NationalityGroup_DR | bigint |  | FK | SI | Des Ref to CTNationalityGroup |
| CTNAT_Owner | varchar |  |  | SI | Owner |
| CTNAT_Resident | varchar |  |  | SI | Resident |
| CTNAT_UpdatedDate | date |  |  | SI | Updated Date |
| CTNAT_UpdatedTime | time |  |  | SI | Updated Time |
| CTNAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | a. Tabaco (cigarrillos, cigarros habanos, tabaco d... |
| Q02 | - |  |  | SI | b. Bebidas alcohólicas (cerveza, vino, licores, de... |
| Q03 | - |  |  | SI | c. Cannabis (marihuana, costo, hierba, hashish, et... |
| Q04 | - |  |  | SI | d. Cocaína (coca, farlopa, crack, base, etc.) |
| Q05 | - |  |  | SI | e. Anfetaminas u otro tipo de estimulantes (speed,... |
| Q06 | - |  |  | SI | f. Inhalantes (colas, gasolina/nafta, pegamento, e... |
| Q07 | - |  |  | SI | g. Tranquilizantes o pastillas para dormir (valium... |
| Q08 | - |  |  | SI | h. Alucinógenos (LSD, ácidos, ketamina, PCP, etc.) |
| Q09 | - |  |  | SI | i. Opiáceos (heroína, metadona, codeína, morfina, ... |
| Q10 | - |  |  | SI | j. Otros - Especifique: |
| Q100 | - |  |  | SI | Intervención |
| Q101 | - |  |  | SI | Motivo de Intervención |
| Q11 | - |  |  | SI | 1j. Descripción |
| Q12 | - |  |  | SI | 1.2 ¿Tampoco cuando iba al colegio? |
| Q13 | - |  |  | SI | Mensaje 1 |
| Q14 | - |  |  | SI | Mensaje 2 |
| Q15 | - |  |  | SI | a. Tabaco (cigarrillos, cigarros habanos, tabaco d... |
| Q16 | - |  |  | SI | b. Bebidas alcohólicas (cerveza, vino, licores, de... |
| Q17 | - |  |  | SI | c. Cannabis (marihuana, costo, hierba, hashish, et... |
| Q18 | - |  |  | SI | d. Cocaína (coca, farlopa, crack, base, etc.) |
| Q19 | - |  |  | SI | e. Anfetaminas u otro tipo de estimulantes (speed,... |
| Q20 | - |  |  | SI | f. Inhalantes (colas, gasolina/nafta, pegamento, e... |
| Q21 | - |  |  | SI | g. Tranquilizantes o pastillas para dormir (valium... |
| Q22 | - |  |  | SI | h. Alucinógenos (LSD, ácidos, ketamina, PCP, etc.) |
| Q23 | - |  |  | SI | i. Opiáceos (heroína, metadona, codeína, morfina, ... |
| Q24 | - |  |  | SI | j. Otros - Especifique: |
| Q25 | - |  |  | SI | 2j. Descripción |
| Q26 | - |  |  | SI | a. Tabaco (cigarrillos, cigarros habanos, tabaco d... |
| Q27 | - |  |  | SI | b. Bebidas alcohólicas (cerveza, vino, licores, de... |
| Q28 | - |  |  | SI | c. Cannabis (marihuana, costo, hierba, hashish, et... |
| Q29 | - |  |  | SI | d. Cocaína (coca, farlopa, crack, base, etc.) |
| Q30 | - |  |  | SI | e. Anfetaminas u otro tipo de estimulantes (speed,... |
| Q31 | - |  |  | SI | f. Inhalantes (colas, gasolina/nafta, pegamento, e... |
| Q32 | - |  |  | SI | g. Tranquilizantes o pastillas para dormir (valium... |
| Q33 | - |  |  | SI | h. Alucinógenos (LSD, ácidos, ketamina, PCP, etc.) |
| Q34 | - |  |  | SI | i. Opiáceos (heroína, metadona, codeína, morfina, ... |
| Q35 | - |  |  | SI | j. Otros - Especifique: |
| Q36 | - |  |  | SI | 3j. Especifique |
| Q37 | - |  |  | SI | a. Tabaco (cigarrillos, cigarros habanos, tabaco d... |
| Q38 | - |  |  | SI | b. Bebidas alcohólicas (cerveza, vino, licores, de... |
| Q39 | - |  |  | SI | c. Cannabis (marihuana, costo, hierba, hashish, et... |
| Q40 | - |  |  | SI | d. Cocaína (coca, farlopa, crack, base, etc.) |
| Q41 | - |  |  | SI | e. Anfetaminas u otro tipo de estimulantes (speed,... |
| Q42 | - |  |  | SI | f. Inhalantes (colas, gasolina/nafta, pegamento, e... |
| Q43 | - |  |  | SI | g. Tranquilizantes o pastillas para dormir (valium... |
| Q44 | - |  |  | SI | h. Alucinógenos (LSD, ácidos, ketamina, PCP, etc.) |
| Q45 | - |  |  | SI | i. Opiáceos (heroína, metadona, codeína, morfina, ... |
| Q46 | - |  |  | SI | j. Otros - Especifique: |
| Q47 | - |  |  | SI | 4j. Especifique |
| Q48 | - |  |  | SI | a. Tabaco (cigarrillos, cigarros habanos, tabaco d... |
| Q49 | - |  |  | SI | b. Bebidas alcohólicas (cerveza, vino, licores, de... |
| Q50 | - |  |  | SI | c. Cannabis (marihuana, costo, hierba, hashish, et... |
| Q51 | - |  |  | SI | d. Cocaína (coca, farlopa, crack, base, etc.) |
| Q52 | - |  |  | SI | e. Anfetaminas u otro tipo de estimulantes (speed,... |
| Q53 | - |  |  | SI | f. Inhalantes (colas, gasolina/nafta, pegamento, e... |
| Q54 | - |  |  | SI | g. Tranquilizantes o pastillas para dormir (valium... |
| Q55 | - |  |  | SI | h. Alucinógenos (LSD, ácidos, ketamina, PCP, etc.) |
| Q56 | - |  |  | SI | i. Opiáceos (heroína, metadona, codeína, morfina, ... |
| Q57 | - |  |  | SI | j. Otros - Especifique: |
| Q58 | - |  |  | SI | 5j. Especifique |
| Q59 | - |  |  | SI | a. Tabaco (cigarrillos, cigarros habanos, tabaco d... |
| Q60 | - |  |  | SI | b. Bebidas alcohólicas (cerveza, vino, licores, de... |
| Q61 | - |  |  | SI | c. Cannabis (marihuana, costo, hierba, hashish, et... |
| Q62 | - |  |  | SI | d. Cocaína (coca, farlopa, crack, base, etc.) |
| Q63 | - |  |  | SI | e. Anfetaminas u otro tipo de estimulantes (speed,... |
| Q64 | - |  |  | SI | f. Inhalantes (colas, gasolina/nafta, pegamento, e... |
| Q65 | - |  |  | SI | g. Tranquilizantes o pastillas para dormir (valium... |
| Q66 | - |  |  | SI | h. Alucinógenos (LSD, ácidos, ketamina, PCP, etc.) |
| Q67 | - |  |  | SI | i. Opiáceos (heroína, metadona, codeína, morfina, ... |
| Q68 | - |  |  | SI | j. Otros - Especifique: |
| Q69 | - |  |  | SI | 6j. Especifique |
| Q70 | - |  |  | SI | a. Tabaco (cigarrillos, cigarros habanos, tabaco d... |
| Q71 | - |  |  | SI | b. Bebidas alcohólicas (cerveza, vino, licores, de... |
| Q72 | - |  |  | SI | c. Cannabis (marihuana, costo, hierba, hashish, et... |
| Q73 | - |  |  | SI | d. Cocaína (coca, farlopa, crack, base, etc.) |
| Q74 | - |  |  | SI | e. Anfetaminas u otro tipo de estimulantes (speed,... |
| Q75 | - |  |  | SI | f. Inhalantes (colas, gasolina/nafta, pegamento, e... |
| Q76 | - |  |  | SI | g. Tranquilizantes o pastillas para dormir (valium... |
| Q77 | - |  |  | SI | h. Alucinógenos (LSD, ácidos, ketamina, PCP, etc.) |
| Q78 | - |  |  | SI | i. Opiáceos (heroína, metadona, codeína, morfina, ... |
| Q79 | - |  |  | SI | j. Otros - Especifique: |
| Q80 | - |  |  | SI | 7j. Especifique |
| Q81 | - |  |  | SI | ¿Ha consumido alguna vez alguna droga por vía inye... |
| Q82 | - |  |  | SI | Mensaje 1 |
| Q83 | - |  |  | SI | Mensaje 2 |
| Q84 | - |  |  | SI | Entrevistador |
| Q85 | - |  |  | SI | Contexto o Lugar |
| Q86 | - |  |  | SI | Nombre Participante |
| Q87 | - |  |  | SI | Apellido Paterno Participante |
| Q88 | - |  |  | SI | Apellido Materno Participante |
| Q89 | - |  |  | SI | Puntuación Tabaco |
| Q90 | - |  |  | SI | Puntuación Alcohol |
| Q91 | - |  |  | SI | Puntuación Marihuana |
| Q92 | - |  |  | SI | Puntuación Cocaína |
| Q93 | - |  |  | SI | Puntuación Anfetaminas |
| Q94 | - |  |  | SI | Puntuación Inhalantes |
| Q95 | - |  |  | SI | Puntuación Sedantes |
| Q96 | - |  |  | SI | Puntuación Alucinógenos |
| Q97 | - |  |  | SI | Puntuación Opiáceos |
| Q98 | - |  |  | SI | Puntuación Otras Drogas |
| Q99 | - |  |  | SI | 2a. Tabaco |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
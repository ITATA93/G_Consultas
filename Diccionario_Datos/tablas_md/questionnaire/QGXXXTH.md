# questionnaire.QGXXXTH

> Travel History

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Travel History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Have you travelled outside the country in the last... |
| Q02 | varchar |  |  | SI | Country |
| Q03 | varchar |  |  | SI | Location/s |
| Q04 | date |  |  | SI | Date arrived |
| Q05 | date |  |  | SI | Date departed |
| Q06 | varchar |  |  | SI | Reason for travel |
| Q07 | date |  |  | SI | Approximate onset date of illness |
| Q08 | varchar |  |  | SI | Onset in relation to travel |
| Q09 | varchar |  |  | SI | Symptoms of illness |
| Q10 | varchar |  |  | SI | Severity of Illness |
| Q11 | varchar |  |  | SI | Travel Immunisations prior to travel |
| Q12 | varchar |  |  | SI | Other Vaccine Details |
| Q13 | varchar |  |  | SI | Anti malarial prophylaxis |
| Q14 | date |  |  | SI | Date antimalarial started |
| Q15 | varchar |  |  | SI | Adherence to antimalarial propphylaxis |
| Q16 | varchar |  |  | SI | Contact with blood / bodily fluids from anyone suf... |
| Q17 | varchar |  |  | SI | Have been in close association with anyone sufferi... |
| Q18 | varchar |  |  | SI | Involved in funeral preparations |
| Q19 | varchar |  |  | SI | Notes |
| Q20 | varchar |  |  | SI | Had any sexual activity with a new partner who liv... |
| Q21 | varchar |  |  | SI | Had a tattoo or body piercings? |
| Q22 | varchar |  |  | SI | Been hospitalised or received any medical treatmen... |
| Q23 | varchar |  |  | SI | While travelling have you...? |
| Q24 | varchar |  |  | SI | Taken any IV drugs |
| Q25 | varchar |  |  | SI | Eaten raw meat or seafood or unpasteurized dairy p... |
| Q26 | varchar |  |  | SI | Handled, slaughtered or eaten any exotic animals i... |
| Q27 | varchar |  |  | SI | Handled clinical / laboratory specimens |
| Q28 | varchar |  |  | SI | Type of Accommodation while travelling |
| Q29 | varchar |  |  | SI | Any insect / mosquito or animal bites? |
| Q30 | varchar |  |  | SI | Any cuts or lacerations? |
| Q31 | varchar |  |  | SI | Exposure to freshwater (swimming, rafting...) |
| Q32 | varchar |  |  | SI | What water did you drink? |
| Q33 | varchar |  |  | SI | What is your occupation |
| Q34 | varchar |  |  | SI | Type of rash |
| Q35 | varchar |  |  | SI | Type of bleeding |
| Q36 | varchar |  |  | SI | Notes |
| Q37 | varchar |  |  | SI | Notes |
| Q38 | varchar |  |  | SI | Notes |
| Q39 | varchar |  |  | SI | While travelling have you...? |
| Q40 | varchar |  |  | SI | Have you travelled to more than one country? |
| Q41 | varchar |  |  | SI | Country  |
| Q42 | varchar |  |  | SI | Country  |
| Q43 | varchar |  |  | SI | Country |
| Q44 | date |  |  | SI | Date |
| Q45 | time |  |  | SI | Time |
| Q46 | varchar |  |  | SI | Have you travelled outside the country in the last... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
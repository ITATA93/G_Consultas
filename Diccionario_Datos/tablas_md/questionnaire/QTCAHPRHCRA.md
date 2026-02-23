# questionnaire.QTCAHPRHCRA

> Cardiac Rehabilitation Assessment

**Schema:** questionnaire
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Rehabilitation Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Summary of cardiac condition |
| Q02 | varchar |  |  | SI | Cardiac signs and symptoms |
| Q03 | varchar |  |  | SI | (frequency; severity; management;  |
| Q04 | varchar |  |  | SI | Exercise History |
| Q05 | varchar |  |  | SI | Pre cardiac event |
| Q06 | varchar |  |  | SI | From diagnosis to treatment |
| Q07 | varchar |  |  | SI | Current |
| Q08 | varchar |  |  | SI | Leisure |
| Q09 | varchar |  |  | SI | Social |
| Q10 | varchar |  |  | SI | Living arrangement |
| Q11 | varchar |  |  | SI | Detail |
| Q12 | varchar |  |  | SI | Driving |
| Q13 | varchar |  |  | SI | Reason |
| Q14 | varchar |  |  | SI | Occupation |
| Q15 | varchar |  |  | SI | Self Reporting |
| Q16 | varchar |  |  | SI | Has patient returned to work? |
| Q17 | varchar |  |  | SI | Does patient intended to return to work? |
| Q18 | varchar |  |  | SI | Reason |
| Q19 | varchar |  |  | SI | Resumed previous sexual activities |
| Q20 | varchar |  |  | SI | Reason |
| Q21 | varchar |  |  | SI | Finance |
| Q22 | varchar |  |  | SI | Any Financial issues due to illness |
| Q23 | varchar |  |  | SI | Note |
| Q24 | varchar |  |  | SI | Cultural Background |
| Q25 | varchar |  |  | SI | Any sensitivities |
| Q26 | varchar |  |  | SI | Cardiac Blues Red Flags |
| Q27 | bit |  |  | SI | Lives alone / social isolation |
| Q28 | bit |  |  | SI | Past history anxiety / depression |
| Q29 | bit |  |  | SI | Poor self rated health |
| Q30 | bit |  |  | SI | Financial / psychosocial stressers |
| Q31 | bit |  |  | SI | Diabetes; other comorbidities |
| Q32 | bit |  |  | SI | Lives alone / social isolation |
| Q33 | bit |  |  | SI | <55 years of age |
| Q34 | bit |  |  | SI | Compounded loss |
| Q35 | varchar |  |  | SI | If multiple Red Flags provide patient with Cardiac... |
| Q36 | varchar |  |  | SI | Advise patient to discuss with GP |
| Q37 | varchar |  |  | SI | Advance Care Planning |
| Q38 | varchar |  |  | SI | Who should the service contact regarding the patie... |
| Q39 | varchar |  |  | SI | Do you have an Enduring Medical Power of Attorney? |
| Q40 | varchar |  |  | SI | Provide documentation |
| Q41 | varchar |  |  | SI | Do you have an Advanced Care Plan? |
| Q42 | varchar |  |  | SI | Provide documentation |
| Q43 | varchar |  |  | SI | Offer advanced Care Plan referral |
| Q44 | varchar |  |  | SI | Mobility and Falls |
| Q45 | varchar |  |  | SI | Is patient over 65 years of age |
| Q46 | varchar |  |  | SI | Has Patient had a fall int he last 6 months(error) |
| Q47 | varchar |  |  | SI | If answered yes to either question complete the El... |
| Q48 | varchar |  |  | SI | Referral to outpatient rehabilitation service musc... |
| Q49 | varchar |  |  | SI | Mobility Aid |
| Q50 | varchar |  |  | SI | Infection Control |
| Q51 | varchar |  |  | SI | Microorganism |
| Q52 | varchar |  |  | SI | Location |
| Q53 | varchar |  |  | SI | Notify Infection Control |
| Q54 | varchar |  |  | SI | Smoking |
| Q55 | varchar |  |  | SI | Do you currently smoke or have you ever smoked? |
| Q56 | varchar |  |  | SI | How soon after waking do you smoke your first ciga... |
| Q57 | varchar |  |  | SI | How many cigarettes a day do you smoke? |
| Q58 | varchar |  |  | SI | Score |
| Q59 | varchar |  |  | SI | 0-2 = very low dependence |
| Q60 | varchar |  |  | SI | 3 = low dependence |
| Q61 | varchar |  |  | SI | 4 = moderate dependence |
| Q62 | varchar |  |  | SI | 5 = high dependence |
| Q63 | varchar |  |  | SI | 6 = very high dependence |
| Q64 | varchar |  |  | SI | Have you ever tried quitting? |
| Q65 | varchar |  |  | SI | How do you feel about quitting? |
| Q66 | varchar |  |  | SI | Referral to Quit Line |
| Q67 | varchar |  |  | SI | Action Plans |
| Q68 | varchar |  |  | SI | Chest pain action plan |
| Q69 | varchar |  |  | SI | Heart failure action plan |
| Q70 | varchar |  |  | SI | Other |
| Q71 | varchar |  |  | SI | medical review required / conducted) |
| Q72 | varchar |  |  | SI | Has Patient had a fall in the last 6 months |
| Q73 | date |  |  | SI | Date |
| Q74 | time |  |  | SI | Time |
| Q75 | varchar |  |  | SI | Record details of smoking history |
| Q76 | varchar |  |  | SI | Please ensure the patient's record is updated to r... |
| Q77 | varchar |  |  | SI | Usual occupation |
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
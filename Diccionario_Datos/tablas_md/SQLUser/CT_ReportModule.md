# SQLUser.CT_ReportModule

**Schema:** SQLUser
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REPSEL_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Feeding |
| Q03 | - |  |  | SI | Bathing |
| Q04 | - |  |  | SI | Grooming |
| Q05 | - |  |  | SI | Dressing |
| Q06 | - |  |  | SI | Bowels |
| Q07 | - |  |  | SI | Bladder |
| Q08 | - |  |  | SI | Toilet use |
| Q09 | - |  |  | SI | Transfers (bed to chair and back) |
| Q10 | - |  |  | SI | Mobility (on level surfaces) |
| Q11 | - |  |  | SI | Stairs |
| Q12 | - |  |  | SI | 0 - 20: Total dependency |
| Q13 | - |  |  | SI | 21 - 60: Severe dependency |
| Q14 | - |  |  | SI | 61 - 90: Moderate dependency |
| Q15 | - |  |  | SI | 91 - 99: Slight dependency |
| Q16 | - |  |  | SI | The Barthel scale is a scale used to measure perfo... |
| Q17 | - |  |  | SI | General |
| Q18 | - |  |  | SI | • The Index should be used as a record of what a p... |
| Q19 | - |  |  | SI | • The main aim is to establish degree of independe... |
| Q20 | - |  |  | SI | • The need for supervision renders the patient not... |
| Q21 | - |  |  | SI | • A patient's performance should be established us... |
| Q22 | - |  |  | SI | friends / relatives, and nurses will be the usual ... |
| Q23 | - |  |  | SI | • Usually the performance over the preceding 24 – ... |
| Q24 | - |  |  | SI | • Unconscious patients should score '0' throughout... |
| Q25 | - |  |  | SI | • Middle categories imply that the patient supplie... |
| Q26 | - |  |  | SI | • Use of aids to be independent is allowed. |
| Q27 | - |  |  | SI | Bowels (preceding week) |
| Q28 | - |  |  | SI | • If needs enema from nurse, then 'incontinent'. |
| Q29 | - |  |  | SI | • 'Occasional' = once a week. |
| Q30 | - |  |  | SI | Bladder (preceding week) |
| Q31 | - |  |  | SI | • 'Occasional' = less than once a day. |
| Q32 | - |  |  | SI | • A catheterized patient who can completely manage... |
| Q33 | - |  |  | SI | Grooming (preceding 24 – 48 hours) |
| Q34 | - |  |  | SI | • Refers to personal hygiene: doing teeth, fitting... |
| Q35 | - |  |  | SI | Toilet use |
| Q36 | - |  |  | SI | • Should be able to reach toilet / commode, undres... |
| Q37 | - |  |  | SI | • 'With help' = can wipe self and do some other of... |
| Q38 | - |  |  | SI | Feeding |
| Q39 | - |  |  | SI | • Able to eat any normal food (not only soft food)... |
| Q40 | - |  |  | SI | • 'Help' = food cut up, patient feeds self. |
| Q41 | - |  |  | SI | Transfer |
| Q42 | - |  |  | SI | • From bed to chair and back. |
| Q43 | - |  |  | SI | • 'Dependent' = NO sitting balance (unable to sit) |
| Q44 | - |  |  | SI | • 'Major help' = one strong / skilled, or two norm... |
| Q45 | - |  |  | SI | • 'Minor help' = one person easily, OR needs any s... |
| Q46 | - |  |  | SI | Mobility |
| Q47 | - |  |  | SI | • Refers to mobility about house or ward, indoors.... |
| Q48 | - |  |  | SI | • 'Help' = by one untrained person, including supe... |
| Q49 | - |  |  | SI | • 'Help' = by one untrained person, including supe... |
| Q50 | - |  |  | SI | Dressing |
| Q51 | - |  |  | SI | • Should be able to select and put on all clothes,... |
| Q52 | - |  |  | SI | • Should be able to select and put on all clothes,... |
| Q53 | - |  |  | SI | • 'Half' = help with buttons, zips, etc., but can ... |
| Q54 | - |  |  | SI | Stairs |
| Q55 | - |  |  | SI | • Must carry any walking aid used to be independen... |
| Q56 | - |  |  | SI | Bathing |
| Q57 | - |  |  | SI | • Usually the most difficult activity. |
| Q58 | - |  |  | SI | • Must get in and out unsupervised, and wash self. |
| Q59 | - |  |  | SI | • Independent in shower = 'independent' if unsuper... |
| Q60 | - |  |  | SI | Time |
| Q61 | - |  |  | SI | 0 - 20 |
| Q62 | - |  |  | SI | Total dependency |
| Q63 | - |  |  | SI | 21 - 60 |
| Q64 | - |  |  | SI | Severe dependency |
| Q65 | - |  |  | SI | 61 - 90 |
| Q66 | - |  |  | SI | Moderate dependency |
| Q67 | - |  |  | SI | 91 - 99 |
| Q68 | - |  |  | SI | Slight dependency |
| Q69 | - |  |  | SI | Score |
| Q70 | - |  |  | SI | Classification |
| Q71 | - |  |  | SI | 100: Complete independency |
| Q72 | - |  |  | SI | 100 |
| Q73 | - |  |  | SI | Complete independency |
| Q74 | - |  |  | SI | Comment |
| Q75 | - |  |  | SI | Mahoney FI, Barthel DW. Barthel index. Maryland st... |
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
| REPSEL_Code | varchar |  |  | NO | Code |
| REPSEL_CreatedDate | date |  |  | SI | Created Date |
| REPSEL_CreatedTime | time |  |  | SI | Created Time |
| REPSEL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REPSEL_Desc | varchar |  |  | NO | Description |
| REPSEL_UpdatedDate | date |  |  | SI | Updated Date |
| REPSEL_UpdatedTime | time |  |  | SI | Updated Time |
| REPSEL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
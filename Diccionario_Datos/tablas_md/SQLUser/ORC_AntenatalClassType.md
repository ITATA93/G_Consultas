# SQLUser.ORC_AntenatalClassType

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANCLTY_RowId | bigint | PK |  | NO | - |
| ANCLTY_Code | varchar |  |  | NO | Code |
| ANCLTY_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANCLTY_CreatedDate | date |  |  | SI | Created Date |
| ANCLTY_CreatedTime | time |  |  | SI | Created Time |
| ANCLTY_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANCLTY_DateFrom | date |  |  | SI | Date From |
| ANCLTY_DateTo | date |  |  | SI | Date To |
| ANCLTY_Desc | varchar |  |  | NO | Description |
| ANCLTY_Owner | varchar |  |  | SI | Owner |
| ANCLTY_UpdatedDate | date |  |  | SI | Updated Date |
| ANCLTY_UpdatedTime | time |  |  | SI | Updated Time |
| ANCLTY_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Speech |
| Q02 | - |  |  | SI | Salivation |
| Q03 | - |  |  | SI | Swallowing |
| Q04 | - |  |  | SI | Handwriting |
| Q05 | - |  |  | SI | Patients with gastrostomy and >50% daily nutrition... |
| Q06 | - |  |  | SI | Cutting food and handling utensils Patients withou... |
| Q07 | - |  |  | SI | Cutting food and handling utensils Patients with g... |
| Q08 | - |  |  | SI | Dressing and hygiene |
| Q09 | - |  |  | SI | Turning in bed and adjusting bed clothes |
| Q10 | - |  |  | SI | Walking |
| Q11 | - |  |  | SI | Climbing stairs |
| Q12 | - |  |  | SI | Dyspnea |
| Q13 | - |  |  | SI | Orthopnea |
| Q14 | - |  |  | SI | Respiratory insufficiency |
| Q15 | - |  |  | SI | Score |
| Q16 | - |  |  | SI | Classification |
| Q17 | - |  |  | SI | ≤15 |
| Q18 | - |  |  | SI | ≤25% 9-month survival |
| Q19 | - |  |  | SI | 16-20 |
| Q20 | - |  |  | SI | ~25-40% 9-month survival |
| Q21 | - |  |  | SI | 21-25 |
| Q22 | - |  |  | SI | ~40-60% 9-month survival |
| Q23 | - |  |  | SI | 26-30 |
| Q24 | - |  |  | SI | ~60-70% 9-month survival |
| Q25 | - |  |  | SI | 31-35 |
| Q26 | - |  |  | SI | ~70-80% 9-month survival |
| Q27 | - |  |  | SI | 36-40 |
| Q28 | - |  |  | SI | ~80-90% 9-month survival |
| Q29 | - |  |  | SI | ≥41 |
| Q30 | - |  |  | SI | >90% 9-month survival |
| Q31 | - |  |  | SI | <=15: <=25% 9-month survival |
| Q32 | - |  |  | SI | 16-20: ~25-40% 9-month survival |
| Q33 | - |  |  | SI | 21-25: ~25-40% 9-month survival |
| Q34 | - |  |  | SI | 26-30: ~60-70% 9-month survival |
| Q35 | - |  |  | SI | 31-35: ~70-80% 9-month survival |
| Q36 | - |  |  | SI | 36-40: ~80-90% 9-month survival |
| Q37 | - |  |  | SI | <=41: >90% 9-month survival |
| Q38 | - |  |  | SI | The Revised Amyotrophic Lateral Sclerosis Function... |
| Q39 | - |  |  | SI | for Patients with ALS (Amyotrophic Lateral Scleros... |
| Q40 | - |  |  | SI | Figures are approximate and estimated as per refer... |
| Q41 | - |  |  | SI | Cedarbaum JM, Stambler N. Performance of the Amyot... |
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
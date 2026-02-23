# SQLUser.OEC_PriorityAllocation

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRIALL_RowId | bigint | PK |  | NO | - |
| PRIALL_Category_DR | bigint |  | FK | SI | Color |
| PRIALL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRIALL_CreatedDate | date |  |  | SI | Created Date |
| PRIALL_CreatedTime | time |  |  | SI | Created Time |
| PRIALL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRIALL_DateFrom | date |  |  | SI | Date From |
| PRIALL_DateTo | date |  |  | SI | Date To |
| PRIALL_Owner | varchar |  |  | SI | Owner |
| PRIALL_Priority_DR | bigint |  | FK | NO | Priority |
| PRIALL_UpdatedDate | date |  |  | SI | Updated Date |
| PRIALL_UpdatedTime | time |  |  | SI | Updated Time |
| PRIALL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q01a | - |  |  | SI | Time |
| Q02 | - |  |  | SI | Pain |
| Q02a | - |  |  | SI | Pain |
| Q03 | - |  |  | SI | Since |
| Q04 | - |  |  | SI | Since |
| Q05 | - |  |  | SI | Localisation |
| Q06 | - |  |  | SI | Bodymap |
| Q07 | - |  |  | SI | Type |
| Q08 | - |  |  | SI | Duration |
| Q09 | - |  |  | SI | Continuous |
| Q10 | - |  |  | SI | Time |
| Q11 | - |  |  | SI | Description of the patient |
| Q12 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | 0: No pain |
| Q21 | - |  |  | SI | 1-2: Mild Pain |
| Q22 | - |  |  | SI | 3-4: Moderate Pain |
| Q23 | - |  |  | SI | 5-6: Severe Pain |
| Q24 | - |  |  | SI | 7-8: Very Severe Pain |
| Q25 | - |  |  | SI | 9-10: Worst Possible Pain |
| Q26 | - |  |  | SI | This is a detailed Pain Assessment and verbal scal... |
| Q27 | - |  |  | SI | Analgesia |
| Q28 | - |  |  | SI | 0 |
| Q29 | - |  |  | SI | No pain |
| Q30 | - |  |  | SI | 1 - 2 |
| Q31 | - |  |  | SI | Mild Pain |
| Q32 | - |  |  | SI | 3 - 4 |
| Q33 | - |  |  | SI | Moderate Pain |
| Q34 | - |  |  | SI | 5 - 6 |
| Q35 | - |  |  | SI | Severe Pain |
| Q36 | - |  |  | SI | 7 - 8 |
| Q37 | - |  |  | SI | Very Severe Pain |
| Q38 | - |  |  | SI | 9 - 10 |
| Q39 | - |  |  | SI | Worst Possible Pain |
| Q40 | - |  |  | SI | Classification |
| Q41 | - |  |  | SI | Score |
| Q42 | - |  |  | SI | Localization (multiple choice) |
| Q43 | - |  |  | SI | Score |
| Q43ObsDR | - |  |  | SI | Score DR |
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
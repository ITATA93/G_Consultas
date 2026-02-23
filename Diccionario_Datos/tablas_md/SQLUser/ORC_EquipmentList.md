# SQLUser.ORC_EquipmentList

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LS_ParRef | bigint | PK |  | NO | ORC_Equipment Parent Reference |
| LS_Childsub | double |  |  | NO | Childsub |
| LS_Code | varchar |  |  | SI | Code |
| LS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LS_CreatedDate | date |  |  | SI | Created Date |
| LS_CreatedTime | time |  |  | SI | Created Time |
| LS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LS_DateFrom | date |  |  | SI | DateFrom |
| LS_DateTo | date |  |  | SI | DateTo |
| LS_Desc | varchar |  |  | SI | Description |
| LS_RowId | varchar |  |  | NO | - |
| LS_SerialNo | varchar |  |  | SI | Serial No |
| LS_UpdatedDate | date |  |  | SI | Updated Date |
| LS_UpdatedTime | time |  |  | SI | Updated Time |
| LS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Instructions - Walk at your normal speed from here... |
| Q04 | - |  |  | SI | 1. Gait level surface |
| Q05 | - |  |  | SI | Instructions - Begin walking at your normal pace (... |
| Q06 | - |  |  | SI | 2. Change in gait speed |
| Q07 | - |  |  | SI | Instructions - Begin walking at your normal pace. ... |
| Q08 | - |  |  | SI | Keep looking to the right until I tell you, ''look... |
| Q09 | - |  |  | SI | Keep your head to the left until I tell you ''look... |
| Q10 | - |  |  | SI | 3. Gait with horizontal head turns |
| Q11 | - |  |  | SI | Instructions - Begin walking at your normal pace. ... |
| Q12 | - |  |  | SI | Keep looking up until I tell you, ''look down'', t... |
| Q13 | - |  |  | SI | 4. Gait with vertical head turns |
| Q14 | - |  |  | SI | Instructions - Begin walking at your normal pace. ... |
| Q15 | - |  |  | SI | 5. Gait and pivot turn |
| Q16 | - |  |  | SI | Instructions - Begin walking at your normal speed.... |
| Q17 | - |  |  | SI | 6. Step over obstacle |
| Q18 | - |  |  | SI | Instructions - Begin walking at normal speed. When... |
| Q19 | - |  |  | SI | When you come to the second cone (6 ft / 1.8 m pas... |
| Q20 | - |  |  | SI | 7. Step around obstacles |
| Q21 | - |  |  | SI | Instructions - Walk up these stairs as you would a... |
| Q22 | - |  |  | SI | 8. Steps |
| Q23 | - |  |  | SI | Notes |
| Q24 | - |  |  | SI | Herdman SJ. Vestibular Rehabilitation. 2nd ed. Phi... |
| Q25 | - |  |  | SI | Shumway-Cook A, Woollacott M. Motor Control Theory... |
| Q26 | - |  |  | SI | Whitney SL, Marchetti GF, Schade A, Wrisley DM. Th... |
| Q27 | - |  |  | SI | Equipment needed - Box (Shoebox), Cones (2), Stair... |
| Q28 | - |  |  | SI | Completion time: 15 min |
| Q29 | - |  |  | SI | Scoring - A four-point ordinal scale, ranging from... |
| Q30 | - |  |  | SI | Grading - Mark the lowest category that applies. |
| Q31 | - |  |  | SI | The Dynamic Gait Index was developed to assess the... |
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
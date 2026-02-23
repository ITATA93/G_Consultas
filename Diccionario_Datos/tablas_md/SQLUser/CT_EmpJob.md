# SQLUser.CT_EmpJob

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTEMJ_RowId | bigint | PK |  | NO | - |
| CTEMJ_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTEMJ_Code | varchar |  |  | NO | Employee Job Code |
| CTEMJ_CreatedDate | date |  |  | SI | Created Date |
| CTEMJ_CreatedTime | time |  |  | SI | Created Time |
| CTEMJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTEMJ_DateFrom | date |  |  | SI | DateFrom |
| CTEMJ_DateTo | date |  |  | SI | DateTo |
| CTEMJ_Desc | varchar |  |  | NO | Employee Job Description |
| CTEMJ_UpdatedDate | date |  |  | SI | Updated Date |
| CTEMJ_UpdatedTime | time |  |  | SI | Updated Time |
| CTEMJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Prothrombin time |
| Q04 | - |  |  | SI | sec |
| Q05 | - |  |  | SI | Control time |
| Q06 | - |  |  | SI | sec |
| Q07 | - |  |  | SI | Bilirubin |
| Q08 | - |  |  | SI | mg/dL |
| Q09 | - |  |  | SI | Score |
| Q10 | - |  |  | SI | Maddrey score item |
| Q11 | - |  |  | SI | Normal range |
| Q12 | - |  |  | SI | Description |
| Q13 | - |  |  | SI | Prothrombin time |
| Q14 | - |  |  | SI | 11 – 13.5 seconds  (in patients who are not in the... |
| Q15 | - |  |  | SI | Indicates the clotting performance and indirectly ... |
| Q16 | - |  |  | SI | Control time |
| Q17 | - |  |  | SI | 10 – 14 seconds |
| Q18 | - |  |  | SI | Indicates the clotting performance and indirectly ... |
| Q19 | - |  |  | SI | Bilirubin |
| Q20 | - |  |  | SI | 0.3 to 1.9 mg/dL |
| Q21 | - |  |  | SI | Reflects the metabolic function of the liver. Elev... |
| Q22 | - |  |  | SI | All Maddrey score results above 32 are indicative ... |
| Q23 | - |  |  | SI | The Maddrey Score is a discriminant method that pr... |
| Q24 | - |  |  | SI | Score |
| Q25 | - |  |  | SI | Classification |
| Q26 | - |  |  | SI | please use score defined at 09 |
| Q27 | - |  |  | SI | No score caption |
| Q28 | - |  |  | SI | Maddrey score item |
| Q29 | - |  |  | SI | Maddrey score item |
| Q30 | - |  |  | SI | Maddrey score item |
| Q31 | - |  |  | SI | Normal range |
| Q32 | - |  |  | SI | Normal range |
| Q33 | - |  |  | SI | Normal range |
| Q34 | - |  |  | SI | Description |
| Q35 | - |  |  | SI | Description |
| Q36 | - |  |  | SI | Description |
| Q37 | - |  |  | SI | All results above 32 are indicative of a poor prog... |
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
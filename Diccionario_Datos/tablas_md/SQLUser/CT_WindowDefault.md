# SQLUser.CT_WindowDefault

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WIND_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Temperature °C (°F) |
| Q04 | - |  |  | SI | Central nervous system effects |
| Q05 | - |  |  | SI | Gastrointestinal-hepatic dysfunction |
| Q06 | - |  |  | SI | Heart rate (beats/minute) |
| Q07 | - |  |  | SI | Congestive heart failure |
| Q08 | - |  |  | SI | Atrial fibrillation present |
| Q09 | - |  |  | SI | Precipitating event |
| Q10 | - |  |  | SI | Score |
| Q11 | - |  |  | SI | Classification |
| Q12 | - |  |  | SI | > 45 |
| Q13 | - |  |  | SI | Highly suggestive of thyroid storm |
| Q14 | - |  |  | SI | 25 – 45 |
| Q15 | - |  |  | SI | Suggestive of impending thyroid storm |
| Q16 | - |  |  | SI | < 25 |
| Q17 | - |  |  | SI | Unlikely to represent thyroid storm |
| Q18 | - |  |  | SI | > 45: Highly suggestive of thyroid storm |
| Q19 | - |  |  | SI | 25 – 45: Suggestive of impending thyroid storm |
| Q20 | - |  |  | SI | < 25: Unlikely to represent thyroid storm |
| Q21 | - |  |  | SI | The Burch-Wartofsky Point Scale (BWPS) predicts li... |
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
| WIND_CreatedDate | date |  |  | SI | Created Date |
| WIND_CreatedTime | time |  |  | SI | Created Time |
| WIND_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WIND_Data | varchar |  |  | SI | Data |
| WIND_Height | double |  |  | SI | Height |
| WIND_Index | varchar |  |  | SI | Index |
| WIND_LeftCoord | double |  |  | SI | Left Coord |
| WIND_Name | varchar |  |  | SI | Name |
| WIND_TopCoord | double |  |  | SI | Top Coord |
| WIND_UpdatedDate | date |  |  | SI | Updated Date |
| WIND_UpdatedTime | time |  |  | SI | Updated Time |
| WIND_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WIND_Visible | varchar |  |  | SI | Visible |
| WIND_Width | double |  |  | SI | Width |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
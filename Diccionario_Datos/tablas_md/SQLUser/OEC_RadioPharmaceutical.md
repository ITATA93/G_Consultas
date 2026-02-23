# SQLUser.OEC_RadioPharmaceutical

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RADF_RowId | bigint | PK |  | NO | - |
| Q02 | - |  |  | SI | Si no hay sibilancias debido a la entrada mínima d... |
| Q03 | - |  |  | SI | Frecuencia respiratoria |
| Q04 | - |  |  | SI | Sibilancias |
| Q05 | - |  |  | SI | Relación inspiratoria / espiratoria |
| Q06 | - |  |  | SI | Uso de músculos accesorios-esternocleidomastoideo |
| Q07 | - |  |  | SI | Saturación de oxígeno |
| Q08 | - |  |  | SI | Score < 7: Mild attack |
| Q09 | - |  |  | SI | Score 7 - 11: Moderate / severe attack |
| Q10 | - |  |  | SI | Score = or > 12: Severe attack |
| Q11 | - |  |  | SI | Sin embargo, el índice pulmonar puede subestimar e... |
| Q12 | - |  |  | SI | The total score ranges from 0 - 15: |
| Q13 | - |  |  | SI | La puntuación del índice pulmonar ayuda a evaluar ... |
| Q14 | - |  |  | SI | Fecha |
| Q15 | - |  |  | SI | Hora |
| QLA | - |  |  | SI | The total score ranges from 0 - 15: |
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
| RADF_Code | varchar |  |  | NO | Code |
| RADF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RADF_CreatedDate | date |  |  | SI | Created Date |
| RADF_CreatedTime | time |  |  | SI | Created Time |
| RADF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RADF_Desc | varchar |  |  | NO | Description |
| RADF_Owner | varchar |  |  | SI | Owner |
| RADF_UpdatedDate | date |  |  | SI | Updated Date |
| RADF_UpdatedTime | time |  |  | SI | Updated Time |
| RADF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
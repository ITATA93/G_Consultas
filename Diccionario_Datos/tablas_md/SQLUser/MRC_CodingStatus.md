# SQLUser.MRC_CodingStatus

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CODST_RowId | bigint | PK |  | NO | - |
| CODST_Code | varchar |  |  | NO | Code |
| CODST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CODST_CreatedDate | date |  |  | SI | Created Date |
| CODST_CreatedTime | time |  |  | SI | Created Time |
| CODST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CODST_DateFrom | date |  |  | SI | Date From |
| CODST_DateTo | date |  |  | SI | Date To |
| CODST_Desc | varchar |  |  | NO | Description |
| CODST_Owner | varchar |  |  | SI | Owner |
| CODST_UpdatedDate | date |  |  | SI | Updated Date |
| CODST_UpdatedTime | time |  |  | SI | Updated Time |
| CODST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Condición física |
| Q02 | - |  |  | SI | Estado Mental |
| Q03 | - |  |  | SI | Actividad |
| Q04 | - |  |  | SI | Movilidad |
| Q05 | - |  |  | SI | Incontinencia |
| Q06 | - |  |  | SI | Resultado Escala de Norton |
| Q06ObsDR | - |  |  | SI | Resultado Escala de Norton DR |
| Q07 | - |  |  | SI | Se realizan medidas según riesgo evaluado |
| Q08 | - |  |  | SI | Información a familiar (Primer Contacto) |
| Q09 | - |  |  | SI | Fecha de información a Familiar |
| Q10 | - |  |  | SI | Aceptación de Medidas |
| Q11 | - |  |  | SI | Nombre del Familiar |
| Q12 | - |  |  | SI | Nombre Responsable |
| Q13 | - |  |  | SI | Razón de No Realización |
| Q14 | - |  |  | SI | Etiqueta Riesgo Bajo |
| Q15 | - |  |  | SI | Etiqueta Riesgo Moderado |
| Q16 | - |  |  | SI | Etiqueta Riesgo Alto |
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
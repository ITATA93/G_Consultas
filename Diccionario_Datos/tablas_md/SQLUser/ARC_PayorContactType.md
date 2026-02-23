# SQLUser.ARC_PayorContactType

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PCT_RowId | bigint | PK |  | NO | - |
| PCT_Code | varchar |  |  | NO | Code |
| PCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PCT_CreatedDate | date |  |  | SI | Created Date |
| PCT_CreatedTime | time |  |  | SI | Created Time |
| PCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PCT_DateFrom | date |  |  | SI | Date From |
| PCT_DateTo | date |  |  | SI | Date To |
| PCT_Desc | varchar |  |  | NO | Description |
| PCT_Owner | varchar |  |  | SI | Owner |
| PCT_UpdatedDate | date |  |  | SI | Updated Date |
| PCT_UpdatedTime | time |  |  | SI | Updated Time |
| PCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Entrevista al Paciente |
| Q02 | - |  |  | SI | I.- ¿Tiene su dolor alguna de estas característica... |
| Q03 | - |  |  | SI | 1. Quemazón |
| Q04 | - |  |  | SI | 2. Sensación de frío doloroso |
| Q05 | - |  |  | SI | 3. Descargas eléctricas |
| Q06 | - |  |  | SI | II.-  ¿Tiene en la zona donde le duele alguno de e... |
| Q07 | - |  |  | SI | 4. Hormigueo |
| Q08 | - |  |  | SI | 5. Pinchazos |
| Q09 | - |  |  | SI | 6. Entumecimiento |
| Q10 | - |  |  | SI | 7. Picazón |
| Q11 | - |  |  | SI | Exploración del Paciente |
| Q12 | - |  |  | SI | III.- ¿Se evidencia en la exploración alguno de es... |
| Q13 | - |  |  | SI | 8. Hipoestesia al tacto |
| Q14 | - |  |  | SI | 9. Hipoestesia al pinchazo |
| Q15 | - |  |  | SI | IV.- ¿El dolor se provoca o intensifica por? |
| Q16 | - |  |  | SI | 10. El roce |
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
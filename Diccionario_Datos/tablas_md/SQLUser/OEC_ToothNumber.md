# SQLUser.OEC_ToothNumber

**Schema:** SQLUser
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TOOTHN_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Ronquidos: ¿Ronca fuerte (tan fuerte que se escuch... |
| Q02 | - |  |  | SI | Cansado: ¿Se siente con frecuencia cansado, fatiga... |
| Q03 | - |  |  | SI | Lo observaron: ¿Alguien lo observó dejar de respir... |
| Q04 | - |  |  | SI | Presión Arterial: ¿Tiene o está recibiendo tratami... |
| Q05 | - |  |  | SI | IMC: ¿Índice de masa corporal de más de 35 kg/m2? |
| Q06 | - |  |  | SI | Edad: ¿Tiene más de 50 años? |
| Q07 | - |  |  | SI | Circunferencia del cuello: ¿El tamaño de su cuello... |
| Q08 | - |  |  | SI | Sexo: ¿Masculino? |
| QHIGH | - |  |  | SI | Alto riesgo de AOS: Sí a 5-8 preguntas |
| QLOW | - |  |  | SI | Bajo riesgo de AOS (Apnea Obstructiva del Sueño): ... |
| QSTOPBang | - |  |  | SI | El cuestionario STOP Bang es una herramienta para ... |
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
| TOOTHN_Code | varchar |  |  | NO | Code |
| TOOTHN_CreatedDate | date |  |  | SI | Created Date |
| TOOTHN_CreatedTime | time |  |  | SI | Created Time |
| TOOTHN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TOOTHN_Desc | varchar |  |  | NO | Description |
| TOOTHN_UpdatedDate | date |  |  | SI | Updated Date |
| TOOTHN_UpdatedTime | time |  |  | SI | Updated Time |
| TOOTHN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
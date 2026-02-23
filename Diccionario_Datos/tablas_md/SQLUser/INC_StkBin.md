# SQLUser.INC_StkBin

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCSB_RowId | bigint | PK |  | NO | - |
| ChildQ24DR | - |  |  | SI | Child Reference: Motivo de consulta según adolecen... |
| INCSB_Code | varchar |  |  | NO | Storage Bin Code |
| INCSB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCSB_CreatedDate | date |  |  | SI | Created Date |
| INCSB_CreatedTime | time |  |  | SI | Created Time |
| INCSB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCSB_Desc | varchar |  |  | NO | Description |
| INCSB_Owner | varchar |  |  | SI | Owner |
| INCSB_UpdatedDate | date |  |  | SI | Updated Date |
| INCSB_UpdatedTime | time |  |  | SI | Updated Time |
| INCSB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Establecimiento |
| Q03 | - |  |  | SI | Evolución N° |
| Q04 | - |  |  | SI | Fecha |
| Q05 | - |  |  | SI | Edad años |
| Q051 | - |  |  | SI | Edad Meses |
| Q051b | - |  |  | SI | Edad Meses Database |
| Q06 | - |  |  | SI | Acompañante |
| Q07 | - |  |  | SI | Estado Civil |
| Q08 | - |  |  | SI | Fecha de la última menstruación |
| Q09 | - |  |  | SI | Fecha |
| Q10 | - |  |  | SI | Peso (Kg) |
| Q10ObsDR | - |  |  | SI | Peso (Kg) DR |
| Q11 | - |  |  | SI | Celtil Peso/Talla (IMC) |
| Q11ObsDR | - |  |  | SI | Celtil Peso/Talla (IMC) DR |
| Q12 | - |  |  | SI | Talla (cm) |
| Q12ObsDR | - |  |  | SI | Talla (cm) DR |
| Q13 | - |  |  | SI | Centil Talla/Edad |
| Q13ObsDR | - |  |  | SI | Centil Talla/Edad DR |
| Q14 | - |  |  | SI | Centil Peso/Edad |
| Q14ObsDR | - |  |  | SI | Centil Peso/Edad DR |
| Q15 | - |  |  | SI | Presión Sistólica mmHg |
| Q15ObsDR | - |  |  | SI | Presión Sistólica mmHg DR |
| Q16 | - |  |  | SI | Presión Distólica mmHg |
| Q16ObsDR | - |  |  | SI | Presión Distólica mmHg DR |
| Q17 | - |  |  | SI | Frecuencia Cardiaca |
| Q17ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q19 | - |  |  | SI | Mamas |
| Q19ObsDR | - |  |  | SI | Mamas DR |
| Q20 | - |  |  | SI | Vello púbico |
| Q20ObsDR | - |  |  | SI | Vello púbico DR |
| Q21 | - |  |  | SI | Genitales |
| Q21ObsDR | - |  |  | SI | Genitales DR |
| Q22 | - |  |  | SI | Volumen testicular derecho (cm3) |
| Q23 | - |  |  | SI | Volumen testicular izquierdo (cm3) |
| Q26 | - |  |  | SI | Cambios relevantes/observaciones |
| Q27 | - |  |  | SI | Diagnóstico integral |
| Q28 | - |  |  | SI | Indicaciones e Interconsultas |
| Q29 | - |  |  | SI | Responsable |
| Q30 | - |  |  | SI | Fecha próxima visita |
| Q31 | - |  |  | SI | IMC |
| QIIM | - |  |  | SI | Ingreso información manualmente |
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
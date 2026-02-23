# SQLUser.LBC_TestItemCodedResultCancerCode

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTICRCC_ParRef | varchar | PK |  | NO | - |
| LBCTICRCC_CancerCode_DR | bigint |  | FK | SI | - |
| LBCTICRCC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTICRCC_DefaultValue | varchar |  |  | SI | - |
| LBCTICRCC_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Caídas Previas |
| Q02 | - |  |  | SI | Medicamentos |
| Q03 | - |  |  | SI | Déficit Sensoriales |
| Q04 | - |  |  | SI | Estado Mental |
| Q05 | - |  |  | SI | Deambulación |
| Q06 | - |  |  | SI | Resultado Escala Riesgo de Caidas Downton |
| Q06ObsDR | - |  |  | SI | Resultado Escala Riesgo de Caidas Downton DR |
| Q08 | - |  |  | SI | Etiqueta Riesgo Bajo |
| Q09 | - |  |  | SI | Etiqueta Riesgo Moderado |
| Q10 | - |  |  | SI | Etiqueta Riesgo Alto |
| Q11 | - |  |  | SI | Se Realizan Medidas Según Riesgo Evaluado |
| Q12 | - |  |  | SI | Información a familiar (Primer Contacto) |
| Q13 | - |  |  | SI | Fecha de Información a familia |
| Q14 | - |  |  | SI | Aceptación a Medidas |
| Q15 | - |  |  | SI | Nombre de Familiar |
| Q16 | - |  |  | SI | Nombre Responsable |
| Q17 | - |  |  | SI | Razón de No Realización |
| Q20 | - |  |  | SI | Barandas en Alto: 24 hrs. del día |
| Q21 | - |  |  | SI | Métodos de Contención: Emocional/Ambiental |
| Q22 | - |  |  | SI | Altura de la Cama: bajar a 42 cm en T.N. |
| Q23 | - |  |  | SI | Requiere Acompañante Permanente: SI |
| Q24 | - |  |  | SI | Vigilancia al Levantar: SI |
| Q25 | - |  |  | SI | Timbre de llamado: Dejar al Alcance del Paciente |
| Q30 | - |  |  | SI | Barandas en Alto: 24 hrs. del día |
| Q31 | - |  |  | SI | Métodos de Contención: Emocional/Ambiental |
| Q32 | - |  |  | SI | Altura de la Cama: bajar a 42 cm en T.N. |
| Q33 | - |  |  | SI | Requiere Acompañante Permanente: NO |
| Q34 | - |  |  | SI | Vigilancia al Levantar: SI |
| Q35 | - |  |  | SI | Timbre de llamado: Dejar al Alcance del paciente |
| Q40 | - |  |  | SI | Barandas en Alto: 24 hrs. del día |
| Q41 | - |  |  | SI | Métodos de Contención: Farmacológica y/o Mecánica |
| Q42 | - |  |  | SI | Altura de la Cama: bajar a 42 cm en T.N. |
| Q43 | - |  |  | SI | Requiere Acompañante Permanente: SI |
| Q44 | - |  |  | SI | Vigilancia al Levantar: SI |
| Q45 | - |  |  | SI | Timbre de llamado: Dejar al Alcance del Paciente |
| Q46 | - |  |  | SI | Observaciones |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
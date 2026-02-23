# questionnaire.QTCEERC

> Escala de Riesgo de Caídas (J.H.Downton)

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Riesgo de Caídas (J.H.Downton)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Caídas Previas |
| Q02 | varchar |  |  | SI | Medicamentos |
| Q03 | varchar |  |  | SI | Déficit Sensoriales |
| Q04 | varchar |  |  | SI | Estado Mental |
| Q05 | varchar |  |  | SI | Deambulación |
| Q06 | varchar |  |  | SI | Resultado Escala Riesgo de Caidas Downton |
| Q06ObsDR | varchar |  | FK | SI | Resultado Escala Riesgo de Caidas Downton DR |
| Q08 | varchar |  |  | SI | Etiqueta Riesgo Bajo |
| Q09 | varchar |  |  | SI | Etiqueta Riesgo Moderado |
| Q10 | varchar |  |  | SI | Etiqueta Riesgo Alto |
| Q11 | varchar |  |  | SI | Se Realizan Medidas Según Riesgo Evaluado  |
| Q12 | varchar |  |  | SI | Información a familiar (Primer Contacto) |
| Q13 | date |  |  | SI | Fecha de Información a familia |
| Q14 | varchar |  |  | SI | Aceptación a Medidas |
| Q15 | varchar |  |  | SI | Nombre de Familiar |
| Q16 | varchar |  |  | SI | Nombre Responsable  |
| Q17 | varchar |  |  | SI | Razón de No Realización |
| Q20 | varchar |  |  | SI | Barandas en Alto: 24 hrs. del día |
| Q21 | varchar |  |  | SI | Métodos de Contención: Emocional/Ambiental |
| Q22 | varchar |  |  | SI | Altura de la Cama: bajar a 42 cm en T.N. |
| Q23 | varchar |  |  | SI | Requiere Acompañante Permanente: SI |
| Q24 | varchar |  |  | SI | Vigilancia al Levantar: SI |
| Q25 | varchar |  |  | SI | Timbre de llamado: Dejar al Alcance del Paciente  |
| Q30 | varchar |  |  | SI | Barandas en Alto: 24 hrs. del día |
| Q31 | varchar |  |  | SI | Métodos de Contención: Emocional/Ambiental |
| Q32 | varchar |  |  | SI | Altura de la Cama: bajar a 42 cm en T.N. |
| Q33 | varchar |  |  | SI | Requiere Acompañante Permanente: NO  |
| Q34 | varchar |  |  | SI | Vigilancia al Levantar: SI  |
| Q35 | varchar |  |  | SI | Timbre de llamado: Dejar al Alcance del paciente |
| Q40 | varchar |  |  | SI | Barandas en Alto: 24 hrs. del día |
| Q41 | varchar |  |  | SI | Métodos de Contención: Farmacológica y/o Mecánica |
| Q42 | varchar |  |  | SI | Altura de la Cama: bajar a 42 cm en T.N. |
| Q43 | varchar |  |  | SI | Requiere Acompañante Permanente: SI |
| Q44 | varchar |  |  | SI | Vigilancia al Levantar: SI |
| Q45 | varchar |  |  | SI | Timbre de llamado: Dejar al Alcance del Paciente  |
| Q46 | varchar |  |  | SI | Observaciones |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
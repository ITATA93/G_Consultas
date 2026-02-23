# questionnaire.QTCEEDODON

> Examen Odontológico

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Odontológico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Motivo de Consulta |
| Q02 | varchar |  |  | SI | Control de Mantención  |
| Q03 | varchar |  |  | SI | Evaluación de Ansiedad |
| Q04 | varchar |  |  | SI | Malos Habitos |
| Q05 | varchar |  |  | SI | Examen Intraoral 2 |
| Q06 | varchar |  |  | SI | Mucosa |
| Q07 | varchar |  |  | SI | Periodonto |
| Q08 | varchar |  |  | SI | Observacion Mucosa |
| Q09 | varchar |  |  | SI | Oclusión |
| Q10 | varchar |  |  | SI | Alteración del Esmalte |
| Q24 | varchar |  |  | SI | Fumador |
| Q25 | varchar |  |  | SI | Observacion Malos Habitos |
| Q26 | varchar |  |  | SI | Hábitos de higiene |
| Q27 | varchar |  |  | SI | Hábitos de higiene (frecuencia) |
| Q28 | varchar |  |  | SI | MER |
| Q28ObsDR | varchar |  | FK | SI | MER DR |
| Q29 | varchar |  |  | SI | Condición del Paciente |
| Q30 | varchar |  |  | SI | Otros Antecedentes |
| Q31 | varchar |  |  | SI | Examen Intraoral |
| Q32 | numeric |  |  | SI | Número Total de Dientes Primarios en Boca |
| Q33 | numeric |  |  | SI | Número Total de Dientes Permanentes&nbsp;en Boca |
| Q35 | varchar |  |  | SI | Consumo Dieta Cariogenica |
| Q36 | varchar |  |  | SI | Educacion en Tecnica de Higiene Bucal indicada |
| Q41 | varchar |  |  | SI | Educacion individual con instruccion de tecnica de... |
| Q45 | varchar |  |  | SI | Observacion Educacion en Tecnica de Higiene Bucal ... |
| Q51 | varchar |  |  | SI | Observacion Consumo Dieta Cariogenica |
| Q52 | varchar |  |  | SI | Observacion Periodonto |
| Q53 | varchar |  |  | SI | Observacion Oclusión |
| Q54 | varchar |  |  | SI | Observacion Alteración del Esmalte |
| QCO | varchar |  |  | SI | Colegio |
| QCU | varchar |  |  | SI | Curso |
| QJN | varchar |  |  | SI | Paciente Junaeb |
| QNE | varchar |  |  | SI | Nivel de Escolaridad |
| QRem1 | date |  |  | SI | Instalación/Alta |
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
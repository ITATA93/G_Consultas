# questionnaire.QTCEACCMOR

> Denuncia Accidente por Mordeduras

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Denuncia Accidente por Mordeduras

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Folio N° |
| Q02 | varchar |  |  | SI | Tipo de Accidente |
| Q03 | date |  |  | SI | Fecha Accidente |
| Q04 | date |  |  | SI | Fecha Denuncia |
| Q05 | varchar |  |  | SI | Animal Mordedor |
| Q06 | varchar |  |  | SI | Otro |
| Q07 | varchar |  |  | SI | Ignora Domicilio |
| Q08 | bit |  |  | SI | Animal Vago |
| Q09 | varchar |  |  | SI | Muerto / Sacrificado |
| Q10 | varchar |  |  | SI | Tamaño |
| Q11 | varchar |  |  | SI | Color |
| Q12 | varchar |  |  | SI | Domicilio Animal |
| Q13 | varchar |  |  | SI | Poblacion  |
| Q14 | varchar |  |  | SI | Comuna |
| Q15 | varchar |  |  | SI | Ciudad |
| Q16 | numeric |  |  | SI | Telefono |
| Q17 | varchar |  |  | SI | Derivado SEREMI |
| Q18 | date |  |  | SI | Fecha de la Observacion |
| Q19 | varchar |  |  | SI | Condiciones del Animal a la Observacion |
| Q20 | varchar |  |  | SI | Signos de la Enfermedad |
| Q21 | varchar |  |  | SI | Observacion |
| Q22 | varchar |  |  | SI | Nombre y Firma del Funcionario |
| Q23 | varchar |  |  | SI | Envio Informe a Consultorio de Origen |
| Q24 | varchar |  |  | SI | Indicación de Vacuna  |
| Q25 | date |  |  | SI | Fecha Inicio Tratamiento |
| Q27 | varchar |  |  | SI | Nombre del Consultorio |
| Q28 | varchar |  |  | SI | Cuantificador accidente |
| Q29 | varchar |  |  | SI | Localidad |
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
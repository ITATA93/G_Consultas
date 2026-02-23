# questionnaire.QTCECSR

> Chequeo Salida de Recuperación

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Chequeo Salida de Recuperación

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha realización chequeo |
| Q02 | time |  |  | SI | Hora realización chequeo  |
| Q03 | varchar |  |  | SI | Chequeo Presencia de Brazalete de Identificación |
| Q04 | varchar |  |  | SI | Chequeo condición correcta de accesos venosos |
| Q05 | varchar |  |  | SI | Chequeo condición correcta de apósitos/vendajes |
| Q06 | varchar |  |  | SI | Chequeo presencia de globo vesical y/o medición de... |
| Q07 | varchar |  |  | SI | Chequeo documentación del caso |
| Q08 | varchar |  |  | SI | Chequeo condición ropa de cama del paciente |
| Q09 | varchar |  |  | SI | Chequeo último control de signos vitales |
| Q10 | varchar |  |  | SI | Chequear que el paciente egrese con todos los artí... |
| Q11 | varchar |  |  | SI | Observaciones al Egreso de Recuperación |
| Q12 | varchar |  |  | SI | Auxiliar de Enfermería responsable  |
| Q13 | varchar |  |  | SI | Enfermera / Matrona responsable |
| Q14 | varchar |  |  | SI | Anestesia |
| Q15 | varchar |  |  | SI | Zona Operatoria |
| Q16 | varchar |  |  | SI | Uso medias antiembólicas |
| Q17 | varchar |  |  | SI | Uso Bomba Infusión |
| Q18 | varchar |  |  | SI | Procedencia |
| Q19 | varchar |  |  | SI | Responsable del traslado |
| Q20 | varchar |  |  | SI | Unidad de atención |
| Q21 | varchar |  |  | SI | Chequeo Presencia Brazalete Alergias |
| Q22 | varchar |  |  | SI | Comentario |
| Q23 | varchar |  |  | SI | Comentario |
| Q24 | varchar |  |  | SI | Comentario |
| Q25 | varchar |  |  | SI | Comentario |
| Q26 | varchar |  |  | SI | Comentario |
| Q27 | varchar |  |  | SI | Comentario |
| Q28 | varchar |  |  | SI | Comentario |
| Q29 | varchar |  |  | SI | Comentario |
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
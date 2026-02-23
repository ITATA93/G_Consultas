# SQLUser.MRC_NursingNoteCodes

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NURN_RowId | bigint | PK |  | NO | - |
| NURN_Code | varchar |  |  | NO | Code |
| NURN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NURN_CreatedDate | date |  |  | SI | Created Date |
| NURN_CreatedTime | time |  |  | SI | Created Time |
| NURN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NURN_FirstLine | varchar |  |  | SI | First Line of Descr |
| NURN_NURG_DR | bigint |  | FK | SI | Des Ref to NURN_NURG |
| NURN_Owner | varchar |  |  | SI | Owner |
| NURN_Text | varchar |  |  | SI | Text |
| NURN_UpdatedDate | date |  |  | SI | Updated Date |
| NURN_UpdatedTime | time |  |  | SI | Updated Time |
| NURN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02 | - |  |  | SI | Ferulización |
| Q03 | - |  |  | SI | Impresión |
| Q04 | - |  |  | SI | Prueba de cera |
| Q05 | - |  |  | SI | Instalación de planos de alivio oclusal/alta |
| Q06 | - |  |  | SI | Controles 1 |
| Q07 | - |  |  | SI | Controles 2 |
| Q08 | - |  |  | SI | Controles 3 |
| Q09 | - |  |  | SI | Cirugia Periodontal |
| Q10 | - |  |  | SI | Destartraje supragingival y pulido coronario |
| Q11 | - |  |  | SI | Destartraje subgingival y pulido radicular |
| Q12 | - |  |  | SI | Pronostico |
| Q17 | - |  |  | SI | Observaciones |
| Q18 | - |  |  | SI | Periodontal |
| Q19 | - |  |  | SI | De Mantención |
| Q24 | - |  |  | SI | Destartraje |
| Q28 | - |  |  | SI | Categoria de la carta |
| Q29 | - |  |  | SI | Malo |
| Q30 | - |  |  | SI | Digitado Por |
| Q33 | - |  |  | SI | Estado de la Pieza |
| QPer | - |  |  | SI | Periodontograma |
| QRem1 | - |  |  | SI | Instalación / Alta |
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
| Qo1 | - |  |  | SI | Observación 1 |
| Qo2 | - |  |  | SI | Observación 2 |
| Qo3 | - |  |  | SI | Observación 3 |
| Qo4 | - |  |  | SI | Observación 4 |
| Qo5 | - |  |  | SI | Observación 5 |
| Qo6 | - |  |  | SI | Observación 6 |
| Qo7 | - |  |  | SI | Observación 7 |
| Qo8 | - |  |  | SI | Observación 8 |
| Qo9 | - |  |  | SI | Observación 9 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
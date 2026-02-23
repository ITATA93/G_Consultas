# questionnaire.QCLXXRMTRR

> Registro Monitorización Terapia de Reemplazo Renal Agudo

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Monitorización Terapia de Reemplazo Renal Agudo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | I. Indicación |
| Q02 | varchar |  |  | SI | Tipo de Terapia de Reemplazo Renal |
| Q02ObsDR | varchar |  | FK | SI | Tipo de Terapia de Reemplazo Renal DR |
| Q03 | varchar |  |  | SI | Tipo de Anticoagulación |
| Q04 | varchar |  |  | SI | Comentario TTR |
| Q05 | varchar |  |  | SI | Comentario TA |
| Q06 | varchar |  |  | SI | Acceso Vascular |
| Q07 | varchar |  |  | SI | Comentario AV |
| Q08 | numeric |  |  | SI | Dosis Renal |
| Q09 | varchar |  |  | SI | Comentario DR |
| Q10 | varchar |  |  | SI | II. Monitorización - Parámetros Relativos a la San... |
| Q11 | varchar |  |  | SI | Flujo de Sangre |
| Q11ObsDR | varchar |  | FK | SI | Flujo de Sangre DR |
| Q12 | numeric |  |  | SI | Presión Arterial Mín (PA) |
| Q13 | numeric |  |  | SI | Presión Arterial Máx (PA) |
| Q14 | numeric |  |  | SI | PBE Máx |
| Q15 | varchar |  |  | SI | Ventana de Presión Venosa |
| Q15ObsDR | varchar |  | FK | SI | Ventana de Presión Venosa DR |
| Q16 | numeric |  |  | SI | PDF Descenso Máx de Presión |
| Q17 | varchar |  |  | SI | Presión Transmembrana Máx (TMP) |
| Q17ObsDR | varchar |  | FK | SI | Presión Transmembrana Máx (TMP) DR |
| Q18 | numeric |  |  | SI | Temperatura Calefactor |
| Q19 | varchar |  |  | SI | Comentario FS |
| Q20 | varchar |  |  | SI | Comentario PAMi |
| Q21 | varchar |  |  | SI | Comentario PAMa |
| Q22 | varchar |  |  | SI | Comentario PBE |
| Q23 | varchar |  |  | SI | Comentario VPV |
| Q24 | varchar |  |  | SI | Comentario PDF |
| Q25 | varchar |  |  | SI | Comentario TPM |
| Q26 | varchar |  |  | SI | Comentario Temp |
| Q27 | varchar |  |  | SI | III. Monitorización - Parámetros Relativos al Líqu... |
| Q28 | numeric |  |  | SI | PD2 Mín |
| Q29 | varchar |  |  | SI | Comentario PD2 |
| Q30 | varchar |  |  | SI | Velocidad de UF |
| Q30ObsDR | varchar |  | FK | SI | Velocidad de UF DR |
| Q31 | varchar |  |  | SI | Comentario VUF |
| Q32 | numeric |  |  | SI | Volumen Bolsa de UF |
| Q33 | varchar |  |  | SI | Comentario VBU |
| Q34 | numeric |  |  | SI | Volumen Líquido de UF |
| Q35 | varchar |  |  | SI | Comentario VLU |
| Q36 | numeric |  |  | SI | Volumen Líquido de Diálisis |
| Q37 | varchar |  |  | SI | Comentario VLD |
| Q38 | numeric |  |  | SI | Flujo Líquido de Sustitución |
| Q39 | varchar |  |  | SI | Comentario FLS |
| Q40 | varchar |  |  | SI | Flujo Líquido de Diálisis |
| Q40ObsDR | varchar |  | FK | SI | Flujo Líquido de Diálisis DR |
| Q41 | varchar |  |  | SI | Comentario FLD |
| Q42 | numeric |  |  | SI | Tiempo de Tratamiento |
| Q43 | numeric |  |  | SI | Tiempo Tratamiento (min) |
| Q44 | varchar |  |  | SI | Comentario TT |
| Q45 | varchar |  |  | SI | IV. Observaciones |
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
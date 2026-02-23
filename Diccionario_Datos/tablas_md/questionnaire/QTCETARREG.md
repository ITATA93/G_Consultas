# questionnaire.QTCETARREG

> Tarjeta de Registro y Control Rehabilitacion Integral N

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tarjeta de Registro y Control Rehabilitacion Integral N

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ01 | varchar |  |  | SI | - |
| CQ14 | varchar |  |  | SI | - |
| CQ19 | varchar |  |  | SI | - |
| Q01 | varchar |  |  | SI | Vive con : |
| Q02 | bit |  |  | SI | HTA |
| Q03 | bit |  |  | SI | DM |
| Q04 | bit |  |  | SI | IG/RI |
| Q05 | bit |  |  | SI | DLP |
| Q06 | bit |  |  | SI | AR |
| Q07 | bit |  |  | SI | OA |
| Q08 | bit |  |  | SI | EPOC |
| Q09 | bit |  |  | SI | ASMA |
| Q10 | bit |  |  | SI | IR |
| Q11 | bit |  |  | SI | IAM |
| Q12 | bit |  |  | SI | AVE |
| Q13 | bit |  |  | SI | IC |
| Q14 | varchar |  |  | SI | Hábitos : |
| Q15 | varchar |  |  | SI | Control Nutricional |
| Q16 | varchar |  |  | SI | Factores de Riesgo |
| Q17 | varchar |  |  | SI | Factores Protectores |
| Q18 | date |  |  | SI | Fecha |
| Q19 | varchar |  |  | SI | Atendido por : |
| Q20 | varchar |  |  | SI | Patologia Base |
| Q21 | date |  |  | SI | Fecha Proximo Control |
| Q22 | varchar |  |  | SI | RND : Registro Nacional de Incapacidad |
| Q23 | varchar |  |  | SI | Patologia Base |
| QACR | bit |  |  | SI | Actividades Recreativas |
| QACT | bit |  |  | SI | Actividades Terapeuticas |
| QADP | bit |  |  | SI | Adaptacion del Hogar |
| QAVD | bit |  |  | SI | Habilitacion y Rehabilitacion de AVD |
| QC2 | bit |  |  | SI | Estilo de Vida y Conductas de Autocuidado |
| QC3 | bit |  |  | SI | Actividades Fisicas |
| QC4 | bit |  |  | SI | Tabaquismo |
| QCAT | bit |  |  | SI | Confeccion de Ayudas Tecnicas |
| QCO | bit |  |  | SI | Confeccion Ortesis |
| QEAT | bit |  |  | SI | Evaluacion Ayudas Tecnicas |
| QET | bit |  |  | SI | Ejercicios Terapeuticos |
| QFST | bit |  |  | SI | Fisioterapia |
| QHAB | bit |  |  | SI | Habilitacion Laboral Educacional |
| QIS | bit |  |  | SI | Inclusion Social |
| QMST | bit |  |  | SI | Masoterapia |
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
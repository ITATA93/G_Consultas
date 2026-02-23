# questionnaire.QTCEVEHC

> VE Higiene Corporal Integridad de la Piel

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* VE Higiene Corporal Integridad de la Piel

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit |  |  | SI | Autonomo |
| Q02 | bit |  |  | SI | Total |
| Q03 | bit |  |  | SI | Parcial |
| Q04 | bit |  |  | SI | Adecuada |
| Q05 | bit |  |  | SI | Inadecuada |
| Q06 | varchar |  |  | SI | Habito de Higene |
| Q07 | bit |  |  | SI | Arreglado |
| Q08 | bit |  |  | SI | Descuidado |
| Q09 | bit |  |  | SI | Piel Integra |
| Q10 | bit |  |  | SI | Fria |
| Q11 | bit |  |  | SI | Sudorosa |
| Q12 | bit |  |  | SI | Normal |
| Q13 | bit |  |  | SI | Palida |
| Q14 | bit |  |  | SI | Icterica |
| Q15 | bit |  |  | SI | Cianotica |
| Q16 | varchar |  |  | SI | Detalle |
| Q17 | bit |  |  | SI | Edemas |
| Q18 | varchar |  |  | SI | Detalle |
| Q19 | bit |  |  | SI | Signo de pliegue positivo |
| Q20 | bit |  |  | SI | Linfedema |
| Q21 | bit |  |  | SI | Heridas |
| Q22 | varchar |  |  | SI | Localizacion |
| Q23 | varchar |  |  | SI | Tipo |
| Q24 | bit |  |  | SI | Flebitis |
| Q25 | varchar |  |  | SI | Localizacion |
| Q26 | varchar |  |  | SI | Estadio |
| Q27 | bit |  |  | SI | Varices |
| Q28 | bit |  |  | SI | Ulceras por presion |
| Q29 | varchar |  |  | SI | Localizacion |
| Q30 | varchar |  |  | SI | Estadio |
| Q31 | varchar |  |  | SI | Tamaño |
| Q32 | bit |  |  | SI | Otras alteraciones de la piel |
| Q33 | varchar |  |  | SI | Detalle |
| Q34 | bit |  |  | SI | Cateteres |
| Q35 | varchar |  |  | SI | Localizacion |
| Q36 | varchar |  |  | SI | Tipo |
| Q37 | date |  |  | SI | Fecha |
| Q38 | varchar |  |  | SI | Diagnostico 1 |
| Q39 | varchar |  |  | SI | Diagnostico 2 |
| Q40 | varchar |  |  | SI | Conclusión |
| Q41 | varchar |  |  | SI | Objetivo Registro |
| Q42 | varchar |  |  | SI | Higiene |
| Q43 | varchar |  |  | SI | Higiene Corporal Integridad de la Piel |
| Q44 | varchar |  |  | SI | Higiene Adecuada |
| Q45 | varchar |  |  | SI | Arreglo Personal |
| Q46 | varchar |  |  | SI | Color de la Piel |
| Q47 | varchar |  |  | SI | Detalle Ictérica |
| Q48 | varchar |  |  | SI | Detalle Cianótica |
| Q49 | varchar |  |  | SI | Localización de Varices |
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
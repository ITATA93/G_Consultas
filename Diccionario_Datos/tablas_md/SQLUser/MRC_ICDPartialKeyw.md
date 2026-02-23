# SQLUser.MRC_ICDPartialKeyw

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PARTKEYW_MRCID_ParRef | bigint | PK |  | NO | Des Ref to MRCID |
| PARTKEYW_Childsub | numeric |  |  | NO | PARTKEYW Childsub (NewKey) |
| PARTKEYW_Location | varchar |  |  | SI | Location |
| PARTKEYW_Name | varchar |  |  | SI | Name |
| PARTKEYW_Name1 | varchar |  |  | SI | Name1 |
| PARTKEYW_Name2 | varchar |  |  | SI | Name2 |
| PARTKEYW_NameAll | varchar |  |  | SI | Name All |
| PARTKEYW_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | ESPACIOS COMUNITARIOS |
| Q02 | - |  |  | SI | ESPACIOS COMUNITARIOS 1 |
| Q03 | - |  |  | SI | ESPACIOS COMUNITARIOS 2 |
| Q04 | - |  |  | SI | ESPACIOS COMUNITARIOS 3 |
| Q05 | - |  |  | SI | ESPACIOS COMUNITARIOS 4 |
| Q06 | - |  |  | SI | ESPACIOS COMUNITARIOS 5 |
| Q07 | - |  |  | SI | ESPACIOS COMUNITARIOS 6 |
| Q08 | - |  |  | SI | ESPACIOS COMUNITARIOS 7 |
| Q09 | - |  |  | SI | ESPACIOS COMUNITARIOS 8 |
| Q10 | - |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES |
| Q11 | - |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 1 |
| Q12 | - |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 2 |
| Q13 | - |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 3 |
| Q14 | - |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 4 |
| Q15 | - |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 5 |
| Q16 | - |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 6 |
| Q17 | - |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 7 |
| Q18 | - |  |  | SI | ESTABLECIMIENTOS EDUCACIONALES 8 |
| Q19 | - |  |  | SI | CENTROS DE SALUD |
| Q20 | - |  |  | SI | CENTROS DE SALUD 1 |
| Q21 | - |  |  | SI | CENTROS DE SALUD 2 |
| Q22 | - |  |  | SI | CENTROS DE SALUD 3 |
| Q23 | - |  |  | SI | CENTROS DE SALUD 4 |
| Q24 | - |  |  | SI | CENTROS DE SALUD 5 |
| Q25 | - |  |  | SI | CENTROS DE SALUD 6 |
| Q26 | - |  |  | SI | CENTROS DE SALUD 7 |
| Q27 | - |  |  | SI | CENTROS DE SALUD 8 |
| Q29 | - |  |  | SI | Mes |
| Q30 | - |  |  | SI | Año |
| QHR | - |  |  | SI | Establecimiento |
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
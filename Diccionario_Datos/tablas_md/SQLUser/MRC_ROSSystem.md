# SQLUser.MRC_ROSSystem

**Schema:** SQLUser
**Columnas:** 130
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTROS_ParRef | bigint | PK |  | NO | Parent Reference |
| CTROS_Childsub | double |  |  | NO | Childsub |
| CTROS_Code | varchar |  |  | SI | Code |
| CTROS_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CTROS_CreatedDate | date |  |  | SI | Created Date |
| CTROS_CreatedTime | time |  |  | SI | Created Time |
| CTROS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTROS_DateFrom | date |  |  | SI | Date From |
| CTROS_DateTo | date |  |  | SI | Date To |
| CTROS_Desc | varchar |  |  | SI | Description |
| CTROS_RowId | varchar |  |  | NO | - |
| CTROS_Sequence | integer |  |  | SI | Sequence |
| CTROS_UpdatedDate | date |  |  | SI | Updated Date |
| CTROS_UpdatedTime | time |  |  | SI | Updated Time |
| CTROS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | N° de Sesiones Círculo de Actividad Física |
| Q02 | - |  |  | SI | N° de Sesiones Círculo de Vida Sana |
| Q03 | - |  |  | SI | N° de Sesiones Actividades Masivas |
| Q04 | - |  |  | SI | N° de Participantes Círculo de Actividad Física |
| Q05 | - |  |  | SI | N° de Participantes Círculo de Vida Sana |
| Q06 | - |  |  | SI | N° de Participantes Actividades Masivas |
| Q07 | - |  |  | SI | Acompañantes Menor 1 año Actividad Física |
| Q08 | - |  |  | SI | Acompañantes Menor 1 año Vida Sana |
| Q09 | - |  |  | SI | Acompañantes Menor 1 año Actividades Masivas |
| Q10 | - |  |  | SI | Acompañantes Niños 12 a 23 meses Actividad Física |
| Q11 | - |  |  | SI | Acompañantes Niños 12 a 23 meses Vida Sana |
| Q12 | - |  |  | SI | Acompañantes Niños 12 a 23 meses Actividades Masiv... |
| Q13 | - |  |  | SI | Acompañantes Niños de 2 a 5 años Actividad Física |
| Q14 | - |  |  | SI | Acompañantes Niños de 2 a 5 años Vida Sana |
| Q15 | - |  |  | SI | Acompañantes Niños de 2 a 5 años Actividades Masiv... |
| Q16 | - |  |  | SI | Acompañantes Niños de 6 a 9 años Actividad Física |
| Q17 | - |  |  | SI | Acompañantes Niños de 6 a 9 años Vida Sana |
| Q18 | - |  |  | SI | Acompañantes Niños de 6 a 9 años Actividades Masiv... |
| Q19 | - |  |  | SI | Acompañantes 10 a 14 años Actividad Física |
| Q20 | - |  |  | SI | Acompañantes 10 a 14 años Vida Sana |
| Q21 | - |  |  | SI | Acompañantes 10 a 14 años Actividades Masivas |
| Q22 | - |  |  | SI | Menor de 2 años Actividad Física |
| Q23 | - |  |  | SI | Menor de 2 años Vida Sana |
| Q24 | - |  |  | SI | Menor de 2 años Actividades Masivas |
| Q25 | - |  |  | SI | 2 a 4 años Actividad Física |
| Q26 | - |  |  | SI | 2 a 4 años Vida Sana |
| Q27 | - |  |  | SI | 2 a 4 años Actividades Masivas |
| Q28 | - |  |  | SI | 5 a 9 años Actividad Física |
| Q29 | - |  |  | SI | 5 a 9 años Vida Sana |
| Q30 | - |  |  | SI | 5 a 9 años Actividades Masivas |
| Q31 | - |  |  | SI | 10 a 14 años Actividad Física |
| Q32 | - |  |  | SI | 10 a 14 años Vida Sana |
| Q33 | - |  |  | SI | 10 a 14 años Actividades Masivas |
| Q34 | - |  |  | SI | 15 a 19 años Actividad Física |
| Q35 | - |  |  | SI | 15 a 19 años Visa Sana |
| Q36 | - |  |  | SI | 15 a 19 años Actividades Masivas |
| Q37 | - |  |  | SI | 20 a 24 años Actividad Física |
| Q38 | - |  |  | SI | 20 a 24 años Vida Sana |
| Q39 | - |  |  | SI | 20 a 24 años Actividades Masivas |
| Q40 | - |  |  | SI | 25 - 29 años Actividad Física |
| Q41 | - |  |  | SI | 25 - 29 años Vida Sana |
| Q42 | - |  |  | SI | 25 - 29 años Actividades Masivas |
| Q43 | - |  |  | SI | 30 - 34 años Actividad Física |
| Q44 | - |  |  | SI | 30 - 34 años Vida Sana |
| Q45 | - |  |  | SI | 30 - 34 años Actividades Masivas |
| Q46 | - |  |  | SI | 35 - 39 años Actividad Física |
| Q47 | - |  |  | SI | 35 - 39 años Vida Sana |
| Q48 | - |  |  | SI | 35 - 39 años Actividades Masivas |
| Q49 | - |  |  | SI | 40 - 44 años Actividad Física |
| Q50 | - |  |  | SI | 40 - 44 años Vida Sana |
| Q51 | - |  |  | SI | 40 - 44 años Actividades Masivas |
| Q52 | - |  |  | SI | 45 - 49 años Actividad Física |
| Q53 | - |  |  | SI | 45 - 49 años Vida Sana |
| Q54 | - |  |  | SI | 45 - 49 años Actividades Masivas |
| Q55 | - |  |  | SI | 50 - 54 años Actividad Física |
| Q56 | - |  |  | SI | 50 - 54 años Vida Sana |
| Q57 | - |  |  | SI | 50 - 54 años Actividades Masivas |
| Q58 | - |  |  | SI | 55 - 59 años Actividad Física |
| Q59 | - |  |  | SI | 55 - 59 años Vida Sana |
| Q60 | - |  |  | SI | 55 - 59 años Actividades Masivas |
| Q61 | - |  |  | SI | 60 - 64 años Actividad Física |
| Q62 | - |  |  | SI | 60 - 64 años Vida Sana |
| Q63 | - |  |  | SI | 60 - 64 años Actividades Masivas |
| Q64 | - |  |  | SI | Gestantes Actividad Física |
| Q65 | - |  |  | SI | Gestantes Visa Sana |
| Q66 | - |  |  | SI | Gestantes Actividades Masivas |
| Q67 | - |  |  | SI | Post Parto Actividad Física |
| Q68 | - |  |  | SI | Post Parto Vida Sana |
| Q69 | - |  |  | SI | Post Parto Actividades Masivas |
| Q70 | - |  |  | SI | CIRCULO DE ACTIVIDAD FISICA		 |
| Q71 | - |  |  | SI | CIRCULO DE VIDA SANA |
| Q72 | - |  |  | SI | ACTIVIDADES MASIVAS |
| Q74 | - |  |  | SI | Año |
| Q75 | - |  |  | SI | Mes |
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
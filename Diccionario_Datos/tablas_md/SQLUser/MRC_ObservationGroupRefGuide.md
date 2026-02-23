# SQLUser.MRC_ObservationGroupRefGuide

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GRPGUIDE_ParRef | bigint | PK |  | NO | MRC_ObservationGroup Parent Reference |
| GRPGUIDE_Childsub | double |  |  | NO | Childsub |
| GRPGUIDE_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| GRPGUIDE_CreatedDate | date |  |  | SI | Created Date |
| GRPGUIDE_CreatedTime | time |  |  | SI | Created Time |
| GRPGUIDE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GRPGUIDE_DateFrom | date |  |  | SI | Date From |
| GRPGUIDE_DateTo | date |  |  | SI | Date To |
| GRPGUIDE_Guide_DR | bigint |  | FK | SI | Des Ref Reference Guide |
| GRPGUIDE_RowId | varchar |  |  | NO | - |
| GRPGUIDE_UpdatedDate | date |  |  | SI | Updated Date |
| GRPGUIDE_UpdatedTime | time |  |  | SI | Updated Time |
| GRPGUIDE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | < 15 años 1 |
| Q02 | - |  |  | SI | < 15 años 2 |
| Q03 | - |  |  | SI | < 15 años 3 |
| Q04 | - |  |  | SI | < 15 años 4 |
| Q05 | - |  |  | SI | < 15 años 5 |
| Q06 | - |  |  | SI | < 15 años 6 |
| Q07 | - |  |  | SI | < 15 años 7 |
| Q08 | - |  |  | SI | < 15 años 8 |
| Q09 | - |  |  | SI | < 15 años 9 |
| Q10 | - |  |  | SI | < 15 años 10 |
| Q11 | - |  |  | SI | < 15 años 11 |
| Q12 | - |  |  | SI | < 15 años 12 |
| Q13 | - |  |  | SI | > 15-64 años 1 |
| Q14 | - |  |  | SI | > 15-64 años 2 |
| Q15 | - |  |  | SI | > 15-64 años 3 |
| Q16 | - |  |  | SI | > 15-64 años 4 |
| Q17 | - |  |  | SI | > 15-64 años 5 |
| Q18 | - |  |  | SI | > 15-64 años 6 |
| Q19 | - |  |  | SI | > 15-64 años 7 |
| Q20 | - |  |  | SI | > 15-64 años 8 |
| Q21 | - |  |  | SI | > 15-64 años 9 |
| Q22 | - |  |  | SI | > 15-64 años 10 |
| Q23 | - |  |  | SI | > 15-64 años 11 |
| Q24 | - |  |  | SI | > 15-64 años 12 |
| Q25 | - |  |  | SI | 65 y más años 1 |
| Q26 | - |  |  | SI | 65 y más años 2 |
| Q27 | - |  |  | SI | 65 y más años 3 |
| Q28 | - |  |  | SI | 65 y más años 4 |
| Q29 | - |  |  | SI | 65 y más años 5 |
| Q30 | - |  |  | SI | 65 y más años 6 |
| Q31 | - |  |  | SI | 65 y más años 7 |
| Q32 | - |  |  | SI | 65 y más años 8 |
| Q33 | - |  |  | SI | 65 y más años 9 |
| Q34 | - |  |  | SI | 65 y más años 10 |
| Q35 | - |  |  | SI | 65 y más años 11 |
| Q36 | - |  |  | SI | 65 y más años 12 |
| Q37 | - |  |  | SI | Informados 1 |
| Q38 | - |  |  | SI | Informados 2 |
| Q39 | - |  |  | SI | Informados 3 |
| Q40 | - |  |  | SI | Informados 4 |
| Q41 | - |  |  | SI | Informados 5 |
| Q42 | - |  |  | SI | Informados 6 |
| Q43 | - |  |  | SI | Informados 7 |
| Q44 | - |  |  | SI | Informados 8 |
| Q45 | - |  |  | SI | Informados 9 |
| Q46 | - |  |  | SI | Informados 10 |
| Q47 | - |  |  | SI | Informados 11 |
| Q48 | - |  |  | SI | Informados 12 |
| Q49 | - |  |  | SI | Positivo 1 |
| Q50 | - |  |  | SI | Positivo 2 |
| Q51 | - |  |  | SI | Positivo 3 |
| Q52 | - |  |  | SI | Positivo 4 |
| Q53 | - |  |  | SI | Positivo 5 |
| Q54 | - |  |  | SI | Positivo 6 |
| Q55 | - |  |  | SI | Positivo 7 |
| Q56 | - |  |  | SI | Positivo 8 |
| Q57 | - |  |  | SI | Positivo 9 |
| Q58 | - |  |  | SI | Positivo 10 |
| Q59 | - |  |  | SI | Positivo 11 |
| Q60 | - |  |  | SI | Positivo 12 |
| Q61 | - |  |  | SI | Negativo 1 |
| Q62 | - |  |  | SI | Negativo 2 |
| Q63 | - |  |  | SI | Negativo 3 |
| Q64 | - |  |  | SI | Negativo 4 |
| Q65 | - |  |  | SI | Negativo 5 |
| Q66 | - |  |  | SI | Negativo 6 |
| Q67 | - |  |  | SI | Negativo 7 |
| Q68 | - |  |  | SI | Negativo 8 |
| Q69 | - |  |  | SI | Negativo 9 |
| Q70 | - |  |  | SI | Negativo 10 |
| Q71 | - |  |  | SI | Negativo 11 |
| Q72 | - |  |  | SI | Negativo 12 |
| Q73 | - |  |  | SI | Total < 15 años |
| Q74 | - |  |  | SI | Total > 15-64 años |
| Q75 | - |  |  | SI | Total 65 y más años |
| Q76 | - |  |  | SI | Total Informados |
| Q77 | - |  |  | SI | Total Positivo |
| Q78 | - |  |  | SI | Total Negativo |
| Q79 | - |  |  | SI | Tota Prueba 1 |
| Q80 | - |  |  | SI | Tota Prueba 2 |
| Q81 | - |  |  | SI | Tota Prueba 3 |
| Q82 | - |  |  | SI | Tota Prueba 4 |
| Q83 | - |  |  | SI | Tota Prueba 5 |
| Q84 | - |  |  | SI | Tota Prueba 6 |
| Q85 | - |  |  | SI | Tota Prueba 7 |
| Q86 | - |  |  | SI | Tota Prueba 8 |
| Q87 | - |  |  | SI | Tota Prueba 9 |
| Q88 | - |  |  | SI | Tota Prueba 10 |
| Q89 | - |  |  | SI | Tota Prueba 11 |
| Q90 | - |  |  | SI | Tota Prueba 12 |
| Q92 | - |  |  | SI | Mes |
| Q93 | - |  |  | SI | Año |
| Q94 | - |  |  | SI | TOTAL |
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
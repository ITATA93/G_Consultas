# SQLUser.GLC_Acct

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contabilidad General (GL)**. Libro mayor y asientos contables.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GLCAC_RowId | bigint | PK |  | NO | - |
| GLCAC_BudFlag | varchar |  |  | SI | Budget Flag For Cash Management |
| GLCAC_Class | varchar |  |  | SI | Account Class |
| GLCAC_CoCode_DR | bigint |  | FK | SI | Des Ref to CTCO |
| GLCAC_Code | varchar |  |  | NO | Account Code |
| GLCAC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GLCAC_CreatedDate | date |  |  | SI | Created Date |
| GLCAC_CreatedTime | time |  |  | SI | Created Time |
| GLCAC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GLCAC_Desc | varchar |  |  | NO | Description |
| GLCAC_Owner | varchar |  |  | SI | Owner |
| GLCAC_RcFlag | varchar |  |  | SI | Archived Flag |
| GLCAC_Type | varchar |  |  | SI | Account Type |
| GLCAC_UpdatedDate | date |  |  | SI | Updated Date |
| GLCAC_UpdatedTime | time |  |  | SI | Updated Time |
| GLCAC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | P° Palpatoria - Brazo |
| Q02 | - |  |  | SI | P° Palpatoria - PAS |
| Q03 | - |  |  | SI | P° Palpatoria - PAD |
| Q04 | - |  |  | SI | 1° Medición - Brazo |
| Q05 | - |  |  | SI | 1° Medición - PAS |
| Q06 | - |  |  | SI | 1° Medición - PAD |
| Q07 | - |  |  | SI | 2° Medición - Brazo |
| Q08 | - |  |  | SI | 2° Medición - PAS |
| Q09 | - |  |  | SI | 2° Medición - PAD |
| Q10 | - |  |  | SI | 3° Medición - Brazo |
| Q11 | - |  |  | SI | 3° Medición - PAS |
| Q12 | - |  |  | SI | 3° Medición - PAD |
| Q13 | - |  |  | SI | 4° Medición de Pié - Brazo	 |
| Q14 | - |  |  | SI | 4° Medición de Pié - PAS |
| Q15 | - |  |  | SI | 4° Medición de Pié - PAD |
| Q16 | - |  |  | SI | Promedio Primer Perfil PAS Estabilizada	 |
| Q17 | - |  |  | SI | Promedio Primer Perfil PAD Estabilizada |
| Q18 | - |  |  | SI | Responsable Primer Perfil |
| Q19 | - |  |  | SI | Fecha Primer Perfil |
| Q20 | - |  |  | SI | 1° Medición - Brazo |
| Q21 | - |  |  | SI | 1° Medición - PAS |
| Q22 | - |  |  | SI | 1° Medición - PAD |
| Q23 | - |  |  | SI | 2° Medición - Brazo |
| Q24 | - |  |  | SI | 2° Medición - PAS |
| Q25 | - |  |  | SI | 2° Medición - PAD |
| Q26 | - |  |  | SI | 3° Medición - Brazo |
| Q27 | - |  |  | SI | 3° Medición - PAS |
| Q28 | - |  |  | SI | 3° Medición - PAD |
| Q29 | - |  |  | SI | Promedio Segundo Perfil PAS Estabilizada |
| Q30 | - |  |  | SI | Promedio Segundo Perfil PAD Estabilizada |
| Q31 | - |  |  | SI | Responsable Segundo Perfil |
| Q32 | - |  |  | SI | Fecha Segundo Perfil |
| Q33 | - |  |  | SI | 1° Medición - Brazo |
| Q34 | - |  |  | SI | 1° Medición - PAS |
| Q35 | - |  |  | SI | 1° Medición - PAD |
| Q36 | - |  |  | SI | 2° Medición - Brazo |
| Q37 | - |  |  | SI | 2° Medición - PAS |
| Q38 | - |  |  | SI | 2° Medición - PAD |
| Q39 | - |  |  | SI | 3° Medición - Brazo |
| Q40 | - |  |  | SI | 3° Medición - PAS |
| Q41 | - |  |  | SI | 3° Medición - PAD |
| Q42 | - |  |  | SI | Promedio Tercer Perfil PAS Estabilizada	 |
| Q43 | - |  |  | SI | Promedio Tercer Perfil PAD Estabilizada |
| Q44 | - |  |  | SI | Responsable Tercer Perfil |
| Q45 | - |  |  | SI | Fecha Tercer Perfil |
| Q46 | - |  |  | SI | PROMEDIO DE PERFILES DE PRESION ARTERIAL DIASTÓLIC... |
| Q47 | - |  |  | SI | PROMEDIO DE PERFILES DE PRESION ARTERIAL SISTÓLICA |
| Q48 | - |  |  | SI | RESULTADO |
| Q49 | - |  |  | SI | CONDUCTA |
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
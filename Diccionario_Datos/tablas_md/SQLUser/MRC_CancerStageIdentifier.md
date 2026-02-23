# SQLUser.MRC_CancerStageIdentifier

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANSTID_RowId | bigint | PK |  | NO | - |
| CANSTID_Code | varchar |  |  | NO | Code |
| CANSTID_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CANSTID_CreatedDate | date |  |  | SI | Created Date |
| CANSTID_CreatedTime | time |  |  | SI | Created Time |
| CANSTID_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CANSTID_DateFrom | date |  |  | SI | Date From |
| CANSTID_DateTo | date |  |  | SI | Date To |
| CANSTID_Desc | varchar |  |  | NO | Description |
| CANSTID_Owner | varchar |  |  | SI | Owner |
| CANSTID_UpdatedDate | date |  |  | SI | Updated Date |
| CANSTID_UpdatedTime | time |  |  | SI | Updated Time |
| CANSTID_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Registro de Dispositivos Instalados |
| Q02 | - |  |  | SI | Nº Bránula |
| Q03 | - |  |  | SI | Ubicaciòn |
| Q04 | - |  |  | SI | Nº días |
| Q05 | - |  |  | SI | Nº Bránula |
| Q06 | - |  |  | SI | Ubicación |
| Q07 | - |  |  | SI | Nº días |
| Q08 | - |  |  | SI | Nº Bránula |
| Q09 | - |  |  | SI | Ubicaciòn |
| Q10 | - |  |  | SI | Nº días |
| Q11 | - |  |  | SI | Nº Tubo |
| Q12 | - |  |  | SI | cm |
| Q13 | - |  |  | SI | Pº Cuf |
| Q14 | - |  |  | SI | Nº días |
| Q15 | - |  |  | SI | Nº Tubo |
| Q16 | - |  |  | SI | Nº dìas |
| Q17 | - |  |  | SI | Nº lùmenes |
| Q18 | - |  |  | SI | cm |
| Q19 | - |  |  | SI | Nº dìas |
| Q20 | - |  |  | SI | cm |
| Q21 | - |  |  | SI | Nº dìas |
| Q22 | - |  |  | SI | Ubicaciòn |
| Q23 | - |  |  | SI | Nº dìas |
| Q24 | - |  |  | SI | Nº |
| Q25 | - |  |  | SI | Ubicaciòn |
| Q26 | - |  |  | SI | Nº dìas |
| Q27 | - |  |  | SI | Nº |
| Q28 | - |  |  | SI | Ubicaciòn |
| Q29 | - |  |  | SI | Nº dìas |
| Q30 | - |  |  | SI | Nº |
| Q31 | - |  |  | SI | cc Cuf |
| Q32 | - |  |  | SI | Nº dìas |
| Q33 | - |  |  | SI | cm H2O |
| Q34 | - |  |  | SI | Nº dìas |
| Q35 | - |  |  | SI | Ubicaciòn |
| Q36 | - |  |  | SI | Nº dìas |
| Q37 | - |  |  | SI | Ubicaciòn |
| Q38 | - |  |  | SI | Nº dìas |
| Q39 | - |  |  | SI | Ubicaciòn |
| Q40 | - |  |  | SI | Nº dìas |
| Q41 | - |  |  | SI | Nº dìas |
| Q42 | - |  |  | SI | Nº |
| Q43 | - |  |  | SI | Ubicaciòn |
| Q44 | - |  |  | SI | Nº |
| Q45 | - |  |  | SI | Ubicaciòn |
| Q46 | - |  |  | SI | Cúal |
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
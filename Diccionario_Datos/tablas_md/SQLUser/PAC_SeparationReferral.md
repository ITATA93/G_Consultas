# SQLUser.PAC_SeparationReferral

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SEPREF_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Referred to appropriate specialist |
| Q04 | - |  |  | SI | Comment |
| Q05 | - |  |  | SI | Right heart catheterisation |
| Q06 | - |  |  | SI | Date completed |
| Q07 | - |  |  | SI | Comments |
| Q08 | - |  |  | SI | Computerised tomography (CT) pulmonary angiogram |
| Q09 | - |  |  | SI | Date completed |
| Q10 | - |  |  | SI | Comments |
| Q11 | - |  |  | SI | Echocardiogram |
| Q12 | - |  |  | SI | Date completed |
| Q13 | - |  |  | SI | Comments |
| Q14 | - |  |  | SI | High resolution CT chest |
| Q15 | - |  |  | SI | Date completed |
| Q16 | - |  |  | SI | Comments |
| Q17 | - |  |  | SI | Ventilation / Perfusion (VQ) scan completed |
| Q18 | - |  |  | SI | Date completed |
| Q19 | - |  |  | SI | Comments |
| Q20 | - |  |  | SI | Pulmonary function tests |
| Q21 | - |  |  | SI | Date completed |
| Q22 | - |  |  | SI | Comment |
| Q23 | - |  |  | SI | Arterial blood gas |
| Q24 | - |  |  | SI | Comments |
| Q25 | - |  |  | SI | Autoimmune screen |
| Q26 | - |  |  | SI | Comments |
| Q27 | - |  |  | SI | N-terminal prohormone of brain natriuretic peptide... |
| Q28 | - |  |  | SI | Comments |
| Q29 | - |  |  | SI | Liver function tests |
| Q30 | - |  |  | SI | Comments |
| Q31 | - |  |  | SI | Sleep study |
| Q32 | - |  |  | SI | Date completed |
| Q33 | - |  |  | SI | Comment |
| Q34 | - |  |  | SI | 6 minute walk test |
| Q35 | - |  |  | SI | Date completed |
| Q36 | - |  |  | SI | Comments |
| Q37 | - |  |  | SI | Other tests |
| Q38 | - |  |  | SI | Details of other tests |
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
| SEPREF_ACASStatus | varchar |  |  | SI | ACAS Status codes |
| SEPREF_AgeFrom | double |  |  | SI | Age From |
| SEPREF_AgeTo | double |  |  | SI | Age To |
| SEPREF_AgeType | varchar |  |  | SI | Age Type |
| SEPREF_CareType | varchar |  |  | SI | Care Type Codes |
| SEPREF_Code | varchar |  |  | SI | Code |
| SEPREF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SEPREF_CreatedDate | date |  |  | SI | Created Date |
| SEPREF_CreatedTime | time |  |  | SI | Created Time |
| SEPREF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SEPREF_DateFrom | date |  |  | SI | Date From |
| SEPREF_DateTo | date |  |  | SI | Date To |
| SEPREF_Default | varchar |  |  | SI | Default |
| SEPREF_Desc | varchar |  |  | SI | Description |
| SEPREF_DischargeType | varchar |  |  | SI | Discharge Type codes |
| SEPREF_NationCode | varchar |  |  | SI | National Code |
| SEPREF_Owner | varchar |  |  | SI | Owner |
| SEPREF_Sex | varchar |  |  | SI | Sex codes |
| SEPREF_UpdatedDate | date |  |  | SI | Updated Date |
| SEPREF_UpdatedTime | time |  |  | SI | Updated Time |
| SEPREF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
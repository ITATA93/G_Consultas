# SQLUser.FHC_MicroArea

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCMA_RowId | bigint | PK |  | NO | - |
| FHCMA_Area_DR | bigint |  | FK | SI | Des Ref to FHCArea |
| FHCMA_Code | varchar |  |  | NO | Micro Area Code |
| FHCMA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCMA_CreatedDate | date |  |  | SI | Created Date |
| FHCMA_CreatedTime | time |  |  | SI | Created Time |
| FHCMA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCMA_DateFrom | date |  |  | NO | Date From |
| FHCMA_DateTo | date |  |  | SI | Date To |
| FHCMA_Desc | varchar |  |  | NO | Micro Area Description |
| FHCMA_Hosp_DR | bigint |  | FK | SI | Des Ref to CTHospital |
| FHCMA_NationalCode | varchar |  |  | SI | National Code |
| FHCMA_Owner | varchar |  |  | SI | Owner |
| FHCMA_Questionnaire_DR | bigint |  | FK | SI | Des REf Questionnaire |
| FHCMA_UpdatedDate | date |  |  | SI | Updated Date |
| FHCMA_UpdatedTime | time |  |  | SI | Updated Time |
| FHCMA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of application |
| Q04 | - |  |  | SI | Application time in |
| Q05 | - |  |  | SI | Cast applied as per doctor's instructions |
| Q06 | - |  |  | SI | Other details |
| Q07 | - |  |  | SI | Instructions given to patient |
| Q08 | - |  |  | SI | Application time out |
| Q09 | - |  |  | SI | Application total time taken (mins) |
| Q10 | - |  |  | SI | Additional comments |
| Q11 | - |  |  | SI | Date of review / removal |
| Q12 | - |  |  | SI | Review / Removal time in |
| Q13 | - |  |  | SI | Cast review |
| Q14 | - |  |  | SI | Other cast review details |
| Q15 | - |  |  | SI | Cast condition |
| Q16 | - |  |  | SI | Cast review notes |
| Q17 | - |  |  | SI | Skin condition |
| Q18 | - |  |  | SI | Other skin condition details |
| Q19 | - |  |  | SI | Review / Removal time out |
| Q20 | - |  |  | SI | Review / Removal total time taken (mins) |
| Q21 | - |  |  | SI | Additional notes |
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
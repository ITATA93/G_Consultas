# SQLUser.CT_EditionManagement

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EDMG_RowId | bigint | PK |  | NO | - |
| EDMG_CreatedDate | date |  |  | SI | Created Date |
| EDMG_CreatedTime | time |  |  | SI | Created Time |
| EDMG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EDMG_OnceOnly | bit |  |  | SI | Release Once Only |
| EDMG_Owners | varchar |  |  | NO | Owners |
| EDMG_Remarks | varchar |  |  | SI | Remarks |
| EDMG_TableName | varchar |  |  | NO | Table Name |
| EDMG_UpdatedDate | date |  |  | SI | Updated Date |
| EDMG_UpdatedTime | time |  |  | SI | Updated Time |
| EDMG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | General information |
| Q02 | - |  |  | SI | Marital status |
| Q03 | - |  |  | SI | Number of children |
| Q04 | - |  |  | SI | Occupation |
| Q05 | - |  |  | SI | Noise exposure |
| Q06 | - |  |  | SI | Primary reason for referral |
| Q07 | - |  |  | SI | Medical history |
| Q08 | - |  |  | SI | How long have you had this problem? |
| Q09 | - |  |  | SI | Have you previously consulted an Audiologist / ENT... |
| Q10 | - |  |  | SI | When |
| Q11 | - |  |  | SI | Where |
| Q12 | - |  |  | SI | Have you had any of the following in the last 90 d... |
| Q13 | - |  |  | SI | Are (were) you regularly exposed to loud noise? |
| Q14 | - |  |  | SI | Are (were) you taking any of the following medicat... |
| Q15 | - |  |  | SI | Do (did) you have any of the following medical con... |
| Q16 | - |  |  | SI | Do you have a family history of hearing loss and/o... |
| Q17 | - |  |  | SI | Do you have an allergy towards any of the followin... |
| Q18 | - |  |  | SI | Hearing Loss and Communication |
| Q19 | - |  |  | SI | Do you have a known hearing loss? |
| Q20 | - |  |  | SI | Which ear is the better ear? |
| Q21 | - |  |  | SI | Do you currently use Hearing Aids? |
| Q22 | - |  |  | SI | Do they help? |
| Q23 | - |  |  | SI | Please specify |
| Q24 | - |  |  | SI | Does your difficulty in hearing restrict you from ... |
| Q25 | - |  |  | SI | How does your hearing difficulty affect others? (F... |
| Q26 | - |  |  | SI | Do you have a problem in the following situations? |
| Q27 | - |  |  | SI | Additional comments |
| Q28 | - |  |  | SI | Do you have known hearing loss? |
| Q29 | - |  |  | SI | Was the onset of hearing loss gradual or sudden? |
| Q30 | - |  |  | SI | Any blocked feeling / pressure inside the ear? |
| Q31 | - |  |  | SI | Any dizziness or vertigo? |
| Q32 | - |  |  | SI | Any ringing inside the ear? |
| Q33 | - |  |  | SI | Which ear? |
| Q34 | - |  |  | SI | Date |
| Q35 | - |  |  | SI | Time |
| Q36 | - |  |  | SI | Which ear is the better ear? |
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
# SQLUser.PAC_SnomedSubsetDuplTerms

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNODT_ParRef | bigint | PK |  | NO | PAC_SnomedSubset Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Any previous depression, anxiety or other mental h... |
| Q04 | - |  |  | SI | Specify treatment for any depression, anxiety or o... |
| Q05 | - |  |  | SI | Mental health notes |
| Q06 | - |  |  | SI | Have any difficult events happened to you in the p... |
| Q07 | - |  |  | SI | Difficult events notes |
| Q08 | - |  |  | SI | Is there a problem with alcohol and/or drugs in yo... |
| Q09 | - |  |  | SI | Alcohol / Drugs notes |
| Q10 | - |  |  | SI | Is your partner or someone else in the household s... |
| Q11 | - |  |  | SI | Abusive behaviour notes |
| Q12 | - |  |  | SI | Have you experienced any kind of abuse in the past... |
| Q13 | - |  |  | SI | Abuse notes |
| Q14 | - |  |  | SI | Do all of your children still live with you |
| Q15 | - |  |  | SI | Children notes |
| Q16 | - |  |  | SI | Is your home environment stressful (e.g. too many ... |
| Q17 | - |  |  | SI | Home environment notes |
| Q18 | - |  |  | SI | Are your finances reasonable, can you live within ... |
| Q19 | - |  |  | SI | Financial notes |
| Q20 | - |  |  | SI | Have you experienced any trauma in the past - misc... |
| Q21 | - |  |  | SI | Trauma notes |
| Q22 | - |  |  | SI | Do you feel pleased about being pregnant |
| Q23 | - |  |  | SI | Pregnancy pleasure notes |
| Q24 | - |  |  | SI | Are you and your partner currently together |
| Q25 | - |  |  | SI | Partner notes |
| Q26 | - |  |  | SI | Is your partner supportive of you |
| Q27 | - |  |  | SI | Supportive partner notes |
| Q28 | - |  |  | SI | Does your family and friends care about how you fe... |
| Q29 | - |  |  | SI | Family / Friends notes |
| Q30 | - |  |  | SI | Do you know where to seek help if necessary regard... |
| Q31 | - |  |  | SI | Seek help notes |
| Q32 | - |  |  | SI | Miscellaneous notes |
| Q33 | - |  |  | SI | Actions (referrals to other services, review at ne... |
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
| SNODT_Childsub | double |  |  | NO | Childsub |
| SNODT_CreatedDate | date |  |  | SI | Created Date |
| SNODT_CreatedTime | time |  |  | SI | Created Time |
| SNODT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNODT_LinkedID_DR | bigint |  | FK | SI | Des Ref SnomedConcept |
| SNODT_MemberID_DR | bigint |  | FK | SI | Des Ref SnomedConcept |
| SNODT_MemberStatus | varchar |  |  | SI | MemberStatus |
| SNODT_RowId | varchar |  |  | NO | - |
| SNODT_UpdatedDate | date |  |  | SI | Updated Date |
| SNODT_UpdatedTime | time |  |  | SI | Updated Time |
| SNODT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
# SQLUser.CT_MentalHealthACT

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHACT_RowId | bigint | PK |  | NO | - |
| MHACT_Code | varchar |  |  | NO | Code |
| MHACT_CreatedDate | date |  |  | SI | Created Date |
| MHACT_CreatedTime | time |  |  | SI | Created Time |
| MHACT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHACT_DateFrom | date |  |  | SI | DateFrom |
| MHACT_DateTo | date |  |  | SI | DateTo |
| MHACT_Desc | varchar |  |  | NO | Description |
| MHACT_UpdatedDate | date |  |  | SI | Updated Date |
| MHACT_UpdatedTime | time |  |  | SI | Updated Time |
| MHACT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Is your child having any difficulty understanding ... |
| Q02 | - |  |  | SI | Is your child responding to his/her name when call... |
| Q03 | - |  |  | SI | Is your child able to answer simple questions? |
| Q04 | - |  |  | SI | Is your child able to follow simple directions aro... |
| Q05 | - |  |  | SI | Is your child showing an interest in what you or o... |
| Q06 | - |  |  | SI | Comprehension & Expressive Language |
| Q07 | - |  |  | SI | How does your child make his/her wants known? |
| Q08 | - |  |  | SI | Is your child communicating using true words? |
| Q09 | - |  |  | SI | Is your child combining words into sentences? |
| Q10 | - |  |  | SI | Is your child communicating using combination of w... |
| Q11 | - |  |  | SI | Is your child able to express his/her thoughts cle... |
| Q12 | - |  |  | SI | Is your child experiencing any frustration communi... |
| Q13 | - |  |  | SI | Speech Development |
| Q14 | - |  |  | SI | Is your child pronouncing words clearly? |
| Q15 | - |  |  | SI | Is your child having trouble pronouncing certain s... |
| Q16 | - |  |  | SI | Do you understand what your child is saying? |
| Q17 | - |  |  | SI | Do others understand what your child is saying? |
| Q18 | - |  |  | SI | Is your child having any difficulties moving his/h... |
| Q19 | - |  |  | SI | Social Language |
| Q20 | - |  |  | SI | Does your child look at you and others during a co... |
| Q21 | - |  |  | SI | Does your child request assistance or information ... |
| Q22 | - |  |  | SI | Does your child appropriately respond to questions... |
| Q23 | - |  |  | SI | Does your child naturally imitate phrases heard in... |
| Q24 | - |  |  | SI | Does your child enjoy / avoid communicative intera... |
| Q25 | - |  |  | SI | Used to assess speech and language development in ... |
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
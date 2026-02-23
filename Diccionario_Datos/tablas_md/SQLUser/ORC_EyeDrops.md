# SQLUser.ORC_EyeDrops

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EYEDRO_RowId | bigint | PK |  | NO | - |
| EYEDRO_Code | varchar |  |  | NO | Code |
| EYEDRO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EYEDRO_CreatedDate | date |  |  | SI | Created Date |
| EYEDRO_CreatedTime | time |  |  | SI | Created Time |
| EYEDRO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EYEDRO_DateFrom | date |  |  | SI | Date From |
| EYEDRO_DateTo | date |  |  | SI | Date To |
| EYEDRO_Desc | varchar |  |  | NO | Description |
| EYEDRO_Owner | varchar |  |  | SI | Owner |
| EYEDRO_UpdatedDate | date |  |  | SI | Updated Date |
| EYEDRO_UpdatedTime | time |  |  | SI | Updated Time |
| EYEDRO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient alone for screening process |
| Q04 | - |  |  | SI | Mandatory reporting obligations explained and unde... |
| Q05 | - |  |  | SI | Privacy and confidentiality limits discussed |
| Q06 | - |  |  | SI | Explained information will be saved in their elect... |
| Q07 | - |  |  | SI | Explained, in own words, purpose of questions and ... |
| Q08 | - |  |  | SI | Please refer to Guidelines section below for detai... |
| Q09 | - |  |  | SI | Pre-screening notes |
| Q10 | - |  |  | SI | If the patient answers ''yes'' to any of the below... |
| Q11 | - |  |  | SI | For example, ask ''Would you like to talk more abo... |
| Q12 | - |  |  | SI | Within the last year has your partner, ex-partner ... |
| Q13 | - |  |  | SI | Yelled at you, talked down to you or called you ba... |
| Q14 | - |  |  | SI | Become jealous or tried to control what you do |
| Q15 | - |  |  | SI | Within the last year, have you been: |
| Q16 | - |  |  | SI | Afraid of your partner, ex-partner or anyone in yo... |
| Q17 | - |  |  | SI | Hit, kicked, punched or hurt by your partner, ex-p... |
| Q18 | - |  |  | SI | Made to have sex or have any sexual activity when ... |
| Q19 | - |  |  | SI | D&FV screening outcome |
| Q20 | - |  |  | SI | Reason for no screening |
| Q21 | - |  |  | SI | Screening outcome notes |
| Q22 | - |  |  | SI | Before screening, please explain the following con... |
| Q23 | - |  |  | SI | 1. Many people experience problems with their fami... |
| Q24 | - |  |  | SI | OR, if pregnant: |
| Q25 | - |  |  | SI | 1a. Women who are pregnant commonly experience vio... |
| Q26 | - |  |  | SI | 2. Domestic and family violence is any type of abu... |
| Q27 | - |  |  | SI | 3. Abuse does not have to be physical to be domest... |
| Q28 | - |  |  | SI | 4. It can take many forms. Examples include: |
| Q29 | - |  |  | SI | • Controlling behaviours |
| Q30 | - |  |  | SI | • Financial abuse (denying access to money) |
| Q31 | - |  |  | SI | • Emotional abuse (name calling) |
| Q32 | - |  |  | SI | • Intimidation (smashing things) |
| Q33 | - |  |  | SI | • Isolation (preventing you from having contact wi... |
| Q34 | - |  |  | SI | • Sexual abuse (forcing you to have sex, touching ... |
| Q35 | - |  |  | SI | • Spiritual abuse (putting down your culture or yo... |
| Q36 | - |  |  | SI | Explained to patient participation is voluntary |
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
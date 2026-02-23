# SQLUser.OR_AnaestIVInsertSite

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IVINSST_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| IVINSST_Childsub | double |  |  | NO | Childsub |
| IVINSST_RowId | varchar |  |  | NO | - |
| IVINSST_Site_DR | bigint |  | FK | SI | Des Ref ORCCannulaInsertionSite |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Breakfast - Requires food / eating behaviour monit... |
| Q04 | - |  |  | SI | Breakfast - Type of food offered |
| Q05 | - |  |  | SI | Breakfast - Amount of food offered |
| Q06 | - |  |  | SI | Breakfast - Amount eaten |
| Q07 | - |  |  | SI | Breakfast - Oral intake (ml) |
| Q08 | - |  |  | SI | Breakfast notes |
| Q09 | - |  |  | SI | Mid-morning - Requires food / eating behaviour mon... |
| Q10 | - |  |  | SI | Mid-morning - Type of food offered |
| Q11 | - |  |  | SI | Mid-morning - Amount of food offered |
| Q12 | - |  |  | SI | Mid-morning - Amount eaten |
| Q13 | - |  |  | SI | Mid-morning - Oral intake (ml) |
| Q14 | - |  |  | SI | Mid-morning notes |
| Q15 | - |  |  | SI | Lunch - Requires food / eating behaviour monitorin... |
| Q16 | - |  |  | SI | Lunch - Type of food offered |
| Q17 | - |  |  | SI | Lunch - Amount of food offered |
| Q18 | - |  |  | SI | Lunch - Amount eaten |
| Q19 | - |  |  | SI | Lunch - Oral intake (ml) |
| Q20 | - |  |  | SI | Lunch notes |
| Q21 | - |  |  | SI | Mid-afternoon - Requires food / eating behaviour m... |
| Q22 | - |  |  | SI | Mid-afternoon - Type of food offered |
| Q23 | - |  |  | SI | Mid-afternoon - Amount of food offered |
| Q24 | - |  |  | SI | Mid-afternoon - Amount eaten |
| Q25 | - |  |  | SI | Mid-afternoon - Oral intake (ml) |
| Q26 | - |  |  | SI | Mid-afternoon notes |
| Q27 | - |  |  | SI | Evening meal - Requires food / eating behaviour mo... |
| Q28 | - |  |  | SI | Evening meal - Type of food offered |
| Q29 | - |  |  | SI | Evening meal - Amount of food offered |
| Q30 | - |  |  | SI | Evening meal - Amount eaten |
| Q31 | - |  |  | SI | Evening meal - Oral intake (ml) |
| Q32 | - |  |  | SI | Evening meal notes |
| Q33 | - |  |  | SI | Supper - Requires food / eating behaviour monitori... |
| Q34 | - |  |  | SI | Supper - Type of food offered |
| Q35 | - |  |  | SI | Supper - Amount of food offered |
| Q36 | - |  |  | SI | Supper - Amount eaten |
| Q37 | - |  |  | SI | Supper - Oral intake (ml) |
| Q38 | - |  |  | SI | Supper notes |
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
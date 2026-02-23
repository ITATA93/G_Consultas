# SQLUser.CT_GenderPronouns

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GENPRON_RowId | bigint | PK |  | NO | - |
| GENPRON_Code | varchar |  |  | NO | Code |
| GENPRON_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GENPRON_CreatedDate | date |  |  | SI | Created Date |
| GENPRON_CreatedTime | time |  |  | SI | Created Time |
| GENPRON_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GENPRON_DateFrom | date |  |  | SI | Date From |
| GENPRON_DateTo | date |  |  | SI | Date To |
| GENPRON_Desc | varchar |  |  | NO | Description |
| GENPRON_Owner | varchar |  |  | SI | Owner |
| GENPRON_UpdatedDate | date |  |  | SI | Updated Date |
| GENPRON_UpdatedTime | time |  |  | SI | Updated Time |
| GENPRON_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Does the patient still require / want the surgery |
| Q04 | - |  |  | SI | Reason |
| Q05 | - |  |  | SI | Surgical team informed |
| Q06 | - |  |  | SI | Theatre schedulers informed |
| Q07 | - |  |  | SI | Patient allergies checked and recorded as appropri... |
| Q08 | - |  |  | SI | Any changes in condition since completion of last ... |
| Q09 | - |  |  | SI | What has changed |
| Q10 | - |  |  | SI | Notes |
| Q11 | - |  |  | SI | Is the patient currently well |
| Q12 | - |  |  | SI | Details of illness |
| Q13 | - |  |  | SI | Discussed with anaesthetist |
| Q14 | - |  |  | SI | Theatre schedulers notified and pre-admission clin... |
| Q15 | - |  |  | SI | Infection status confirmed with patient and docume... |
| Q16 | - |  |  | SI | Weight recorded and checked with patient |
| Q17 | - |  |  | SI | Schedulers informed to book day of surgery admissi... |
| Q18 | - |  |  | SI | Patient's skin is intact – free from cuts, scratch... |
| Q19 | - |  |  | SI | Skin condition notes |
| Q20 | - |  |  | SI | Patient’s medications have been confirmed |
| Q21 | - |  |  | SI | Has the patient recently started taking any new me... |
| Q22 | - |  |  | SI | Is the patient on anticoagulants |
| Q23 | - |  |  | SI | Vitamins or natural supplements have been discusse... |
| Q24 | - |  |  | SI | Transport for admission and discharge has been arr... |
| Q25 | - |  |  | SI | Somebody is available to assist with activities of... |
| Q26 | - |  |  | SI | Comment |
| Q27 | - |  |  | SI | Admission |
| Q28 | - |  |  | SI | Admission time confirmed |
| Q29 | - |  |  | SI | Expected admission date |
| Q30 | - |  |  | SI | Expected admission time |
| Q31 | - |  |  | SI | Patient informed of admission location |
| Q32 | - |  |  | SI | Morning medication discussed |
| Q33 | - |  |  | SI | Fasting time instructions given |
| Q34 | - |  |  | SI | Pre-Operative |
| Q35 | - |  |  | SI | Patient journey explained |
| Q36 | - |  |  | SI | Expected length of stay discussed |
| Q37 | - |  |  | SI | Day case |
| Q38 | - |  |  | SI | Admit full care |
| Q39 | - |  |  | SI | Patient informed waiting times are variable |
| Q40 | - |  |  | SI | Showering discussed - prior to surgery |
| Q41 | - |  |  | SI | Shaving discussed – use caution to prevent cuts |
| Q42 | - |  |  | SI | Skin care discussed - avoiding cuts etc |
| Q43 | - |  |  | SI | Nails discussed -  all nail polish and acrylic / g... |
| Q44 | - |  |  | SI | Valuables discussed - jewellery to be removed and ... |
| Q45 | - |  |  | SI | Discharge Restrictions / Requirements |
| Q46 | - |  |  | SI | Driving restriction |
| Q47 | - |  |  | SI | Lifting restriction |
| Q48 | - |  |  | SI | Post-operative visit required |
| Q49 | - |  |  | SI | Household chores restriction |
| Q50 | - |  |  | SI | Pre-prepared foods required |
| Q51 | - |  |  | SI | Responsible adult available for 24 hours for a day... |
| Q52 | - |  |  | SI | Name of responsible adult |
| Q53 | - |  |  | SI | Contact details of responsible adult |
| Q54 | - |  |  | SI | Reviewed by Nursing / Medical Staff |
| Q55 | - |  |  | SI | Suitable for anaesthetic review on day of procedur... |
| Q56 | - |  |  | SI | Requires referral to anaesthetic assessment |
| Q57 | - |  |  | SI | Patient requires specialist anaesthetic assessment |
| Q58 | - |  |  | SI | Comments |
| Q59 | - |  |  | SI | Infectious status comment |
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
# SQLUser.CT_LocOTOpenDateTime

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTOP_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| OTOP_CTLOC_DR | bigint |  | FK | NO | Theatre, Des Ref To CTLOC – can be the same as par... |
| OTOP_Childsub | double |  |  | NO | Childsub |
| OTOP_CloseDate | date |  |  | SI | Close Date  |
| OTOP_CloseTime | time |  |  | SI | Close Time  |
| OTOP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OTOP_Comment | varchar |  |  | SI | Comment |
| OTOP_CreatedDate | date |  |  | SI | Created Date |
| OTOP_CreatedTime | time |  |  | SI | Created Time |
| OTOP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OTOP_OpenDate | date |  |  | NO | Open Date |
| OTOP_OpenTime | time |  |  | SI | Open Time  |
| OTOP_RBResource_DR | bigint |  | FK | SI | OT Room, Des Ref To RBResource – when blank record... |
| OTOP_RowId | varchar |  |  | NO | - |
| OTOP_TheatreRecord | varchar |  |  | SI | Theatre date/time record |
| OTOP_UpdateDate | date |  |  | SI | Update Date  |
| OTOP_UpdateTime | time |  |  | SI | Update Time  |
| OTOP_UpdateUser_DR | bigint |  | FK | SI | Des Ref Update User |
| OTOP_UpdatedDate | date |  |  | SI | Updated Date |
| OTOP_UpdatedTime | time |  |  | SI | Updated Time |
| OTOP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02 | - |  |  | SI | Trivalent seasonal influenza vaccine |
| Q03 | - |  |  | SI | Pertussis (whooping cough) vaccine |
| Q04 | - |  |  | SI | Healthy eating in pregnancy |
| Q05 | - |  |  | SI | Folic acid |
| Q06 | - |  |  | SI | Importance of iron and best dietary sources |
| Q07 | - |  |  | SI | Vitamin D supplementation |
| Q08 | - |  |  | SI | Food safety and hygiene |
| Q09 | - |  |  | SI | Alcohol and caffeine current consumption recommend... |
| Q10 | - |  |  | SI | Previous breast feeding experiences |
| Q11 | - |  |  | SI | BCG vaccination |
| Q12 | - |  |  | SI | Common pregnancy symptoms |
| Q13 | - |  |  | SI | Exercise |
| Q14 | - |  |  | SI | HIV |
| Q15 | - |  |  | SI | Parenting classes |
| Q16 | - |  |  | SI | Sex in pregnancy |
| Q17 | - |  |  | SI | Other topics |
| Q18 | - |  |  | SI | Details |
| Q19 | - |  |  | SI | Eligible for Health Start |
| Q20 | - |  |  | SI | Accessed vitamin supplements |
| Q21 | - |  |  | SI | Screening tests for you and your baby |
| Q22 | - |  |  | SI | Amniocentesis |
| Q23 | - |  |  | SI | Birth choices after a caesarian section |
| Q24 | - |  |  | SI | Birth place choice |
| Q25 | - |  |  | SI | Domestic abuse |
| Q26 | - |  |  | SI | Folic acid - what all women should know |
| Q27 | - |  |  | SI | FSA - eating while you are pregnant |
| Q28 | - |  |  | SI | Home birth |
| Q29 | - |  |  | SI | Breast feeding - off to the best start |
| Q30 | - |  |  | SI | Other leaflets given |
| Q31 | - |  |  | SI | Details |
| Q32 | - |  |  | SI | Medical examination by your GP |
| Q33 | - |  |  | SI | Has a referral been made for GP medical examinatio... |
| Q34 | - |  |  | SI | Certificate of pregnancy FW8 |
| Q35 | - |  |  | SI | Certificate of expected confinement MatB1 |
| Q36 | - |  |  | SI | Maternity allowances |
| Q37 | - |  |  | SI | Other |
| Q38 | - |  |  | SI | Details |
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
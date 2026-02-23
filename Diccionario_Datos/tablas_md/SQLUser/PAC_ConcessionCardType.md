# SQLUser.PAC_ConcessionCardType

**Schema:** SQLUser
**Columnas:** 152
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONCCARD_RowId | bigint | PK |  | NO | - |
| CONCCARD_Code | varchar |  |  | NO | Code |
| CONCCARD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONCCARD_CreatedDate | date |  |  | SI | Created Date |
| CONCCARD_CreatedTime | time |  |  | SI | Created Time |
| CONCCARD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONCCARD_DateFrom | date |  |  | SI | Date From |
| CONCCARD_DateTo | date |  |  | SI | Date To |
| CONCCARD_Desc | varchar |  |  | NO | Description |
| CONCCARD_Owner | varchar |  |  | SI | Owner |
| CONCCARD_UpdatedDate | date |  |  | SI | Updated Date |
| CONCCARD_UpdatedTime | time |  |  | SI | Updated Time |
| CONCCARD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Donor name |
| Q04 | - |  |  | SI | Donor MRN |
| Q05 | - |  |  | SI | ABO (blood group) |
| Q06 | - |  |  | SI | Donor type |
| Q07 | - |  |  | SI | Drugs administered |
| Q08 | - |  |  | SI | Kidney |
| Q09 | - |  |  | SI | Cross clamp (deceased) date |
| Q10 | - |  |  | SI | Cross clamp (deceased) time |
| Q11 | - |  |  | SI | Arterial clamp (living) date |
| Q12 | - |  |  | SI | Arterial clamp (living) time |
| Q13 | - |  |  | SI | Warm ischemia total start date |
| Q14 | - |  |  | SI | Warm ischemia total start time |
| Q15 | - |  |  | SI | Warm ischemia total end date |
| Q17 | - |  |  | SI | Warm ischemia total end time |
| Q18 | - |  |  | SI | Initial perfusion solution (deceased) |
| Q19 | - |  |  | SI | Expiration date |
| Q20 | - |  |  | SI | Lot number |
| Q21 | - |  |  | SI | Start date |
| Q22 | - |  |  | SI | Start time |
| Q23 | - |  |  | SI | End date |
| Q24 | - |  |  | SI | End time |
| Q25 | - |  |  | SI | Volume |
| Q26 | - |  |  | SI | Quality of perfusion |
| Q27 | - |  |  | SI | Back Table Perfusion Solution |
| Q28 | - |  |  | SI | Expiration date |
| Q29 | - |  |  | SI | Lot number |
| Q30 | - |  |  | SI | Start date |
| Q31 | - |  |  | SI | Start time |
| Q32 | - |  |  | SI | End date |
| Q33 | - |  |  | SI | End time |
| Q34 | - |  |  | SI | Volume |
| Q35 | - |  |  | SI | Quality of perfusion |
| Q36 | - |  |  | SI | Kidney Storage Solution |
| Q37 | - |  |  | SI | Volume |
| Q38 | - |  |  | SI | Expiration date |
| Q39 | - |  |  | SI | Lot number |
| Q40 | - |  |  | SI | Kidney weight (gm) |
| Q41 | - |  |  | SI | Kidney length (cm) |
| Q42 | - |  |  | SI | Kidney ventral-dorsal dimension |
| Q43 | - |  |  | SI | Number of renal arteries |
| Q44 | - |  |  | SI | Number of renal veins |
| Q45 | - |  |  | SI | Number of ureters |
| Q46 | - |  |  | SI | Ureters length |
| Q47 | - |  |  | SI | Kidney general description |
| Q48 | - |  |  | SI | Kidney biopsy |
| Q49 | - |  |  | SI | Prepared for implantation |
| Q50 | - |  |  | SI | Prepared for implantation start date |
| Q51 | - |  |  | SI | Prepared for implantation start time |
| Q52 | - |  |  | SI | Prepared for implantation end date |
| Q53 | - |  |  | SI | Prepared for implantation end time |
| Q54 | - |  |  | SI | Preparing surgeon |
| Q55 | - |  |  | SI | Life port used |
| Q56 | - |  |  | SI | Transplant surgeon's name |
| Q57 | - |  |  | SI | Comments |
| Q58 | - |  |  | SI | Donor coordinator / nurse name |
| Q59 | - |  |  | SI | Signature |
| Q59UDt | - |  |  | SI | Signature Last Updated Date |
| Q59UTm | - |  |  | SI | Signature Last Updated Time |
| Q60 | - |  |  | SI | Assessment date |
| Q61 | - |  |  | SI | Assessment time |
| Q62 | - |  |  | SI | Recipient name |
| Q63 | - |  |  | SI | Recipient MRN |
| Q64 | - |  |  | SI | ABO (blood group) |
| Q65 | - |  |  | SI | ABO (blood group) |
| Q66 | - |  |  | SI | Kidney implanted in iliac fossa |
| Q67 | - |  |  | SI | Kidney out in ice date |
| Q68 | - |  |  | SI | Kidney out in ice time |
| Q69 | - |  |  | SI | Renal vein anastomosis total start date |
| Q70 | - |  |  | SI | Renal vein anastomosis total start time |
| Q71 | - |  |  | SI | Renal vein anastomosis total end date |
| Q72 | - |  |  | SI | Renal vein anastomosis total end time |
| Q73 | - |  |  | SI | Renal artery anastomosis start date |
| Q74 | - |  |  | SI | Renal artery anastomosis start time |
| Q75 | - |  |  | SI | Renal artery anastomosis end date |
| Q76 | - |  |  | SI | Renal artery anastomosis end time |
| Q77 | - |  |  | SI | Artery un-clamped date |
| Q78 | - |  |  | SI | Artery un-clamped time |
| Q79 | - |  |  | SI | Cold ischemia time |
| Q80 | - |  |  | SI | Warm ischemia time |
| Q81 | - |  |  | SI | Total ischemia time |
| Q82 | - |  |  | SI | Transplant surgeon |
| Q83 | - |  |  | SI | Comments |
| Q84 | - |  |  | SI | Time out process for blood group |
| Q85 | - |  |  | SI | Time out process for tissue match |
| Q86 | - |  |  | SI | Donor coordinator / nurse name |
| Q87 | - |  |  | SI | Signature |
| Q87UDt | - |  |  | SI | Signature Last Updated Date |
| Q87UTm | - |  |  | SI | Signature Last Updated Time |
| Q88 | - |  |  | SI | Assessment date |
| Q89 | - |  |  | SI | Assessment time |
| Q90 | - |  |  | SI | Please attach report in documents |
| Q91 | - |  |  | SI | Donor coordinator / nurse name |
| Q92 | - |  |  | SI | Donor coordinator / nurse name |
| Q93 | - |  |  | SI | Donor coordinator / nurse name |
| Q94 | - |  |  | SI | Donor coordinator / nurse name |
| Q95 | - |  |  | SI | Transplant surgeon |
| Q96 | - |  |  | SI | Transplant surgeon |
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
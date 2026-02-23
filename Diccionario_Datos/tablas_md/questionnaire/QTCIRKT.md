# questionnaire.QTCIRKT

> Intraoperative Record for Kidney Transplant

**Schema:** questionnaire
**Columnas:** 140
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intraoperative Record for Kidney Transplant

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Donor name |
| Q04 | varchar |  |  | SI | Donor MRN |
| Q05 | varchar |  |  | SI | ABO (blood group) |
| Q06 | varchar |  |  | SI | Donor type |
| Q07 | varchar |  |  | SI | Drugs administered |
| Q08 | varchar |  |  | SI | Kidney |
| Q09 | date |  |  | SI | Cross clamp (deceased) date |
| Q10 | time |  |  | SI | Cross clamp (deceased) time |
| Q11 | date |  |  | SI | Arterial clamp (living) date |
| Q12 | time |  |  | SI | Arterial clamp (living) time |
| Q13 | date |  |  | SI | Warm ischemia total start date |
| Q14 | time |  |  | SI | Warm ischemia total start time |
| Q15 | date |  |  | SI | Warm ischemia total end date |
| Q17 | time |  |  | SI | Warm ischemia total end time |
| Q18 | varchar |  |  | SI | Initial perfusion solution (deceased) |
| Q19 | date |  |  | SI | Expiration date |
| Q20 | varchar |  |  | SI | Lot number |
| Q21 | date |  |  | SI | Start date |
| Q22 | time |  |  | SI | Start time |
| Q23 | date |  |  | SI | End date |
| Q24 | time |  |  | SI | End time |
| Q25 | numeric |  |  | SI | Volume |
| Q26 | varchar |  |  | SI | Quality of perfusion |
| Q27 | varchar |  |  | SI | Back Table Perfusion Solution |
| Q28 | date |  |  | SI | Expiration date |
| Q29 | varchar |  |  | SI | Lot number |
| Q30 | date |  |  | SI | Start date |
| Q31 | time |  |  | SI | Start time |
| Q32 | date |  |  | SI | End date |
| Q33 | time |  |  | SI | End time |
| Q34 | numeric |  |  | SI | Volume |
| Q35 | varchar |  |  | SI | Quality of perfusion |
| Q36 | varchar |  |  | SI | Kidney Storage Solution |
| Q37 | numeric |  |  | SI | Volume |
| Q38 | date |  |  | SI | Expiration date |
| Q39 | varchar |  |  | SI | Lot number |
| Q40 | numeric |  |  | SI | Kidney weight (gm) |
| Q41 | numeric |  |  | SI | Kidney length (cm) |
| Q42 | varchar |  |  | SI | Kidney ventral-dorsal dimension |
| Q43 | numeric |  |  | SI | Number of renal arteries |
| Q44 | numeric |  |  | SI | Number of renal veins |
| Q45 | numeric |  |  | SI | Number of ureters |
| Q46 | numeric |  |  | SI | Ureters length |
| Q47 | varchar |  |  | SI | Kidney general description |
| Q48 | varchar |  |  | SI | Kidney biopsy |
| Q49 | varchar |  |  | SI | Prepared for implantation |
| Q50 | date |  |  | SI | Prepared for implantation start date |
| Q51 | time |  |  | SI | Prepared for implantation start time |
| Q52 | date |  |  | SI | Prepared for implantation end date |
| Q53 | time |  |  | SI | Prepared for implantation end time |
| Q54 | varchar |  |  | SI | Preparing surgeon |
| Q55 | varchar |  |  | SI | Life port used |
| Q56 | varchar |  |  | SI | Transplant surgeon's name |
| Q57 | varchar |  |  | SI | Comments |
| Q58 | varchar |  |  | SI | Donor coordinator / nurse name |
| Q59 | longvarbinary |  |  | SI | Signature |
| Q59UDt | date |  |  | SI | Signature Last Updated Date |
| Q59UTm | time |  |  | SI | Signature Last Updated Time |
| Q60 | date |  |  | SI | Assessment date |
| Q61 | time |  |  | SI | Assessment time |
| Q62 | varchar |  |  | SI | Recipient name |
| Q63 | varchar |  |  | SI | Recipient MRN |
| Q64 | varchar |  |  | SI | ABO (blood group) |
| Q65 | varchar |  |  | SI | ABO (blood group) |
| Q66 | varchar |  |  | SI | Kidney implanted in iliac fossa |
| Q67 | date |  |  | SI | Kidney out in ice date |
| Q68 | time |  |  | SI | Kidney out in ice time |
| Q69 | date |  |  | SI | Renal vein anastomosis total start date |
| Q70 | time |  |  | SI | Renal vein anastomosis total start time |
| Q71 | date |  |  | SI | Renal vein anastomosis total end date |
| Q72 | time |  |  | SI | Renal vein anastomosis total end time |
| Q73 | date |  |  | SI | Renal artery anastomosis start date |
| Q74 | time |  |  | SI | Renal artery anastomosis start time |
| Q75 | date |  |  | SI | Renal artery anastomosis end date |
| Q76 | time |  |  | SI | Renal artery anastomosis end time |
| Q77 | date |  |  | SI | Artery un-clamped date |
| Q78 | time |  |  | SI | Artery un-clamped time |
| Q79 | time |  |  | SI | Cold ischemia time |
| Q80 | time |  |  | SI | Warm ischemia time |
| Q81 | time |  |  | SI | Total ischemia time |
| Q82 | varchar |  |  | SI | Transplant surgeon |
| Q83 | varchar |  |  | SI | Comments |
| Q84 | varchar |  |  | SI | Time out process for blood group |
| Q85 | varchar |  |  | SI | Time out process for tissue match |
| Q86 | varchar |  |  | SI | Donor coordinator / nurse name |
| Q87 | longvarbinary |  |  | SI | Signature |
| Q87UDt | date |  |  | SI | Signature Last Updated Date |
| Q87UTm | time |  |  | SI | Signature Last Updated Time |
| Q88 | date |  |  | SI | Assessment date |
| Q89 | time |  |  | SI | Assessment time |
| Q90 | varchar |  |  | SI | Please attach report in documents |
| Q91 | varchar |  |  | SI | Donor coordinator / nurse name |
| Q92 | varchar |  |  | SI | Donor coordinator / nurse name |
| Q93 | varchar |  |  | SI | Donor coordinator / nurse name |
| Q94 | varchar |  |  | SI | Donor coordinator / nurse name |
| Q95 | varchar |  |  | SI | Transplant surgeon |
| Q96 | varchar |  |  | SI | Transplant surgeon |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
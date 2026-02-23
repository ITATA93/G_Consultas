# questionnaire.QTCIVAL

> Intravascular Access Lines

**Schema:** questionnaire
**Columnas:** 140
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intravascular Access Lines

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | IntraVascular Access Type	 |
| Q02 | varchar |  |  | SI | Central IV Activity	 |
| Q03 | varchar |  |  | SI | Central IV Procedure Type	 |
| Q04 | varchar |  |  | SI | Central IV Access Type	 |
| Q05 | varchar |  |  | SI | Central IV Number Of Lumens	 |
| Q06 | varchar |  |  | SI | Central IV Location	 |
| Q07 | varchar |  |  | SI | Central IV Site	 |
| Q08 | varchar |  |  | SI | Central IV Catheter Size	 |
| Q09 | varchar |  |  | SI | Central IV Patient Identified	 |
| Q10 | date |  |  | SI | Date of Insertion	 |
| Q102 | varchar |  |  | SI | Peripheral IV Condition	 |
| Q103 | numeric |  |  | SI | Peripheral IV Extravasation Score	 |
| Q104 | numeric |  |  | SI | Peripheral IV Infiltration Score	 |
| Q105 | numeric |  |  | SI | Peripheral IV Phlebitis Score	 |
| Q107 | varchar |  |  | SI | Peripheral IV Equipment used	 |
| Q108 | date |  |  | SI | Peripheral IV Removal Date	 |
| Q109 | time |  |  | SI | Peripheral IV Removal Time	 |
| Q11 | time |  |  | SI | Time of Insertion	 |
| Q110 | varchar |  |  | SI | Peripheral Removal Indication	 |
| Q111 | varchar |  |  | SI | Referred To IV Nurse	 |
| Q112 | varchar |  |  | SI | Peripheral IV Site	 |
| Q113 | varchar |  |  | SI | Central IV Present, Date Of Insertion	 |
| Q114 | date |  |  | SI | Central IV Known, Date Of Insertion	 |
| Q115 | varchar |  |  | SI | Other |
| Q116 | varchar |  |  | SI | Others |
| Q119 | varchar |  |  | SI | Peripheral IV Procedure Result	 |
| Q12 | varchar |  |  | SI | Central IV Reason For Insertion	 |
| Q120 | varchar |  |  | SI | Lumen color |
| Q13 | varchar |  |  | SI | CVC Insertion Unit	 |
| Q14 | varchar |  |  | SI | Central Guided Ultrasound Used	 |
| Q15 | varchar |  |  | SI | Central IV Radiographic Confirmation	 |
| Q16 | varchar |  |  | SI | CVC Antibiotic Coated Used	 |
| Q17 | varchar |  |  | SI | Central IV Performing Provider	 |
| Q18 | varchar |  |  | SI | Central IV Procedure Result	 |
| Q19 | numeric |  |  | SI | Central IV Number Of Attempts	 |
| Q20 | varchar |  |  | SI | Central IV Procedure Preparation	 |
| Q21 | varchar |  |  | SI | Central IV Sterile Field	 |
| Q22 | varchar |  |  | SI | Central IV MBP Compliance	 |
| Q23 | varchar |  |  | SI | Central IV Non Compliant MBP	 |
| Q31 | varchar |  |  | SI | Central IV Catheter Tip Confirmation	 |
| Q333 | varchar |  |  | SI | empty |
| Q38 | date |  |  | SI | Discontinue Date	 |
| Q39 | time |  |  | SI | Discontinue Time	 |
| Q40 | varchar |  |  | SI | Central IV Removal Reason	 |
| Q41 | varchar |  |  | SI | Central IV Removal Result	 |
| Q42 | numeric |  |  | SI | Central IV Direct Pressure Duration	 |
| Q43 | varchar |  |  | SI | Central IV Catheter Tunnel	 |
| Q44 | varchar |  |  | SI | Central IV Tunnel Exit Site/Port Pocket	 |
| Q45 | varchar |  |  | SI | Central IV Port Needle Type	 |
| Q46 | varchar |  |  | SI | Central IV Accessing Port	 |
| Q47 | varchar |  |  | SI | Central IV Accessing Port Reason	 |
| Q48 | varchar |  |  | SI | Tunnel Catheter Anchor Suture Removed	 |
| Q50 | varchar |  |  | SI | CVC Unit Transferred To	 |
| Q51 | varchar |  |  | SI | Arterial Line Activity	 |
| Q52 | varchar |  |  | SI | Arterial Line Procedure Type	 |
| Q53 | varchar |  |  | SI | Arterial Line Location	 |
| Q54 | varchar |  |  | SI | Arterial Line Site	 |
| Q55 | varchar |  |  | SI | Arterial Line Catheter Size	 |
| Q56 | numeric |  |  | SI | Arterial Line Catheter Length	 |
| Q57 | date |  |  | SI | Arterial Line Insertion Date	 |
| Q58 | time |  |  | SI | Arterial Line Insertion Time	 |
| Q59 | varchar |  |  | SI | A-Line Present, Date Of Insertion	 |
| Q60 | date |  |  | SI | A-Line Known, Date Of Insertion	 |
| Q61 | varchar |  |  | SI | Arterial Line Patient Identified	 |
| Q62 | varchar |  |  | SI | Arterial Line Procedure Preparation	 |
| Q63 | varchar |  |  | SI | Arterial Line Sterile Field	 |
| Q64 | varchar |  |  | SI | Arterial Line MBP Compliance	 |
| Q65 | varchar |  |  | SI | Arterial Line Non Compliant MBP	 |
| Q66 | varchar |  |  | SI | Arterial Line Performing Insertion	 |
| Q67 | varchar |  |  | SI | Arterial Line Assisting In Insertion	 |
| Q69 | varchar |  |  | SI | Arterial Line Care / Troubleshoot	 |
| Q70 | varchar |  |  | SI | Arterial Line Site Care	 |
| Q71 | varchar |  |  | SI | Arterial Line Site Condition	 |
| Q72 | varchar |  |  | SI | Arterial Line Dressing Condition	 |
| Q73 | varchar |  |  | SI | Arterial Line Dressing	 |
| Q74 | varchar |  |  | SI | Arterial Line Drainage Present	 |
| Q75 | varchar |  |  | SI | Arterial Line Drainage Description	 |
| Q76 | varchar |  |  | SI | AL Unexpected Events	 |
| Q77 | varchar |  |  | SI | Arterial Line Procedure Result |
| Q78 | varchar |  |  | SI | Arterial Line Collateral Flow Assured	 |
| Q79 | varchar |  |  | SI | Arterial Line Allen Test	 |
| Q80 | date |  |  | SI | Arterial Line Discontinue Date	 |
| Q81 | time |  |  | SI | Arterial Line Discontinue Time	 |
| Q82 | varchar |  |  | SI | Arterial Line Removal Reason	 |
| Q83 | varchar |  |  | SI | Arterial Line Removal Result	 |
| Q84 | numeric |  |  | SI | Arterial Line Direct Pressure Duration	 |
| Q85 | varchar |  |  | SI | Peripheral IV Activity	 |
| Q86 | date |  |  | SI | Peripheral IV Insertion Date	 |
| Q87 | time |  |  | SI | Peripheral IV Insertion Time	 |
| Q88 | varchar |  |  | SI | Peripheral IV Known, Date Of Insertion	 |
| Q89 | date |  |  | SI | Peripheral IV Known Date Of Insertion	 |
| Q90 | varchar |  |  | SI | Peripheral IV Catheter Type	 |
| Q91 | varchar |  |  | SI | Peripheral IV Location	 |
| Q92 | varchar |  |  | SI | Peripheral IV Gauge	 |
| Q93 | varchar |  |  | SI | Peripheral IV Procedure Preparation	 |
| Q94 | varchar |  |  | SI | Peripheral IV Insertion Indication	 |
| Q95 | numeric |  |  | SI | Peripheral IV Number Of Attempts	 |
| Q98 | varchar |  |  | SI | Peripheral IV Drainage Present	 |
| Q99 | varchar |  |  | SI | Peripheral IV Drainage Description	 |
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
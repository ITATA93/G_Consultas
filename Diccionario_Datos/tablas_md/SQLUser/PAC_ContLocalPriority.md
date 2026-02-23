# SQLUser.PAC_ContLocalPriority

**Schema:** SQLUser
**Columnas:** 153
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOCPR_RowId | bigint | PK |  | NO | - |
| ChildQ117DR | - |  |  | SI | Child Reference: CVC Site Assesst	 |
| LOCPR_Code | varchar |  |  | NO | Code |
| LOCPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOCPR_CreatedDate | date |  |  | SI | Created Date |
| LOCPR_CreatedTime | time |  |  | SI | Created Time |
| LOCPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOCPR_DateFrom | date |  |  | SI | Date From |
| LOCPR_DateTo | date |  |  | SI | Date To |
| LOCPR_Desc | varchar |  |  | NO | Description |
| LOCPR_Owner | varchar |  |  | SI | Owner |
| LOCPR_UpdatedDate | date |  |  | SI | Updated Date |
| LOCPR_UpdatedTime | time |  |  | SI | Updated Time |
| LOCPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | IntraVascular Access Type	 |
| Q02 | - |  |  | SI | Central IV Activity	 |
| Q03 | - |  |  | SI | Central IV Procedure Type	 |
| Q04 | - |  |  | SI | Central IV Access Type	 |
| Q05 | - |  |  | SI | Central IV Number Of Lumens	 |
| Q06 | - |  |  | SI | Central IV Location	 |
| Q07 | - |  |  | SI | Central IV Site	 |
| Q08 | - |  |  | SI | Central IV Catheter Size	 |
| Q09 | - |  |  | SI | Central IV Patient Identified	 |
| Q10 | - |  |  | SI | Date of Insertion	 |
| Q102 | - |  |  | SI | Peripheral IV Condition	 |
| Q103 | - |  |  | SI | Peripheral IV Extravasation Score	 |
| Q104 | - |  |  | SI | Peripheral IV Infiltration Score	 |
| Q105 | - |  |  | SI | Peripheral IV Phlebitis Score	 |
| Q107 | - |  |  | SI | Peripheral IV Equipment used	 |
| Q108 | - |  |  | SI | Peripheral IV Removal Date	 |
| Q109 | - |  |  | SI | Peripheral IV Removal Time	 |
| Q11 | - |  |  | SI | Time of Insertion	 |
| Q110 | - |  |  | SI | Peripheral Removal Indication	 |
| Q111 | - |  |  | SI | Referred To IV Nurse	 |
| Q112 | - |  |  | SI | Peripheral IV Site	 |
| Q113 | - |  |  | SI | Central IV Present, Date Of Insertion	 |
| Q114 | - |  |  | SI | Central IV Known, Date Of Insertion	 |
| Q115 | - |  |  | SI | Other |
| Q116 | - |  |  | SI | Others |
| Q119 | - |  |  | SI | Peripheral IV Procedure Result	 |
| Q12 | - |  |  | SI | Central IV Reason For Insertion	 |
| Q120 | - |  |  | SI | Lumen color |
| Q13 | - |  |  | SI | CVC Insertion Unit	 |
| Q14 | - |  |  | SI | Central Guided Ultrasound Used	 |
| Q15 | - |  |  | SI | Central IV Radiographic Confirmation	 |
| Q16 | - |  |  | SI | CVC Antibiotic Coated Used	 |
| Q17 | - |  |  | SI | Central IV Performing Provider	 |
| Q18 | - |  |  | SI | Central IV Procedure Result	 |
| Q19 | - |  |  | SI | Central IV Number Of Attempts	 |
| Q20 | - |  |  | SI | Central IV Procedure Preparation	 |
| Q21 | - |  |  | SI | Central IV Sterile Field	 |
| Q22 | - |  |  | SI | Central IV MBP Compliance	 |
| Q23 | - |  |  | SI | Central IV Non Compliant MBP	 |
| Q31 | - |  |  | SI | Central IV Catheter Tip Confirmation	 |
| Q333 | - |  |  | SI | empty |
| Q38 | - |  |  | SI | Discontinue Date	 |
| Q39 | - |  |  | SI | Discontinue Time	 |
| Q40 | - |  |  | SI | Central IV Removal Reason	 |
| Q41 | - |  |  | SI | Central IV Removal Result	 |
| Q42 | - |  |  | SI | Central IV Direct Pressure Duration	 |
| Q43 | - |  |  | SI | Central IV Catheter Tunnel	 |
| Q44 | - |  |  | SI | Central IV Tunnel Exit Site/Port Pocket	 |
| Q45 | - |  |  | SI | Central IV Port Needle Type	 |
| Q46 | - |  |  | SI | Central IV Accessing Port	 |
| Q47 | - |  |  | SI | Central IV Accessing Port Reason	 |
| Q48 | - |  |  | SI | Tunnel Catheter Anchor Suture Removed	 |
| Q50 | - |  |  | SI | CVC Unit Transferred To	 |
| Q51 | - |  |  | SI | Arterial Line Activity	 |
| Q52 | - |  |  | SI | Arterial Line Procedure Type	 |
| Q53 | - |  |  | SI | Arterial Line Location	 |
| Q54 | - |  |  | SI | Arterial Line Site	 |
| Q55 | - |  |  | SI | Arterial Line Catheter Size	 |
| Q56 | - |  |  | SI | Arterial Line Catheter Length	 |
| Q57 | - |  |  | SI | Arterial Line Insertion Date	 |
| Q58 | - |  |  | SI | Arterial Line Insertion Time	 |
| Q59 | - |  |  | SI | A-Line Present, Date Of Insertion	 |
| Q60 | - |  |  | SI | A-Line Known, Date Of Insertion	 |
| Q61 | - |  |  | SI | Arterial Line Patient Identified	 |
| Q62 | - |  |  | SI | Arterial Line Procedure Preparation	 |
| Q63 | - |  |  | SI | Arterial Line Sterile Field	 |
| Q64 | - |  |  | SI | Arterial Line MBP Compliance	 |
| Q65 | - |  |  | SI | Arterial Line Non Compliant MBP	 |
| Q66 | - |  |  | SI | Arterial Line Performing Insertion	 |
| Q67 | - |  |  | SI | Arterial Line Assisting In Insertion	 |
| Q69 | - |  |  | SI | Arterial Line Care / Troubleshoot	 |
| Q70 | - |  |  | SI | Arterial Line Site Care	 |
| Q71 | - |  |  | SI | Arterial Line Site Condition	 |
| Q72 | - |  |  | SI | Arterial Line Dressing Condition	 |
| Q73 | - |  |  | SI | Arterial Line Dressing	 |
| Q74 | - |  |  | SI | Arterial Line Drainage Present	 |
| Q75 | - |  |  | SI | Arterial Line Drainage Description	 |
| Q76 | - |  |  | SI | AL Unexpected Events	 |
| Q77 | - |  |  | SI | Arterial Line Procedure Result |
| Q78 | - |  |  | SI | Arterial Line Collateral Flow Assured	 |
| Q79 | - |  |  | SI | Arterial Line Allen Test	 |
| Q80 | - |  |  | SI | Arterial Line Discontinue Date	 |
| Q81 | - |  |  | SI | Arterial Line Discontinue Time	 |
| Q82 | - |  |  | SI | Arterial Line Removal Reason	 |
| Q83 | - |  |  | SI | Arterial Line Removal Result	 |
| Q84 | - |  |  | SI | Arterial Line Direct Pressure Duration	 |
| Q85 | - |  |  | SI | Peripheral IV Activity	 |
| Q86 | - |  |  | SI | Peripheral IV Insertion Date	 |
| Q87 | - |  |  | SI | Peripheral IV Insertion Time	 |
| Q88 | - |  |  | SI | Peripheral IV Known, Date Of Insertion	 |
| Q89 | - |  |  | SI | Peripheral IV Known Date Of Insertion	 |
| Q90 | - |  |  | SI | Peripheral IV Catheter Type	 |
| Q91 | - |  |  | SI | Peripheral IV Location	 |
| Q92 | - |  |  | SI | Peripheral IV Gauge	 |
| Q93 | - |  |  | SI | Peripheral IV Procedure Preparation	 |
| Q94 | - |  |  | SI | Peripheral IV Insertion Indication	 |
| Q95 | - |  |  | SI | Peripheral IV Number Of Attempts	 |
| Q98 | - |  |  | SI | Peripheral IV Drainage Present	 |
| Q99 | - |  |  | SI | Peripheral IV Drainage Description	 |
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
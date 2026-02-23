# SQLUser.OEC_OrdCatPregnBrFdAlert

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBA_ParRef | bigint | PK |  | NO | OEC_OrderCategory Parent Reference |
| ChildQ05DR | - |  |  | SI | Child Reference: PARR Table |
| PBA_Childsub | double |  |  | NO | Childsub |
| PBA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBA_CreatedDate | date |  |  | SI | Created Date |
| PBA_CreatedTime | time |  |  | SI | Created Time |
| PBA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBA_DateFrom | date |  |  | SI | DateFrom |
| PBA_DateTo | date |  |  | SI | DateTo |
| PBA_Message | varchar |  |  | SI | Message |
| PBA_Options | varchar |  |  | SI | Options |
| PBA_RowId | varchar |  |  | NO | - |
| PBA_UpdatedDate | date |  |  | SI | Updated Date |
| PBA_UpdatedTime | time |  |  | SI | Updated Time |
| PBA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Ultrasound - start |
| Q02 | - |  |  | SI | Ultrasound - finish |
| Q03 | - |  |  | SI | VER/ERG - start |
| Q04 | - |  |  | SI | VER/ERG - finsh |
| Q06 | - |  |  | SI | Photos - start |
| Q07 | - |  |  | SI | Photos - finish |
| Q08 | - |  |  | SI | CT Scan/MRI - start |
| Q09 | - |  |  | SI | CT Scan/MRI - finish |
| Q10 | - |  |  | SI | Contact Lens Fitting - start |
| Q11 | - |  |  | SI | Contact Lens Fitting - finish |
| Q12 | - |  |  | SI | EUS |
| Q13 | - |  |  | SI | Slit lamp |
| Q14 | - |  |  | SI | Suture removal |
| Q15 | - |  |  | SI | Fundus exam |
| Q16 | - |  |  | SI | Intraocular pressure |
| Q17 | - |  |  | SI | Refraction |
| Q18 | - |  |  | SI | Other |
| Q19 | - |  |  | SI | Number of previous Sedations |
| Q20 | - |  |  | SI | Previous Failed Sedations |
| Q21 | - |  |  | SI | NPO - Milk / Solids |
| Q22 | - |  |  | SI | NPO - Fluids |
| Q23 | - |  |  | SI | Not applicable |
| Q24 | - |  |  | SI | NPO Breast Milk |
| Q25 | - |  |  | SI | Ramsay Sedation Scale |
| Q26 | - |  |  | SI | Post Anaesthesia Recovery Score for Ambulatory Pat... |
| Q27 | - |  |  | SI | Instructions: to enter data , fill in the fields, ... |
| Q28 | - |  |  | SI | Sign out time |
| Q29 | - |  |  | SI | Date |
| Q30 | - |  |  | SI | Follow Up Apointment Given |
| Q31 | - |  |  | SI | Medication instructions |
| Q32 | - |  |  | SI | Removal of Eye pad |
| Q33 | - |  |  | SI | Feeding instructions |
| Q34 | - |  |  | SI | Discharge destination |
| Q35 | - |  |  | SI | ASA level |
| Q36 | - |  |  | SI | NPO Breast milk |
| Q37 | - |  |  | SI | Given to and verbalised by (name) |
| Q38 | - |  |  | SI | Relationship |
| Q39 | - |  |  | SI | Mode of transport |
| Q40 | - |  |  | SI | Notes |
| Q41 | - |  |  | SI | Sedation History |
| Q42 | - |  |  | SI | Fasting |
| Q43 | - |  |  | SI | Start time |
| Q44 | - |  |  | SI | Finish time |
| Q45 | - |  |  | SI | Ultrasound |
| Q46 | - |  |  | SI | VER / ERG |
| Q47 | - |  |  | SI | Photos |
| Q48 | - |  |  | SI | CT Scan / MRI |
| Q49 | - |  |  | SI | Contact lens fitting |
| Q50 | - |  |  | SI | NPO - Breast Milk |
| Q51 | - |  |  | SI | Notes |
| Q52 | - |  |  | SI | Ultrasound |
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
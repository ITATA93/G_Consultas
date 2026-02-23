# SQLUser.MR_EncEntry

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ENTRY_RowId | bigint | PK |  | NO | - |
| ENTRY_CareProvType_DR | bigint |  | FK | SI | User/CareProvider's type at the time of entry's cr... |
| ENTRY_ClinicalSpecialty_DR | bigint |  | FK | SI | - |
| ENTRY_Deleted | bit |  |  | SI | Shows if Entry has been deleted because it has bee... |
| ENTRY_DeletedDate | date |  |  | SI | Date entry was deleted |
| ENTRY_DeletedTime | time |  |  | SI | Time entry was deleted |
| ENTRY_DeletedUser_DR | bigint |  | FK | SI | User who deleted the Entry  |
| ENTRY_Encounter_DR | bigint |  | FK | SI | - |
| ENTRY_EndDate | date |  |  | SI | - |
| ENTRY_EndTime | time |  |  | SI | - |
| ENTRY_EntryType_DR | bigint |  | FK | SI | - |
| ENTRY_Locked | bit |  |  | SI | - |
| ENTRY_StartDate | date |  |  | SI | - |
| ENTRY_StartLocation_DR | bigint |  | FK | SI | - |
| ENTRY_StartTime | time |  |  | SI | - |
| ENTRY_StartUser_DR | bigint |  | FK | SI | - |
| Q01 | - |  |  | SI | Red blood cells |
| Q01ObsDR | - |  |  | SI | Red blood cells DR |
| Q02 | - |  |  | SI | Haemoglobin |
| Q02ObsDR | - |  |  | SI | Haemoglobin DR |
| Q03 | - |  |  | SI | Hematocrit |
| Q03ObsDR | - |  |  | SI | Hematocrit DR |
| Q04 | - |  |  | SI | Platelets |
| Q04ObsDR | - |  |  | SI | Platelets DR |
| Q05 | - |  |  | SI | Potassium (K+) |
| Q05ObsDR | - |  |  | SI | Potassium (K+) DR |
| Q06 | - |  |  | SI | Sodium (Na+) |
| Q06ObsDR | - |  |  | SI | Sodium (Na+) DR |
| Q07 | - |  |  | SI | Glycemia |
| Q07ObsDR | - |  |  | SI | Glycemia DR |
| Q08 | - |  |  | SI | Activated partial thromboplastin time (aPTT) contr... |
| Q08ObsDR | - |  |  | SI | Activated partial thromboplastin time (aPTT) contr... |
| Q09 | - |  |  | SI | Urea |
| Q09ObsDR | - |  |  | SI | Urea DR |
| Q10 | - |  |  | SI | Prothrombin time (PT) control / patient |
| Q10ObsDR | - |  |  | SI | Prothrombin time (PT) control / patient DR |
| Q11 | - |  |  | SI | Creatinine |
| Q11ObsDR | - |  |  | SI | Creatinine DR |
| Q12 | - |  |  | SI | aPTT |
| Q12ObsDR | - |  |  | SI | aPTT DR |
| Q13 | - |  |  | SI | Prothrombin time / International normalized ratio ... |
| Q13ObsDR | - |  |  | SI | Prothrombin time / International normalized ratio ... |
| Q14 | - |  |  | SI | Electrocardiogram |
| Q15 | - |  |  | SI | Thorax X Ray |
| Q16 | - |  |  | SI | Observation |
| Q17 | - |  |  | SI | Mallampati |
| Q18 | - |  |  | SI | American Society of Anaesthesiologists (ASA) physi... |
| Q19 | - |  |  | SI | Mouth opening |
| Q20 | - |  |  | SI | Thyromental distance |
| Q21 | - |  |  | SI | Cervical mobility |
| Q22 | - |  |  | SI | Mandibular protrusion |
| Q23 | - |  |  | SI | Airway |
| Q24 | - |  |  | SI | Additional tests |
| Q25 | - |  |  | SI | Comments |
| Q26 | - |  |  | SI | Red blood cells comment |
| Q27 | - |  |  | SI | Haemoglobin comment |
| Q28 | - |  |  | SI | Hematocrit |
| Q29 | - |  |  | SI | Platelets comment |
| Q30 | - |  |  | SI | aPTT control / patient comment |
| Q31 | - |  |  | SI | PT control / patient comment |
| Q32 | - |  |  | SI | aPTT comment |
| Q33 | - |  |  | SI | K+ comment |
| Q34 | - |  |  | SI | Na+ comment |
| Q35 | - |  |  | SI | Glycemia comment |
| Q36 | - |  |  | SI | Urea comment |
| Q37 | - |  |  | SI | Creatinine comment |
| Q38 | - |  |  | SI | PT/INR comment |
| Q39 | - |  |  | SI | Date |
| Q40 | - |  |  | SI | Time |
| Q41 | - |  |  | SI | and comments |
| Q42 | - |  |  | SI | Patient fully consented |
| Q43 | - |  |  | SI | Comments |
| Q44 | - |  |  | SI | Mallampati |
| Q45 | - |  |  | SI | Intubation grade |
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
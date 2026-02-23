# SQLUser.IN_Manufacture_OrderINCI

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCI_ParRef | bigint | PK |  | NO | IN_Manufacture_Order Parent Reference |
| ChildQ25DR | - |  |  | SI | Child Reference: Treatment |
| INCI_Childsub | double |  |  | NO | Childsub |
| INCI_DoseQty | varchar |  |  | SI | DoseQty |
| INCI_DoseUOM_DR | bigint |  | FK | SI | Des Ref DoseUOM |
| INCI_INCI_DR | bigint |  | FK | SI | Des Ref INCI |
| INCI_Qty | double |  |  | SI | Qty |
| INCI_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date of Referral |
| Q02 | - |  |  | SI | Referring Physician |
| Q03 | - |  |  | SI | Referral |
| Q04 | - |  |  | SI | Symptoms |
| Q05 | - |  |  | SI | Smear (General) |
| Q06 | - |  |  | SI | Smear (Specific) |
| Q07 | - |  |  | SI | Smear (Specific) Other |
| Q08 | - |  |  | SI | Gravida |
| Q09 | - |  |  | SI | Para |
| Q10 | - |  |  | SI | Age 1st Pregnancy |
| Q11 | - |  |  | SI | Gross Appearance |
| Q12 | - |  |  | SI | Contraception |
| Q13 | - |  |  | SI | Contraception Other |
| Q14 | - |  |  | SI | Clinical Indications Comments |
| Q15 | - |  |  | SI | Date of Report |
| Q16 | - |  |  | SI | Cytology |
| Q17 | - |  |  | SI | Other Comments |
| Q18 | - |  |  | SI | Diagnosis |
| Q19 | - |  |  | SI | Abnormal Features |
| Q20 | - |  |  | SI | Colposcopy Diagram |
| Q21 | - |  |  | SI | Pregnant Months |
| Q22 | - |  |  | SI | Extent of Lesion |
| Q23 | - |  |  | SI | Recommended Treatment |
| Q24 | - |  |  | SI | Recommended Treatment Other |
| Q26 | - |  |  | SI | Treatment Comments |
| Q27 | - |  |  | SI | Treatment Date |
| Q28 | - |  |  | SI | Pregnancy History |
| Q29 | - |  |  | SI | Referral Details |
| Q30 | - |  |  | SI | Colposcopy |
| Q31 | - |  |  | SI | Directed Biopsy |
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
# SQLUser.INC_ItmRegNoAudit

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCIRNA_ParRef | varchar | PK |  | NO | Par Ref to INCItmRegNo |
| INCIRNA_AdminQty | double |  |  | SI | Administered Quantity |
| INCIRNA_ChildSub | numeric |  |  | NO | Childsub |
| INCIRNA_CollectedQty | double |  |  | SI | Collected Quantity |
| INCIRNA_Date | date |  |  | SI | Entry Date |
| INCIRNA_ManufBatch_DR | varchar |  | FK | SI | Des Ref to INCItmLcBt for Admixture Manufacture ba... |
| INCIRNA_OEOrdExec_DR | varchar |  | FK | SI | Des Ref to OEOrdExec |
| INCIRNA_OEOrdItem_DR | varchar |  | FK | SI | Des Ref to OEOrdItem |
| INCIRNA_PackedQty | double |  |  | SI | Packed Quantity |
| INCIRNA_RowId | varchar |  |  | NO | - |
| INCIRNA_Time | time |  |  | SI | Entry Time |
| Q01 | - |  |  | SI | Where has the patient had treatment? |
| Q02 | - |  |  | SI | Has the patient called before? |
| Q03 | - |  |  | SI | If yes, when? |
| Q04 | - |  |  | SI | Person calling |
| Q05 | - |  |  | SI | Telephone number |
| Q06 | - |  |  | SI | Date of call |
| Q07 | - |  |  | SI | Time of call |
| Q08 | - |  |  | SI | Duration of call |
| Q09 | - |  |  | SI | Presenting problem |
| Q10 | - |  |  | SI | Please ask the patient if they have any of the fol... |
| Q11 | - |  |  | SI | Diarrhoea |
| Q12 | - |  |  | SI | Central Venous Catheter (CVC) in situ |
| Q13 | - |  |  | SI | Nausea and vomiting |
| Q14 | - |  |  | SI | Constipation |
| Q15 | - |  |  | SI | Shaking and shivering |
| Q16 | - |  |  | SI | Raised temperature |
| Q17 | - |  |  | SI | Sore throat / mouth |
| Q18 | - |  |  | SI | Flu-like symptoms |
| Q19 | - |  |  | SI | Bleeding |
| Q20 | - |  |  | SI | If the answer to any of the above is YES, please r... |
| Q21 | - |  |  | SI | Temp more than 36°C |
| Q22 | - |  |  | SI | Persistent headache |
| Q23 | - |  |  | SI | Other signs of infection. e.g. cellulitis / wound |
| Q24 | - |  |  | SI | MRSA screen |
| Q25 | - |  |  | SI | Advice given |
| Q26 | - |  |  | SI | MRSA screen |
| Q27 | - |  |  | SI | Temp more than 36°C |
| Q28 | - |  |  | SI | Check against known UK / overseas list areas of co... |
| Q29 | - |  |  | SI | Multidisciplinary assessment / treatment plan |
| Q30 | - |  |  | SI | Date |
| Q31 | - |  |  | SI | Time |
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
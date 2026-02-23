# SQLUser.ORC_OperationPartialKeywords

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPPARTKEYW_ParRef | bigint | PK |  | NO | ORC_Operation Parent Reference |
| OPPARTKEYW_Childsub | double |  |  | NO | Childsub |
| OPPARTKEYW_RowId | varchar |  |  | NO | - |
| OPPARTKEYW_Text | varchar |  |  | SI | Partial Keyword |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Pertinent health issues / concerns have been discu... |
| Q11 | - |  |  | SI | Inclusion and Exclusion Criteria |
| Q12 | - |  |  | SI | Inclusion criteria |
| Q13 | - |  |  | SI | Exclusion criteria |
| Q14 | - |  |  | SI | Signatures |
| Q15 | - |  |  | SI | Nurse |
| Q16 | - |  |  | SI | If any of the exclusion criteria have been selecte... |
| Q17 | - |  |  | SI | Name |
| Q18 | - |  |  | SI | Signature |
| Q18UDt | - |  |  | SI | Signature Last Updated Date |
| Q18UTm | - |  |  | SI | Signature Last Updated Time |
| Q19 | - |  |  | SI | Date |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Doctor |
| Q21 | - |  |  | SI | Notes |
| Q22 | - |  |  | SI | Name |
| Q23 | - |  |  | SI | Signature |
| Q23UDt | - |  |  | SI | Signature Last Updated Date |
| Q23UTm | - |  |  | SI | Signature Last Updated Time |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Blood and Bag Samples (As per Doctor's Orders) |
| Q26 | - |  |  | SI | Pre-procedure |
| Q27 | - |  |  | SI | During procedure |
| Q28 | - |  |  | SI | Post procedure |
| Q29 | - |  |  | SI | Bag: Pre-photoactivation |
| Q3 | - |  |  | SI | ECP session number |
| Q30 | - |  |  | SI | Bag: Post photoactivation |
| Q31 | - |  |  | SI | Notes |
| Q32 | - |  |  | SI | Nurse |
| Q33 | - |  |  | SI | Signature |
| Q33UDt | - |  |  | SI | Signature Last Updated Date |
| Q33UTm | - |  |  | SI | Signature Last Updated Time |
| Q34 | - |  |  | SI | Date |
| Q35 | - |  |  | SI | Doctor |
| Q36 | - |  |  | SI | Signature |
| Q36UDt | - |  |  | SI | Signature Last Updated Date |
| Q36UTm | - |  |  | SI | Signature Last Updated Time |
| Q37 | - |  |  | SI | Date |
| Q5 | - |  |  | SI | Documentation Checklist |
| Q6 | - |  |  | SI | Dermatology clearance |
| Q7 | - |  |  | SI | Hematology clearance |
| Q8 | - |  |  | SI | Other relevant clearance(s) given |
| Q9 | - |  |  | SI | Evaluation |
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
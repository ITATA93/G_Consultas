# SQLUser.PAC_PointOfClosureEpisType

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPIS_ParRef | bigint | PK |  | NO | PAC_PointOfClosure Parent Reference |
| EPIS_Childsub | double |  |  | NO | Childsub |
| EPIS_CreatedDate | date |  |  | SI | Created Date |
| EPIS_CreatedTime | time |  |  | SI | Created Time |
| EPIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPIS_EpisSubType_DR | bigint |  | FK | SI | Des Ref to PACEpisodeSubType |
| EPIS_EpisodeType | varchar |  |  | NO | EpisodeType |
| EPIS_Rowid | varchar |  |  | NO | - |
| EPIS_UpdatedDate | date |  |  | SI | Updated Date |
| EPIS_UpdatedTime | time |  |  | SI | Updated Time |
| EPIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Procedure |
| Q02 | - |  |  | SI | Methicillin-sensitive Staphylococcus aureus (MSSA) |
| Q03 | - |  |  | SI | Methicillin-resistant Staphylococcus aureus (MRSA) |
| Q04 | - |  |  | SI | Clostridium difficile (Cdiff) |
| Q05 | - |  |  | SI | Severe acute respiratory syndrome (SARS) |
| Q06 | - |  |  | SI | Creutzfeldt-Jakob disease (CJD) |
| Q07 | - |  |  | SI | Carbapenemase-producing Enterobacteriaceae (CPE) |
| Q08 | - |  |  | SI | Other infections |
| Q09 | - |  |  | SI | Other specify |
| Q10 | - |  |  | SI | High risk infection |
| Q11 | - |  |  | SI | Date |
| Q12 | - |  |  | SI | Time |
| Q13 | - |  |  | SI | Has the patient been screened for MRSA? |
| Q14 | - |  |  | SI | Is the patient MRSA positive or known to have a hi... |
| Q15 | - |  |  | SI | If ‘Yes’ has antimicrobial and antiseptic skin cle... |
| Q16 | - |  |  | SI | Are wound or skin lesions securely covered? |
| Q17 | - |  |  | SI | Specify |
| Q18 | - |  |  | SI | Has a transmissible spongiform encephalopathy risk... |
| Q19 | - |  |  | SI | There should be a record that the patient has been... |
| Q20 | - |  |  | SI | Is there a record of the patients answer? |
| Q21 | - |  |  | SI | If the patient has answered ‘YES’ to the question,... |
| Q22 | - |  |  | SI | For further advice regarding the need for any addi... |
| Q23 | - |  |  | SI | Additional information |
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
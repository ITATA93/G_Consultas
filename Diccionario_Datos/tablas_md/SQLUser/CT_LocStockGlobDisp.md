# SQLUser.CT_LocStockGlobDisp

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STGD_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient category |
| Q04 | - |  |  | SI | Antibiotic allergies and prophylaxis plan |
| Q05 | - |  |  | SI | Vaccinations |
| Q06 | - |  |  | SI | Pneumococcal vaccination up to date |
| Q07 | - |  |  | SI | Meningococcal vaccination up to date |
| Q08 | - |  |  | SI | Haemophilus influenza type b vaccination up to dat... |
| Q09 | - |  |  | SI | Influenza vaccination up to date |
| Q10 | - |  |  | SI | Vaccination notes |
| Q11 | - |  |  | SI | Patient Education |
| Q12 | - |  |  | SI | Emergency plan |
| Q13 | - |  |  | SI | Patient has received education on the risk of seps... |
| Q14 | - |  |  | SI | Fact sheets given |
| Q15 | - |  |  | SI | Patient carries an alert card or bracelet |
| Q16 | - |  |  | SI | Patient education notes |
| Q17 | - |  |  | SI | Date of last pneumococcal vaccination |
| Q18 | - |  |  | SI | Date of last meningococcal vaccination |
| Q19 | - |  |  | SI | Date of last Haemophilus influenza type B vaccinat... |
| Q20 | - |  |  | SI | Date of last influenza vaccination |
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
| STGD_Childsub | double |  |  | NO | Childsub |
| STGD_CodeTableTags | varchar |  |  | SI | - |
| STGD_CreatedDate | date |  |  | SI | Created Date |
| STGD_CreatedTime | time |  |  | SI | Created Time |
| STGD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STGD_DateFrom | date |  |  | SI | Effective date for the record |
| STGD_DateTo | date |  |  | SI | Last day the record is active  |
| STGD_INCItm_DR | bigint |  | FK | SI | Des Ref INCItm |
| STGD_RowId | varchar |  |  | NO | - |
| STGD_UpdatedDate | date |  |  | SI | Updated Date |
| STGD_UpdatedTime | time |  |  | SI | Updated Time |
| STGD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
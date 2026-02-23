# SQLUser.LBC_AntibioticPanelItem

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCAPI_ParRef | bigint | PK |  | NO | LBC_AntibioticPanel Parent Reference |
| LBCAPI_Antibiotic_DR | bigint |  | FK | SI | Des Ref Antibiotics |
| LBCAPI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCAPI_DateFrom | date |  |  | SI | Date From |
| LBCAPI_DateTo | date |  |  | SI | Date To |
| LBCAPI_Reported | varchar |  |  | SI | Reported |
| LBCAPI_RowID | varchar |  |  | NO | - |
| LBCAPI_Sequence | double |  |  | SI | Sequence |
| Q01 | - |  |  | SI | Diagnosis Contact Lens |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Type / Brand |
| Q04 | - |  |  | SI | Right Eye |
| Q05 | - |  |  | SI | Left Eye |
| Q07 | - |  |  | SI | BC |
| Q08 | - |  |  | SI | bc 2 |
| Q09 | - |  |  | SI | Power |
| Q10 | - |  |  | SI | Power 2 |
| Q11 | - |  |  | SI | Diameter |
| Q12 | - |  |  | SI | Diameter 2 |
| Q13 | - |  |  | SI | Optic zone |
| Q14 | - |  |  | SI | Optic zone 2 |
| Q15 | - |  |  | SI | Design |
| Q16 | - |  |  | SI | design 2 |
| Q17 | - |  |  | SI | Tint |
| Q18 | - |  |  | SI | tint 2 |
| Q200 | - |  |  | SI | Notes |
| Q201 | - |  |  | SI | Notes |
| Q202 | - |  |  | SI | Contact Lens image |
| Q21 | - |  |  | SI | Material |
| Q22 | - |  |  | SI | Material 2 |
| Q25 | - |  |  | SI | Notes |
| Q26 | - |  |  | SI | Final Contact Lens Prescription |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Type / Brand |
| Q29 | - |  |  | SI | Right Eye |
| Q30 | - |  |  | SI | Left Eye |
| Q32 | - |  |  | SI | BC |
| Q33 | - |  |  | SI | bc2 |
| Q34 | - |  |  | SI | Power |
| Q35 | - |  |  | SI | power 2 |
| Q36 | - |  |  | SI | Diameter |
| Q37 | - |  |  | SI | diaeter 2 |
| Q38 | - |  |  | SI | Optic zone |
| Q39 | - |  |  | SI | optic zone 2 |
| Q40 | - |  |  | SI | Design |
| Q41 | - |  |  | SI | design 2 |
| Q42 | - |  |  | SI | Tint |
| Q43 | - |  |  | SI | tint 2 |
| Q44 | - |  |  | SI | Cosmetic Contact Lens |
| Q45 | - |  |  | SI | Iris colour |
| Q46 | - |  |  | SI | Iris diameter |
| Q47 | - |  |  | SI | VA-Nr 3 |
| Q48 | - |  |  | SI | Material |
| Q49 | - |  |  | SI | Material 2 |
| Q50 | - |  |  | SI | Opaque |
| Q51 | - |  |  | SI | Pupil |
| Q52 | - |  |  | SI | Pupil size |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
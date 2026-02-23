# SQLUser.PAC_VacDeclineReason

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VACDECR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Attended since last visit	 |
| Q02 | - |  |  | SI | Outcome |
| Q03 | - |  |  | SI | Medication or device change |
| Q04 | - |  |  | SI | Date of Medication or Device change	 |
| Q05 | - |  |  | SI | Medication or Device change by	 |
| Q06 | - |  |  | SI | Other |
| Q07 | - |  |  | SI | Nebuliser |
| Q08 | - |  |  | SI | Other |
| Q09 | - |  |  | SI | Ever ventilated	 |
| Q10 | - |  |  | SI | Ventilated year	 |
| Q11 | - |  |  | SI | Ventilated information	 |
| Q12 | - |  |  | SI | Triggers |
| Q13 | - |  |  | SI |  Other	 |
| Q14 | - |  |  | SI | Nocturnal symptoms	 |
| Q15 | - |  |  | SI | Nocturnal symptom notes	 |
| Q16 | - |  |  | SI | Daytime symptoms	 |
| Q17 | - |  |  | SI | Daytime symptom notes	 |
| Q18 | - |  |  | SI | Affected daily activities	 |
| Q19 | - |  |  | SI | Affected daily activities notes	 |
| Q20 | - |  |  | SI | Emergency advice given	 |
| Q21 | - |  |  | SI | Previous Self Management Plan	 |
| Q22 | - |  |  | SI | Was the Self Management Plan reviewed today	 |
| Q23 | - |  |  | SI | Inhaler technique	 |
| Q24 | - |  |  | SI | Oxygen |
| Q25 | - |  |  | SI | Oxygen type	 |
| Q26 | - |  |  | SI | Walking |
| Q27 | - |  |  | SI | Climbing stairs	 |
| Q28 | - |  |  | SI | Social circumstances	 |
| Q29 | - |  |  | SI | Other social circumstances	 |
| Q30 | - |  |  | SI | Notes |
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
| VACDECR_Code | varchar |  |  | NO | Code |
| VACDECR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VACDECR_CreatedDate | date |  |  | SI | Created Date |
| VACDECR_CreatedTime | time |  |  | SI | Created Time |
| VACDECR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VACDECR_DateFrom | date |  |  | SI | Date From |
| VACDECR_DateTo | date |  |  | SI | Date To |
| VACDECR_Desc | varchar |  |  | NO | Description |
| VACDECR_Owner | varchar |  |  | SI | Owner |
| VACDECR_UpdatedDate | date |  |  | SI | Updated Date |
| VACDECR_UpdatedTime | time |  |  | SI | Updated Time |
| VACDECR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
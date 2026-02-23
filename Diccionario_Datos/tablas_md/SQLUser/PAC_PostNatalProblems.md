# SQLUser.PAC_PostNatalProblems

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| POSPRO_RowId | bigint | PK |  | NO | - |
| POSPRO_Code | varchar |  |  | NO | Code |
| POSPRO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| POSPRO_CreatedDate | date |  |  | SI | Created Date |
| POSPRO_CreatedTime | time |  |  | SI | Created Time |
| POSPRO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| POSPRO_DateFrom | date |  |  | SI | - |
| POSPRO_DateTo | date |  |  | SI | Date To |
| POSPRO_Desc | varchar |  |  | NO | Description |
| POSPRO_Owner | varchar |  |  | SI | Owner |
| POSPRO_UpdatedDate | date |  |  | SI | Updated Date |
| POSPRO_UpdatedTime | time |  |  | SI | Updated Time |
| POSPRO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Procedure |
| Q02 | - |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q03 | - |  |  | SI | Contact lenses / glasses with patient - Leaving Wa... |
| Q04 | - |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q05 | - |  |  | SI | Dentures - Leaving Ward |
| Q06 | - |  |  | SI | Hearing aid with patient - Leaving Ward |
| Q07 | - |  |  | SI | Slippers - Leaving Ward |
| Q08 | - |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q09 | - |  |  | SI | Contact lenses / glasses with patient - Theatre Re... |
| Q10 | - |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q11 | - |  |  | SI | Dentures - Theatre Reception |
| Q12 | - |  |  | SI | Hearing aid with patient - Theatre Reception |
| Q13 | - |  |  | SI | Slippers - Theatre Reception |
| Q14 | - |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q15 | - |  |  | SI | Contact lenses / glasses with patient - Anaestheti... |
| Q16 | - |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q17 | - |  |  | SI | Dentures - Anaesthetic Room |
| Q18 | - |  |  | SI | Hearing aid with patient - Anaesthetic Room |
| Q19 | - |  |  | SI | Slippers - Anaesthetic Room |
| Q20 | - |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q21 | - |  |  | SI | Contact lenses / glasses with patient - Leaving Ro... |
| Q22 | - |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q23 | - |  |  | SI | Dentures - Leaving Room |
| Q24 | - |  |  | SI | Hearing aid with patient - Leaving Room |
| Q25 | - |  |  | SI | Slippers - Leaving Room |
| Q26 | - |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q27 | - |  |  | SI | Contact lenses / glasses with patient |
| Q28 | - |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q29 | - |  |  | SI | Dentures |
| Q30 | - |  |  | SI | Hearing aid with patient |
| Q31 | - |  |  | SI | Slippers |
| Q32 | - |  |  | SI | Leaving Ward |
| Q33 | - |  |  | SI | Arrival in Theatre Reception |
| Q34 | - |  |  | SI | Arrival in Anaesthetic Room |
| Q35 | - |  |  | SI | Leaving Recovery |
| Q36 | - |  |  | SI | Notes |
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
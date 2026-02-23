# SQLUser.LBC_Superset

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSS_RowID | bigint | PK |  | NO | - |
| LBCSS_AllowSelection | varchar |  |  | SI | Allow Selection
Allow user to select the test set... |
| LBCSS_Code | varchar |  |  | NO | Code |
| LBCSS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSS_CreatedDate | date |  |  | SI | Created Date |
| LBCSS_CreatedTime | time |  |  | SI | Created Time |
| LBCSS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSS_DateFrom | date |  |  | SI | Date From
Effective date for the record |
| LBCSS_DateTo | date |  |  | SI | Date To
Last day the record is active  |
| LBCSS_Desc | varchar |  |  | NO | Description |
| LBCSS_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCSS_Owner | varchar |  |  | SI | Owner |
| LBCSS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Via Aerea |
| Q02 | - |  |  | SI | Via Aerea 2 |
| Q03 | - |  |  | SI | Comentarios Ventilación |
| Q04 | - |  |  | SI | Vía Aérea Difícil |
| Q05 | - |  |  | SI | Observaciones/Complicaciones |
| Q06 | - |  |  | SI | Intubación |
| Q07 | - |  |  | SI | Mallampati |
| Q08 | - |  |  | SI | Diámetro TET |
| Q09 | - |  |  | SI | TET con CUff |
| Q10 | - |  |  | SI | ¿TET con cuff? |
| Q11 | - |  |  | SI | ANANO |
| Q12 | - |  |  | SI | Escala de Cormack - Lehane (Laringoscopía) |
| Q13 | - |  |  | SI | Tamponamiento |
| Q14 | - |  |  | SI | Vía Aérea Difícil |
| Q15 | - |  |  | SI | N° Máscara Laríngea |
| Q16 | - |  |  | SI | N° Tubo Endotraqueal (TET) |
| Q17 | - |  |  | SI | Ventilación Difícil |
| Q18 | - |  |  | SI | Intubacion&nbsp |
| Q19 | - |  |  | SI | Cánula Mayo |
| Q20 | - |  |  | SI | Dilatador de goma elástica |
| Q21 | - |  |  | SI | Máscara Facial |
| Q22 | - |  |  | SI | Otro |
| Q23 | - |  |  | SI | Máscara Laríngea |
| Q24 | - |  |  | SI | Tubo Endotraqueal (TET) |
| Q25 | - |  |  | SI | Otro |
| Q26 | - |  |  | SI | Obs Máscara |
| Q27 | - |  |  | SI | Obs Tubo |
| Q28 | - |  |  | SI | Comentarios Vía Aérea |
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
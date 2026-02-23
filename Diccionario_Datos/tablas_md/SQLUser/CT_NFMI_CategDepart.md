# SQLUser.CT_NFMI_CategDepart

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEP_ParRef | bigint | PK |  | NO | CT_NFMI_Category Parent Reference |
| DEP_Childsub | double |  |  | NO | Childsub |
| DEP_Code | varchar |  |  | NO | Code |
| DEP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEP_CreatedDate | date |  |  | SI | Created Date |
| DEP_CreatedTime | time |  |  | SI | Created Time |
| DEP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEP_DateFrom | date |  |  | SI | DateFrom |
| DEP_DateTo | date |  |  | SI | DateTo |
| DEP_Desc | varchar |  |  | NO | Description |
| DEP_Priority | double |  |  | SI | Priority |
| DEP_RowId | varchar |  |  | NO | - |
| DEP_UpdatedDate | date |  |  | SI | Updated Date |
| DEP_UpdatedTime | time |  |  | SI | Updated Time |
| DEP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Lateralisation |
| Q04 | - |  |  | SI | Lift of tongue |
| Q05 | - |  |  | SI | Extension of tongue |
| Q06 | - |  |  | SI | Spread of anterior tongue |
| Q07 | - |  |  | SI | Cupping of tongue |
| Q08 | - |  |  | SI | Peristalsis |
| Q09 | - |  |  | SI | Function Items Score |
| Q10 | - |  |  | SI | Appearance of tongue when lifted |
| Q11 | - |  |  | SI | Length of lingual frenulum when tongue lifted |
| Q12 | - |  |  | SI | Attachment of lingual frenulum to inferior  alveol... |
| Q13 | - |  |  | SI | Elasticity of frenulum |
| Q14 | - |  |  | SI | Attachment of lingual frenulum to tongue |
| Q15 | - |  |  | SI | Appearance Score |
| Q16 | - |  |  | SI | Scoring / Frenotomy Decision Rule |
| Q17 | - |  |  | SI | • 14 = Perfect Function score regardless of Appear... |
| Q18 | - |  |  | SI | • 11 = Acceptable Function score only if Appearanc... |
| Q19 | - |  |  | SI | • < 11 = Function Score indicates function impaire... |
| Q20 | - |  |  | SI | • Hazelbaker AK. Assessment tool for lingual frenu... |
| Q21 | - |  |  | SI | Snap back |
| Q22 | - |  |  | SI | Documents the assessment of the frenulum function ... |
| Q23 | - |  |  | SI | The ATLFF™© remains the only valid and reliable to... |
| Q24 | - |  |  | SI | Total Score |
| Q25 | - |  |  | SI | Function Items Score |
| Q26 | - |  |  | SI | Appearance Score |
| Q27 | - |  |  | SI | 14 = Perfect Function score regardless of Appearan... |
| Q28 | - |  |  | SI | 11 = Acceptable Function score only if Appearance ... |
| Q29 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q30 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q31 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q32 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q33 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q34 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q35 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q36 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q37 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q38 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q39 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q40 | - |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q41 | - |  |  | SI | Hazelbaker AK. Assessment tool for lingual frenulu... |
| Q42 | - |  |  | SI | Documents the assessment of the frenulum function ... |
| Q43 | - |  |  | SI | Appearance Items Score |
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
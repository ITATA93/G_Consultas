# SQLUser.CT_SexualOrientation

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Sexo**. Valores: M, F, I.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SEXOR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Problems associated with loss of function / body c... |
| Q01TxtOnly | - |  |  | SI | Problems associated with loss of function / body c... |
| Q02 | - |  |  | SI | Concern about the disease: |
| Q03 | - |  |  | SI | Acceptance |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Acceptance DR |
| Q05 | - |  |  | SI | Anxiety |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Anxiety DR |
| Q07 | - |  |  | SI | Aggression |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Aggression DR |
| Q09 | - |  |  | SI | Agitation |
| Q09N | - |  |  | SI | Note |
| Q09ObsDR | - |  |  | SI | Agitation DR |
| Q11 | - |  |  | SI | Depression |
| Q11N | - |  |  | SI | Note |
| Q11ObsDR | - |  |  | SI | Depression DR |
| Q13 | - |  |  | SI | Crying |
| Q13N | - |  |  | SI | Note |
| Q13ObsDR | - |  |  | SI | Crying DR |
| Q15 | - |  |  | SI | Religion related |
| Q15ObsDR | - |  |  | SI | Religion related DR |
| Q16 | - |  |  | SI | Notes and rules observed by culture or religion |
| Q16TxtOnly | - |  |  | SI | Notes and rules observed by culture or religion Pl... |
| Q17 | - |  |  | SI | Values and Beliefs |
| Q18 | - |  |  | SI | Perception |
| Q19 | - |  |  | SI | Family / Relationship Concerns	 |
| Q20 | - |  |  | SI | Action taken	 |
| Q21 | - |  |  | SI | Date |
| Q22 | - |  |  | SI | Emotional Concerns or other difficult thoughts and... |
| Q23 | - |  |  | SI | Action taken	 |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Spiritual, religious or cultural beliefs, practice... |
| Q26 | - |  |  | SI | Action taken	 |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Would you like to talk to the hospital chaplain ab... |
| Q29 | - |  |  | SI | Comment |
| Q30 | - |  |  | SI | Date |
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
| SEXOR_Code | varchar |  |  | NO | Code |
| SEXOR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SEXOR_CreatedDate | date |  |  | SI | Created Date |
| SEXOR_CreatedTime | time |  |  | SI | Created Time |
| SEXOR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SEXOR_DateFrom | date |  |  | SI | Date From |
| SEXOR_DateTo | date |  |  | SI | Date To |
| SEXOR_Desc | varchar |  |  | NO | Description |
| SEXOR_NationalCode | varchar |  |  | SI | National Code |
| SEXOR_Owner | varchar |  |  | SI | Owner |
| SEXOR_UpdatedDate | date |  |  | SI | Updated Date |
| SEXOR_UpdatedTime | time |  |  | SI | Updated Time |
| SEXOR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
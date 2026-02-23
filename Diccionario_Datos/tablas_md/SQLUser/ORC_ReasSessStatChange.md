# SQLUser.ORC_ReasSessStatChange

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RSSTATCH_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | What happens during the seizure (seizure semiology... |
| Q02 | - |  |  | SI | (Aura) or warning or unusual feeling at the onset ... |
| Q03 | - |  |  | SI | Type of aura |
| Q04 | - |  |  | SI | Note |
| Q05 | - |  |  | SI | Motor Features |
| Q06 | - |  |  | SI | Type of movement |
| Q07 | - |  |  | SI | Note |
| Q08 | - |  |  | SI | Distribution of movement |
| Q09 | - |  |  | SI | Type |
| Q10 | - |  |  | SI | Distribution |
| Q11 | - |  |  | SI | Level of consciousness during the attack |
| Q12 | - |  |  | SI | Is the patient able to talk during attack? |
| Q13 | - |  |  | SI | Does the patient display any of the following duri... |
| Q14 | - |  |  | SI | Note |
| Q15 | - |  |  | SI | Duration of attacks (minutes) |
| Q16 | - |  |  | SI | Seizure frequency |
| Q17 | - |  |  | SI | How many times |
| Q18 | - |  |  | SI | Seizure clusters (per day) |
| Q19 | - |  |  | SI | Maximum seizure free period (specify if per days o... |
| Q20 | - |  |  | SI | Post ictal symptoms |
| Q21 | - |  |  | SI | Note |
| Q22 | - |  |  | SI | Event triggering factors |
| Q23 | - |  |  | SI | Note |
| Q24 | - |  |  | SI | History of previous hospitalization with seizure |
| Q25 | - |  |  | SI | History of sustained injuries due to seizure |
| Q26 | - |  |  | SI | Is there a diurnal variation of seizure |
| Q27 | - |  |  | SI | Previously epilepsy investigations |
| Q28 | - |  |  | SI | Date |
| Q29 | - |  |  | SI | Time |
| Q30 | - |  |  | SI | Sensory Features |
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
| RSSTATCH_Code | varchar |  |  | NO | Code |
| RSSTATCH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RSSTATCH_CreatedDate | date |  |  | SI | Created Date |
| RSSTATCH_CreatedTime | time |  |  | SI | Created Time |
| RSSTATCH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RSSTATCH_DateFrom | date |  |  | SI | Date From |
| RSSTATCH_DateTo | date |  |  | SI | Date To |
| RSSTATCH_Desc | varchar |  |  | NO | Description |
| RSSTATCH_NationalCode | varchar |  |  | SI | National Code |
| RSSTATCH_OnAssign | varchar |  |  | SI | Default On Assign |
| RSSTATCH_OnCancel | varchar |  |  | SI | Default On Assig |
| RSSTATCH_OnDelete | varchar |  |  | SI | Default On Delete |
| RSSTATCH_OnOffer | varchar |  |  | SI | Default On Offer |
| RSSTATCH_Owner | varchar |  |  | SI | Owner |
| RSSTATCH_UpdatedDate | date |  |  | SI | Updated Date |
| RSSTATCH_UpdatedTime | time |  |  | SI | Updated Time |
| RSSTATCH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
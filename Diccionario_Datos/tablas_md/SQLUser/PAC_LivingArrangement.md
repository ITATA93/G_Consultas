# SQLUser.PAC_LivingArrangement

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LIVARR_RowId | bigint | PK |  | NO | - |
| LIVARR_Code | varchar |  |  | NO | Code |
| LIVARR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LIVARR_CreatedDate | date |  |  | SI | Created Date |
| LIVARR_CreatedTime | time |  |  | SI | Created Time |
| LIVARR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LIVARR_DateFrom | date |  |  | SI | Date From |
| LIVARR_DateTo | date |  |  | SI | Date To |
| LIVARR_Desc | varchar |  |  | NO | Description |
| LIVARR_NationCode | varchar |  |  | SI | National Code |
| LIVARR_NationCodeDesc | varchar |  |  | SI | National Code Description |
| LIVARR_Owner | varchar |  |  | SI | Owner |
| LIVARR_UpdatedDate | date |  |  | SI | Updated Date |
| LIVARR_UpdatedTime | time |  |  | SI | Updated Time |
| LIVARR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Relative / carer / other informed of discharge? |
| Q02 | - |  |  | SI | Date Informed	 |
| Q03 | - |  |  | SI | Details 	 |
| Q04 | - |  |  | SI | Relevant service providers informed of patients di... |
| Q05 | - |  |  | SI | Details |
| Q06 | - |  |  | SI | Care package complete? |
| Q07 | - |  |  | SI | Detail Rationale	 |
| Q08 | - |  |  | SI | Start Date of Care Package	 |
| Q09 | - |  |  | SI | Details of Care Package: Company, How Many Calls P... |
| Q10 | - |  |  | SI | Relevant aids ordered? |
| Q11 | - |  |  | SI | Details	 |
| Q12 | - |  |  | SI | Relevant aids delivered?	 |
| Q13 | - |  |  | SI | Details	 |
| Q14 | - |  |  | SI | Hospital / patient arranged transport? |
| Q15 | - |  |  | SI | Mode of transport |
| Q16 | - |  |  | SI | Key / access to home available? |
| Q17 | - |  |  | SI | Details	 |
| Q18 | - |  |  | SI | Valuables / property returned to patient? |
| Q19 | - |  |  | SI | Cannula removed and site healed? |
| Q20 | - |  |  | SI | Ensure community IV team referral has been made |
| Q21 | - |  |  | SI | Clinical supplies provided i.e. dressings, nasal g... |
| Q22 | - |  |  | SI | Detail items provided |
| Q23 | - |  |  | SI | If patient is being discharged with catheter insit... |
| Q24 | - |  |  | SI | Does patient require outpatient appointment(OPD)? |
| Q25 | - |  |  | SI | Has patient (or carer / relative if appropriate) b... |
| Q26 | - |  |  | SI | Details	 |
| Q27 | - |  |  | SI | Appointment card given |
| Q28 | - |  |  | SI | Has home oxygen been installed if required |
| Q29 | - |  |  | SI | Ensure hospital computer records updated to confir... |
| Q30 | - |  |  | SI | Discharge address confirmed as |
| Q31 | - |  |  | SI | Details 	 |
| Q32 | - |  |  | SI | Heating available at home?	 |
| Q33 | - |  |  | SI | Ensure relevant referrals are made |
| Q34 | - |  |  | SI | Food available at home? 	 |
| Q35 | - |  |  | SI | Supply patient with food pack |
| Q36 | - |  |  | SI | Ensure patient is adequately clothed for journey h... |
| Q37 | - |  |  | SI | Ensure patient has been given a contact number sho... |
| Q38 | - |  |  | SI | Have To Take Out (TTO) medication been supplied	 |
| Q39 | - |  |  | SI | Details 	 |
| Q40 | - |  |  | SI | Copy of medication given to patient (relative or c... |
| Q41 | - |  |  | SI | Ensure you explain to patient (relative or carer i... |
| Q42 | - |  |  | SI | Ensure patient (relative or carer if necessary) ar... |
| Q43 | - |  |  | SI | I have been given information regarding my operati... |
| Q43UDt | - |  |  | SI | I have been given information regarding my operati... |
| Q43UTm | - |  |  | SI | I have been given information regarding my operati... |
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
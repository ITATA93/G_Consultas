# SQLUser.LBC_InstrumentProcedure

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINP_ParRef | bigint | PK |  | NO | Parent instrument DR |
| LBCINP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINP_DateFrom | date |  |  | SI | Date From |
| LBCINP_DateTo | date |  |  | SI | Date To |
| LBCINP_InstrumentProcedureID | varchar |  |  | SI | Inbound Instrument Procedure ID (Channel ID)
Only... |
| LBCINP_OutboundInstrumentProcedureID | varchar |  |  | SI | Outbound Instrument Procedure ID (Channel ID)
Onl... |
| LBCINP_Procedure_DR | bigint |  | FK | SI | Procedure |
| LBCINP_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Find-Assessment and Investigation |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Step 1: Part 1 - Exclusions |
| Q04 | - |  |  | SI | Exclusions (select any that apply to the patient) |
| Q05 | - |  |  | SI | Is patient excluded from assessment |
| Q06 | - |  |  | SI | DO NOT PROCEED with assessment. Go to end of profo... |
| Q07 | - |  |  | SI | Step 1: Part 2- Diagnosis |
| Q08 | - |  |  | SI | Is there already a formal Diagnosis of Dementia re... |
| Q09 | - |  |  | SI | Continue usual care but consider referral to the M... |
| Q10 | - |  |  | SI | Does the patient have delirium |
| Q11 | - |  |  | SI | Continue to ''Step 2: Assess & Investigate |
| Q12 | - |  |  | SI | Has the patient been forgetful in the last 12 mont... |
| Q13 | - |  |  | SI | Who has been asked |
| Q14 | - |  |  | SI | Continue usual care. Go to end of questionnaire an... |
| Q15 | - |  |  | SI | Continue to ''Step 2: Assess & Investigate''  Plea... |
| Q16 | - |  |  | SI | Ensure the following orders have been recorded if ... |
| Q17 | - |  |  | SI | Please complete the Abbreviated Mental Test Score ... |
| Q18 | - |  |  | SI | Does the patient have a resolving delirium or inco... |
| Q19 | - |  |  | SI | Refer to GP for Review |
| Q20 | - |  |  | SI | Does the patient have delirium and need inpatient ... |
| Q21 | - |  |  | SI | Refer to DME or Mental Health Liaison Service via ... |
| Q22 | - |  |  | SI | Does the patient have dementia and need assistance... |
| Q23 | - |  |  | SI | Refer to Mental Health Liaison Service via referra... |
| Q24 | - |  |  | SI | Completed |
| Q25 | - |  |  | SI | For all emergency admissions, 75 years of age and ... |
| Q26 | - |  |  | SI | STEP 2 & 3: Can be completed later |
| Q27 | - |  |  | SI | If this patient HAS a known formal diagnosis of De... |
| Q28 | - |  |  | SI | If the patients Demential status is unknown, conti... |
| Q29 | - |  |  | SI | Continue to ''Step 1: Part 2- Diagnosis |
| Q30 | - |  |  | SI | Continue to ''Step 2: Assess & Investigate |
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
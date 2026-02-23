# SQLUser.PA_AdverseEvent

**Schema:** SQLUser
**Columnas:** 183
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADEV_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| ADEV_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| ADEV_Actions | varchar |  |  | SI | Des Ref MRCAderActions |
| ADEV_AdditionalInfoFreeText | varchar |  |  | SI | Additional information |
| ADEV_AllergySeverity_DR | bigint |  | FK | SI | Des Ref PACAllergySeverity -- no longer used, kept... |
| ADEV_Childsub | double |  |  | NO | Childsub |
| ADEV_DateReported | date |  |  | SI | Date Reported |
| ADEV_DateResolved | date |  |  | SI | Resolved date |
| ADEV_Description | varchar |  |  | SI | Description |
| ADEV_DisplayOEWarning | varchar |  |  | SI | Display order entry warning |
| ADEV_EnteredInErrorReason_DR | bigint |  | FK | SI | Des Ref PACEnteredInErrorReason |
| ADEV_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| ADEV_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| ADEV_ManagementFreeText | varchar |  |  | SI | Event treatment/care given |
| ADEV_OnsetDate | date |  |  | SI | OnsetDate |
| ADEV_OnsetTime | time |  |  | SI | Onset date |
| ADEV_OrdExec_DR | varchar |  | FK | SI | Des Ref OEOrdExec |
| ADEV_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| ADEV_OutcomeFreeText | varchar |  |  | SI | Event outcome |
| ADEV_OutcomeText1 | varchar |  |  | SI | OutcomeText1 |
| ADEV_OutcomeText2 | varchar |  |  | SI | OutcomeText2 |
| ADEV_OutcomeText3 | varchar |  |  | SI | OutcomeText3 |
| ADEV_OutcomeText4 | varchar |  |  | SI | OutcomeText4 |
| ADEV_OutcomeText5 | varchar |  |  | SI | OutcomeText5 |
| ADEV_OutcomeYesNo1 | varchar |  |  | SI | OutcomeYesNo1 |
| ADEV_OutcomeYesNo2 | varchar |  |  | SI | OutcomeYesNo2 |
| ADEV_OutcomeYesNo3 | varchar |  |  | SI | OutcomeYesNo3 |
| ADEV_OutcomeYesNo4 | varchar |  |  | SI | OutcomeYesNo4 |
| ADEV_OutcomeYesNo5 | varchar |  |  | SI | OutcomeYesNo5 |
| ADEV_Outcomes | varchar |  |  | SI | Des Ref MRCAderOutcomes |
| ADEV_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref Reason For Correction |
| ADEV_ReportedBy_DR | bigint |  | FK | SI | Des Ref SSUser |
| ADEV_RowId | varchar |  |  | NO | - |
| ADEV_Severity_DR | bigint |  | FK | SI | Des Ref MRCSeverity -- replacing PAAllergySeverity |
| ADEV_SignsAndSymptoms | varchar |  |  | SI | SNOMED Signs and Symptoms |
| ADEV_TimeReported | time |  |  | SI | Date reported |
| ADEV_TimeResolved | time |  |  | SI | Resolved time |
| ADEV_TreatmentNotes | varchar |  |  | SI | TreatmentNotes |
| ADEV_TreatmentText1 | varchar |  |  | SI | TreatmentText1 |
| ADEV_TreatmentText2 | varchar |  |  | SI | TreatmentText2 |
| ADEV_TreatmentText3 | varchar |  |  | SI | TreatmentText3 |
| ADEV_TreatmentText4 | varchar |  |  | SI | TreatmentText4 |
| ADEV_TreatmentText5 | varchar |  |  | SI | TreatmentText5 |
| ADEV_TreatmentYesNo1 | varchar |  |  | SI | TreatmentYesNo1 |
| ADEV_TreatmentYesNo2 | varchar |  |  | SI | TreatmentYesNo2 |
| ADEV_TreatmentYesNo3 | varchar |  |  | SI | TreatmentYesNo3 |
| ADEV_TreatmentYesNo4 | varchar |  |  | SI | TreatmentYesNo4 |
| ADEV_TreatmentYesNo5 | varchar |  |  | SI | TreatmentYesNo5 |
| ADEV_VacSchedDisDose_DR | varchar |  | FK | SI | Des Ref PAVacSchedDisDose |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Post-op day |
| Q04 | - |  |  | SI | Alert and oriented |
| Q05 | - |  |  | SI | Variance |
| Q06 | - |  |  | SI | Patient monitored and assessed for delirium |
| Q07 | - |  |  | SI | Observations are within acceptable limits and stab... |
| Q08 | - |  |  | SI | Variance |
| Q09 | - |  |  | SI | Neurovascular observations remain aligned to basel... |
| Q10 | - |  |  | SI | Variance |
| Q11 | - |  |  | SI | Patient provided education on using patient-contro... |
| Q12 | - |  |  | SI | Variance |
| Q13 | - |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q14 | - |  |  | SI | Variance |
| Q15 | - |  |  | SI | All medication administered as ordered |
| Q16 | - |  |  | SI | Variance |
| Q17 | - |  |  | SI | Variance |
| Q18 | - |  |  | SI | IV fluid therapy administered as prescribed |
| Q19 | - |  |  | SI | Variance |
| Q20 | - |  |  | SI | Patient is receiving appropriate venous thrombus p... |
| Q21 | - |  |  | SI | Variance |
| Q22 | - |  |  | SI | Patient provided education and demonstrated how to... |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | Patient supervised in the self administration of e... |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | All ordered investigations / tests taken and resul... |
| Q27 | - |  |  | SI | Variance |
| Q28 | - |  |  | SI | Episodes of nausea and vomiting are effectively co... |
| Q29 | - |  |  | SI | Variance |
| Q30 | - |  |  | SI | Patient is tolerating oral fluids and diet |
| Q31 | - |  |  | SI | Variance |
| Q32 | - |  |  | SI | Strict fluid balance chart maintained |
| Q33 | - |  |  | SI | Variance |
| Q34 | - |  |  | SI | Urine output > 30 mLs per hour |
| Q35 | - |  |  | SI | Variance |
| Q36 | - |  |  | SI | All bowel motions documented |
| Q37 | - |  |  | SI | Variance |
| Q38 | - |  |  | SI | Regular and PRN aperients prescribed and administe... |
| Q39 | - |  |  | SI | Variance |
| Q40 | - |  |  | SI | Drain remained patent and all drainage documented.... |
| Q41 | - |  |  | SI | Variance |
| Q42 | - |  |  | SI | Drain removed as ordered with no complications |
| Q43 | - |  |  | SI | Variance |
| Q44 | - |  |  | SI | Surgical wound observed for signs of haematoma, oo... |
| Q45 | - |  |  | SI | Variance |
| Q46 | - |  |  | SI | Patient skin integrity assessed and is free from p... |
| Q47 | - |  |  | SI | Variance |
| Q48 | - |  |  | SI | Patient has received regular pressure area care wi... |
| Q49 | - |  |  | SI | Variance |
| Q50 | - |  |  | SI | Pressure relieving devices in situ as needed |
| Q51 | - |  |  | SI | Variance |
| Q52 | - |  |  | SI | Personal hygiene attended |
| Q53 | - |  |  | SI | Variance |
| Q54 | - |  |  | SI | Personal hygiene attended, including axilla care o... |
| Q55 | - |  |  | SI | Variance |
| Q56 | - |  |  | SI | Patient received mouth care as clinically indicate... |
| Q57 | - |  |  | SI | Variance |
| Q58 | - |  |  | SI | Shoulder Immobiliser fitted and comfortable |
| Q59 | - |  |  | SI | Variance |
| Q60 | - |  |  | SI | Patient provided education by physiotherapist on r... |
| Q61 | - |  |  | SI | Variance |
| Q62 | - |  |  | SI | Patient performed regular movements of fingers, ha... |
| Q63 | - |  |  | SI | Variance |
| Q64 | - |  |  | SI | Patient assisted and instructed on how to do daily... |
| Q65 | - |  |  | SI | Variance |
| Q66 | - |  |  | SI | Patient has stood / Sat out of bed |
| Q67 | - |  |  | SI | Variance |
| Q68 | - |  |  | SI | Patient has sat out of bed |
| Q69 | - |  |  | SI | Variance |
| Q70 | - |  |  | SI | Sat out of bed for all meals, mobility aids as per... |
| Q71 | - |  |  | SI | Variance |
| Q72 | - |  |  | SI | All interventions explained to patient / family |
| Q73 | - |  |  | SI | Variance |
| Q74 | - |  |  | SI | Patient / Family / Carers included in educational ... |
| Q75 | - |  |  | SI | Variance |
| Q76 | - |  |  | SI | Educate patients regarding signs and symptoms of w... |
| Q77 | - |  |  | SI | Variance |
| Q78 | - |  |  | SI | Patient provided orientation to ward if required |
| Q79 | - |  |  | SI | Variance |
| Q80 | - |  |  | SI | Patient safety considered (i.e. bedside rails, pat... |
| Q81 | - |  |  | SI | Variance |
| Q82 | - |  |  | SI | Referrals arranged as necessary |
| Q83 | - |  |  | SI | Variance |
| Q84 | - |  |  | SI | Commence discharge planning |
| Q85 | - |  |  | SI | Variance |
| Q86 | - |  |  | SI | Continue discharge planning |
| Q87 | - |  |  | SI | Variance |
| Q88 | - |  |  | SI | Discharge planning includes: |
| Q89 | - |  |  | SI | • Outpatient appointment booked |
| Q90 | - |  |  | SI | • Plan for suture removal if required |
| Q91 | - |  |  | SI | • Enoxaparin information pack provided to patient |
| Q92 | - |  |  | SI | • Community referral for enoxaparin administration... |
| Q93 | - |  |  | SI | • Equipment is ready for discharge |
| Q94 | - |  |  | SI | • Discharge medications ordered |
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
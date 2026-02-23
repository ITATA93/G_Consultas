# SQLUser.NRC_Outcome

**Schema:** SQLUser
**Columnas:** 134
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NRCO_RowID | bigint | PK |  | NO | - |
| ChildQ40DR | - |  |  | SI | Child Reference: CTG |
| NRCO_ARCIM_DR | varchar |  | FK | SI | Order Item |
| NRCO_Code | varchar |  |  | NO | Code  |
| NRCO_CodeTableTags | varchar |  |  | SI | List of code table tags |
| NRCO_DateFrom | date |  |  | NO | Effective date for the record |
| NRCO_DateTo | date |  |  | SI | Last day the record is active |
| NRCO_Definition | varchar |  |  | SI | Free Text Definition is a Long Description |
| NRCO_Desc | varchar |  |  | NO | Description |
| NRCO_Narrative | longvarchar |  |  | SI | Narrative Stream  |
| NRCO_ObservationItem_DR | bigint |  | FK | SI | Des Ref Observation Item  |
| NRCO_Owner | varchar |  |  | SI | Owner |
| NRCO_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| NRCO_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| Q01 | - |  |  | SI | Gestation: Weeks |
| Q01ObsDR | - |  |  | SI | Gestation: Weeks DR |
| Q02 | - |  |  | SI | Reason for admission |
| Q03 | - |  |  | SI | Systolic BP |
| Q03ObsDR | - |  |  | SI | Systolic BP DR |
| Q04 | - |  |  | SI | Diastolic BP |
| Q04ObsDR | - |  |  | SI | Diastolic BP DR |
| Q05 | - |  |  | SI | Temperature |
| Q05ObsDR | - |  |  | SI | Temperature DR |
| Q06 | - |  |  | SI | Pulse |
| Q06ObsDR | - |  |  | SI | Pulse DR |
| Q07 | - |  |  | SI | Urinalysis |
| Q07ObsDR | - |  |  | SI | Urinalysis DR |
| Q08 | - |  |  | SI | Urinalysis abnormalites |
| Q08ObsDR | - |  |  | SI | Urinalysis abnormalites DR |
| Q09 | - |  |  | SI | Oedema |
| Q09ObsDR | - |  |  | SI | Oedema DR |
| Q10 | - |  |  | SI | Fundal height |
| Q10ObsDR | - |  |  | SI | Fundal height DR |
| Q11 | - |  |  | SI | Lie |
| Q11ObsDR | - |  |  | SI | Lie DR |
| Q12 | - |  |  | SI | Presentation |
| Q12ObsDR | - |  |  | SI | Presentation DR |
| Q13 | - |  |  | SI | Position |
| Q13ObsDR | - |  |  | SI | Position DR |
| Q14 | - |  |  | SI | Presentation / 5ths palpable |
| Q14ObsDR | - |  |  | SI | Presentation / 5ths palpable DR |
| Q15 | - |  |  | SI | Fetal heart rate |
| Q15ObsDR | - |  |  | SI | Fetal heart rate DR |
| Q16 | - |  |  | SI | Fetal movement felt |
| Q16ObsDR | - |  |  | SI | Fetal movement felt DR |
| Q17 | - |  |  | SI | Antenatal steroids given |
| Q17ObsDR | - |  |  | SI | Antenatal steroids given DR |
| Q18 | - |  |  | SI | Fundal height |
| Q18ObsDR | - |  |  | SI | Fundal height DR |
| Q19 | - |  |  | SI | IV cannula |
| Q19ObsDR | - |  |  | SI | IV cannula DR |
| Q20 | - |  |  | SI | IV fluids prescribed |
| Q20ObsDR | - |  |  | SI | IV fluids prescribed DR |
| Q21 | - |  |  | SI | IV cannula site check |
| Q21ObsDR | - |  |  | SI | IV cannula site check DR |
| Q22 | - |  |  | SI | IV cannula flush |
| Q22ObsDR | - |  |  | SI | IV cannula flush DR |
| Q23 | - |  |  | SI | IV cannula change (48hrs) |
| Q23ObsDR | - |  |  | SI | IV cannula change (48hrs) DR |
| Q24 | - |  |  | SI | Antenatal steroids given |
| Q24ObsDR | - |  |  | SI | Antenatal steroids given DR |
| Q25 | - |  |  | SI | Antenatal steroids 2nd dose given |
| Q25ObsDR | - |  |  | SI | Antenatal steroids 2nd dose given DR |
| Q26 | - |  |  | SI | Medicines required |
| Q26ObsDR | - |  |  | SI | Medicines required DR |
| Q27 | - |  |  | SI | Medicines prescribed |
| Q27ObsDR | - |  |  | SI | Medicines prescribed DR |
| Q28 | - |  |  | SI | Prescribed medicines review |
| Q28ObsDR | - |  |  | SI | Prescribed medicines review DR |
| Q29 | - |  |  | SI | PV loss |
| Q29ObsDR | - |  |  | SI | PV loss DR |
| Q30 | - |  |  | SI | Bleeding |
| Q30ObsDR | - |  |  | SI | Bleeding DR |
| Q31 | - |  |  | SI | SRM date |
| Q32 | - |  |  | SI | SRM time |
| Q33 | - |  |  | SI | SRM |
| Q33ObsDR | - |  |  | SI | SRM DR |
| Q34 | - |  |  | SI | Liquor clear |
| Q34ObsDR | - |  |  | SI | Liquor clear DR |
| Q35 | - |  |  | SI | Liquor blood stained |
| Q35ObsDR | - |  |  | SI | Liquor blood stained DR |
| Q36 | - |  |  | SI | Liquor meconium stained |
| Q36ObsDR | - |  |  | SI | Liquor meconium stained DR |
| Q37 | - |  |  | SI | Liquor odourless |
| Q37ObsDR | - |  |  | SI | Liquor odourless DR |
| Q38 | - |  |  | SI | Plan of care |
| Q39 | - |  |  | SI | Midwife countersigning |
| Q41 | - |  |  | SI | Comments |
| Q42 | - |  |  | SI | Estimated blood loss |
| Q42ObsDR | - |  |  | SI | Estimated blood loss DR |
| Q43 | - |  |  | SI | Gestation: Days |
| Q43ObsDR | - |  |  | SI | Gestation: Days DR |
| Q44 | - |  |  | SI | Date |
| Q45 | - |  |  | SI | Time |
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
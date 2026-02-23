# SQLUser.OE_AdmixManuf

**Schema:** SQLUser
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MANUF_ParRef | bigint | PK |  | NO | OE_OrdAdmix Parent Reference |
| MANUF_AdditionalCost | double |  |  | SI | Additional Cost |
| MANUF_Batch | varchar |  |  | SI | Batch |
| MANUF_CheckingNotes | varchar |  |  | SI | Free text field allowing the checking pharmacist t... |
| MANUF_Childsub | double |  |  | NO | Childsub |
| MANUF_CompletedDate | date |  |  | SI | UpdateDate |
| MANUF_CompletedTime | time |  |  | SI | UpdateTime |
| MANUF_CompletedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| MANUF_ExpiryDate | date |  |  | SI | ExpiryDate |
| MANUF_ExpiryTime | time |  |  | SI | ExpiryTime |
| MANUF_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| MANUF_ManufacturedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| MANUF_NurseManufacturedSolventVolumeBeforeMixing | double |  |  | SI | Nurse Manufactured Solvent Volume Before Mixing |
| MANUF_NurseManufacturedVolume | double |  |  | SI | Nurse Manufactured Volume |
| MANUF_OEOrdExec_DR | varchar |  | FK | SI | Des Ref OEOrdExec |
| MANUF_OrderDate | date |  |  | SI | OrderDate |
| MANUF_PartialStatus | varchar |  |  | SI | PartialStatus |
| MANUF_Quantity | double |  |  | SI | Quantity |
| MANUF_ReasManufAbort_DR | bigint |  | FK | SI | Des Ref ReasonManufactureAbort |
| MANUF_ReassignedFrom_DR | varchar |  | FK | SI | Reassigned From |
| MANUF_RecomDilOverReas_DR | bigint |  | FK | SI | des Ref OECRecommendedDilOverReason |
| MANUF_RowId | varchar |  |  | NO | - |
| MANUF_StartedDate | date |  |  | SI | StartedDate |
| MANUF_StartedTime | time |  |  | SI | UpdateTime |
| MANUF_StartedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| MANUF_ToBeReassigned | varchar |  |  | SI | To Be Reassigned |
| MANUF_TransactionNo | varchar |  |  | SI | MANUFTransactionNo |
| MANUF_UpdateDate | date |  |  | SI | UpdateDate |
| MANUF_UpdateHospital_DR | bigint |  | FK | SI | des Ref CTHospital |
| MANUF_UpdateTime | time |  |  | SI | UpdateTime |
| MANUF_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| MANUF_UserDefinedExpiry | varchar |  |  | SI | User Defined Expiry |
| Q01 | - |  |  | SI | 1 - Active cancer (treatment ongoing, within 6 mon... |
| Q02 | - |  |  | SI | 1 - Paralysis, paresis or recent plaster immobilis... |
| Q03 | - |  |  | SI | 1 - Recently bedridden for longer than 3 days or m... |
| Q04 | - |  |  | SI | 1 - Localised tenderness along the distribution of... |
| Q05 | - |  |  | SI | 1 - Entire leg swollen |
| Q06 | - |  |  | SI | 1 - Calf swelling >3 cm compared with the asymptom... |
| Q07 | - |  |  | SI | 1 - Unilateral pitting edema |
| Q08 | - |  |  | SI | -2 - Alternative diagnosis as likely or greater th... |
| Q09 | - |  |  | SI | >=3: High probability, about 75% risk of DVT |
| Q10 | - |  |  | SI | 1–2: Moderate probability, about 17% risk of DVT |
| Q11 | - |  |  | SI | -2 - 0: Low probability, about 3% risk of DVT |
| Q12 | - |  |  | SI | The Wells prediction score for deep vein thrombosi... |
| Q13 | - |  |  | SI | 1 - Collateral (nonvaricose) superficial veins pre... |
| Q14 | - |  |  | SI | 1 - Previously documented DVT |
| Q15 | - |  |  | SI | <=0: Low probability, about 3% risk of DVT |
| Q16 | - |  |  | SI | 1–2: Moderate probability, about 17% risk of DVT |
| Q17 | - |  |  | SI | >=3: High probability, about 75% risk of DVT |
| Q18 | - |  |  | SI | Date |
| Q19 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Score |
| Q21 | - |  |  | SI | Classification |
| Q22 | - |  |  | SI | 1 - Active cancer (treatment ongoing, within 6 mon... |
| Q23 | - |  |  | SI | 1 - Paralysis, paresis or recent plaster immobilis... |
| Q24 | - |  |  | SI | 1 - Recently bedridden for longer than 3 days or m... |
| Q25 | - |  |  | SI | 1 - Localised tenderness along the distribution of... |
| Q26 | - |  |  | SI | 1 - Entire leg swollen |
| Q27 | - |  |  | SI | 1 - Calf swelling >3 cm compared with the asymptom... |
| Q28 | - |  |  | SI | 1 - Unilateral pitting edema |
| Q29 | - |  |  | SI | -2 - Alternative diagnosis as likely or greater th... |
| Q30 | - |  |  | SI | 1 - Collateral (nonvaricose) superficial veins pre... |
| Q31 | - |  |  | SI | 1 - Previously documented DVT |
| Q32 | - |  |  | SI | ≤0 |
| Q33 | - |  |  | SI | Low probability, about 3% risk of DVT |
| Q34 | - |  |  | SI | 1 – 2 |
| Q35 | - |  |  | SI | Moderate probability, about 17% risk of DVT |
| Q36 | - |  |  | SI | ≥3 |
| Q37 | - |  |  | SI | High probability, about 75% risk of DVT |
| Q38 | - |  |  | SI | Active cancer (treatment ongoing, within 6 months ... |
| Q39 | - |  |  | SI | Paralysis, paresis or recent plaster immobilisatio... |
| Q40 | - |  |  | SI | Recently bedridden for longer than 3 days or major... |
| Q41 | - |  |  | SI | Localised tenderness along the distribution of the... |
| Q42 | - |  |  | SI | Entire leg swollen |
| Q43 | - |  |  | SI | Calf swelling >3 cm compared with the asymptomatic... |
| Q44 | - |  |  | SI | Unilateral pitting edema |
| Q45 | - |  |  | SI | Alternative diagnosis as likely or greater than th... |
| Q46 | - |  |  | SI | Collateral (nonvaricose) superficial veins present |
| Q47 | - |  |  | SI | Previously documented DVT |
| Q48 | - |  |  | SI | Primary References |
| Q49 | - |  |  | SI | Wells PS, Hirsh J, Anderson DR, Lensing AW, Foster... |
| Q50 | - |  |  | SI | Wells PS, Anderson DR, Bormanis J, et al. Value of... |
| Q51 | - |  |  | SI | Wells PS, Anderson DR, Rodger M, Forgie M, Kearon ... |
| Q52 | - |  |  | SI | Tool Validation |
| Q53 | - |  |  | SI | Scarvelis D, Wells PS. Diagnosis and treatment of ... |
| Q54 | - |  |  | SI | Author endorsed tool: |
| Q55 | - |  |  | SI | https://www.mdcalc.com/calc/362/wells-criteria-dvt... |
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
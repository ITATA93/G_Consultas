# SQLUser.LBC_PathogenAntibiotic

**Schema:** SQLUser
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPAA_ParRef | bigint | PK |  | NO | LBCPathogen Parent Reference |
| LBCPAA_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site DR |
| LBCPAA_Antibiotic_DR | bigint |  | FK | SI | Des Ref LBCAntibiotic |
| LBCPAA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPAA_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPAA_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPAA_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCPAA_Lesion_DR | bigint |  | FK | SI | Lesion DR |
| LBCPAA_NotApplicable | varchar |  |  | SI | Not Aplicable |
| LBCPAA_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCPAA_Reported | varchar |  |  | SI | Reported |
| LBCPAA_RowID | varchar |  |  | NO | - |
| LBCPAA_Sequence | double |  |  | SI | Sequence
[DEPRECATED]Not used. (Used: LBCANTSeque... |
| LBCPAA_Species_DR | bigint |  | FK | SI | Species |
| LBCPAA_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group DR |
| LBCPAA_Specimen_DR | bigint |  | FK | SI | Specimen DR |
| LBCPAA_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCPAA_WeightedSequence | double |  |  | SI | Weighted Sequence |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Deferment or cancellation |
| Q04 | - |  |  | SI | Reason |
| Q05 | - |  |  | SI | Dummy1 |
| Q06 | - |  |  | SI | Vital Signs Observations |
| Q07 | - |  |  | SI | Systolic |
| Q07ObsDR | - |  |  | SI | Systolic DR |
| Q08 | - |  |  | SI | Diastolic |
| Q08ObsDR | - |  |  | SI | Diastolic DR |
| Q09 | - |  |  | SI | Heart Rate |
| Q09ObsDR | - |  |  | SI | Heart Rate DR |
| Q10 | - |  |  | SI | Respirations |
| Q10ObsDR | - |  |  | SI | Respirations DR |
| Q11 | - |  |  | SI | Oxygen Saturation |
| Q11ObsDR | - |  |  | SI | Oxygen Saturation DR |
| Q12 | - |  |  | SI | Temperature |
| Q12ObsDR | - |  |  | SI | Temperature DR |
| Q13 | - |  |  | SI | Stat Lab / Point of Care Results |
| Q14 | - |  |  | SI | Serum Potassium |
| Q14ObsDR | - |  |  | SI | Serum Potassium DR |
| Q15 | - |  |  | SI | Dummy2 |
| Q16 | - |  |  | SI | Fluid Status Assessment |
| Q17 | - |  |  | SI | Dyspnoea |
| Q17ObsDR | - |  |  | SI | Dyspnoea DR |
| Q18 | - |  |  | SI | Oedema |
| Q18ObsDR | - |  |  | SI | Oedema DR |
| Q19 | - |  |  | SI | Urine output |
| Q20 | - |  |  | SI | Urine Output (mL) |
| Q20ObsDR | - |  |  | SI | Urine Output (mL) DR |
| Q21 | - |  |  | SI | Chest pain |
| Q22 | - |  |  | SI | Chest pain details |
| Q23 | - |  |  | SI | Vomiting |
| Q24 | - |  |  | SI | Diarrhoea |
| Q25 | - |  |  | SI | Appetite |
| Q26 | - |  |  | SI | Current weight |
| Q26ObsDR | - |  |  | SI | Current weight DR |
| Q27 | - |  |  | SI | Dry Weight Target (Renal Replacement Therapy) |
| Q27ObsDR | - |  |  | SI | Dry Weight Target (Renal Replacement Therapy) DR |
| Q28 | - |  |  | SI | Greater than 8% variance weight gain |
| Q29 | - |  |  | SI | Clinical assessment notes |
| Q30 | - |  |  | SI | Missed Session Review |
| Q31 | - |  |  | SI | Total number of dialysis sessions missed over last... |
| Q32 | - |  |  | SI | Dates missed in last 7 days |
| Q33 | - |  |  | SI | Review previous missed dialysis session reasons |
| Q34 | - |  |  | SI | Missed session review notes |
| Q35 | - |  |  | SI | Treatment Plan |
| Q36 | - |  |  | SI | Doctor in attendance |
| Q37 | - |  |  | SI | Attending doctor |
| Q38 | - |  |  | SI | Plan |
| Q39 | - |  |  | SI | Signature of doctor |
| Q39UDt | - |  |  | SI | Signature of doctor Last Updated Date |
| Q39UTm | - |  |  | SI | Signature of doctor Last Updated Time |
| Q40 | - |  |  | SI | Name of doctor contacted |
| Q41 | - |  |  | SI | Verbal plan |
| Q42 | - |  |  | SI | Name of care provider taking verbal plan and inter... |
| Q43 | - |  |  | SI | Signature of care provider |
| Q43UDt | - |  |  | SI | Signature of care provider Last Updated Date |
| Q43UTm | - |  |  | SI | Signature of care provider Last Updated Time |
| Q44 | - |  |  | SI | Clinical Nurse Manager / Haemodialysis Coordinator... |
| Q45 | - |  |  | SI | Reason CNM / HD Coordinator not aware |
| Q46 | - |  |  | SI | Explanation of plan and interventions provided to ... |
| Q47 | - |  |  | SI | Interpreter details, if applicable |
| Q48 | - |  |  | SI | Additional Requirements |
| Q49 | - |  |  | SI | Dummy3 |
| Q50 | - |  |  | SI | Dummy4 |
| Q51 | - |  |  | SI | Dummy5 |
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
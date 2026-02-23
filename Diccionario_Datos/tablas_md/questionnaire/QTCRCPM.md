# questionnaire.QTCRCPM

> Ranson’s Criteria for Pancreatitis Mortality

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ranson’s Criteria for Pancreatitis Mortality

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | White Blood Cell (WBC) count &gt; 16,000 mm/3 |
| Q04 | varchar |  |  | SI | Age &gt;55 years |
| Q05 | varchar |  |  | SI | Blood glucose &gt;200 mg/dL (&gt;11 mmol/L) |
| Q06 | varchar |  |  | SI | Aspartate transaminase (AST) &gt;250 U/L |
| Q07 | varchar |  |  | SI | Lactate dehydrogenase (LDH) &gt;350 U/L |
| Q08 | varchar |  |  | SI | Haematocrit drop &gt;10% |
| Q09 | varchar |  |  | SI | Blood urea nitrogen increase &gt;5 mg/dL (&gt;1.79... |
| Q10 | varchar |  |  | SI | Calcium &lt;8 mg/dL (&lt;2 mmol/L) |
| Q11 | varchar |  |  | SI | Arterial PO2 &lt;60 mmHg |
| Q12 | varchar |  |  | SI | Base deficit &gt;4 mEq/L |
| Q13 | varchar |  |  | SI | Positive fluid balance &gt;6 L |
| Q14 | varchar |  |  | SI | The Ranson criteria can only be calculated once th... |
| Q15 | varchar |  |  | SI | Score |
| Q16 | varchar |  |  | SI | Classification |
| Q17 | varchar |  |  | SI | 0 - 2 |
| Q18 | varchar |  |  | SI | 0 - 2: Mortality 0% to 3% |
| Q19 | varchar |  |  | SI | 3 - 4 |
| Q20 | varchar |  |  | SI | 3 - 4: 15% predicted mortality |
| Q21 | varchar |  |  | SI | 5 - 6 |
| Q22 | varchar |  |  | SI | 5 - 6: 40% predicted mortality |
| Q23 | varchar |  |  | SI | 7 - 11 |
| Q24 | varchar |  |  | SI | 7 - 11: 100% predicted mortality |
| Q25 | varchar |  |  | SI | Consider ICU admission if score is 3 or greater. |
| Q26 | varchar |  |  | SI | 1% predicted mortality |
| Q27 | varchar |  |  | SI | 15% predicted mortality |
| Q28 | varchar |  |  | SI | 40% predicted mortality |
| Q29 | varchar |  |  | SI | 100% predicted mortality |
| Q30 | varchar |  |  | SI | Ranson's criteria is one of the earliest scoring s... |
| Q31 | varchar |  |  | SI | It consists of 11 indices measured at two time sta... |
| Q32 | varchar |  |  | SI | White blood cell count &gt;16 x 10<sup>9</sup>&nbs... |
| Q33 | varchar |  |  | SI | 1.&nbsp;Ranson JH, Rifkind KM, Roses DF, et al. Pr... |
| Q34 | varchar |  |  | SI | 2.&nbsp;Ranson JHC. The Timing of Biliary Surgery ... |
| Q35 | varchar |  |  | SI | 3.&nbsp;Meek K, Toosie K, Stabile BE, et al. Simpl... |
| Q36 | varchar |  |  | SI | 4.&nbsp;Blamey SL, Imrie CW, O’Neill J, Gilmour WH... |
| Q37 | varchar |  |  | SI | 5.&nbsp;Ranson JH. Etiological and prognostic fact... |
| Q38 | varchar |  |  | SI | 6.&nbsp;Venkataraman A, Rich PB. Pancreatitis - Tr... |
| Q39 | varchar |  |  | SI | 7.&nbsp;Somayaji BN, Stone WD, Glover PB. Risk of ... |
| Q40 | varchar |  |  | SI | 8.&nbsp;Lee DW, Cho CM. Predicting Severity of Acu... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
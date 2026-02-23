# SQLUser.PA_AdmDietDetails

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIET_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| DIET_Childsub | double |  |  | NO | Childsub |
| DIET_LowCholesterol | varchar |  |  | SI | Low Cholesterol |
| DIET_LowPotassium | varchar |  |  | SI | Low Potassium |
| DIET_PasturizeFood | varchar |  |  | SI | Pasturize Food |
| DIET_RowId | varchar |  |  | NO | - |
| DIET_SaltContent_DR | bigint |  | FK | SI | Des Ref Salt Content |
| DIET_SterilizeUtensils | varchar |  |  | SI | Sterilize Utensils |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | 1.&nbsp |
| Q04 | - |  |  | SI | 2.&nbsp |
| Q05 | - |  |  | SI | 3. I was too tired to do what I wanted to do |
| Q06 | - |  |  | SI | 1.&nbsp |
| Q07 | - |  |  | SI | 2.&nbsp |
| Q08 | - |  |  | SI | 3.&nbsp |
| Q09 | - |  |  | SI | 1.&nbsp |
| Q10 | - |  |  | SI | 2.&nbsp |
| Q11 | - |  |  | SI | 3.&nbsp |
| Q12 | - |  |  | SI | 4.&nbsp |
| Q13 | - |  |  | SI | 5.&nbsp |
| Q14 | - |  |  | SI | 1. Did you have trouble walking? |
| Q15 | - |  |  | SI | 2.&nbsp |
| Q16 | - |  |  | SI | 3. Did you have trouble climbing stairs? |
| Q17 | - |  |  | SI | 4.&nbsp |
| Q18 | - |  |  | SI | 5.&nbsp |
| Q19 | - |  |  | SI | 6.&nbsp |
| Q20 | - |  |  | SI | 1.&nbsp |
| Q21 | - |  |  | SI | 2.&nbsp |
| Q22 | - |  |  | SI | 3. I felt withdrawn from other people |
| Q23 | - |  |  | SI | 4.&nbsp |
| Q24 | - |  |  | SI | 5.&nbsp |
| Q25 | - |  |  | SI | 1.&nbsp |
| Q26 | - |  |  | SI | 2.&nbsp |
| Q27 | - |  |  | SI | 3.&nbsp |
| Q28 | - |  |  | SI | 1. Did you need help preparing food? |
| Q29 | - |  |  | SI | 2.&nbsp |
| Q30 | - |  |  | SI | 3. Did you need help getting dressed? For example,... |
| Q31 | - |  |  | SI | 4.&nbsp |
| Q32 | - |  |  | SI | 5.&nbsp |
| Q33 | - |  |  | SI | 1.&nbsp |
| Q34 | - |  |  | SI | 2.&nbsp |
| Q35 | - |  |  | SI | 3. I didn't see as many of my friends as I would l... |
| Q36 | - |  |  | SI | 4. I had sex less often than I would like. |
| Q37 | - |  |  | SI | 5. My physical condition interfered with my social... |
| Q38 | - |  |  | SI | 1.&nbsp |
| Q39 | - |  |  | SI | 2. I had trouble remembering things |
| Q40 | - |  |  | SI | 3. I had to write things down to remember them |
| Q41 | - |  |  | SI | 1.&nbsp |
| Q42 | - |  |  | SI | 2. Did you have trouble putting on socks? |
| Q43 | - |  |  | SI | 3. Did you have trouble buttoning buttons? |
| Q44 | - |  |  | SI | 4. Did you have trouble zipping a zipper? |
| Q45 | - |  |  | SI | 5. Did you have trouble opening a jar? |
| Q46 | - |  |  | SI | 1.&nbsp |
| Q47 | - |  |  | SI | 2. Did you have trouble reaching things because of... |
| Q48 | - |  |  | SI | 3. Did you have trouble seeing things off to one s... |
| Q49 | - |  |  | SI | 1.&nbsp |
| Q50 | - |  |  | SI | 2. Did you have trouble finishing jobs that you st... |
| Q51 | - |  |  | SI | 3. Did you have trouble doing the work you used to... |
| Q52 | - |  |  | SI | Notes |
| Q53 | - |  |  | SI | Total score |
| Q54 | - |  |  | SI | Williams LS, Weinberger M, Harris LE, Clark DO, Bi... |
| Q55 | - |  |  | SI | Higher score indicates better of quality of life |
| Q56 | - |  |  | SI | Should not be used in: |
| Q57 | - |  |  | SI | • Patients without stroke. The SS-QOL was develope... |
| Q58 | - |  |  | SI | • Severe stroke populations. The SS-QOL has not ye... |
| Q59 | - |  |  | SI | • Patients who require a proxy to complete. |
| Q60 | - |  |  | SI | • Should be used with caution in patients with aph... |
| Q61 | - |  |  | SI | Although the modified version of the scale, the SA... |
| Q62 | - |  |  | SI | • Not to be used in patients under 18 years. |
| Q63 | - |  |  | SI | The performance characteristics of this instrument... |
| Q64 | - |  |  | SI | The Stroke Specific Quality of Life Scale assesses... |
| Q65 | - |  |  | SI | 1. Did you have trouble walking? |
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
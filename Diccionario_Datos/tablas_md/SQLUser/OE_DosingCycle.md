# SQLUser.OE_DosingCycle

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOSECYCLE_RowId | bigint | PK |  | NO | - |
| DOSECYCLE_DayNumber | varchar |  |  | SI | Day Number |
| DOSECYCLE_DayOfTheWeek | varchar |  |  | SI | Day of the week |
| DOSECYCLE_DoseQty | varchar |  |  | SI | Dosing cycle quantity |
| DOSECYCLE_Instruction | varchar |  |  | SI | Instruction  |
| DOSECYCLE_IsConditional | varchar |  |  | SI | Dosing cycle is a Conditional Dose |
| DOSECYCLE_MinDoseQty | varchar |  |  | SI | Minimum dosing cycle quantity |
| DOSECYCLE_Time | time |  |  | SI | Dispensing Time |
| Q01 | - |  |  | SI | 1. Are there previous conclusive reports on this r... |
| Q02 | - |  |  | SI | 2. Did the adverse event appear after the suspecte... |
| Q03 | - |  |  | SI | 3. Did the adverse reaction improve when the drug ... |
| Q04 | - |  |  | SI | 4. Did the adverse reaction reappear when the drug... |
| Q05 | - |  |  | SI | 5. Are there alternative causes (other than the dr... |
| Q06 | - |  |  | SI | 6. Did the reaction reappear when a placebo was gi... |
| Q07 | - |  |  | SI | 7. Was the drug detected in the blood (or other fl... |
| Q08 | - |  |  | SI | 8. Was the reaction more severe when the dose was ... |
| Q09 | - |  |  | SI | 9. Did the patient have a similar reaction to the ... |
| Q10 | - |  |  | SI | 10. Was the adverse event confirmed by any objecti... |
| Q11 | - |  |  | SI | >= 9:  Definite ADR |
| Q12 | - |  |  | SI | 5 - 8: Probable ADR |
| Q13 | - |  |  | SI | 1 - 4: Possible ADR |
| Q14 | - |  |  | SI | < 1: Doubtful ADR |
| Q15 | - |  |  | SI | The Naranjo Algorithm assesses Adverse Drug Reacti... |
| Q16 | - |  |  | SI | Note |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Time |
| Q19 | - |  |  | SI | ≥ 9 |
| Q20 | - |  |  | SI | Definite ADR |
| Q21 | - |  |  | SI | 5 - 8 |
| Q22 | - |  |  | SI | Probable ADR |
| Q23 | - |  |  | SI | 1 - 4 |
| Q24 | - |  |  | SI | Possible ADR |
| Q25 | - |  |  | SI | < 1 |
| Q26 | - |  |  | SI | Doubtful ADR |
| Q27 | - |  |  | SI | Score |
| Q28 | - |  |  | SI | Classification |
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
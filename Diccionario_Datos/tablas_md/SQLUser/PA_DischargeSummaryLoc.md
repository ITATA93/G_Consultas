# SQLUser.PA_DischargeSummaryLoc

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | bigint | PK |  | NO | PA_DischargeSummary Parent Reference |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_Loc_DR | bigint |  | FK | SI | Des Ref Loc |
| LOC_PrimaryRecipient | varchar |  |  | SI | Primary Recipient |
| LOC_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | 1.Blome C, Baade K, Debus ES, Price P, Augustin M.... |
| Q04 | - |  |  | SI | Wound Repair Regen 2014 |
| Q05 | - |  |  | SI | 2. Augustin M, Baade K, Herberger K, Protz K, Goep... |
| Q06 | - |  |  | SI | In the last 7 days... |
| Q07 | - |  |  | SI | My wound hurt |
| Q08 | - |  |  | SI | My wound had a bad smell |
| Q09 | - |  |  | SI | There was a disturbing discharge from the wound |
| Q10 | - |  |  | SI | The wound has affected my sleep |
| Q11 | - |  |  | SI | The treatment of the wound has been a burden to me |
| Q12 | - |  |  | SI | The wound has made me unhappy |
| Q13 | - |  |  | SI | I have felt frustrated because the wound is taking... |
| Q14 | - |  |  | SI | I have worried about my wound |
| Q15 | - |  |  | SI | I have been afraid of the wound getting worse or o... |
| Q16 | - |  |  | SI | I have been afraid of knocking the wound |
| Q17 | - |  |  | SI | I have had trouble moving about because of the wou... |
| Q18 | - |  |  | SI | Climbing stairs has been difficult because of the ... |
| Q19 | - |  |  | SI | I have had trouble with day-to-day activities beca... |
| Q20 | - |  |  | SI | The wound has limited my leisure activities |
| Q21 | - |  |  | SI | The wound has forced me to limit my activities wit... |
| Q22 | - |  |  | SI | I have felt dependent on help from others because ... |
| Q23 | - |  |  | SI | The wound has been a financial burden to me |
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
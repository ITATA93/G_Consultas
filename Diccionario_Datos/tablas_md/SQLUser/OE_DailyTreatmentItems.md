# SQLUser.OE_DailyTreatmentItems

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | OE_DailyTreatment Parent Reference |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| ITM_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Height |
| Q03ObsDR | - |  |  | SI | Height DR |
| Q04 | - |  |  | SI | Weight |
| Q04ObsDR | - |  |  | SI | Weight DR |
| Q05 | - |  |  | SI | The distance between the two ends of the circuit i... |
| Q06 | - |  |  | SI | Able to complete practice lap? |
| Q07 | - |  |  | SI | Why not? |
| Q08 | - |  |  | SI | Heart rate before testing (bpm) |
| Q08ObsDR | - |  |  | SI | Heart rate before testing (bpm) DR |
| Q09 | - |  |  | SI | Heart rate after testing (bpm) (Value should be do... |
| Q10 | - |  |  | SI | Time required to finish (Minutes) |
| Q11 | - |  |  | SI | Number of lengths achieved |
| Q12 | - |  |  | SI | Distance completed (meter) |
| Q13 | - |  |  | SI | Tyre pressures left (psi) |
| Q14 | - |  |  | SI | Tyre pressures Right (psi) |
| Q15 | - |  |  | SI | Notes |
| Q16 | - |  |  | SI | Cowan RE, Callahan MK, Nash MS. The 6-min Push Tes... |
| Q17 | - |  |  | SI | The six-minute push test is conducted on a flat, s... |
| Q18 | - |  |  | SI | The distance between the two cones should be measu... |
| Q19 | - |  |  | SI | The distance travelled in the minutes is computed ... |
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
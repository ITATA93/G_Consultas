# SQLUser.MR_Prescriptions

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRESC_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| PRESC_Childsub | double |  |  | NO | Childsub |
| PRESC_Comments | varchar |  |  | SI | Comments |
| PRESC_Date | date |  |  | SI | Date |
| PRESC_Desc | varchar |  |  | SI | Description |
| PRESC_Doctor_DR | varchar |  | FK | SI | Des Ref Doctor |
| PRESC_DrugMaster_DR | bigint |  | FK | SI | Des Ref DrugMaster |
| PRESC_RowId | varchar |  |  | NO | - |
| PRESC_Time | time |  |  | SI | Time |
| PRESC_User_DR | bigint |  | FK | SI | Des Ref User_DR |
| Q01 | - |  |  | SI | Discharge agreed by intensivist |
| Q02 | - |  |  | SI | Ward notified / bed available |
| Q03 | - |  |  | SI | Taken off monitor - discharge / cords cleaned |
| Q04 | - |  |  | SI | Events and medical orders ceased |
| Q05 | - |  |  | SI | Allergies updated webpas |
| Q06 | - |  |  | SI | Webpas alerts reviewed |
| Q07 | - |  |  | SI | Lines removed / flushed, named and dated |
| Q08 | - |  |  | SI | Unused IVC removal |
| Q09 | - |  |  | SI | Dressings changed and dated |
| Q10 | - |  |  | SI | X-Rays collected from bed slot |
| Q11 | - |  |  | SI | Medications removed from drawer and fridge |
| Q12 | - |  |  | SI | Patients belongings and toiletries removed from ro... |
| Q13 | - |  |  | SI | Family aware of transfer |
| Q14 | - |  |  | SI | Critical care certificate an ANZICS form placed at... |
| Q15 | - |  |  | SI | Carefusion pumps changed to ward protocol |
| Q16 | - |  |  | SI | Active and finished medications printed to paper |
| Q17 | - |  |  | SI | Medical discharge printed to paper |
| Q18 | - |  |  | SI | Nursing discharge printed to paper |
| Q19 | - |  |  | SI | Time, date and bed number noted in admission book |
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
# SQLUser.AR_PatBillPaymAlloc

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYM_ParREf | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| ChildQ23DR | - |  |  | SI | Child Reference: Control |
| PAYM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| PAYM_ARRCA_DR | varchar |  | FK | SI | Des Ref ARRCA |
| PAYM_Amount | double |  |  | SI | Amount |
| PAYM_BillAmount | double |  |  | SI | Bill Amount |
| PAYM_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| PAYM_BillItem_DR | varchar |  | FK | SI | Des Ref BillItem |
| PAYM_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| PAYM_BillWriteOff_DR | varchar |  | FK | SI | Des Ref BillWriteOff |
| PAYM_Childsub | double |  |  | NO | Childsub |
| PAYM_ClaimAmount | double |  |  | SI | Claim Amount |
| PAYM_DiscAmtSoFar | double |  |  | SI | Discount Amounts So Far |
| PAYM_NotClaimAmount | double |  |  | SI | Not Claim Amount |
| PAYM_PaidSoFar | double |  |  | SI | Amount Allocated So Far - This value includes disc... |
| PAYM_PaymentsSoFar | double |  |  | SI | Payment Amounts So Far |
| PAYM_RowId | varchar |  |  | NO | - |
| PAYM_WOAmount | double |  |  | SI | WOAmount |
| PAYM_WOAmountSoFar | double |  |  | SI | WO Amount So Far |
| Q01 | - |  |  | SI | 1.- ¿Se utilizó previamente Contención Emocional? |
| Q02 | - |  |  | SI | 2.- ¿Se utilizó previamente Contención Ambiental? |
| Q03 | - |  |  | SI | 3.- ¿Se utilizó previamente Contención Farmacológi... |
| Q05 | - |  |  | SI | Contención Mecánica |
| Q06 | - |  |  | SI | 4. Existe Indicación Médica de Contención Mecánica |
| Q07 | - |  |  | SI | 5. Médico quien realiza Indicación |
| Q08 | - |  |  | SI | Fecha y Hora Indicación Médica de Contención Mecán... |
| Q09 | - |  |  | SI | Hora Indicación Médica de Contención Mecánica |
| Q10 | - |  |  | SI | 7. ¿Se inicia Contención Mecánica? |
| Q11 | - |  |  | SI | 8. Motivo de la Contención |
| Q12 | - |  |  | SI | Otro |
| Q13 | - |  |  | SI | 9. Tipo de Contención Utilizada |
| Q14 | - |  |  | SI | 10. Se educa a Paciente y/o Familia sobre medidas ... |
| Q15 | - |  |  | SI | 11. Persona quien recibe Educación |
| Q16 | - |  |  | SI | Fecha de Información a Familiar |
| Q17 | - |  |  | SI | Aceptación de Medidas |
| Q18 | - |  |  | SI | 14. Nombre de quien Acepta o Rechaza Medidas de Co... |
| Q19 | - |  |  | SI | 15. Relación con el paciente de Quien Acepta o Rec... |
| Q20 | - |  |  | SI | Otro |
| Q21 | - |  |  | SI | 16.  Medidas Adoptadas ante Rechazo Contención Mec... |
| Q22 | - |  |  | SI | Otros |
| Q24 | - |  |  | SI | 17. Fecha y Hora de término de contención |
| Q25 | - |  |  | SI | 17. Hora de término de contención |
| Q26 | - |  |  | SI | 18. Responsable del término de contención |
| Q27 | - |  |  | SI | 19. Estado de Término |
| Q28 | - |  |  | SI | 20. Motivo de la suspensión anticipada |
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
# SQLUser.ARC_PayAgreemDRG

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRG_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| DRG_ChargeDesc | varchar |  |  | SI | DRGChargeDescription |
| DRG_Childsub | double |  |  | NO | DRG_Childsub |
| DRG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRG_CreatedDate | date |  |  | SI | Created Date |
| DRG_CreatedTime | time |  |  | SI | Created Time |
| DRG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRG_DRGCode_DR | bigint |  | FK | SI | Des Ref DRGCode |
| DRG_Days | double |  |  | SI | Days |
| DRG_ItmMast_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DRG_OverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| DRG_OverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| DRG_PayorCode | varchar |  |  | SI | DRGPayorCode |
| DRG_RowId | varchar |  |  | NO | - |
| DRG_UpdatedDate | date |  |  | SI | Updated Date |
| DRG_UpdatedTime | time |  |  | SI | Updated Time |
| DRG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Responsable de Evaluación |
| Q03 | - |  |  | SI | 1. Mi problema para tragar me ha llevado a perder ... |
| Q04 | - |  |  | SI | 2. Mi problema para tragar interfiere con mi capac... |
| Q05 | - |  |  | SI | 3. Tragar líquidos me supene un esfuerzo extra |
| Q06 | - |  |  | SI | 4. Tragar sólidos me supone un esfuerzo extra |
| Q07 | - |  |  | SI | 5. Tragar pastillas me supone un esfuerzo extra |
| Q08 | - |  |  | SI | 6. Tragar es doloroso |
| Q09 | - |  |  | SI | 7. El Placer de comer se ve afectado por mi proble... |
| Q10 | - |  |  | SI | 8. Cuando trago, la comida se pega en mi garganta |
| Q11 | - |  |  | SI | 9. Toso cuando como |
| Q12 | - |  |  | SI | 10. Tragar es estresante |
| Q13 | - |  |  | SI | A. INSTRUCCIONES |
| Q14 | - |  |  | SI | B. PUNTUACIÓN |
| Q15 | - |  |  | SI | C.  QUÉ HACER AHORA |
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
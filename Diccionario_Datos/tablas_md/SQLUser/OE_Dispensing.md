# SQLUser.OE_Dispensing

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DSP_OEORE_ParRef | varchar | PK |  | NO | Des Ref to OEORE |
| DSP_Billed | varchar |  |  | SI | Billed Flag |
| DSP_CheckedBy_DR | bigint |  | FK | SI | Des Ref CheckedBy |
| DSP_CheckedDate | date |  |  | SI | CheckedDate |
| DSP_CheckedTime | time |  |  | SI | CheckedTime |
| DSP_ChildSub | numeric |  |  | NO | DSP Child Sub (New Key) |
| DSP_CollectedDate | date |  |  | SI | Collected Date |
| DSP_CollectedPatientRep | varchar |  |  | SI | CollectedPatientRep |
| DSP_CollectedTime | time |  |  | SI | Collected Time |
| DSP_CollectedUser_DR | bigint |  | FK | SI | Des Ref CollectedUser_DR |
| DSP_Date | date |  |  | SI | Dispensing Date |
| DSP_DispUOMQty | double |  |  | SI | Disp Uom Qty |
| DSP_ExtUnpackID | varchar |  |  | SI | ExtUnpackID |
| DSP_ExternalBatchID | varchar |  |  | SI | ExternalBatchID |
| DSP_ExternalBatchNo | varchar |  |  | SI | ExternalBatchNo |
| DSP_INCLB_DR | varchar |  | FK | SI | Des Ref to INCLB |
| DSP_IsBarcodeReturn | varchar |  |  | SI | Is Barcode Return |
| DSP_IsOverDueAdmin | varchar |  |  | SI | Is Over Due Administration |
| DSP_NurseManufUsedQty | double |  |  | SI | Nurse Manuf Used Qty |
| DSP_OECHG_DR | varchar |  | FK | SI | Des Ref to OECHG |
| DSP_PackedUser_DR | bigint |  | FK | SI | Packed User |
| DSP_Qty | double |  |  | NO | Quantity |
| DSP_ReasDispCorrect_DR | bigint |  | FK | SI | Des Ref INCReasDispCorrection |
| DSP_ReturnDate | date |  |  | SI | Return Date |
| DSP_ReturnLoc_DR | bigint |  | FK | SI | Des Ref ReturnLoc |
| DSP_ReturnQty | double |  |  | SI | Return Qty |
| DSP_ReturnTime | time |  |  | SI | Return Time |
| DSP_RowId | varchar |  |  | NO | - |
| DSP_SSUSR_DR | bigint |  | FK | SI | Des Ref SSUSR |
| DSP_Status | varchar |  |  | SI | Status |
| DSP_Time | time |  |  | SI | Dispensing Time |
| DSP_TotalReturnedQty | double |  |  | SI | TotalReturnedQty |
| DSP_UOM_DR | bigint |  | FK | SI | Des Ref UOM |
| Q01 | - |  |  | SI | Para medir el dolor en personas que no pueden verb... |
| Q02 | - |  |  | SI | Vocalización: lamentos, gruñidos, llanto |
| Q03 | - |  |  | SI | Expresión facial: expresión tensa, fruncida, lamen... |
| Q04 | - |  |  | SI | Cambios de lenguaje corporal: movimientos de nervi... |
| Q05 | - |  |  | SI | Cambios de comportamiento: aumento de confusión, r... |
| Q06 | - |  |  | SI | Cambios fisiológicos: temperatura, pulso o de&nbsp |
| Q07 | - |  |  | SI | Cambios físicos: cortes en la piel, áreas de presi... |
| Q08 | - |  |  | SI | Marque la opción que corresponda al tipo de dolor |
| Q09 | - |  |  | SI | 0-2 Sin Dolor |
| Q10 | - |  |  | SI | 3-7 Leve |
| Q11 | - |  |  | SI | 8-13 Moderado |
| Q12 | - |  |  | SI | 14+ Severo |
| Q13 | - |  |  | SI | Puntaje |
| Q14 | - |  |  | SI | Clasificación |
| Q15 | - |  |  | SI | 0 - 2 |
| Q16 | - |  |  | SI | Sin Dolor |
| Q17 | - |  |  | SI | 3 - 7 |
| Q18 | - |  |  | SI | Leve |
| Q19 | - |  |  | SI | 8 - 13 |
| Q20 | - |  |  | SI | Moderado |
| Q21 | - |  |  | SI | ≥ 14 |
| Q22 | - |  |  | SI | Severo |
| Q23 | - |  |  | SI | 0 - 2: Sin Dolor |
| Q24 | - |  |  | SI | 3 - 7: Leve |
| Q25 | - |  |  | SI | 8 - 13: Moderado |
| Q26 | - |  |  | SI | ≥ 14: Severo |
| Q27 | - |  |  | SI | Fecha |
| Q28 | - |  |  | SI | Hora |
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
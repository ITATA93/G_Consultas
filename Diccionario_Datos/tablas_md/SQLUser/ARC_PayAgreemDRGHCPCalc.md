# SQLUser.ARC_PayAgreemDRGHCPCalc

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGHCP_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| DRGHCP_AddOnOrdItem_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DRGHCP_AddOnPaymentPerc | double |  |  | SI | Add On Payment %  |
| DRGHCP_AddOnPharmPaymentPerc | double |  |  | SI | Add On Pharmacy Payment %  |
| DRGHCP_Childsub | double |  |  | NO | Childsub |
| DRGHCP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGHCP_Contract_DR | bigint |  | FK | SI | Des Ref BLCContractDetails |
| DRGHCP_CreatedDate | date |  |  | SI | Created Date |
| DRGHCP_CreatedTime | time |  |  | SI | Created Time |
| DRGHCP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGHCP_DateFrom | date |  |  | SI | Date From |
| DRGHCP_DateTo | date |  |  | SI | Date To |
| DRGHCP_HighCostLimitAmount | double |  |  | SI | High Cost Limit Amount |
| DRGHCP_LimPerOIAddOnOrdItm_DR | varchar |  | FK | SI | Des Ref ARCItmMast, Limit Per Order Item Add-On It... |
| DRGHCP_LimPerOIContract_DR | bigint |  | FK | SI | Limit Per Order Item contract, Des Ref BLCContract... |
| DRGHCP_LimPerOILimAmount | double |  |  | SI | Limit Per Order Item Limit Amount |
| DRGHCP_LimPerOIPaymentPerc | double |  |  | SI | Limit Per Order Item Payment %  |
| DRGHCP_LimSumOIAddOnOrdItm_DR | varchar |  | FK | SI | Des Ref ARCItmMast, Limit Per Sum of Order Items A... |
| DRGHCP_LimSumOIContract_DR | bigint |  | FK | SI | Limit Per Sum of Order Items contract, Des Ref BLC... |
| DRGHCP_LimSumOILimAmount | double |  |  | SI | Limit Per Sum of Order Items Limit Amount |
| DRGHCP_LimSumOIPaymentPerc | double |  |  | SI | Limit Per Sum of Order Items Payment %  |
| DRGHCP_PharmAddOnOrdItem_DR | varchar |  | FK | SI | Des Ref ARCItmMast, Pharmacy Add-On Item |
| DRGHCP_PharmContract_DR | bigint |  | FK | SI | Pharmacy contract, Des Ref BLCContractDetails |
| DRGHCP_PharmHighCostLimAmount | double |  |  | SI | Pharmacy High Cost Limit Amount |
| DRGHCP_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| DRGHCP_RowId | varchar |  |  | NO | - |
| DRGHCP_SurgHighCostContract_DR | bigint |  | FK | SI | Surgical High Cost contract, Des Ref BLCContractDe... |
| DRGHCP_SurgHighCostLimAmount | double |  |  | SI | Surgical High Cost Limit Amount |
| DRGHCP_SurgHighCostOrdItm_DR | varchar |  | FK | SI | Des Ref ARCItmMast, Surgical High Cost Add-On Item |
| DRGHCP_SurgHighCostPaymentPerc | double |  |  | SI | Surgical High Cost Payment %  |
| DRGHCP_UpdatedDate | date |  |  | SI | Updated Date |
| DRGHCP_UpdatedTime | time |  |  | SI | Updated Time |
| DRGHCP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nivel de Conciencia |
| Q02 | - |  |  | SI | Preguntar mes y edad |
| Q03 | - |  |  | SI | Ordenes (Abrir y cerrar los ojos - Apretar y abrir... |
| Q04 | - |  |  | SI | Mirada horizontal |
| Q05 | - |  |  | SI | Campos visuales |
| Q06 | - |  |  | SI | Parálisis facial |
| Q07 | - |  |  | SI | Examen Motor (ESI - examinar por 10 segs.) |
| Q08 | - |  |  | SI | Examen Motor (ESD - examinar por 10 segs.) |
| Q09 | - |  |  | SI | Examen Motor (EII - examinar por 5 segs.) |
| Q10 | - |  |  | SI | Examen Motor (EID - examinar por 5 segs.) |
| Q11 | - |  |  | SI | Ataxia de extremidades de un hemicuerpo (ES: Índic... |
| Q12 | - |  |  | SI | Sensibilidad al dolor |
| Q13 | - |  |  | SI | Lenguaje |
| Q14 | - |  |  | SI | Disartria |
| Q15 | - |  |  | SI | Extinción o inatención |
| Q16 | - |  |  | SI | Resultado |
| Q16ObsDR | - |  |  | SI | Resultado DR |
| Q17 | - |  |  | SI | Recomendaciones 1 al 4 |
| Q18 | - |  |  | SI | Recomendaciones 5 a 14 |
| Q19 | - |  |  | SI | Recomendaciones 15 a 20 |
| Q20 | - |  |  | SI | Recomendaciones 21 a 42 |
| Q21 | - |  |  | SI | Recomendaciones 1 al 4 MEUI |
| Q22 | - |  |  | SI | Recomendaciones 5 a 14 MEUI |
| Q23 | - |  |  | SI | Recomendaciones 15 a 20 MEUI |
| Q24 | - |  |  | SI | Recomendaciones 21 a 42 MEUI |
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
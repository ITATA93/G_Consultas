# SQLUser.ARC_PayAgreemDRGBaseRate

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGBR_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| DRGBR_ApplyEpisodeDateDRGCost | varchar |  |  | SI | Apply Episode Date for DRG Cost |
| DRGBR_ApplySurgHighCost | varchar |  |  | SI | Apply Surgical High Cost Calculation  |
| DRGBR_BaseRate | double |  |  | SI | Base Rate |
| DRGBR_Childsub | double |  |  | NO | Childsub |
| DRGBR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGBR_CreatedDate | date |  |  | SI | Created Date |
| DRGBR_CreatedTime | time |  |  | SI | Created Time |
| DRGBR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGBR_DRGCostTariff_DR | bigint |  | FK | SI | DRG Cost Tariff, Des Ref ARCTariff |
| DRGBR_DRGGap | double |  |  | SI | DRG Gap |
| DRGBR_DRGMargin | double |  |  | SI | DRG Margin |
| DRGBR_DateFrom | date |  |  | SI | Date From |
| DRGBR_DateTo | date |  |  | SI | Date To |
| DRGBR_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| DRGBR_HighOutlierMedARCIM_DR | varchar |  | FK | SI | High Outlier Medical, Des Ref ARCItmMast |
| DRGBR_HighOutlierProcARCIM_DR | varchar |  | FK | SI | High Outlier Procedural, Des Ref ARCItmMast |
| DRGBR_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| DRGBR_LTCARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DRGBR_LowOutlierARCIM_DR | varchar |  | FK | SI | Low Outlier, Des Ref ARCItmMast |
| DRGBR_OutlierARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DRGBR_OutlierDiscMed | double |  |  | SI | Outlier Discount - Medical |
| DRGBR_OutlierDiscSurg | double |  |  | SI | Outlier Discount - Surgical |
| DRGBR_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| DRGBR_RowId | varchar |  |  | NO | - |
| DRGBR_SplitPayorPerc | double |  |  | SI | Split Payor Percentage |
| DRGBR_TransHighOutlierARCIM_DR | varchar |  | FK | SI | Transfer High Outlier, Des Ref ARCItmMast |
| DRGBR_TransLowOutlierARCIM_DR | varchar |  | FK | SI | Transfer Low Outlier, Des Ref ARCItmMast |
| DRGBR_UpdatedDate | date |  |  | SI | Updated Date |
| DRGBR_UpdatedTime | time |  |  | SI | Updated Time |
| DRGBR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Responsable Evaluación |
| Q03 | - |  |  | SI | 1. Lenguaje |
| Q04 | - |  |  | SI | 2. Salivación |
| Q05 | - |  |  | SI | 3. Deglución |
| Q06 | - |  |  | SI | 4. Escritura |
| Q07 | - |  |  | SI | 5.a. Cortado de comida y uso de utensilios (pacien... |
| Q08 | - |  |  | SI | 5.b. Cortado de comida y uso de utensilios (pacien... |
| Q09 | - |  |  | SI | 6. Vestidoehigiene |
| Q10 | - |  |  | SI | 7. Voltearse en la cama y ajustar las cobijas |
| Q11 | - |  |  | SI | 8. Caminar |
| Q12 | - |  |  | SI | 9. Subir escaleras |
| Q13 | - |  |  | SI | 10. Disnea |
| Q14 | - |  |  | SI | 11. Ortopnea |
| Q15 | - |  |  | SI | 12. Insuficiencia respiratoria |
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
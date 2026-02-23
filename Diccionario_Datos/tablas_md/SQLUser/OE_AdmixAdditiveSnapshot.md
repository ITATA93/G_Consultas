# SQLUser.OE_AdmixAdditiveSnapshot

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITMS_ParRef | varchar | PK |  | NO | OE_OrdAdmix Parent Reference |
| ITMS_Additive_DR | varchar |  | FK | NO | Additive |
| ITMS_Childsub | double |  |  | NO | Childsub |
| ITMS_Date | date |  |  | SI | Date |
| ITMS_Dose | double |  |  | SI | Dose |
| ITMS_DoseUOM_DR | bigint |  | FK | SI | Dose UOM |
| ITMS_DrugDeliveryPerUOM | varchar |  |  | SI | Drug Delivery Rate Per UOM |
| ITMS_DrugDeliveryRate | double |  |  | SI | Drug Delivery Rate |
| ITMS_DrugDeliveryUOM_DR | bigint |  | FK | SI | Drug Delivery Rate UOM |
| ITMS_MaxDrugDeliveryRate | double |  |  | SI | Max Drug Delivery Rate |
| ITMS_MinDrugDeliveryRate | double |  |  | SI | Min Drug Delivery Rate |
| ITMS_PCALoadingDose | double |  |  | SI | PCA Loading Dose |
| ITMS_PCALoadingDoseUOM_DR | bigint |  | FK | SI | PCA Loading Dose UOM |
| ITMS_PerQuantity | double |  |  | SI | Quantity |
| ITMS_PerUOM_DR | bigint |  | FK | SI | UOM |
| ITMS_Quantity | double |  |  | SI | Quantity |
| ITMS_ReqPercentage | double |  |  | SI | Required Percentage |
| ITMS_RowId | varchar |  |  | NO | - |
| ITMS_Significant | varchar |  |  | SI | Significant |
| ITMS_Time | time |  |  | SI | Time |
| ITMS_UOM_DR | bigint |  | FK | SI | UOM |
| Q01 | - |  |  | SI | Location |
| Q02 | - |  |  | SI | Appearance |
| Q03 | - |  |  | SI | Cap. refill time |
| Q04 | - |  |  | SI | Comments |
| Q05 | - |  |  | SI | Type |
| Q06 | - |  |  | SI | Warmth |
| Q07 | - |  |  | SI | Doppler |
| Q08 | - |  |  | SI | Turgidity |
| Q09 | - |  |  | SI | Location |
| Q10 | - |  |  | SI | Appearance |
| Q11 | - |  |  | SI | Cap. refill time |
| Q12 | - |  |  | SI | Comments |
| Q13 | - |  |  | SI | Type |
| Q14 | - |  |  | SI | Warmth |
| Q15 | - |  |  | SI | Doppler |
| Q16 | - |  |  | SI | Turgidity |
| Q17 | - |  |  | SI | Flap 1 |
| Q18 | - |  |  | SI | Flap 2 |
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
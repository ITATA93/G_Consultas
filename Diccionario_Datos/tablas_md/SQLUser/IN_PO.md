# SQLUser.IN_PO

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IN_PO | bigint | PK |  | NO | - |
| ChildQ07DR | - |  |  | SI | Child Reference: COLPOSCOPÍA ANORMAL |
| INPO_APCVM_DR | bigint |  | FK | NO | Des Ref to APCVM |
| INPO_Approved | varchar |  |  | SI | PO Approved |
| INPO_CTCUR_DR | bigint |  | FK | NO | Des Ref to CTCUR |
| INPO_Cancelled | varchar |  |  | SI | Cancelled |
| INPO_Completed | varchar |  |  | SI | PO Completed |
| INPO_CreditTerm_DR | bigint |  | FK | SI | Des Ref CreditTerm |
| INPO_Date | date |  |  | NO | Date of Purchase Order |
| INPO_DateCancelFullFilled | date |  |  | SI | DateCancelFullFilled |
| INPO_DateNeeded | date |  |  | SI | DateNeeded |
| INPO_ExRate | double |  |  | SI | Exchange Rate |
| INPO_FullFilled | varchar |  |  | SI | FullFilled |
| INPO_HandChg | double |  |  | NO | Handling Charges |
| INPO_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| INPO_No | varchar |  |  | NO | Purchase Order No |
| INPO_POSessionNo | varchar |  |  | SI | PO Session No |
| INPO_ReasonCancFullFilled_DR | bigint |  | FK | SI | Des Ref ReasonCancFullFilled |
| INPO_Reference_DR | bigint |  | FK | SI | Des Ref to INPO_Reference |
| INPO_Remarks | varchar |  |  | SI | Remarks |
| INPO_SSUSR_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| INPO_TimeCancelFullFilled | time |  |  | SI | TimeCancelFullFilled |
| INPO_TotalApprovedNetValue | double |  |  | SI | Total Value of Approved Quantity Items (Net, exclu... |
| INPO_TotalApprovedTaxValue | double |  |  | SI | Total Tax Value of Approved Quantity Items
Total ... |
| INPO_TotalNetValue | double |  |  | SI | Total Value of Items (Net, excludes Tax)
Total of... |
| INPO_TotalTaxValue | double |  |  | SI | Total Tax Value of Items
Total of children INPOIt... |
| INPO_TransDate | date |  |  | SI | TransDate |
| INPO_TransTime | time |  |  | SI | TransTime |
| INPO_UserCancFullFilled_DR | bigint |  | FK | SI | Des Ref UserCancFullFilled |
| INPO_UserCompleted | varchar |  |  | SI | User Completed |
| INPO_UserCompleted_DR | bigint |  | FK | SI | Des Ref User |
| INPO_UserUpdated_DR | bigint |  | FK | SI | User Last Updated |
| INPO_ValueUnderMin | varchar |  |  | SI | TotalNetValue is less than Vendor's Minimum PO Val... |
| INPO_VendorMinValue | double |  |  | SI | Vendor's Minimum PO Value at update (or at complet... |
| Q01 | - |  |  | SI | Fecha de realización |
| Q02 | - |  |  | SI | Hora de realización |
| Q03 | - |  |  | SI | Indicación de procedimiento |
| Q04 | - |  |  | SI | Cérvix conizable |
| Q05 | - |  |  | SI | COLPOSCOPÍA NORMAL |
| Q06 | - |  |  | SI | COLPOSCOPÍA INSATISFACTORIA |
| Q08 | - |  |  | SI | HALLAZGOS MISCELÁNEOS |
| Q09 | - |  |  | SI | Observaciones (hallazgos misceláneos) |
| Q10 | - |  |  | SI | APARIENCIA DE LA VULVA |
| Q11 | - |  |  | SI | Observaciones (vulva) |
| Q12 | - |  |  | SI | IMPRESIÓN DIAGNÓSTICA |
| Q14 | - |  |  | SI | CÉRVIX |
| Q15 | - |  |  | SI | SITIO DE LA(S) BIOPSIA(S) |
| Q16 | - |  |  | SI | Observaciones (biopsia) |
| Q17 | - |  |  | SI | OBSERVACIONES GENERALES |
| Q18 | - |  |  | SI | PROCEDIMIENTO REALIZADO POR |
| Q19 | - |  |  | SI | Fotografía |
| Q19TxtOnly | - |  |  | SI | Fotografía Plain Text Only |
| Q20 | - |  |  | SI | Observaciones (cérvix) |
| Q21 | - |  |  | SI | Agregar Diagrama Colposcopía |
| Q22 | - |  |  | SI | Cervix |
| Q23 | - |  |  | SI | Para agregar una imagen digital, haga click sobre ... |
| Q24 | - |  |  | SI | Éste le dirigirá a una ventana que le permitirá su... |
| Q25 | - |  |  | SI | Colposcopía |
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
# SQLUser.PA_AdmInsuranceBGLimits

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LIM_ParRef | varchar | PK |  | NO | PA_AdmInsurance Parent Reference |
| LIM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| LIM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| LIM_AuthClinicians | varchar |  |  | SI | AuthClinicians |
| LIM_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| LIM_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| LIM_Childsub | double |  |  | NO | Childsub |
| LIM_CoPaymentPercentage | double |  |  | SI | Co-Payment Percentage |
| LIM_DiscountAmt | double |  |  | SI | Discount Amt |
| LIM_DiscountComments | varchar |  |  | SI | Discount Comments |
| LIM_DiscountPerc | double |  |  | SI | Discount Percentage |
| LIM_DiscountReason_DR | bigint |  | FK | SI | Des Ref DiscountReason |
| LIM_MaxCoPayAmountBeforeTax | double |  |  | SI | Maximum Co-Payment Amount Before Tax |
| LIM_MaxCoPaymentAmount | double |  |  | SI | Maximum Co-Payment Amount |
| LIM_MaxCoverage | double |  |  | SI | Max Coverage |
| LIM_MaxCoverageUsed | double |  |  | SI | Max Coverage Used |
| LIM_MaxDailyAmount | double |  |  | SI | MaxDailyAmount |
| LIM_MinCoPaymentAmount | double |  |  | SI | Minimum Co-Payment Amount |
| LIM_OrderStatus_DR | bigint |  | FK | SI | Des Ref OrderStatus |
| LIM_PatientAmount | double |  |  | SI | Patient Amount |
| LIM_PayorPerc | double |  |  | SI | PayorPerc |
| LIM_Price | double |  |  | SI | Price |
| LIM_Priority_DR | bigint |  | FK | SI | Des Ref OECPriority |
| LIM_Qty | double |  |  | SI | Qty allowed |
| LIM_QtyUsed | double |  |  | SI | Qty Used |
| LIM_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| LIM_RowId | varchar |  |  | NO | - |
| LIM_UpdateDate | date |  |  | SI | Update Date |
| LIM_UpdateTime | time |  |  | SI | Update Time |
| LIM_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Long QT Syndrome (LQTS) Diagnostic Criteria (Updat... |
| Q04 | - |  |  | SI | A. Syncope (mutually exclusive) |
| Q05 | - |  |  | SI | A. QTc |
| Q06 | - |  |  | SI | Calculated by Bazett's formula where QTc = QT/√RR |
| Q07 | - |  |  | SI | B. QTc† 4th minute of recovery from exercise stres... |
| Q08 | - |  |  | SI | Calculated by Bazett's formula where QTc = QT/√RR |
| Q09 | - |  |  | SI | C. Torsades de Pointes (mutually exclusive) |
| Q10 | - |  |  | SI | D. T - wave alternans |
| Q11 | - |  |  | SI | D. T - wave alternans |
| Q12 | - |  |  | SI | E. Notched T wave in 3 leads |
| Q13 | - |  |  | SI | F. Low heart rate for age (resting heart rate belo... |
| Q14 | - |  |  | SI | B. Congenital deafness |
| Q15 | - |  |  | SI | For questions A and B in Family History, the same ... |
| Q16 | - |  |  | SI | A. Family members with definite LQTS |
| Q17 | - |  |  | SI | B. Unexplained sudden cardiac death below age 30 a... |
| Q18 | - |  |  | SI | Score |
| Q19 | - |  |  | SI | Classification |
| Q20 | - |  |  | SI | ≤ 1 |
| Q21 | - |  |  | SI | Low probability of Long QT Syndrome |
| Q22 | - |  |  | SI | 1.5 – 3 |
| Q23 | - |  |  | SI | Intermediate probability of Long QT Syndrome |
| Q24 | - |  |  | SI | ≥ 3.5 |
| Q25 | - |  |  | SI | High probability of Long QT Syndrome |
| Q26 | - |  |  | SI | <= 1: Low probability of Long QT Syndrome |
| Q27 | - |  |  | SI | 1.5 – 3: Intermediate probability of Long QT Syndr... |
| Q28 | - |  |  | SI | >= 3.5: High probability of Long QT Syndrome |
| Q29 | - |  |  | SI | A tool to assess the patient’s probability of Long... |
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
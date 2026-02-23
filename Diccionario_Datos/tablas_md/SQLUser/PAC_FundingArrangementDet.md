# SQLUser.PAC_FundingArrangementDet

**Schema:** SQLUser
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_FundingArrangement Parent Reference |
| DET_AdmSource | varchar |  |  | SI | AdmSource |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DET_ContractRole | varchar |  |  | SI | ContractRole |
| DET_ContractType | varchar |  |  | SI | ContractType |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | Date From |
| DET_DateTo | date |  |  | SI | DateTo |
| DET_DischDestin | varchar |  |  | SI | DischDestin |
| DET_RowId | varchar |  |  | NO | - |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Stage of assessment |
| Q04 | - |  |  | SI | Side of assessment	 |
| Q05 | - |  |  | SI | Supine to side-lying (onto intact side) |
| Q06 | - |  |  | SI | Supine to sitting over side of bed |
| Q07 | - |  |  | SI | Balance sitting	 |
| Q08 | - |  |  | SI | Sitting to standing |
| Q09 | - |  |  | SI | Walking |
| Q10 | - |  |  | SI | Upper arm function |
| Q11 | - |  |  | SI | Hand movements |
| Q12 | - |  |  | SI | Advanced hand activities |
| Q13 | - |  |  | SI | Comments |
| Q14 | - |  |  | SI | Physical therapist |
| Q15 | - |  |  | SI | Date and time of assessment |
| Q16 | - |  |  | SI | Occupational therapist |
| Q17 | - |  |  | SI | Date and time of assessment |
| Q18 | - |  |  | SI | Time |
| Q19 | - |  |  | SI | • The test should preferably be carried out in a q... |
| Q20 | - |  |  | SI | • The test should be carried out when patient is m... |
| Q21 | - |  |  | SI | Record should be made if patient is under the infl... |
| Q22 | - |  |  | SI | • Patient should be dressed in suitable street clo... |
| Q23 | - |  |  | SI | • Each item is recorded on a scale of 0 to 6. |
| Q24 | - |  |  | SI | • All items are to be performed independently by t... |
| Q25 | - |  |  | SI | • Patient should be scored on their best performan... |
| Q26 | - |  |  | SI | Because the scale is designed to score patient's b... |
| Q27 | - |  |  | SI | • Sensitivity to the patient is necessary to enabl... |
| Q28 | - |  |  | SI | • Instructions should be repeated and demonstratio... |
| Q29 | - |  |  | SI | • The order of administration of items can be vari... |
| Q30 | - |  |  | SI | • If patient becomes emotionally labile at any sta... |
| Q31 | - |  |  | SI | The examiner should cease testing, and rescore thi... |
| Q32 | - |  |  | SI | • If performance is scored differently on left and... |
| Q33 | - |  |  | SI | The patient should be informed when being timed. |
| Q34 | - |  |  | SI | Equipment required |
| Q35 | - |  |  | SI | • Low wide plinth |
| Q36 | - |  |  | SI | • Stopwatch |
| Q37 | - |  |  | SI | • Polystyrene cup |
| Q38 | - |  |  | SI | • Eight jellybeans |
| Q39 | - |  |  | SI | • Two teacups |
| Q40 | - |  |  | SI | • Rubber ball approximately 14 - cm (5 - in) diame... |
| Q41 | - |  |  | SI | • Stool |
| Q42 | - |  |  | SI | • Comb |
| Q43 | - |  |  | SI | • Top of a pen |
| Q44 | - |  |  | SI | • Table |
| Q45 | - |  |  | SI | • Dessert spoon and water |
| Q46 | - |  |  | SI | • Pen |
| Q47 | - |  |  | SI | • Prepared sheet for drawing lines |
| Q48 | - |  |  | SI | • Cylindrical object such as a jar |
| Q49 | - |  |  | SI | 0 - 40 |
| Q50 | - |  |  | SI | The higher the score – the higher functioning the ... |
| Q51 | - |  |  | SI | Time |
| Q52 | - |  |  | SI | The Motor Assessment Scale (MAS) is a performance ... |
| Q53 | - |  |  | SI | (1988) modified item descriptions and deleted the ... |
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
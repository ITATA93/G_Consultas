# SQLUser.OR_An_Oper_SecProc

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPR_ParRef | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | My pain was caused by physical activity |
| Q04 | - |  |  | SI | Physical activity makes my pain worse |
| Q05 | - |  |  | SI | Physical activity might harm my back… |
| Q06 | - |  |  | SI | I should not do physical activities which (might) ... |
| Q07 | - |  |  | SI | I cannot do physical activities which (might) make... |
| Q08 | - |  |  | SI | My pain was caused by my work or by an accident at... |
| Q09 | - |  |  | SI | My work aggravated my pain |
| Q10 | - |  |  | SI | I have a claim for compensation for my pain |
| Q11 | - |  |  | SI | My work is too heavy for me |
| Q12 | - |  |  | SI | My work makes, or would make, my pain worse |
| Q13 | - |  |  | SI | My work might harm my back |
| Q14 | - |  |  | SI | I should not do my normal work with my present pai... |
| Q15 | - |  |  | SI | I cannot do my normal work with my present pain |
| Q16 | - |  |  | SI | I cannot do my normal work till my pain is treated |
| Q17 | - |  |  | SI | I do not think that i will be back to my normal wo... |
| Q18 | - |  |  | SI | I do not think that i will ever be able to go back... |
| Q19 | - |  |  | SI | George SZ, Fritz JM, Childs JD. Investigation of E... |
| Q20 | - |  |  | SI | Physical Activity Subscale (FABQPA |
| Q21 | - |  |  | SI | Work Subscale (FABQW |
| Q22 | - |  |  | SI | For each statement please select any number from 0... |
| Q23 | - |  |  | SI | This instrument quantifies the role of fear-avoida... |
| Q24 | - |  |  | SI | J Orthop Sports Phys Ther 2008 |
| Q25 | - |  |  | SI | Burton AK, Waddell G, Tillotson KM, Summerton N. I... |
| Q26 | - |  |  | SI | Spine. 1999 Dec 1 |
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
| SPR_Childsub | double |  |  | NO | Childsub |
| SPR_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| SPR_Operation_DR | bigint |  | FK | SI | Des Ref Operation |
| SPR_RowId | varchar |  |  | NO | - |
| SPR_StatePPP_DR | bigint |  | FK | SI | Des Ref StatePPP |
| SPR_SurgeonAssist_DR | varchar |  | FK | SI | Des Ref Surgeon Assistant |
| SPR_Surgeon_DR | varchar |  | FK | SI | Des Ref Surgeon |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
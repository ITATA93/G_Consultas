# SQLUser.OE_OrdReviewStatus

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REVST_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| Q01 | - |  |  | SI | Maintaining a Posture |
| Q02 | - |  |  | SI | Give the subject instructions for each item as wri... |
| Q03 | - |  |  | SI | 1. Sitting without support |
| Q04 | - |  |  | SI | Examiner: Have the subject sit on a bench / mat wi... |
| Q05 | - |  |  | SI | 2. Standing with support |
| Q06 | - |  |  | SI | Examiner: Have the subject stand, providing suppor... |
| Q06A | - |  |  | SI | Do not consider the quality of the stance. |
| Q07 | - |  |  | SI | 3. Standing without support |
| Q08 | - |  |  | SI | Examiner: Have the subject stand without support. ... |
| Q08A | - |  |  | SI | Do not consider the quality of the stance. |
| Q09 | - |  |  | SI | 4. Standing on nonparetic leg |
| Q10 | - |  |  | SI | Examiner: Have the subject stand on the nonparetic... |
| Q10A | - |  |  | SI | Do not consider how the subject accomplishes the t... |
| Q11 | - |  |  | SI | 5. Standing on paretic leg |
| Q12 | - |  |  | SI | Examiner: Have the subject stand on the paretic le... |
| Q12A | - |  |  | SI | Do not consider how the subject accomplishes the t... |
| Q13 | - |  |  | SI | Maintaining Posture SUBTOTAL |
| Q14 | - |  |  | SI | Changing a Posture |
| Q15 | - |  |  | SI | 6. Supine to paretic side lateral |
| Q16 | - |  |  | SI | Examiner: Begin with the subject in supine on a tr... |
| Q16A | - |  |  | SI | Assist as necessary. Evaluate the subject's perfor... |
| Q17 | - |  |  | SI | 7. Supine to nonparetic side lateral |
| Q18 | - |  |  | SI | Examiner: Begin with the subject in supine on a tr... |
| Q18A | - |  |  | SI | Assist as necessary. Evaluate the subject's perfor... |
| Q19 | - |  |  | SI | 8. Supine to sitting up on the edge of the mat |
| Q20 | - |  |  | SI | Examiner: Begin with the subject in supine on a tr... |
| Q20A | - |  |  | SI | Assist as necessary. Evaluate the subject's perfor... |
| Q24 | - |  |  | SI | 9. Sitting on the edge of the mat to supine |
| Q25 | - |  |  | SI | Examiner: Begin with the subject sitting on the ed... |
| Q25A | - |  |  | SI | Evaluate the subject's performance on the amount o... |
| Q27 | - |  |  | SI | 10. Sitting to standing up |
| Q28 | - |  |  | SI | Examiner: Begin with the subject sitting on the ed... |
| Q28A | - |  |  | SI | Assist if necessary. Evaluate the subject's perfor... |
| Q30 | - |  |  | SI | 11. Standing up to sitting down |
| Q31 | - |  |  | SI | Examiner: Begin with the subject standing by the e... |
| Q32 | - |  |  | SI | Assist if necessary. Evaluate the subject's perfor... |
| Q33 | - |  |  | SI | 12. Standing, picking up a pencil from the floor |
| Q34 | - |  |  | SI | Examiner: Begin with the subject standing. Instruc... |
| Q34A | - |  |  | SI | Evaluate the subject's performance on the amount o... |
| Q36 | - |  |  | SI | Changing Posture SUBTOTAL |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Time |
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
| REVST_Childsub | double |  |  | NO | Childsub |
| REVST_Date | date |  |  | SI | Date |
| REVST_DateReviewDue | date |  |  | SI | DateReviewDue  |
| REVST_DateReviewed | date |  |  | SI | DateReviewed |
| REVST_PhOrdRevAuthClin_DR | varchar |  | FK | SI | Des Ref AuthoriseClinician |
| REVST_PhOrdRevDate | date |  |  | SI | REVSTphOrdReviewDate |
| REVST_PhOrdRevSignOffDate | date |  |  | SI | REVSTPhOrdReviewDate |
| REVST_PhOrdRevSignOffTime | time |  |  | SI | REVSTPhOrdReviewTime |
| REVST_PhOrdRevSignOffUser_DR | bigint |  | FK | SI | Des Ref AuthoriseClinician |
| REVST_PhOrdRevTime | time |  |  | SI | REVSTPhOrdReviewTime |
| REVST_PhOrdRevUser_DR | bigint |  | FK | SI | Des Ref SSUSR |
| REVST_PhOrdReviewFlag | varchar |  |  | SI | REVSTPhOrdReviewFlag |
| REVST_ReviewStatus_DR | bigint |  | FK | SI | Des Ref ReviewStatus |
| REVST_ReviewType | varchar |  |  | SI | Review Type |
| REVST_RowId | varchar |  |  | NO | - |
| REVST_Time | time |  |  | SI | Time |
| REVST_TimeReviewDue | time |  |  | SI | Time |
| REVST_TimeReviewed | time |  |  | SI | TimeReviewed |
| REVST_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
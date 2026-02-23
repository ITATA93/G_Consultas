# questionnaire.QTCAHPRHPAS

> Postural Assessment Scale for Stroke Patients (PASS)

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Postural Assessment Scale for Stroke Patients (PASS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Maintaining a Posture |
| Q02 | varchar |  |  | SI | Give the subject instructions for each item as wri... |
| Q03 | varchar |  |  | SI | 1. Sitting without support |
| Q04 | varchar |  |  | SI | Examiner: Have the subject sit on a bench / mat wi... |
| Q05 | varchar |  |  | SI | 2. Standing with support |
| Q06 | varchar |  |  | SI | Examiner: Have the subject stand, providing suppor... |
| Q06A | varchar |  |  | SI | Do not consider the quality of the stance. |
| Q07 | varchar |  |  | SI | 3. Standing without support |
| Q08 | varchar |  |  | SI | Examiner: Have the subject stand without support. ... |
| Q08A | varchar |  |  | SI | Do not consider the quality of the stance. |
| Q09 | varchar |  |  | SI | 4. Standing on nonparetic leg |
| Q10 | varchar |  |  | SI | Examiner: Have the subject stand on the nonparetic... |
| Q10A | varchar |  |  | SI | Do not consider how the subject accomplishes the t... |
| Q11 | varchar |  |  | SI | 5. Standing on paretic leg |
| Q12 | varchar |  |  | SI | Examiner: Have the subject stand on the paretic le... |
| Q12A | varchar |  |  | SI | Do not consider how the subject accomplishes the t... |
| Q13 | varchar |  |  | SI | Maintaining Posture SUBTOTAL |
| Q14 | varchar |  |  | SI | Changing a Posture |
| Q15 | varchar |  |  | SI | 6. Supine to paretic side lateral |
| Q16 | varchar |  |  | SI | Examiner: Begin with the subject in supine on a tr... |
| Q16A | varchar |  |  | SI | Assist as necessary. Evaluate the subject's perfor... |
| Q17 | varchar |  |  | SI | 7. Supine to nonparetic side lateral |
| Q18 | varchar |  |  | SI | Examiner: Begin with the subject in supine on a tr... |
| Q18A | varchar |  |  | SI | Assist as necessary. Evaluate the subject's perfor... |
| Q19 | varchar |  |  | SI | 8. Supine to sitting up on the edge of the mat |
| Q20 | varchar |  |  | SI | Examiner: Begin with the subject in supine on a tr... |
| Q20A | varchar |  |  | SI | Assist as necessary. Evaluate the subject's perfor... |
| Q24 | varchar |  |  | SI | 9. Sitting on the edge of the mat to supine |
| Q25 | varchar |  |  | SI | Examiner: Begin with the subject sitting on the ed... |
| Q25A | varchar |  |  | SI | Evaluate the subject's performance on the amount o... |
| Q27 | varchar |  |  | SI | 10. Sitting to standing up |
| Q28 | varchar |  |  | SI | Examiner: Begin with the subject sitting on the ed... |
| Q28A | varchar |  |  | SI | Assist if necessary. Evaluate the subject's perfor... |
| Q30 | varchar |  |  | SI | 11. Standing up to sitting down |
| Q31 | varchar |  |  | SI | Examiner: Begin with the subject standing by the e... |
| Q32 | varchar |  |  | SI | Assist if necessary. Evaluate the subject's perfor... |
| Q33 | varchar |  |  | SI | 12. Standing, picking up a pencil from the floor |
| Q34 | varchar |  |  | SI | Examiner: Begin with the subject standing. Instruc... |
| Q34A | varchar |  |  | SI |  Evaluate the subject's performance on the amount ... |
| Q36 | varchar |  |  | SI | Changing Posture SUBTOTAL |
| Q41 | date |  |  | SI | Date |
| Q42 | time |  |  | SI | Time |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
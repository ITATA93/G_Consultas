# questionnaire.QTCCAFF

> Consent for Artificial Formula Feeding

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Consent for Artificial Formula Feeding

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | The Ten Steps to Successful Breastfeeding indicate... |
| Q02 | varchar |  |  | SI | Each individual artificial feed or formula must ha... |
| Q03 | varchar |  |  | SI | We know that breast milk is the best food for infa... |
| Q04 | varchar |  |  | SI | feedings, so that you can make an informed decisio... |
| Q05 | varchar |  |  | SI | The World Health Organisation, and the National He... |
| Q06 | varchar |  |  | SI | Mothers should be made aware of the importance of ... |
| Q07 | varchar |  |  | SI | Artificial formula feeds are any fluid other than ... |
| Q08 | varchar |  |  | SI | Our Midwifery Unit does not routinely give artific... |
| Q09 | varchar |  |  | SI | 1. Even one artificial formula feed in the newborn... |
| Q10 | varchar |  |  | SI | Increasing the risk of allergies which can be life... |
| Q11 | varchar |  |  | SI | 2. Artificial formula is harder to digest than bre... |
| Q12 | varchar |  |  | SI | 3. Giving artificial formula interferes with mothe... |
| Q13 | varchar |  |  | SI | 4. Baby’s suck on a bottle teat is different to su... |
| Q14 | varchar |  |  | SI | This consent is for |
| Q15 | varchar |  |  | SI | I have been advised to give formula for the follow... |
| Q16 | varchar |  |  | SI | I have made an informed decision for this artifici... |
| Q17 | varchar |  |  | SI | I acknowledge the above information and understand... |
| Q18 | varchar |  |  | SI | I acknowledge that I have had adequate opportunity... |
| Q19 | longvarbinary |  |  | SI | Mothers Signature |
| Q19UDt | date |  |  | SI | Mothers Signature Last Updated Date |
| Q19UTm | time |  |  | SI | Mothers Signature Last Updated Time |
| Q20 | date |  |  | SI | Date |
| Q21 | time |  |  | SI | Time |
| Q22 | varchar |  |  | SI | What are artificial formula feeds? |
| Q23 | varchar |  |  | SI | unless there is a medical indication. |
| Q24 | varchar |  |  | SI | Interpreter services required |
| Q25 | varchar |  |  | SI | Interpreter services provided |
| Q26 | varchar |  |  | SI | Information above provided to patient |
| Q27 | varchar |  |  | SI | Information provided by |
| Q28 | varchar |  |  | SI | Reason for parent requesting a supplementary feed |
| Q29 | varchar |  |  | SI | Other reason |
| Q30 | varchar |  |  | SI | Notes |
| Q31 | varchar |  |  | SI | I understand the information which has been provid... |
| Q32 | varchar |  |  | SI | My questions and concerns have been discussed and ... |
| Q33 | varchar |  |  | SI | I request my baby to have a supplementary feed(s) ... |
| Q34 | varchar |  |  | SI | Notes |
| Q35 | varchar |  |  | SI | Parent / Guardian name |
| Q36 | longvarbinary |  |  | SI | Signature |
| Q36UDt | date |  |  | SI | Signature Last Updated Date |
| Q36UTm | time |  |  | SI | Signature Last Updated Time |
| Q37 | varchar |  |  | SI | This consent only applies to the complementary fee... |
| Q38 | varchar |  |  | SI | Dummy1 |
| Q39 | varchar |  |  | SI | Dummy2 |
| Q40 | varchar |  |  | SI | Dummy3 |
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
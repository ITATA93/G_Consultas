# SQLUser.LBC_AnatomicalSite

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCAS_RowID | bigint | PK |  | NO | - |
| LBCAS_Code | varchar |  |  | NO | Code |
| LBCAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCAS_CodeTranslated | varchar |  |  | SI | - |
| LBCAS_CreatedDate | date |  |  | SI | Created Date |
| LBCAS_CreatedTime | time |  |  | SI | Created Time |
| LBCAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCAS_DateFrom | date |  |  | SI | Effective date for the record |
| LBCAS_DateTo | date |  |  | SI | Last day the record is active  |
| LBCAS_Desc | varchar |  |  | NO | Description |
| LBCAS_DescTranslated | varchar |  |  | SI | - |
| LBCAS_Owner | varchar |  |  | SI | Owner |
| LBCAS_Sequence | double |  |  | SI | Display Sequence |
| LBCAS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCAS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | The Ten Steps to Successful Breastfeeding indicate... |
| Q02 | - |  |  | SI | Each individual artificial feed or formula must ha... |
| Q03 | - |  |  | SI | We know that breast milk is the best food for infa... |
| Q04 | - |  |  | SI | feedings, so that you can make an informed decisio... |
| Q05 | - |  |  | SI | The World Health Organisation, and the National He... |
| Q06 | - |  |  | SI | Mothers should be made aware of the importance of ... |
| Q07 | - |  |  | SI | Artificial formula feeds are any fluid other than ... |
| Q08 | - |  |  | SI | Our Midwifery Unit does not routinely give artific... |
| Q09 | - |  |  | SI | 1. Even one artificial formula feed in the newborn... |
| Q10 | - |  |  | SI | Increasing the risk of allergies which can be life... |
| Q11 | - |  |  | SI | 2. Artificial formula is harder to digest than bre... |
| Q12 | - |  |  | SI | 3. Giving artificial formula interferes with mothe... |
| Q13 | - |  |  | SI | 4. Baby’s suck on a bottle teat is different to su... |
| Q14 | - |  |  | SI | This consent is for |
| Q15 | - |  |  | SI | I have been advised to give formula for the follow... |
| Q16 | - |  |  | SI | I have made an informed decision for this artifici... |
| Q17 | - |  |  | SI | I acknowledge the above information and understand... |
| Q18 | - |  |  | SI | I acknowledge that I have had adequate opportunity... |
| Q19 | - |  |  | SI | Mothers Signature |
| Q19UDt | - |  |  | SI | Mothers Signature Last Updated Date |
| Q19UTm | - |  |  | SI | Mothers Signature Last Updated Time |
| Q20 | - |  |  | SI | Date |
| Q21 | - |  |  | SI | Time |
| Q22 | - |  |  | SI | What are artificial formula feeds? |
| Q23 | - |  |  | SI | unless there is a medical indication. |
| Q24 | - |  |  | SI | Interpreter services required |
| Q25 | - |  |  | SI | Interpreter services provided |
| Q26 | - |  |  | SI | Information above provided to patient |
| Q27 | - |  |  | SI | Information provided by |
| Q28 | - |  |  | SI | Reason for parent requesting a supplementary feed |
| Q29 | - |  |  | SI | Other reason |
| Q30 | - |  |  | SI | Notes |
| Q31 | - |  |  | SI | I understand the information which has been provid... |
| Q32 | - |  |  | SI | My questions and concerns have been discussed and ... |
| Q33 | - |  |  | SI | I request my baby to have a supplementary feed(s) ... |
| Q34 | - |  |  | SI | Notes |
| Q35 | - |  |  | SI | Parent / Guardian name |
| Q36 | - |  |  | SI | Signature |
| Q36UDt | - |  |  | SI | Signature Last Updated Date |
| Q36UTm | - |  |  | SI | Signature Last Updated Time |
| Q37 | - |  |  | SI | This consent only applies to the complementary fee... |
| Q38 | - |  |  | SI | Dummy1 |
| Q39 | - |  |  | SI | Dummy2 |
| Q40 | - |  |  | SI | Dummy3 |
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
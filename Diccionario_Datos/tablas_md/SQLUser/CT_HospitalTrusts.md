# SQLUser.CT_HospitalTrusts

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRUST_ParRef | bigint | PK |  | NO | CT_Hospital Parent Reference |
| Q01 | - |  |  | SI | Likelihood of appendicitis based on symptoms, sign... |
| Q02 | - |  |  | SI | Right lower quadrant tenderness |
| Q03 | - |  |  | SI | Elevated temperature (37.3°C or 99.1°F) |
| Q04 | - |  |  | SI | Rebound tenderness |
| Q05 | - |  |  | SI | Migration of pain to the right lower quadrant |
| Q06 | - |  |  | SI | Anorexia |
| Q07 | - |  |  | SI | Nausea or Vomiting |
| Q08 | - |  |  | SI | Leukocytosis > 10,000 |
| Q09 | - |  |  | SI | Leukocyte left shift |
| Q10 | - |  |  | SI | 0 - 4: Unlikely appendicitis by the Alvarado score |
| Q11 | - |  |  | SI | 5 - 6: Possible appendicitis by the Alvarado score |
| Q12 | - |  |  | SI | 7 - 8: Probable / Likely appendicitis by the Alvar... |
| Q13 | - |  |  | SI | 9 - 10: Definite appendicitis by the Alvarado scor... |
| Q14 | - |  |  | SI | Unlikely appendicitis by the Alvarado score |
| Q15 | - |  |  | SI | Possible appendicitis by the Alvarado score |
| Q16 | - |  |  | SI | Probable / Likely appendicitis by the Alvarado sco... |
| Q17 | - |  |  | SI | Definite appendicitis by the Alvarado score |
| Q18 | - |  |  | SI | Score |
| Q19 | - |  |  | SI | Classification |
| Q20 | - |  |  | SI | 0 - 4 |
| Q21 | - |  |  | SI | 5 - 6 |
| Q22 | - |  |  | SI | 7 - 8 |
| Q23 | - |  |  | SI | 9 - 10 |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Time |
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
| TRUST_Childsub | double |  |  | NO | Childsub |
| TRUST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRUST_CreatedDate | date |  |  | SI | Created Date |
| TRUST_CreatedTime | time |  |  | SI | Created Time |
| TRUST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRUST_DateFrom | date |  |  | SI | Date From |
| TRUST_DateTo | date |  |  | SI | Date To |
| TRUST_Rowid | varchar |  |  | NO | - |
| TRUST_Trust_DR | bigint |  | FK | SI | Des Ref Trust |
| TRUST_UpdatedDate | date |  |  | SI | Updated Date |
| TRUST_UpdatedTime | time |  |  | SI | Updated Time |
| TRUST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
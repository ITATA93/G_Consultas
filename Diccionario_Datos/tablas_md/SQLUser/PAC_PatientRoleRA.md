# SQLUser.PAC_PatientRoleRA

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATROL_RowId | bigint | PK |  | NO | - |
| PATROL_Code | varchar |  |  | NO | Code |
| PATROL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PATROL_CreatedDate | date |  |  | SI | Created Date |
| PATROL_CreatedTime | time |  |  | SI | Created Time |
| PATROL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PATROL_DateFrom | date |  |  | SI | Date From |
| PATROL_DateTo | date |  |  | SI | Date To |
| PATROL_Desc | varchar |  |  | NO | Description |
| PATROL_Owner | varchar |  |  | SI | Owner |
| PATROL_UpdatedDate | date |  |  | SI | Updated Date |
| PATROL_UpdatedTime | time |  |  | SI | Updated Time |
| PATROL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of examination |
| Q02 | - |  |  | SI | Time of examination |
| Q03 | - |  |  | SI | Non-Speech |
| Q04 | - |  |  | SI | I. Facial Musculature - (Sensory - CN V) (Motor - ... |
| Q05 | - |  |  | SI | At rest |
| Q06 | - |  |  | SI | Squinting |
| Q07 | - |  |  | SI | Raise eyebrows |
| Q08 | - |  |  | SI | Facial weakness |
| Q09 | - |  |  | SI | Other |
| Q10 | - |  |  | SI | II. Labial Musculature - |
| Q11 | - |  |  | SI | (Sensory - CN V) (Motor - CN VII) |
| Q12 | - |  |  | SI | At rest |
| Q13 | - |  |  | SI | Smile (show teeth) |
| Q14 | - |  |  | SI | Pursing |
| Q15 | - |  |  | SI | Smile to pursing |
| Q16 | - |  |  | SI | Close lips and puff cheeks |
| Q17 | - |  |  | SI | Close lips as tightly as possible |
| Q18 | - |  |  | SI | Close lips and resist pulling |
| Q19 | - |  |  | SI | Other |
| Q20 | - |  |  | SI | III. Mandibular Musculature - |
| Q21 | - |  |  | SI | (Sensory / Motor CN V) |
| Q22 | - |  |  | SI | At rest |
| Q23 | - |  |  | SI | Open jaw wide |
| Q24 | - |  |  | SI | Move jaw side to side |
| Q25 | - |  |  | SI | Resist examiner's attempt to force the lower jaw o... |
| Q26 | - |  |  | SI | Resist examiner's attempt to close the jaw while p... |
| Q27 | - |  |  | SI | Pathologic reflex |
| Q28 | - |  |  | SI | Other |
| Q29 | - |  |  | SI | IV. Tongue Musculature - |
| Q30 | - |  |  | SI | (Sensory CN VII (taste ant) 2/3, XI (post 1/3)) (M... |
| Q31 | - |  |  | SI | At rest |
| Q32 | - |  |  | SI | Tongue Protrusion |
| Q33 | - |  |  | SI | Tongue lateralization |
| Q34 | - |  |  | SI | Tongue elevation |
| Q35 | - |  |  | SI | Tongue strength |
| Q36 | - |  |  | SI | Patient reports change in taste |
| Q37 | - |  |  | SI | Other |
| Q38 | - |  |  | SI | V. Palato-pharyngeal Musculature - |
| Q39 | - |  |  | SI | (Sensory / Motor CN X) |
| Q40 | - |  |  | SI | At rest |
| Q41 | - |  |  | SI | Take a deep breath and let it out through mouth |
| Q42 | - |  |  | SI | Say 'ah, ah, ah |
| Q43 | - |  |  | SI | Gag reflex |
| Q44 | - |  |  | SI | Dry swallow |
| Q45 | - |  |  | SI | Voluntary cough |
| Q46 | - |  |  | SI | Shortness of breath |
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
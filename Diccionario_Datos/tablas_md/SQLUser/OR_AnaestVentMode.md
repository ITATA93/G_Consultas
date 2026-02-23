# SQLUser.OR_AnaestVentMode

**Schema:** SQLUser
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAVENT_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANAVENT_Childsub | double |  |  | NO | Childsub |
| ANAVENT_RowId | varchar |  |  | NO | - |
| ANAVENT_Type_DR | bigint |  | FK | SI | Des Ref ORCVentilationMode |
| Q01 | - |  |  | SI | Date of test |
| Q02 | - |  |  | SI | Time of test |
| Q03 | - |  |  | SI | Gait aid(s) used |
| Q04 | - |  |  | SI | Time taken to complete test (in sec) |
| Q05 | - |  |  | SI | Comments |
| Q06 | - |  |  | SI | General Information |
| Q07 | - |  |  | SI | The subject is required to sequentially step over ... |
| Q08 | - |  |  | SI | At the start of the test, the subject stands in Sq... |
| Q09 | - |  |  | SI | The aim is to step as fast as possible into each s... |
| Q10 | - |  |  | SI | Test procedure may be demonstrated, one practice t... |
| Q11 | - |  |  | SI | Two trials are then performed, and the better time... |
| Q12 | - |  |  | SI | Timing starts when the first foot contacts the flo... |
| Q13 | - |  |  | SI | Instructions: |
| Q14 | - |  |  | SI | Repeat a trial if the subject: |
| Q15 | - |  |  | SI | Fails to complete the sequence successfully |
| Q16 | - |  |  | SI | Loses balance |
| Q17 | - |  |  | SI | Makes contact with the cane |
| Q18 | - |  |  | SI | Subjects who are unable to face forward during the... |
| Q19 | - |  |  | SI | Any assistive device used during the test are note... |
| Q20 | - |  |  | SI | Set up |
| Q21 | - |  |  | SI | Place 4 canes / rods in a + pattern on the floor. ... |
| Q22 | - |  |  | SI | Patient Instructions |
| Q23 | - |  |  | SI | “Try to complete the sequence as fast and as safel... |
| Q24 | - |  |  | SI | Score |
| Q25 | - |  |  | SI | Classification |
| Q26 | - |  |  | SI | Label the lower left square 1, and move clockwise ... |
| Q27 | - |  |  | SI | 0 |
| Q28 | - |  |  | SI | A score was not recorded |
| Q29 | - |  |  | SI | 5 - 14 |
| Q30 | - |  |  | SI | Patient is NOT at potential risk for falls |
| Q31 | - |  |  | SI | ≥ 15 |
| Q32 | - |  |  | SI | Patient is at potential risk for falls |
| Q33 | - |  |  | SI | 0: A score was not recorded |
| Q34 | - |  |  | SI | 5: ≤5 seconds  - Please review the interpretation ... |
| Q35 | - |  |  | SI | 6: 6 seconds  - Please review the interpretation o... |
| Q36 | - |  |  | SI | The Four Square Step Test (FSST) is used to assess... |
| Q37 | - |  |  | SI | 7: 7 seconds  - Please review the interpretation o... |
| Q38 | - |  |  | SI | 8: 8 seconds  - Please review the interpretation o... |
| Q39 | - |  |  | SI | 9: 9 seconds  - Please review the interpretation o... |
| Q40 | - |  |  | SI | 10: 10 seconds  - Please review the interpretation... |
| Q41 | - |  |  | SI | 11: 11 seconds  - Please review the interpretation... |
| Q42 | - |  |  | SI | 12: 12 seconds  - Please review the interpretation... |
| Q43 | - |  |  | SI | 13: 13 seconds  - Please review the interpretation... |
| Q44 | - |  |  | SI | 14: 14 seconds  - Please review the interpretation... |
| Q45 | - |  |  | SI | 15: 15 seconds  - Please review the interpretation... |
| Q46 | - |  |  | SI | 16: 16 seconds  - Please review the interpretation... |
| Q47 | - |  |  | SI | 17: 17 seconds  - Please review the interpretation... |
| Q48 | - |  |  | SI | 18: 18 seconds  - Please review the interpretation... |
| Q49 | - |  |  | SI | 19: 19 seconds  - Please review the interpretation... |
| Q50 | - |  |  | SI | 20: 20 seconds  - Please review the interpretation... |
| Q51 | - |  |  | SI | 21: 21 seconds  - Please review the interpretation... |
| Q52 | - |  |  | SI | 22: 22 seconds  - Please review the interpretation... |
| Q53 | - |  |  | SI | 23: 23 seconds  - Please review the interpretation... |
| Q54 | - |  |  | SI | 24: 24 seconds  - Please review the interpretation... |
| Q55 | - |  |  | SI | 25: ≥25 seconds - Please review the interpretation... |
| Q56 | - |  |  | SI | Population |
| Q57 | - |  |  | SI | Threshold indicating falls risk |
| Q58 | - |  |  | SI | Parkinson's disease |
| Q59 | - |  |  | SI | > 9.68 seconds |
| Q60 | - |  |  | SI | Acute stroke |
| Q61 | - |  |  | SI | > 15 seconds |
| Q62 | - |  |  | SI | Geriatric population |
| Q63 | - |  |  | SI | > 15 seconds |
| Q64 | - |  |  | SI | Lower extremity amputees |
| Q65 | - |  |  | SI | > 24 seconds |
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
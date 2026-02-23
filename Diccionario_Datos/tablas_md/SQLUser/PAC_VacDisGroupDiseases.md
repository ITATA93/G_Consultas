# SQLUser.PAC_VacDisGroupDiseases

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIS_ParRef | bigint | PK |  | NO | PAC_VaccinationDesease Parent Reference |
| DIS_Childsub | double |  |  | NO | Childsub |
| DIS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DIS_CreatedDate | date |  |  | SI | Created Date |
| DIS_CreatedTime | time |  |  | SI | Created Time |
| DIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DIS_DateFrom | date |  |  | SI | DateFrom |
| DIS_DateTo | date |  |  | SI | DateTo |
| DIS_RowId | varchar |  |  | NO | - |
| DIS_UpdatedDate | date |  |  | SI | Updated Date |
| DIS_UpdatedTime | time |  |  | SI | Updated Time |
| DIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DIS_VaccDisease_DR | bigint |  | FK | SI | Des Ref PACVacDis |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Is this a multiple pregnancy? |
| Q04 | - |  |  | SI | Transverse or oblique lie? |
| Q05 | - |  |  | SI | Single cephalic pregnancy < 37 weeks gestation? |
| Q06 | - |  |  | SI | Is the woman nulliparous? |
| Q07 | - |  |  | SI | Is this a breech pregnancy? |
| Q08 | - |  |  | SI | Spontaneous labour? |
| Q09 | - |  |  | SI | Is this a breech pregnancy? |
| Q10 | - |  |  | SI | Previous uterine scars? |
| Q11 | - |  |  | SI | Spontaneous labour? |
| Q12 | - |  |  | SI | Score |
| Q13 | - |  |  | SI | Classification |
| Q14 | - |  |  | SI | 1 |
| Q15 | - |  |  | SI | Group 1 - Nulliparous women with a single cephalic... |
| Q16 | - |  |  | SI | 2 |
| Q17 | - |  |  | SI | Group 2 - Nulliparous women with a single cephalic... |
| Q18 | - |  |  | SI | 3 |
| Q19 | - |  |  | SI | Group 3 - Multiparous women without a previous CS,... |
| Q20 | - |  |  | SI | 4 |
| Q21 | - |  |  | SI | Group 4 - Multiparous women without a previous CS,... |
| Q22 | - |  |  | SI | 5 |
| Q23 | - |  |  | SI | Group 5 - All multiparous women with at least one ... |
| Q24 | - |  |  | SI | 6 |
| Q25 | - |  |  | SI | Group 6 - All nulliparous women with a single bree... |
| Q26 | - |  |  | SI | 7 |
| Q27 | - |  |  | SI | Group 7 - All multiparous women with a single bree... |
| Q28 | - |  |  | SI | 8 |
| Q29 | - |  |  | SI | Group 8 - All women with multiple pregnancies incl... |
| Q30 | - |  |  | SI | 9 |
| Q31 | - |  |  | SI | Group 9 - All women with a single pregnancy with a... |
| Q32 | - |  |  | SI | 10 |
| Q33 | - |  |  | SI | Group 10 - All women with a single cephalic pregna... |
| Q34 | - |  |  | SI | 1: Group 1 - Nulliparous women with a single cepha... |
| Q35 | - |  |  | SI | 2: Group 2 - Nulliparous women with a single cepha... |
| Q36 | - |  |  | SI | 3: Group 3 - Multiparous women without a previous ... |
| Q37 | - |  |  | SI | 4: Group 4 - Multiparous women without a previous ... |
| Q38 | - |  |  | SI | 5: Group 5 - All multiparous women with at least o... |
| Q39 | - |  |  | SI | 6: Group 6 - All nulliparous women with a single b... |
| Q40 | - |  |  | SI | 7: Group 7 - All multiparous women with a single b... |
| Q41 | - |  |  | SI | 8: Group 8 - All women with multiple pregnancies i... |
| Q42 | - |  |  | SI | 9: Group 9 - All women with a single pregnancy wit... |
| Q43 | - |  |  | SI | 10: Group 10 - All women with a single cephalic pr... |
| Q44 | - |  |  | SI | The system classifies all women into one of 10 cat... |
| Q45 | - |  |  | SI | The categories are based on 5 basic obstetric char... |
| Q46 | - |  |  | SI | (parity, number of foetuses, previous caesarean se... |
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
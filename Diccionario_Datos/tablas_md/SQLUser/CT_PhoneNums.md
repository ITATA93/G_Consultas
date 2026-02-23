# SQLUser.CT_PhoneNums

**Schema:** SQLUser
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHNUM_RowId | bigint | PK |  | NO | - |
| PHNUM_Category_DR | bigint |  | FK | SI | Des Ref Category |
| PHNUM_Code | varchar |  |  | NO | Code |
| PHNUM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHNUM_CreatedDate | date |  |  | SI | Created Date |
| PHNUM_CreatedTime | time |  |  | SI | Created Time |
| PHNUM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHNUM_Desc | varchar |  |  | NO | Description |
| PHNUM_Owner | varchar |  |  | SI | Owner |
| PHNUM_UpdatedDate | date |  |  | SI | Updated Date |
| PHNUM_UpdatedTime | time |  |  | SI | Updated Time |
| PHNUM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Session |
| Q02 | - |  |  | SI | Scale |
| Q03 | - |  |  | SI | Speech |
| Q04 | - |  |  | SI | Language |
| Q05 | - |  |  | SI | Voice |
| Q06 | - |  |  | SI | Fluency |
| Q07 | - |  |  | SI | Cognitive-communication |
| Q08 | - |  |  | SI | Swallowing |
| Q09 | - |  |  | SI | Impairment |
| Q10 | - |  |  | SI | Activity Limitation |
| Q11 | - |  |  | SI | Speech impairment |
| Q12 | - |  |  | SI | Language impairment |
| Q13 | - |  |  | SI | Voice impairment |
| Q14 | - |  |  | SI | Fluency impairment |
| Q15 | - |  |  | SI | Cognitive-communication impairment |
| Q16 | - |  |  | SI | Swallowing impairment |
| Q17 | - |  |  | SI | Speech activity limitation |
| Q18 | - |  |  | SI | Language activity limitation |
| Q19 | - |  |  | SI | Voice activity limitation |
| Q20 | - |  |  | SI | Fluency activity limitation |
| Q21 | - |  |  | SI | Cognitive-communication activity limitation |
| Q22 | - |  |  | SI | Swallowing activity limitation |
| Q23 | - |  |  | SI | Participation restriction |
| Q24 | - |  |  | SI | Distress / Wellbeing |
| Q25 | - |  |  | SI | Carer distress / wellbeing |
| Q26 | - |  |  | SI | General comments |
| Q27 | - |  |  | SI | IMPAIRMENT OF EITHER STRUCTURE OR FUNCTION (AS APP... |
| Q28 | - |  |  | SI | Impairments are problems in body structure (anatom... |
| Q29 | - |  |  | SI | 0 The most severe presentation of impairment |
| Q30 | - |  |  | SI | 1 Severe presentation of this impairment |
| Q31 | - |  |  | SI | 2 Moderate / Severe presentation |
| Q32 | - |  |  | SI | 3 Moderate presentation |
| Q33 | - |  |  | SI | 4 Mild presentation |
| Q34 | - |  |  | SI | 5 No impairment of structure or function |
| Q35 | - |  |  | SI | ACTIVITY LIMITATION (AS APPROPRIATE TO AGE) |
| Q36 | - |  |  | SI | Activity limitation results from the difficulty in... |
| Q37 | - |  |  | SI | 0 Complete difficulty |
| Q38 | - |  |  | SI | 1 Severe difficulty |
| Q39 | - |  |  | SI | 2 Moderate / severe difficulty |
| Q40 | - |  |  | SI | 3 Moderate difficulty |
| Q41 | - |  |  | SI | 4 Mild difficulty |
| Q42 | - |  |  | SI | 5 No difficulty |
| Q43 | - |  |  | SI | PARTICIPATION RESTRICTION (AS APPROPRIATE TO AGE) |
| Q44 | - |  |  | SI | Participation restrictions are difficulties the in... |
| Q45 | - |  |  | SI | Clinicians should ask themselves: “given their pro... |
| Q46 | - |  |  | SI | 0 Unable to fulfill social, work, educational or f... |
| Q47 | - |  |  | SI | 1 Severe difficulties in fulfilling social, work, ... |
| Q48 | - |  |  | SI | Can only rarely reach potential with maximum assis... |
| Q49 | - |  |  | SI | 2 Moderately severe difficulties in fulfilling soc... |
| Q50 | - |  |  | SI | Limited involvement in decision-making. Control ov... |
| Q51 | - |  |  | SI | Usually reaches potential with maximum assistance. |
| Q52 | - |  |  | SI | 3 Moderate difficulties in fulfilling social, work... |
| Q53 | - |  |  | SI | Control over environment in more than one setting.... |
| Q54 | - |  |  | SI | 4 Mild difficulties in fulfilling social, work, ed... |
| Q55 | - |  |  | SI | Reaches potential with little assistance. |
| Q56 | - |  |  | SI | 5 No difficulties in fulfilling social, work, educ... |
| Q57 | - |  |  | SI | Control over environment in all settings. Reaches ... |
| Q58 | - |  |  | SI | DISTRESS / WELLBEING (AS APPROPRIATE TO AGE): |
| Q59 | - |  |  | SI | The level of concern experienced by the individual... |
| Q60 | - |  |  | SI | 0 High and consistent levels of distress or concer... |
| Q61 | - |  |  | SI | 1 Severe concern, becomes distressed or concerned ... |
| Q62 | - |  |  | SI | 2 Moderately severe concern. Frequent emotional en... |
| Q63 | - |  |  | SI | 3 Moderate concern. May be able to manage emotions... |
| Q64 | - |  |  | SI | 4 Mild concern. Able to manage emotions in most si... |
| Q65 | - |  |  | SI | 5 Able to cope with most situations. Accepts and u... |
| Q66 | - |  |  | SI | Date |
| Q67 | - |  |  | SI | Time |
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
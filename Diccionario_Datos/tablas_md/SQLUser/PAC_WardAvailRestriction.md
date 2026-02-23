# SQLUser.PAC_WardAvailRestriction

**Schema:** SQLUser
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AVR_ParRef | bigint | PK |  | NO | PAC_Ward Parent Reference |
| AVR_Childsub | double |  |  | NO | Childsub |
| AVR_CreatedDate | date |  |  | SI | Created Date |
| AVR_CreatedTime | time |  |  | SI | Created Time |
| AVR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AVR_DateFrom | date |  |  | SI | Date From |
| AVR_DateTo | date |  |  | SI | Date To |
| AVR_Friday | varchar |  |  | SI | Friday |
| AVR_Monday | varchar |  |  | SI | Monday |
| AVR_ReasonNotAvail_DR | bigint |  | FK | SI | Des Ref ReasonNotAvail |
| AVR_RowId | varchar |  |  | NO | - |
| AVR_Saturday | varchar |  |  | SI | Saturday |
| AVR_Sunday | varchar |  |  | SI | Sunday |
| AVR_Thursday | varchar |  |  | SI | Thursday |
| AVR_TimeFrom | time |  |  | SI | Time From |
| AVR_TimeTo | time |  |  | SI | Time To |
| AVR_Tuesday | varchar |  |  | SI | Tuesday |
| AVR_UpdatedDate | date |  |  | SI | Updated Date |
| AVR_UpdatedTime | time |  |  | SI | Updated Time |
| AVR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| AVR_Wednesday | varchar |  |  | SI | Wednesday |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Over the past year |
| Q04 | - |  |  | SI | In takes me 30 minutes or more to fall asleep. |
| Q05 | - |  |  | SI | I am awake 30 minutes or more during the night. |
| Q06 | - |  |  | SI | I am awake 30 minutes or more prior to my schedule... |
| Q07 | - |  |  | SI | I am tired, fatigued or sleepy during the day. |
| Q08 | - |  |  | SI | I sleep better if i go to bed before 9:00 pm and w... |
| Q09 | - |  |  | SI | I sleep better if i go to bed late (after 1:00 am)... |
| Q10 | - |  |  | SI | I fall asleep at inappropriate times or places. |
| Q11 | - |  |  | SI | I have been told that i snore. |
| Q12 | - |  |  | SI | I wake up during the night choking or gasping. |
| Q13 | - |  |  | SI | I have been told i stop breathing when i sleep. |
| Q14 | - |  |  | SI | I feel uncomfortable sensations in my legs, especi... |
| Q15 | - |  |  | SI | I have an urge to move my legs that is worse in th... |
| Q16 | - |  |  | SI | I wake up frequently during the night for no reaso... |
| Q17 | - |  |  | SI | I have experienced sudden muscle weakness when lau... |
| Q18 | - |  |  | SI | I have been told that i walk, talk, eat or act str... |
| Q19 | - |  |  | SI | I have nightmares. |
| Q20 | - |  |  | SI | For no reason, i awaken suddenly, startled, and fe... |
| Q21 | - |  |  | SI | Subscale |
| Q22 | - |  |  | SI | Insomnia |
| Q23 | - |  |  | SI | Circadian rythm |
| Q24 | - |  |  | SI | Narcolepsy |
| Q25 | - |  |  | SI | Obstructive sleep apnea |
| Q26 | - |  |  | SI | Restless legs syndrome |
| Q27 | - |  |  | SI | Parasomnias |
| Q28 | - |  |  | SI | Condition |
| Q29 | - |  |  | SI | Insomnia |
| Q30 | - |  |  | SI | Circadian rhythm disorder |
| Q31 | - |  |  | SI | Narcolepsy |
| Q32 | - |  |  | SI | Obstructive sleep apnea |
| Q33 | - |  |  | SI | Restless leg syndrome |
| Q34 | - |  |  | SI | Parasomnias |
| Q35 | - |  |  | SI | Score range |
| Q36 | - |  |  | SI | 0 to 12 |
| Q37 | - |  |  | SI | 0 to 6 |
| Q38 | - |  |  | SI | 0 to 6 |
| Q39 | - |  |  | SI | 0 to 12 |
| Q40 | - |  |  | SI | 0 to 9 |
| Q41 | - |  |  | SI | 0 to 9 |
| Q42 | - |  |  | SI | Cut-point for further screening |
| Q43 | - |  |  | SI | &gt |
| Q44 | - |  |  | SI | - |
| Q45 | - |  |  | SI | &gt |
| Q46 | - |  |  | SI | &gt |
| Q47 | - |  |  | SI | &gt |
| Q48 | - |  |  | SI | - |
| Q49 | - |  |  | SI | The sleep disorders checklist (sds-cl-17) is an in... |
| Q50 | - |  |  | SI | (insomnia, obstructive sleep apnoea, restless legs... |
| Q51 | - |  |  | SI | Source: klingman kj, jungquist cr, perlis ml. intr... |
| Q52 | - |  |  | SI | The Sleep Disorders Checklist (SDS-CL-17) is an in... |
| Q53 | - |  |  | SI | Please refer to the score table in the guidelines |
| Q54 | - |  |  | SI | (insomnia, obstructive sleep apnoea, restless legs... |
| Q55 | - |  |  | SI | Insomnia |
| Q56 | - |  |  | SI | Circadian rythm |
| Q57 | - |  |  | SI | Narcolepsy |
| Q58 | - |  |  | SI | Obstructive sleep apnea |
| Q59 | - |  |  | SI | Restless legs syndrome |
| Q60 | - |  |  | SI | Parasomnias |
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
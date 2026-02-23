# SQLUser.IN_Adj

**Schema:** SQLUser
**Columnas:** 157
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INAD_RowId | bigint | PK |  | NO | - |
| INAD_Completed | varchar |  |  | SI | Completed |
| INAD_CustomDate | date |  |  | SI | CustomDate |
| INAD_CustomText | varchar |  |  | SI | CustomText |
| INAD_Date | date |  |  | NO | Date of Adjustment |
| INAD_DateLastUpdated | date |  |  | SI | DateLastUpdated |
| INAD_INST_DR | bigint |  | FK | SI | Des Ref to INST |
| INAD_NewTransType | varchar |  |  | SI | NewTransType |
| INAD_No | varchar |  |  | NO | Adjustment Reference No |
| INAD_ReasonAdj_DR | bigint |  | FK | SI | Des Ref ReasonAdj |
| INAD_Remarks | varchar |  |  | SI | Remarks |
| INAD_SSUSR_DR | bigint |  | FK | NO | Des Ref to SSUSR |
| INAD_Time | time |  |  | NO | Adjustment time |
| INAD_TimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Head circumference (cm) |
| Q05 | - |  |  | SI | Weight (gm) |
| Q06 | - |  |  | SI | Pregnancy plurality |
| Q07 | - |  |  | SI | Baby number (eg: twin 1) |
| Q08 | - |  |  | SI | Estimated date of intrauterine fetal death (IUFD) |
| Q09 | - |  |  | SI | Maceration degree |
| Q10 | - |  |  | SI | Maceration degree notes |
| Q100 | - |  |  | SI | Fingers - Form notes |
| Q101 | - |  |  | SI | Webbing fingers notes |
| Q102 | - |  |  | SI | If other number of thumbs, please describe |
| Q103 | - |  |  | SI | Estimated gestation of IUFD |
| Q104 | - |  |  | SI | Revised gestational age |
| Q11 | - |  |  | SI | Head |
| Q12 | - |  |  | SI | Head notes |
| Q13 | - |  |  | SI | Eyes |
| Q14 | - |  |  | SI | Eyes notes |
| Q15 | - |  |  | SI | Nose |
| Q16 | - |  |  | SI | Nostrils |
| Q17 | - |  |  | SI | Nostrils notes |
| Q18 | - |  |  | SI | Mouth |
| Q19 | - |  |  | SI | Upper lip |
| Q20 | - |  |  | SI | Palate |
| Q21 | - |  |  | SI | Mandible |
| Q22 | - |  |  | SI | Mandible notes |
| Q23 | - |  |  | SI | Ears |
| Q24 | - |  |  | SI | Ears notes |
| Q25 | - |  |  | SI | Neck |
| Q26 | - |  |  | SI | Neck notes |
| Q27 | - |  |  | SI | Chest |
| Q28 | - |  |  | SI | Chest notes |
| Q29 | - |  |  | SI | Abdomen |
| Q30 | - |  |  | SI | Back |
| Q31 | - |  |  | SI | Back notes |
| Q32 | - |  |  | SI | Anus |
| Q33 | - |  |  | SI | Anus notes |
| Q34 | - |  |  | SI | Gender |
| Q35 | - |  |  | SI | Male |
| Q36 | - |  |  | SI | Penis |
| Q37 | - |  |  | SI | Hypospadias level of opening |
| Q38 | - |  |  | SI | Scrotum |
| Q39 | - |  |  | SI | Scrotum notes |
| Q40 | - |  |  | SI | Testes |
| Q41 | - |  |  | SI | Testes notes |
| Q42 | - |  |  | SI | Female |
| Q43 | - |  |  | SI | Urethral opening |
| Q44 | - |  |  | SI | Vaginal introitus |
| Q45 | - |  |  | SI | Clitoris |
| Q46 | - |  |  | SI | Clitoris notes |
| Q47 | - |  |  | SI | Ambiguous sex |
| Q48 | - |  |  | SI | Ambiguous sex notes |
| Q49 | - |  |  | SI | Limbs - Length |
| Q50 | - |  |  | SI | Please describe short segment |
| Q51 | - |  |  | SI | Limbs - Length notes |
| Q52 | - |  |  | SI | Limbs - Form |
| Q53 | - |  |  | SI | Limbs - Form notes |
| Q54 | - |  |  | SI | Hands - Appearance |
| Q55 | - |  |  | SI | Hands - Length notes |
| Q56 | - |  |  | SI | Fingers - Number present |
| Q57 | - |  |  | SI | If other number of fingers, please describe |
| Q58 | - |  |  | SI | Fingers - Position |
| Q59 | - |  |  | SI | Fingers - Position notes |
| Q60 | - |  |  | SI | Fingers - Form |
| Q61 | - |  |  | SI | Fingers - Form notes |
| Q62 | - |  |  | SI | Webbing fingers (syndactyly) |
| Q63 | - |  |  | SI | Webbing fingers notes |
| Q64 | - |  |  | SI | Thumbs - Number present |
| Q65 | - |  |  | SI | If other number of thumbs, please describe |
| Q66 | - |  |  | SI | Thumbs - Position |
| Q67 | - |  |  | SI | Thumbs - Position notes |
| Q68 | - |  |  | SI | Thumbs - Form |
| Q69 | - |  |  | SI | Thumbs notes |
| Q70 | - |  |  | SI | Finger nails - Presence |
| Q71 | - |  |  | SI | Finger nails notes |
| Q72 | - |  |  | SI | Feet - Appearance |
| Q73 | - |  |  | SI | Feet notes |
| Q74 | - |  |  | SI | Toes - Number present |
| Q75 | - |  |  | SI | If other number of toes, please describe |
| Q76 | - |  |  | SI | Revised gestational age weeks |
| Q77 | - |  |  | SI | Revised gestation based on |
| Q78 | - |  |  | SI | Summary of key findings |
| Q79 | - |  |  | SI | Length (cm) |
| Q80 | - |  |  | SI | Estimated gestation of IUFD weeks |
| Q81 | - |  |  | SI | Estimated gestation of IUFD days |
| Q82 | - |  |  | SI | weeks |
| Q83 | - |  |  | SI | days |
| Q84 | - |  |  | SI | Nose notes |
| Q85 | - |  |  | SI | Mouth notes |
| Q86 | - |  |  | SI | Upper lip notes |
| Q87 | - |  |  | SI | Palate notes |
| Q88 | - |  |  | SI | Abdomen notes |
| Q89 | - |  |  | SI | Penis notes |
| Q90 | - |  |  | SI | Urethral opening notes |
| Q91 | - |  |  | SI | Vaginal introitus notes |
| Q92 | - |  |  | SI | Please describe short segment |
| Q93 | - |  |  | SI | Toe - Spacing |
| Q94 | - |  |  | SI | Toes notes |
| Q95 | - |  |  | SI | Toes nails - Presence |
| Q96 | - |  |  | SI | Toe nails notes |
| Q97 | - |  |  | SI | Revised gestational age (days) |
| Q98 | - |  |  | SI | weeks |
| Q99 | - |  |  | SI | days |
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
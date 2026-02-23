# SQLUser.OEC_BodySite

**Schema:** SQLUser
**Columnas:** 153
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BODS_RowId | bigint | PK |  | NO | - |
| BODS_Code | varchar |  |  | NO | Code |
| BODS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BODS_CodeTranslated | varchar |  |  | SI | - |
| BODS_CreatedDate | date |  |  | SI | Created Date |
| BODS_CreatedTime | time |  |  | SI | Created Time |
| BODS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BODS_DateFrom | date |  |  | SI | Date From |
| BODS_DateTo | date |  |  | SI | Date To |
| BODS_Desc | varchar |  |  | NO | Description |
| BODS_DescTranslated | varchar |  |  | SI | - |
| BODS_MedicationRelated | varchar |  |  | SI | Medication Related |
| BODS_OperProcRestrict | varchar |  |  | SI | Operation/Procedure Restriction |
| BODS_OperRestrict | varchar |  |  | SI | OperationRestriction |
| BODS_Owner | varchar |  |  | SI | Owner |
| BODS_TourniquetSite | varchar |  |  | SI | Tourniquet Site |
| BODS_UpdatedDate | date |  |  | SI | Updated Date |
| BODS_UpdatedTime | time |  |  | SI | Updated Time |
| BODS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| BODS_VaccinRestrict | varchar |  |  | SI | Vaccination Restriction |
| Q01 | - |  |  | SI | Handling my baby safely |
| Q01ObsDR | - |  |  | SI | Handling my baby safely DR |
| Q02 | - |  |  | SI | Choosing nappies |
| Q02ObsDR | - |  |  | SI | Choosing nappies DR |
| Q03 | - |  |  | SI | Changing nappies |
| Q03ObsDR | - |  |  | SI | Changing nappies DR |
| Q04 | - |  |  | SI | Caring for my baby's cord |
| Q04ObsDR | - |  |  | SI | Caring for my baby's cord DR |
| Q05 | - |  |  | SI | Top and tail wash-caring for my baby's skin |
| Q05ObsDR | - |  |  | SI | Top and tail wash-caring for my baby's skin DR |
| Q06 | - |  |  | SI | Bathing my baby |
| Q06ObsDR | - |  |  | SI | Bathing my baby DR |
| Q07 | - |  |  | SI | How to reduce the risk of cot death |
| Q07ObsDR | - |  |  | SI | How to reduce the risk of cot death DR |
| Q08 | - |  |  | SI | Signs that my baby is well |
| Q08ObsDR | - |  |  | SI | Signs that my baby is well DR |
| Q09 | - |  |  | SI | Car and home safety |
| Q09ObsDR | - |  |  | SI | Car and home safety DR |
| Q10 | - |  |  | SI | Registering the birth |
| Q10ObsDR | - |  |  | SI | Registering the birth DR |
| Q11 | - |  |  | SI | Registering with the general practitioner |
| Q11ObsDR | - |  |  | SI | Registering with the general practitioner DR |
| Q12 | - |  |  | SI | Positioning for breast feeding |
| Q12ObsDR | - |  |  | SI | Positioning for breast feeding DR |
| Q13 | - |  |  | SI | Positioning baby for breast feeding |
| Q13ObsDR | - |  |  | SI | Positioning baby for breast feeding DR |
| Q14 | - |  |  | SI | Principles of good attachment |
| Q14ObsDR | - |  |  | SI | Principles of good attachment DR |
| Q15 | - |  |  | SI | How to recognise my baby is feeding well |
| Q15ObsDR | - |  |  | SI | How to recognise my baby is feeding well DR |
| Q16 | - |  |  | SI | Feeding and sleeping patterns in first days |
| Q16ObsDR | - |  |  | SI | Feeding and sleeping patterns in first days DR |
| Q17 | - |  |  | SI | Baby led feeding |
| Q17ObsDR | - |  |  | SI | Baby led feeding DR |
| Q18 | - |  |  | SI | When milk comes in |
| Q18ObsDR | - |  |  | SI | When milk comes in DR |
| Q19 | - |  |  | SI | Sharing a bed with baby discussed |
| Q19ObsDR | - |  |  | SI | Sharing a bed with baby discussed DR |
| Q20 | - |  |  | SI | Winding baby |
| Q20ObsDR | - |  |  | SI | Winding baby DR |
| Q21 | - |  |  | SI | Why dummies / teats should not be used |
| Q21ObsDR | - |  |  | SI | Why dummies / teats should not be used DR |
| Q22 | - |  |  | SI | How to hand express |
| Q22ObsDR | - |  |  | SI | How to hand express DR |
| Q23 | - |  |  | SI | Expressing milk - sterilising equipment |
| Q23ObsDR | - |  |  | SI | Expressing milk - sterilising equipment DR |
| Q24 | - |  |  | SI | Expressing milk - safe storage |
| Q24ObsDR | - |  |  | SI | Expressing milk - safe storage DR |
| Q25 | - |  |  | SI | Importance of good hand hygiene |
| Q25ObsDR | - |  |  | SI | Importance of good hand hygiene DR |
| Q26 | - |  |  | SI | Sterilising equipment |
| Q26ObsDR | - |  |  | SI | Sterilising equipment DR |
| Q27 | - |  |  | SI | Making formula feeds correctly |
| Q27ObsDR | - |  |  | SI | Making formula feeds correctly DR |
| Q28 | - |  |  | SI | Giving formula feeds correctly |
| Q28ObsDR | - |  |  | SI | Giving formula feeds correctly DR |
| Q29 | - |  |  | SI | Choosing the right formula |
| Q29ObsDR | - |  |  | SI | Choosing the right formula DR |
| Q30 | - |  |  | SI | Signs that my baby is feeding well and thriving |
| Q30ObsDR | - |  |  | SI | Signs that my baby is feeding well and thriving DR |
| Q31 | - |  |  | SI | Midwife countersigning |
| Q32 | - |  |  | SI | Signs that my baby may be ill |
| Q32ObsDR | - |  |  | SI | Signs that my baby may be ill DR |
| Q33 | - |  |  | SI | Comments |
| Q34 | - |  |  | SI | Signs that my baby is feeding well and thriving |
| Q34ObsDR | - |  |  | SI | Signs that my baby is feeding well and thriving DR |
| Q35 | - |  |  | SI | Discussed the following safe sleeping environmenta... |
| Q36 | - |  |  | SI | Environmental issues	 |
| Q37 | - |  |  | SI | Discussed the following safe sleeping risk factors... |
| Q38 | - |  |  | SI | Risk factors	 |
| Q39 | - |  |  | SI | Management plan for sleeping in different circumst... |
| Q40 | - |  |  | SI | Family history of Sudden Unexpected Death in Infan... |
| Q41 | - |  |  | SI | Patient agrees with the discussion 	 |
| Q42 | - |  |  | SI | Reason for non agreement	 |
| Q43 | - |  |  | SI | Action plan |
| Q44 | - |  |  | SI | Skin to skin contact in the early days |
| Q45 | - |  |  | SI | Relationship building |
| Q46 | - |  |  | SI | Keeping baby near to identify feeding cues |
| Q47 | - |  |  | SI | Importance of exclusive breastfeeding explained |
| Q48 | - |  |  | SI | Effects of supplementation on breast feeding expla... |
| Q49 | - |  |  | SI | Breast feeding support pack given and explained |
| Q50 | - |  |  | SI | Number of breast feeds in 24 hrs |
| Q51 | - |  |  | SI | Length of effective feeding (mins) |
| Q52 | - |  |  | SI | Second breast offered |
| Q53 | - |  |  | SI | Shape of nipple at the end of a feed discussed |
| Q54 | - |  |  | SI | Breast and nipple comfort |
| Q55 | - |  |  | SI | How to hold your baby for feeding explained |
| Q56 | - |  |  | SI | Bottle feeding support pack given and explained |
| Q57 | - |  |  | SI | Date |
| Q58 | - |  |  | SI | Time |
| Q59 | - |  |  | SI | Follow up appointment given with breastfeeding con... |
| Q60 | - |  |  | SI | Date and time of appointment |
| Q61 | - |  |  | SI | Date and time of appointment |
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
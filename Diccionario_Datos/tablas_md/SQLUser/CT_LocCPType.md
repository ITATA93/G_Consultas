# SQLUser.CT_LocCPType

**Schema:** SQLUser
**Columnas:** 151
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPT_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| CPT_CareProvType_DR | bigint |  | FK | SI | Des Ref CareProvType |
| CPT_Childsub | double |  |  | NO | Childsub |
| CPT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CPT_CreatedDate | date |  |  | SI | Created Date |
| CPT_CreatedTime | time |  |  | SI | Created Time |
| CPT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CPT_RowId | varchar |  |  | NO | - |
| CPT_UpdatedDate | date |  |  | SI | Updated Date |
| CPT_UpdatedTime | time |  |  | SI | Updated Time |
| CPT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Breastfeeding benefits for mothers |
| Q02 | - |  |  | SI | Breastfeeding benefits for mothers |
| Q03 | - |  |  | SI | Breastfeeding benefits for babies |
| Q04 | - |  |  | SI | Breastfeeding benefits for babies |
| Q05 | - |  |  | SI | Exclusive breastfeeding for the first 6 months (WH... |
| Q06 | - |  |  | SI | Exclusive breastfeeding for the first 6 months (WH... |
| Q07 | - |  |  | SI | Mother and baby bonding |
| Q08 | - |  |  | SI | Mother and baby bonding |
| Q09 | - |  |  | SI | (Importance of skin to skin contact immediately af... |
| Q10 | - |  |  | SI | (Importance of skin to skin contact immediately af... |
| Q100 | - |  |  | SI | Time |
| Q11 | - |  |  | SI | Mother and baby in one room |
| Q12 | - |  |  | SI | Mother and baby in one room |
| Q13 | - |  |  | SI | (Rooming in and breastfeeding on demand following ... |
| Q14 | - |  |  | SI | (Rooming in and breastfeeding on demand following ... |
| Q15 | - |  |  | SI | Size of your baby's stomach |
| Q16 | - |  |  | SI | Size of your baby's stomach |
| Q17 | - |  |  | SI | (Colostrum and mature milk and baby's stomach size... |
| Q18 | - |  |  | SI | (Colostrum and mature milk and baby's stomach size... |
| Q19 | - |  |  | SI | Outpatient Lactation Services Bookmark given |
| Q20 | - |  |  | SI | Outpatient Lactation Services Bookmark given |
| Q21 | - |  |  | SI | Date |
| Q22 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Who was taught |
| Q24 | - |  |  | SI | Who was taught |
| Q25 | - |  |  | SI | Tools used |
| Q26 | - |  |  | SI | Tools used |
| Q27 | - |  |  | SI | Understanding |
| Q28 | - |  |  | SI | Understanding |
| Q29 | - |  |  | SI | Handout given |
| Q30 | - |  |  | SI | Handout given |
| Q31 | - |  |  | SI | Note |
| Q32 | - |  |  | SI | Note |
| Q33 | - |  |  | SI | Date |
| Q34 | - |  |  | SI | Date |
| Q35 | - |  |  | SI | Date |
| Q36 | - |  |  | SI | Date |
| Q37 | - |  |  | SI | Date |
| Q38 | - |  |  | SI | Date |
| Q39 | - |  |  | SI | Date |
| Q40 | - |  |  | SI | Date |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Date |
| Q43 | - |  |  | SI | Date |
| Q44 | - |  |  | SI | Who was taught |
| Q45 | - |  |  | SI | Who was taught |
| Q46 | - |  |  | SI | Who was taught |
| Q47 | - |  |  | SI | Who was taught |
| Q48 | - |  |  | SI | Who was taught |
| Q49 | - |  |  | SI | Who was taught |
| Q50 | - |  |  | SI | Who was taught |
| Q51 | - |  |  | SI | Who was taught |
| Q52 | - |  |  | SI | Who was taught |
| Q53 | - |  |  | SI | Who was taught |
| Q54 | - |  |  | SI | Who was taught |
| Q55 | - |  |  | SI | Tools used |
| Q56 | - |  |  | SI | Tools used |
| Q57 | - |  |  | SI | Tools used |
| Q58 | - |  |  | SI | Tools used |
| Q59 | - |  |  | SI | Tools used |
| Q60 | - |  |  | SI | Tools used |
| Q61 | - |  |  | SI | Tools used |
| Q62 | - |  |  | SI | Tools used |
| Q63 | - |  |  | SI | Tools used |
| Q64 | - |  |  | SI | Tools used |
| Q65 | - |  |  | SI | Tools used |
| Q66 | - |  |  | SI | Understanding |
| Q67 | - |  |  | SI | Understanding |
| Q68 | - |  |  | SI | Understanding |
| Q69 | - |  |  | SI | Understanding |
| Q70 | - |  |  | SI | Understanding |
| Q71 | - |  |  | SI | Understanding |
| Q72 | - |  |  | SI | Understanding |
| Q73 | - |  |  | SI | Understanding |
| Q74 | - |  |  | SI | Understanding |
| Q75 | - |  |  | SI | Understanding |
| Q76 | - |  |  | SI | Understanding |
| Q77 | - |  |  | SI | Handout given |
| Q78 | - |  |  | SI | Handout given |
| Q79 | - |  |  | SI | Handout given |
| Q80 | - |  |  | SI | Handout given |
| Q81 | - |  |  | SI | Handout given |
| Q82 | - |  |  | SI | Handout given |
| Q83 | - |  |  | SI | Handout given |
| Q84 | - |  |  | SI | Handout given |
| Q85 | - |  |  | SI | Handout given |
| Q86 | - |  |  | SI | Handout given |
| Q87 | - |  |  | SI | Handout given |
| Q88 | - |  |  | SI | Note |
| Q89 | - |  |  | SI | Note |
| Q90 | - |  |  | SI | Note |
| Q91 | - |  |  | SI | Note |
| Q92 | - |  |  | SI | Note |
| Q93 | - |  |  | SI | Note |
| Q94 | - |  |  | SI | Note |
| Q95 | - |  |  | SI | Note |
| Q96 | - |  |  | SI | Note |
| Q97 | - |  |  | SI | Note |
| Q98 | - |  |  | SI | Note |
| Q99 | - |  |  | SI | Date |
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
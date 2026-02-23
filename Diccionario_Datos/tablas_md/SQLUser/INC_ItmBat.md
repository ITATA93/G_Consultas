# SQLUser.INC_ItmBat

**Schema:** SQLUser
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCIB_INCI_ParRef | bigint | PK |  | NO | INCI Par Ref |
| ChildQ31DR | - |  |  | SI | Child Reference: Lesion details |
| INCIB_ChildSub | numeric |  |  | NO | INCIB ChildSub (New Key) |
| INCIB_CreatedDate | date |  |  | SI | Created Date |
| INCIB_CreatedTime | time |  |  | SI | Created Time |
| INCIB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCIB_ExpDate | date |  |  | SI | Expiry Date |
| INCIB_ExpTime | time |  |  | SI | Expiry Time |
| INCIB_INCIB_DR | varchar |  | FK | SI | The batch that spawned this one.  Used in vial sha... |
| INCIB_No | varchar |  |  | SI | Manufactory Batch No |
| INCIB_RecallFlag | varchar |  |  | NO | Recall Flag |
| INCIB_Remarks | varchar |  |  | SI | Remarks |
| INCIB_RowId | varchar |  |  | NO | - |
| INCIB_UpdatedDate | date |  |  | SI | Updated Date |
| INCIB_UpdatedTime | time |  |  | SI | Updated Time |
| INCIB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Gravida |
| Q04 | - |  |  | SI | Para |
| Q05 | - |  |  | SI | Date of last menstruation |
| Q06 | - |  |  | SI | Pregnant at time of intervention |
| Q07 | - |  |  | SI | Weeks of pregnancy |
| Q08 | - |  |  | SI | Breastfeeding |
| Q09 | - |  |  | SI | Contraceptive method |
| Q10 | - |  |  | SI | Hormone therapy |
| Q11 | - |  |  | SI | Comments |
| Q12 | - |  |  | SI | Previous exams or treatments |
| Q13 | - |  |  | SI | Previous colonization |
| Q14 | - |  |  | SI | History of hysterectomy |
| Q15 | - |  |  | SI | Colposcopy |
| Q16 | - |  |  | SI | Vulvoscopy |
| Q17 | - |  |  | SI | Cervical treatment |
| Q18 | - |  |  | SI | Primary indication for colposcopy |
| Q19 | - |  |  | SI | Indication from cervical screening results |
| Q20 | - |  |  | SI | Comments |
| Q21 | - |  |  | SI | Colposcopy adequacy |
| Q22 | - |  |  | SI | Comments |
| Q23 | - |  |  | SI | Transformation zone (TZ) |
| Q24 | - |  |  | SI | Visualization of the squamocolumnar junction (SCJ) |
| Q25 | - |  |  | SI | Visualization of the cervix |
| Q26 | - |  |  | SI | Normal findings |
| Q27 | - |  |  | SI | Comments |
| Q28 | - |  |  | SI | Miscellaneous findings |
| Q29 | - |  |  | SI | Comments |
| Q30 | - |  |  | SI | Lesion(s) present (acetowhite or other) |
| Q32 | - |  |  | SI | Overall size of the lesion(s) |
| Q33 | - |  |  | SI | Acetowhite |
| Q34 | - |  |  | SI | Vascular patterns |
| Q35 | - |  |  | SI | Margins / border |
| Q36 | - |  |  | SI | Acetowhite |
| Q37 | - |  |  | SI | Vascular patterns |
| Q38 | - |  |  | SI | Margins / border |
| Q39 | - |  |  | SI | Suspicion of invasive disease |
| Q40 | - |  |  | SI | Signs of suspected neoplasm |
| Q41 | - |  |  | SI | Overall findings description |
| Q42 | - |  |  | SI | Primary colposcopic impression / grading |
| Q43 | - |  |  | SI | Overall findings comments |
| Q44 | - |  |  | SI | Cytological sample localization |
| Q45 | - |  |  | SI | Biopsy performed this episode |
| Q47 | - |  |  | SI | Treatment performed this episode |
| Q48 | - |  |  | SI | Complete cervical treatment details |
| Q49 | - |  |  | SI | Overall findings comments |
| Q50 | - |  |  | SI | Overall impression |
| Q51 | - |  |  | SI | Comments |
| Q52 | - |  |  | SI | Excision type |
| Q53 | - |  |  | SI | Modality |
| Q54 | - |  |  | SI | Ablation type |
| Q55 | - |  |  | SI | Hysterectomy performed |
| Q56 | - |  |  | SI | Treatment anesthetic type for hysterectomy |
| Q57 | - |  |  | SI | Location of treatment for hysterectomy |
| Q58 | - |  |  | SI | Concluding notes |
| Q59 | - |  |  | SI | Colposcopy |
| Q60 | - |  |  | SI | Cervical screening test |
| Q61 | - |  |  | SI | Human papillomavirus (HPV) test |
| Q62 | - |  |  | SI | Biopsy / curettage |
| Q63 | - |  |  | SI | Conization |
| Q64 | - |  |  | SI | Type of Conization |
| Q65 | - |  |  | SI | Therapy after procedure |
| Q66 | - |  |  | SI | Hysterectomy |
| Q67 | - |  |  | SI | Other |
| Q68 | - |  |  | SI | Comments |
| Q69 | - |  |  | SI | Date of recommendation |
| Q70 | - |  |  | SI | Care provider name |
| Q71 | - |  |  | SI | Signature |
| Q71UDt | - |  |  | SI | Signature Last Updated Date |
| Q71UTm | - |  |  | SI | Signature Last Updated Time |
| Q72 | - |  |  | SI | Symptoms |
| Q73 | - |  |  | SI | Examination |
| Q74 | - |  |  | SI | Examination findings |
| Q75 | - |  |  | SI | Low severity lesion findings |
| Q76 | - |  |  | SI | High severity lesion findings |
| Q77 | - |  |  | SI | Lesion impression |
| Q78 | - |  |  | SI | Cytologic sample / biopsy collection |
| Q79 | - |  |  | SI | Cytological sample |
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
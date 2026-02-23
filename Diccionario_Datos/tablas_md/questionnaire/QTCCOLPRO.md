# questionnaire.QTCCOLPRO

> Cervical and Vulvar Dysplasia Worksheet

**Schema:** questionnaire
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cervical and Vulvar Dysplasia Worksheet

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | numeric |  |  | SI | Gravida |
| Q04 | numeric |  |  | SI | Para |
| Q05 | date |  |  | SI | Date of last menstruation |
| Q06 | varchar |  |  | SI | Pregnant at time of intervention |
| Q07 | numeric |  |  | SI | Weeks of pregnancy |
| Q08 | varchar |  |  | SI | Breastfeeding |
| Q09 | varchar |  |  | SI | Contraceptive method |
| Q10 | varchar |  |  | SI | Hormone therapy |
| Q11 | varchar |  |  | SI | Comments |
| Q12 | varchar |  |  | SI | Previous exams or treatments |
| Q13 | varchar |  |  | SI | Previous colonization |
| Q14 | varchar |  |  | SI | History of hysterectomy |
| Q15 | bit |  |  | SI | Colposcopy |
| Q16 | bit |  |  | SI | Vulvoscopy |
| Q17 | bit |  |  | SI | Cervical treatment |
| Q18 | varchar |  |  | SI | Primary indication for colposcopy |
| Q19 | varchar |  |  | SI | Indication from cervical screening results |
| Q20 | varchar |  |  | SI | Comments |
| Q21 | varchar |  |  | SI | Colposcopy adequacy |
| Q22 | varchar |  |  | SI | Comments |
| Q23 | varchar |  |  | SI | Transformation zone (TZ)  |
| Q24 | varchar |  |  | SI | Visualization of the squamocolumnar junction (SCJ)... |
| Q25 | varchar |  |  | SI | Visualization of the cervix |
| Q26 | varchar |  |  | SI | Normal findings |
| Q27 | varchar |  |  | SI | Comments |
| Q28 | varchar |  |  | SI | Miscellaneous findings |
| Q29 | varchar |  |  | SI | Comments |
| Q30 | varchar |  |  | SI | Lesion(s) present (acetowhite or other) |
| Q32 | varchar |  |  | SI | Overall size of the lesion(s) |
| Q33 | varchar |  |  | SI | Acetowhite |
| Q34 | varchar |  |  | SI | Vascular patterns |
| Q35 | varchar |  |  | SI | Margins / border |
| Q36 | varchar |  |  | SI | Acetowhite |
| Q37 | varchar |  |  | SI | Vascular patterns |
| Q38 | varchar |  |  | SI | Margins / border |
| Q39 | varchar |  |  | SI | Suspicion of invasive disease  |
| Q40 | varchar |  |  | SI | Signs of suspected neoplasm |
| Q41 | varchar |  |  | SI | Overall findings description |
| Q42 | varchar |  |  | SI | Primary colposcopic impression / grading |
| Q43 | varchar |  |  | SI | Overall findings comments |
| Q44 | varchar |  |  | SI | Cytological sample localization |
| Q45 | varchar |  |  | SI | Biopsy performed this episode |
| Q47 | varchar |  |  | SI | Treatment performed this episode |
| Q48 | varchar |  |  | SI | Complete cervical treatment details |
| Q49 | varchar |  |  | SI | Overall findings comments |
| Q50 | varchar |  |  | SI | Overall impression |
| Q51 | varchar |  |  | SI | Comments |
| Q52 | varchar |  |  | SI | Excision type |
| Q53 | varchar |  |  | SI | Modality |
| Q54 | varchar |  |  | SI | Ablation type |
| Q55 | varchar |  |  | SI | Hysterectomy performed  |
| Q56 | varchar |  |  | SI | Treatment anesthetic type for hysterectomy |
| Q57 | varchar |  |  | SI | Location of treatment for hysterectomy |
| Q58 | varchar |  |  | SI | Concluding notes |
| Q59 | varchar |  |  | SI | Colposcopy |
| Q60 | varchar |  |  | SI | Cervical screening test |
| Q61 | varchar |  |  | SI | Human papillomavirus (HPV) test |
| Q62 | varchar |  |  | SI | Biopsy / curettage |
| Q63 | varchar |  |  | SI | Conization |
| Q64 | varchar |  |  | SI | Type of Conization |
| Q65 | varchar |  |  | SI | Therapy after procedure |
| Q66 | varchar |  |  | SI | Hysterectomy |
| Q67 | varchar |  |  | SI | Other |
| Q68 | varchar |  |  | SI | Comments |
| Q69 | date |  |  | SI | Date of recommendation |
| Q70 | varchar |  |  | SI | Care provider name |
| Q71 | longvarbinary |  |  | SI | Signature |
| Q71UDt | date |  |  | SI | Signature Last Updated Date |
| Q71UTm | time |  |  | SI | Signature Last Updated Time |
| Q72 | varchar |  |  | SI | Symptoms |
| Q73 | varchar |  |  | SI | Examination |
| Q74 | varchar |  |  | SI | Examination findings |
| Q75 | varchar |  |  | SI | Low severity lesion findings |
| Q76 | varchar |  |  | SI | High severity lesion findings |
| Q77 | varchar |  |  | SI | Lesion impression |
| Q78 | varchar |  |  | SI | Cytologic sample / biopsy collection |
| Q79 | varchar |  |  | SI | Cytological sample |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
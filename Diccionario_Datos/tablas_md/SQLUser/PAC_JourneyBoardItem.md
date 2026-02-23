# SQLUser.PAC_JourneyBoardItem

**Schema:** SQLUser
**Columnas:** 203
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| JBITM_RowId | bigint | PK |  | NO | - |
| JBITM_AllEpisodes | varchar |  |  | SI | Include All Episodes |
| JBITM_Code | varchar |  |  | NO | Code |
| JBITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| JBITM_DateFrom | date |  |  | SI | Date From |
| JBITM_DateTo | date |  |  | SI | Date To |
| JBITM_Desc | varchar |  |  | NO | Description |
| JBITM_DischargeMeds | varchar |  |  | SI | Discharge Meds |
| JBITM_ExcludeOrderStatuses | varchar |  |  | SI | List of Order Status to exclude |
| JBITM_ItmMast_DR | varchar |  | FK | SI | Order Item |
| JBITM_LinkEpisodes | varchar |  |  | SI | Include Linked Episodes |
| JBITM_OrdCat_DR | bigint |  | FK | SI | Order Category |
| JBITM_OrdSubcat_DR | bigint |  | FK | SI | Order Subcategory |
| JBITM_Owner | varchar |  |  | SI | Owner |
| JBITM_Questionnaire_DR | bigint |  | FK | SI | Questionnaire |
| Q01 | - |  |  | SI | Nutrient intake |
| Q02 | - |  |  | SI | Duration of inadequate intake |
| Q03 | - |  |  | SI | Inadequate |
| Q04 | - |  |  | SI | Nutrient Intake in past 2 weeks* |
| Q05 | - |  |  | SI | Nutrient intake comments |
| Q06 | - |  |  | SI | Usual weight (kg) |
| Q07 | - |  |  | SI | Current weight (kg) |
| Q08 | - |  |  | SI | Weight difference - usual versus current (kg) |
| Q09 | - |  |  | SI | Percentage difference - usual versus current (%) |
| Q10 | - |  |  | SI | A negative number indicates weight loss. A positiv... |
| Q100 | - |  |  | SI | If there is an underlying predisposing disorder (e... |
| Q101 | - |  |  | SI | Sarcopenia |
| Q102 | - |  |  | SI | If there is an underlying disorder (e.g. aging) an... |
| Q103 | - |  |  | SI | Date |
| Q104 | - |  |  | SI | Time |
| Q105 | - |  |  | SI | Physical examination |
| Q106 | - |  |  | SI | Physical examination |
| Q107 | - |  |  | SI | Physical examination |
| Q108 | - |  |  | SI | Physical examination |
| Q109 | - |  |  | SI | Physical examination |
| Q11 | - |  |  | SI | Non fluid weight change past 6 months |
| Q110 | - |  |  | SI | Physical examination |
| Q111 | - |  |  | SI | Physical examination |
| Q112 | - |  |  | SI | Physical examination |
| Q113 | - |  |  | SI | Physical examination |
| Q114 | - |  |  | SI | Physical examination |
| Q115 | - |  |  | SI | Physical examination |
| Q116 | - |  |  | SI | Normal |
| Q117 | - |  |  | SI | Normal |
| Q118 | - |  |  | SI | Normal |
| Q119 | - |  |  | SI | Normal |
| Q12 | - |  |  | SI | Non fluid weight loss (kg) |
| Q120 | - |  |  | SI | Normal |
| Q121 | - |  |  | SI | Normal |
| Q122 | - |  |  | SI | Normal |
| Q123 | - |  |  | SI | Normal |
| Q124 | - |  |  | SI | Normal |
| Q125 | - |  |  | SI | Normal |
| Q126 | - |  |  | SI | Normal |
| Q127 | - |  |  | SI | Mild / Moderate |
| Q128 | - |  |  | SI | Mild / Moderate |
| Q129 | - |  |  | SI | Mild / Moderate |
| Q13 | - |  |  | SI | If unknown, has there been a subjective loss of we... |
| Q130 | - |  |  | SI | Mild / Moderate |
| Q131 | - |  |  | SI | Mild / Moderate |
| Q132 | - |  |  | SI | Mild / Moderate |
| Q133 | - |  |  | SI | Mild / Moderate |
| Q134 | - |  |  | SI | Mild / Moderate |
| Q135 | - |  |  | SI | Mild / Moderate |
| Q136 | - |  |  | SI | Mild / Moderate |
| Q137 | - |  |  | SI | Mild / Moderate |
| Q138 | - |  |  | SI | Severe |
| Q139 | - |  |  | SI | Severe |
| Q14 | - |  |  | SI | Weight change past 2 weeks |
| Q140 | - |  |  | SI | Severe |
| Q141 | - |  |  | SI | Severe |
| Q142 | - |  |  | SI | Severe |
| Q143 | - |  |  | SI | Severe |
| Q144 | - |  |  | SI | Severe |
| Q145 | - |  |  | SI | Severe |
| Q146 | - |  |  | SI | Severe |
| Q147 | - |  |  | SI | Severe |
| Q148 | - |  |  | SI | Severe |
| Q15 | - |  |  | SI | Amount (if known) Kg |
| Q16 | - |  |  | SI | Symptoms |
| Q17 | - |  |  | SI | Frequency of symptoms |
| Q18 | - |  |  | SI | Symptoms in the past 2 weeks |
| Q19 | - |  |  | SI | Functional capacity |
| Q20 | - |  |  | SI | Duration of change |
| Q21 | - |  |  | SI | Reduced capacity |
| Q22 | - |  |  | SI | Functional capacity in the past 2 weeks |
| Q23 | - |  |  | SI | High metabolic requirement |
| Q24 | - |  |  | SI | Loss of body fat |
| Q25 | - |  |  | SI | Loss of muscle mass |
| Q26 | - |  |  | SI | Presence of edema / ascites |
| Q27 | - |  |  | SI | Subjective Global Assessment (SGA) rating |
| Q28 | - |  |  | SI | Contributing factor |
| Q29 | - |  |  | SI | SUBCUTANEOUS FAT |
| Q30 | - |  |  | SI | Physical examination |
| Q31 | - |  |  | SI | Normal |
| Q32 | - |  |  | SI | Mild / Moderate |
| Q33 | - |  |  | SI | Severe |
| Q34 | - |  |  | SI | Under the eyes |
| Q35 | - |  |  | SI | Slightly bulging area |
| Q36 | - |  |  | SI | Somewhat hollow look, Slightly dark circles, |
| Q37 | - |  |  | SI | Hollowed look, depression, dark circles |
| Q38 | - |  |  | SI | Triceps |
| Q39 | - |  |  | SI | Large space between fingers |
| Q40 | - |  |  | SI | Some depth to fat tissue, but not ample. Loose fit... |
| Q41 | - |  |  | SI | Very little space between fingers, or fingers touc... |
| Q42 | - |  |  | SI | Ribs, lower back, sides of trunk |
| Q43 | - |  |  | SI | Chest is full |
| Q44 | - |  |  | SI | Ribs obvious, but indentations are not marked. Ili... |
| Q45 | - |  |  | SI | Indentation between ribs very obvious. Iliac crest... |
| Q46 | - |  |  | SI | MUSCLE WASTING |
| Q47 | - |  |  | SI | Physical examination |
| Q48 | - |  |  | SI | Normal |
| Q49 | - |  |  | SI | Mild / Moderate |
| Q50 | - |  |  | SI | Severe |
| Q51 | - |  |  | SI | Temple |
| Q52 | - |  |  | SI | Well-defined muscle |
| Q53 | - |  |  | SI | Slight depression |
| Q54 | - |  |  | SI | Hollowing, depression |
| Q55 | - |  |  | SI | Clavicle |
| Q56 | - |  |  | SI | Not visible in males |
| Q57 | - |  |  | SI | Some protrusion |
| Q58 | - |  |  | SI | Protruding / prominent bone |
| Q59 | - |  |  | SI | Shoulder |
| Q60 | - |  |  | SI | Rounded |
| Q61 | - |  |  | SI | No square look |
| Q62 | - |  |  | SI | Square look |
| Q63 | - |  |  | SI | Scapula / ribs |
| Q64 | - |  |  | SI | Bones not prominent |
| Q65 | - |  |  | SI | Mild depressions or bone may show slightly |
| Q66 | - |  |  | SI | Bones prominent |
| Q67 | - |  |  | SI | Quadriceps |
| Q68 | - |  |  | SI | Well defined |
| Q69 | - |  |  | SI | Depression / atrophy medially |
| Q70 | - |  |  | SI | Prominent knee, Severe depression medially |
| Q71 | - |  |  | SI | Interosseous muscle between thumb and forefinger (... |
| Q72 | - |  |  | SI | Muscle protrudes |
| Q73 | - |  |  | SI | Slightly depressed |
| Q74 | - |  |  | SI | Flat or depressed area |
| Q75 | - |  |  | SI | FLUID RETENTION |
| Q76 | - |  |  | SI | Physical examination |
| Q77 | - |  |  | SI | Normal |
| Q78 | - |  |  | SI | Mild / Moderate |
| Q79 | - |  |  | SI | Severe |
| Q80 | - |  |  | SI | Edema |
| Q81 | - |  |  | SI | None |
| Q82 | - |  |  | SI | Pitting edema of extremities / pitting to knees, p... |
| Q83 | - |  |  | SI | Pitting beyond knees, sacral edema if bedridden, m... |
| Q84 | - |  |  | SI | Ascites |
| Q85 | - |  |  | SI | Absent |
| Q86 | - |  |  | SI | Present (may only be present on imaging) |
| Q87 | - |  |  | SI | A - Well-nourished |
| Q88 | - |  |  | SI | No decrease in food / nutrient intake |
| Q89 | - |  |  | SI | no deficit in function |
| Q90 | - |  |  | SI | non-fluid weight gain |
| Q91 | - |  |  | SI | and chronic deficit in fat and muscle mass but wit... |
| Q92 | - |  |  | SI | B - Mildly / moderately malnourished |
| Q93 | - |  |  | SI | Definite decrease in food / nutrient intake |
| Q94 | - |  |  | SI | moderate functional deficit or recent deterioratio... |
| Q95 | - |  |  | SI | recent stabilization of weight, decrease in sympto... |
| Q96 | - |  |  | SI | C - Severely malnourished |
| Q97 | - |  |  | SI | Severe deficit in food / nutrient intake |
| Q98 | - |  |  | SI | severe functional deficit OR *recent significant d... |
| Q99 | - |  |  | SI | Cachexia |
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
# SQLUser.PAC_DischClassifEpisType

**Schema:** SQLUser
**Columnas:** 202
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPIS_ParRef | bigint | PK |  | NO | PAC_DischClassification Parent Reference |
| EPIS_Childsub | double |  |  | NO | Childsub |
| EPIS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EPIS_CreatedDate | date |  |  | SI | Created Date |
| EPIS_CreatedTime | time |  |  | SI | Created Time |
| EPIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPIS_DateFrom | date |  |  | SI | Active Date From for new Episode Entries |
| EPIS_DateTo | date |  |  | SI | Active Date To for new Episode Entries |
| EPIS_EpisSubType_DR | bigint |  | FK | SI | Des Ref to PACEpisodeSubType |
| EPIS_EpisodeType | varchar |  |  | NO | EpisodeType |
| EPIS_Rowid | varchar |  |  | NO | - |
| EPIS_UpdatedDate | date |  |  | SI | Updated Date |
| EPIS_UpdatedTime | time |  |  | SI | Updated Time |
| EPIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Consultation |
| Q04 | - |  |  | SI | Reason for referral |
| Q05 | - |  |  | SI | Other reason for referral |
| Q06 | - |  |  | SI | Referred by |
| Q07 | - |  |  | SI | Referred by other |
| Q08 | - |  |  | SI | Feeding goals |
| Q09 | - |  |  | SI | Preferred method of feeding |
| Q10 | - |  |  | SI | Left |
| Q100 | - |  |  | SI | Settled after feed |
| Q101 | - |  |  | SI | Settled after feed details |
| Q102 | - |  |  | SI | Urine - nappies per 24 hours |
| Q103 | - |  |  | SI | Urates |
| Q104 | - |  |  | SI | Bowels - nappies per 24 hours |
| Q105 | - |  |  | SI | Bowels - Colour |
| Q106 | - |  |  | SI | Dummy / Teat use |
| Q107 | - |  |  | SI | Infant oral check |
| Q108 | - |  |  | SI | Feeding position |
| Q109 | - |  |  | SI | Other feeding position |
| Q11 | - |  |  | SI | Right |
| Q110 | - |  |  | SI | Latch |
| Q111 | - |  |  | SI | Breathe suck / swallow ratio |
| Q112 | - |  |  | SI | Latch comments |
| Q113 | - |  |  | SI | Infant behaviour |
| Q114 | - |  |  | SI | Infant behaviour details |
| Q115 | - |  |  | SI | Maternal comfort and pain score |
| Q116 | - |  |  | SI | Before feed pain |
| Q117 | - |  |  | SI | With latch pain |
| Q118 | - |  |  | SI | After feed pain |
| Q119 | - |  |  | SI | Pain duration (min) |
| Q12 | - |  |  | SI | Breast assessment |
| Q120 | - |  |  | SI | Nipple appearance after feeds |
| Q121 | - |  |  | SI | Left nipple |
| Q122 | - |  |  | SI | Right nipple |
| Q123 | - |  |  | SI | Breast appearance after feeds |
| Q124 | - |  |  | SI | Left breast |
| Q125 | - |  |  | SI | Right breast |
| Q126 | - |  |  | SI | Length of observed feed (min) |
| Q127 | - |  |  | SI | Postnatal plan |
| Q128 | - |  |  | SI | Education |
| Q129 | - |  |  | SI | Resources / Patient information provided |
| Q13 | - |  |  | SI | Breast notes |
| Q130 | - |  |  | SI | Resources provided |
| Q131 | - |  |  | SI | Follow up |
| Q132 | - |  |  | SI | Follow up notes |
| Q133 | - |  |  | SI | Left breast assessment - antenatal |
| Q134 | - |  |  | SI | Left breast notes - antenatal |
| Q135 | - |  |  | SI | Right breast assessment - antenatal |
| Q136 | - |  |  | SI | Right breast notes - antenatal |
| Q137 | - |  |  | SI | Left nipple assessment - antenatal |
| Q138 | - |  |  | SI | Left nipple notes - antenatal |
| Q139 | - |  |  | SI | Right nipple assessment - antenatal |
| Q14 | - |  |  | SI | Nipple assessment |
| Q140 | - |  |  | SI | Right nipple notes - antenatal |
| Q141 | - |  |  | SI | Left breast assessment - postnatal |
| Q142 | - |  |  | SI | Left breast assessment notes - postnatal |
| Q143 | - |  |  | SI | Right breast assessment - postnatal |
| Q144 | - |  |  | SI | Right breast assessment notes - postnatal |
| Q145 | - |  |  | SI | Left nipple assessment - postnatal |
| Q146 | - |  |  | SI | Left nipple assessment notes - postnatal |
| Q147 | - |  |  | SI | Right nipple assessment - postnatal |
| Q148 | - |  |  | SI | Right nipple assessment notes - postnatal |
| Q15 | - |  |  | SI | Nipple notes |
| Q16 | - |  |  | SI | Left breast assessment - antenatal |
| Q17 | - |  |  | SI | Left breast notes - antenatal |
| Q18 | - |  |  | SI | Right breast assessment - antenatal |
| Q19 | - |  |  | SI | Right breast notes - antenatal |
| Q20 | - |  |  | SI | Left nipple assessment - antenatal |
| Q21 | - |  |  | SI | Left nipple notes - antenatal |
| Q22 | - |  |  | SI | Right nipple assessment - antenatal |
| Q23 | - |  |  | SI | Right nipple notes - antenatal |
| Q24 | - |  |  | SI | Antenatal education provided |
| Q25 | - |  |  | SI | Education notes |
| Q26 | - |  |  | SI | Antenatal expressing pack and information given |
| Q27 | - |  |  | SI | Resources / Patient information provided |
| Q28 | - |  |  | SI | Resource / Information provided |
| Q29 | - |  |  | SI | Antenatal plan |
| Q30 | - |  |  | SI | Reason for referral |
| Q31 | - |  |  | SI | Other reason for referral |
| Q32 | - |  |  | SI | Referred by |
| Q33 | - |  |  | SI | Referred by |
| Q34 | - |  |  | SI | Mother |
| Q35 | - |  |  | SI | Health issues |
| Q36 | - |  |  | SI | Other health issue |
| Q37 | - |  |  | SI | Previous surgical history |
| Q38 | - |  |  | SI | Surgery type |
| Q39 | - |  |  | SI | Other surgery |
| Q40 | - |  |  | SI | Smoker |
| Q41 | - |  |  | SI | Smoking details |
| Q42 | - |  |  | SI | Alcohol |
| Q43 | - |  |  | SI | Alcohol details |
| Q44 | - |  |  | SI | Caffeine |
| Q45 | - |  |  | SI | Caffeine details |
| Q46 | - |  |  | SI | Recreational drug use |
| Q47 | - |  |  | SI | Recreational drug use details |
| Q48 | - |  |  | SI | Postnatal discharge haemoglobin (g/dl) |
| Q49 | - |  |  | SI | Lochia |
| Q50 | - |  |  | SI | Maternal goals |
| Q51 | - |  |  | SI | Left |
| Q52 | - |  |  | SI | Right |
| Q53 | - |  |  | SI | Breast assessment |
| Q54 | - |  |  | SI | Breast notes |
| Q55 | - |  |  | SI | Nipple assessment |
| Q56 | - |  |  | SI | Nipple notes |
| Q57 | - |  |  | SI | Left breast assessment - postnatal |
| Q58 | - |  |  | SI | Left breast assessment notes - postnatal |
| Q59 | - |  |  | SI | Right breast assessment - postnatal |
| Q60 | - |  |  | SI | Right breast assessment notes - postnatal |
| Q61 | - |  |  | SI | Left nipple assessment - postnatal |
| Q62 | - |  |  | SI | Left nipple assessment notes - postnatal |
| Q63 | - |  |  | SI | Right nipple assessment - postnatal |
| Q64 | - |  |  | SI | Right nipple assessment notes - postnatal |
| Q65 | - |  |  | SI | Nipple care |
| Q66 | - |  |  | SI | Nipple care details |
| Q67 | - |  |  | SI | Baby |
| Q68 | - |  |  | SI | Postnatal age |
| Q69 | - |  |  | SI | Postnatal age (weeks) |
| Q70 | - |  |  | SI | weeks |
| Q71 | - |  |  | SI | Postnatal age (days) |
| Q72 | - |  |  | SI | days |
| Q73 | - |  |  | SI | Most recent weight (g) |
| Q74 | - |  |  | SI | Date of weight |
| Q75 | - |  |  | SI | Date of weight uncertain |
| Q76 | - |  |  | SI | Baby admitted |
| Q77 | - |  |  | SI | Reason for admission |
| Q78 | - |  |  | SI | Formula ever provided |
| Q79 | - |  |  | SI | Where did this occur |
| Q80 | - |  |  | SI | Reason for formula |
| Q81 | - |  |  | SI | Feeding |
| Q82 | - |  |  | SI | Milk supply |
| Q83 | - |  |  | SI | Milk supply details |
| Q84 | - |  |  | SI | Necessary to wake baby for feeds |
| Q85 | - |  |  | SI | Average length of feed (min) |
| Q86 | - |  |  | SI | Average feeding duration - Left breast |
| Q87 | - |  |  | SI | Average feeding duration - Right breast |
| Q88 | - |  |  | SI | During the day |
| Q89 | - |  |  | SI | During the night |
| Q90 | - |  |  | SI | Feeding details |
| Q91 | - |  |  | SI | Expressing |
| Q92 | - |  |  | SI | Expressing |
| Q93 | - |  |  | SI | How often (hourly) |
| Q94 | - |  |  | SI | Expressing method |
| Q95 | - |  |  | SI | Expressing method details |
| Q96 | - |  |  | SI | Top-ups |
| Q97 | - |  |  | SI | Top-up type |
| Q98 | - |  |  | SI | Top-up method |
| Q99 | - |  |  | SI | Top-up amount tolerated (mls) |
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
# questionnaire.QTCAHPRHLY

> Lymphoedema Assessment

**Schema:** questionnaire
**Columnas:** 302
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Lymphoedema Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Surgery date |
| Q02 | varchar |  |  | SI | Surgery details |
| Q03 | varchar |  |  | SI | Surgery |
| Q04 | varchar |  |  | SI | Node type |
| Q05 | varchar |  |  | SI | Radiotherapy |
| Q06 | date |  |  | SI | Start date |
| Q07 | date |  |  | SI | Finish date |
| Q08 | numeric |  |  | SI | No of treatments |
| Q09 | varchar |  |  | SI | Chemotherapy |
| Q10 | date |  |  | SI | Start date |
| Q100 | varchar |  |  | SI | Neck lateral flexion |
| Q101 | varchar |  |  | SI | Shoulder flexion |
| Q102 | varchar |  |  | SI | Shoulder abduction |
| Q103 | varchar |  |  | SI | Shoulder external rotation (HBH) |
| Q104 | varchar |  |  | SI | Shoulder internal rotation (HBH) |
| Q105 | varchar |  |  | SI | Elbow extension |
| Q106 | varchar |  |  | SI | Elbow flexion |
| Q107 | varchar |  |  | SI | Hip extension |
| Q108 | varchar |  |  | SI | Hip abduction |
| Q109 | varchar |  |  | SI | Hip internal rotation |
| Q11 | date |  |  | SI | Finish date |
| Q110 | varchar |  |  | SI | Hip external rotation |
| Q111 | varchar |  |  | SI | Knee flexion |
| Q112 | varchar |  |  | SI | Knee extension |
| Q113 | varchar |  |  | SI | Ankle plantar flexion |
| Q114 | varchar |  |  | SI | Neck Flexion, Active |
| Q114ObsDR | varchar |  | FK | SI | Neck Flexion, Active DR |
| Q115 | varchar |  |  | SI | Neck Extension, Active |
| Q115ObsDR | varchar |  | FK | SI | Neck Extension, Active DR |
| Q116 | varchar |  |  | SI | Neck flexion, Passive |
| Q116ObsDR | varchar |  | FK | SI | Neck flexion, Passive DR |
| Q117 | varchar |  |  | SI | Neck extension, passive |
| Q117ObsDR | varchar |  | FK | SI | Neck extension, passive DR |
| Q118 | varchar |  |  | SI | Neck rotation, active left |
| Q118ObsDR | varchar |  | FK | SI | Neck rotation, active left DR |
| Q119 | varchar |  |  | SI | Neck rotation, active right |
| Q119ObsDR | varchar |  | FK | SI | Neck rotation, active right DR |
| Q12 | numeric |  |  | SI | No of treatments |
| Q120 | varchar |  |  | SI | Neck rotation, passive left |
| Q120ObsDR | varchar |  | FK | SI | Neck rotation, passive left DR |
| Q121 | varchar |  |  | SI | Neck rotation, passive right |
| Q121ObsDR | varchar |  | FK | SI | Neck rotation, passive right DR |
| Q122 | varchar |  |  | SI | Neck lateral flexion, active left |
| Q122ObsDR | varchar |  | FK | SI | Neck lateral flexion, active left DR |
| Q123 | varchar |  |  | SI | Neck lateral flexion, active right |
| Q123ObsDR | varchar |  | FK | SI | Neck lateral flexion, active right DR |
| Q124 | varchar |  |  | SI | Neck lateral flexion, passive left |
| Q124ObsDR | varchar |  | FK | SI | Neck lateral flexion, passive left DR |
| Q125 | varchar |  |  | SI | Neck lateral flexion, passive right |
| Q125ObsDR | varchar |  | FK | SI | Neck lateral flexion, passive right DR |
| Q126 | varchar |  |  | SI | Shoulder flexion, active left |
| Q126ObsDR | varchar |  | FK | SI | Shoulder flexion, active left DR |
| Q127 | varchar |  |  | SI | Shoulder flexion, active right |
| Q127ObsDR | varchar |  | FK | SI | Shoulder flexion, active right DR |
| Q128 | varchar |  |  | SI | Shoulder flexion, passive left |
| Q128ObsDR | varchar |  | FK | SI | Shoulder flexion, passive left DR |
| Q129 | varchar |  |  | SI | Shoulder flexion, passive right |
| Q129ObsDR | varchar |  | FK | SI | Shoulder flexion, passive right DR |
| Q13 | varchar |  |  | SI | Hormonal therapy |
| Q130 | varchar |  |  | SI | Shoulder abduction, active left |
| Q130ObsDR | varchar |  | FK | SI | Shoulder abduction, active left DR |
| Q131 | varchar |  |  | SI | Shoulder abduction, active right |
| Q131ObsDR | varchar |  | FK | SI | Shoulder abduction, active right DR |
| Q132 | varchar |  |  | SI | Shoulder abduction, passive left |
| Q132ObsDR | varchar |  | FK | SI | Shoulder abduction, passive left DR |
| Q133 | varchar |  |  | SI | Shoulder abduction, passive right |
| Q133ObsDR | varchar |  | FK | SI | Shoulder abduction, passive right DR |
| Q134 | varchar |  |  | SI | Shoulder external rotation, active left |
| Q134ObsDR | varchar |  | FK | SI | Shoulder external rotation, active left DR |
| Q135 | varchar |  |  | SI | Shoulder external rotation, active right |
| Q135ObsDR | varchar |  | FK | SI | Shoulder external rotation, active right DR |
| Q136 | varchar |  |  | SI | Shoulder external rotation, passive left |
| Q136ObsDR | varchar |  | FK | SI | Shoulder external rotation, passive left DR |
| Q137 | varchar |  |  | SI | Shoulder external rotation, passive right |
| Q137ObsDR | varchar |  | FK | SI | Shoulder external rotation, passive right DR |
| Q138 | varchar |  |  | SI | Shoulder internal rotation, active left |
| Q138ObsDR | varchar |  | FK | SI | Shoulder internal rotation, active left DR |
| Q139 | varchar |  |  | SI | Shoulder internal rotation, active right |
| Q139ObsDR | varchar |  | FK | SI | Shoulder internal rotation, active right DR |
| Q14 | date |  |  | SI | Start date |
| Q140 | varchar |  |  | SI | Shoulder internal rotation, passive left |
| Q140ObsDR | varchar |  | FK | SI | Shoulder internal rotation, passive left DR |
| Q141 | varchar |  |  | SI | Shoulder internal rotation, passive right |
| Q141ObsDR | varchar |  | FK | SI | Shoulder internal rotation, passive right DR |
| Q142 | varchar |  |  | SI | Elbow extension, active left |
| Q142ObsDR | varchar |  | FK | SI | Elbow extension, active left DR |
| Q143 | varchar |  |  | SI | Elbow extension, active right |
| Q143ObsDR | varchar |  | FK | SI | Elbow extension, active right DR |
| Q144 | varchar |  |  | SI | Elbow extension, passive left |
| Q144ObsDR | varchar |  | FK | SI | Elbow extension, passive left DR |
| Q145 | varchar |  |  | SI | Elbow extension, passive right |
| Q145ObsDR | varchar |  | FK | SI | Elbow extension, passive right DR |
| Q146 | varchar |  |  | SI | Elbow flexion, active left |
| Q146ObsDR | varchar |  | FK | SI | Elbow flexion, active left DR |
| Q147 | varchar |  |  | SI | Elbow flexion, active right |
| Q147ObsDR | varchar |  | FK | SI | Elbow flexion, active right DR |
| Q148 | varchar |  |  | SI | Elbow flexion, passive left |
| Q148ObsDR | varchar |  | FK | SI | Elbow flexion, passive left DR |
| Q149 | varchar |  |  | SI | Elbow flexion, passive right |
| Q149ObsDR | varchar |  | FK | SI | Elbow flexion, passive right DR |
| Q15 | date |  |  | SI | Finish date |
| Q150 | varchar |  |  | SI | Hip flexion, active left |
| Q150ObsDR | varchar |  | FK | SI | Hip flexion, active left DR |
| Q151 | varchar |  |  | SI | Hip flexion, active right |
| Q151ObsDR | varchar |  | FK | SI | Hip flexion, active right DR |
| Q152 | varchar |  |  | SI | Hip flexion, passive left |
| Q152ObsDR | varchar |  | FK | SI | Hip flexion, passive left DR |
| Q153 | varchar |  |  | SI | Hip flexion, passive right |
| Q153ObsDR | varchar |  | FK | SI | Hip flexion, passive right DR |
| Q154 | varchar |  |  | SI | Hip extension, active left |
| Q154ObsDR | varchar |  | FK | SI | Hip extension, active left DR |
| Q155 | varchar |  |  | SI | Hip extension, active right |
| Q155ObsDR | varchar |  | FK | SI | Hip extension, active right DR |
| Q156 | varchar |  |  | SI | Hip extension, passive left |
| Q156ObsDR | varchar |  | FK | SI | Hip extension, passive left DR |
| Q157 | varchar |  |  | SI | Hip extension, passive right |
| Q157ObsDR | varchar |  | FK | SI | Hip extension, passive right DR |
| Q158 | varchar |  |  | SI | Hip abduction, active left |
| Q158ObsDR | varchar |  | FK | SI | Hip abduction, active left DR |
| Q159 | varchar |  |  | SI | Hip abduction, active right |
| Q159ObsDR | varchar |  | FK | SI | Hip abduction, active right DR |
| Q16 | varchar |  |  | SI | Medication |
| Q160 | varchar |  |  | SI | Hip abduction, passive left |
| Q160ObsDR | varchar |  | FK | SI | Hip abduction, passive left DR |
| Q161 | varchar |  |  | SI | Hip abduction, passive right |
| Q161ObsDR | varchar |  | FK | SI | Hip abduction, passive right DR |
| Q162 | varchar |  |  | SI | Hip internal rotation, active left |
| Q162ObsDR | varchar |  | FK | SI | Hip internal rotation, active left DR |
| Q163 | varchar |  |  | SI | Hip internal rotation, active right |
| Q163ObsDR | varchar |  | FK | SI | Hip internal rotation, active right DR |
| Q164 | varchar |  |  | SI | Hip internal rotation, passive left |
| Q164ObsDR | varchar |  | FK | SI | Hip internal rotation, passive left DR |
| Q165 | varchar |  |  | SI | Hip internal rotation, passive right |
| Q165ObsDR | varchar |  | FK | SI | Hip internal rotation, passive right DR |
| Q166 | varchar |  |  | SI | Hip external rotation, active left |
| Q166ObsDR | varchar |  | FK | SI | Hip external rotation, active left DR |
| Q167 | varchar |  |  | SI | Hip external rotation, active right |
| Q167ObsDR | varchar |  | FK | SI | Hip external rotation, active right DR |
| Q168 | varchar |  |  | SI | Hip external rotation, passive left |
| Q168ObsDR | varchar |  | FK | SI | Hip external rotation, passive left DR |
| Q169 | varchar |  |  | SI | Hip external rotation, passive right |
| Q169ObsDR | varchar |  | FK | SI | Hip external rotation, passive right DR |
| Q17 | varchar |  |  | SI | Dominant side |
| Q170 | varchar |  |  | SI | Knee flexion, active left |
| Q170ObsDR | varchar |  | FK | SI | Knee flexion, active left DR |
| Q171 | varchar |  |  | SI | Knee flexion, active right |
| Q171ObsDR | varchar |  | FK | SI | Knee flexion, active right DR |
| Q172 | varchar |  |  | SI | Knee flexion, passive left |
| Q172ObsDR | varchar |  | FK | SI | Knee flexion, passive left DR |
| Q173 | varchar |  |  | SI | Knee flexion, passive right |
| Q173ObsDR | varchar |  | FK | SI | Knee flexion, passive right DR |
| Q174 | varchar |  |  | SI | Knee extension, active left |
| Q174ObsDR | varchar |  | FK | SI | Knee extension, active left DR |
| Q175 | varchar |  |  | SI | Knee extension, active right |
| Q175ObsDR | varchar |  | FK | SI | Knee extension, active right DR |
| Q176 | varchar |  |  | SI | Knee extension, passive left |
| Q176ObsDR | varchar |  | FK | SI | Knee extension, passive left DR |
| Q177 | varchar |  |  | SI | Knee extension, passive right |
| Q177ObsDR | varchar |  | FK | SI | Knee extension, passive right DR |
| Q178 | varchar |  |  | SI | Ankle plantar flexion, active left |
| Q178ObsDR | varchar |  | FK | SI | Ankle plantar flexion, active left DR |
| Q179 | varchar |  |  | SI | Ankle plantar flexion, active right |
| Q179ObsDR | varchar |  | FK | SI | Ankle plantar flexion, active right DR |
| Q18 | varchar |  |  | SI | Comment |
| Q180 | varchar |  |  | SI | Ankle plantar flexion, passive left |
| Q180ObsDR | varchar |  | FK | SI | Ankle plantar flexion, passive left DR |
| Q181 | varchar |  |  | SI | Ankle plantar flexion, passive right |
| Q181ObsDR | varchar |  | FK | SI | Ankle plantar flexion, passive right DR |
| Q182 | varchar |  |  | SI | Ankle dorsiflexion, active left |
| Q182ObsDR | varchar |  | FK | SI | Ankle dorsiflexion, active left DR |
| Q183 | varchar |  |  | SI | Ankle dorsiflexion, active right |
| Q183ObsDR | varchar |  | FK | SI | Ankle dorsiflexion, active right DR |
| Q184 | varchar |  |  | SI | Ankle dorsiflexion, passive left |
| Q184ObsDR | varchar |  | FK | SI | Ankle dorsiflexion, passive left DR |
| Q185 | varchar |  |  | SI | Ankle dorsiflexion, passive right |
| Q185ObsDR | varchar |  | FK | SI | Ankle dorsiflexion, passive right DR |
| Q186 | date |  |  | SI | Date |
| Q187 | time |  |  | SI | Time |
| Q188 | varchar |  |  | SI | Neck |
| Q189 | varchar |  |  | SI | Shoulder |
| Q19 | varchar |  |  | SI | Pain assessment |
| Q190 | varchar |  |  | SI | Elbow |
| Q191 | varchar |  |  | SI | Hip |
| Q192 | varchar |  |  | SI | Knee |
| Q193 | varchar |  |  | SI | Foot |
| Q194 | varchar |  |  | SI | Ankle dorsiflexion |
| Q195 | varchar |  |  | SI | Hip flexion |
| Q196 | varchar |  |  | SI | Please enter the degree of movement observed for e... |
| Q20 | varchar |  |  | SI | (Present, site, character, pain score) |
| Q26 | varchar |  |  | SI | Other |
| Q27 | varchar |  |  | SI | General comments |
| Q28 | varchar |  |  | SI | (Seromas, wound healing, etc.) |
| Q29 | varchar |  |  | SI | Skin condition |
| Q30 | varchar |  |  | SI | Sensory changes |
| Q31 | varchar |  |  | SI | Skin care routine |
| Q32 | varchar |  |  | SI | Tissues in swollen areas |
| Q33 | varchar |  |  | SI | are predominantly |
| Q34 | varchar |  |  | SI | Comment |
| Q35 | varchar |  |  | SI | Body map |
| Q36 | varchar |  |  | SI | Upper Limb Movement |
| Q37 | varchar |  |  | SI | Shoulder flexion |
| Q38 | varchar |  |  | SI | Shoulder abduction |
| Q39 | varchar |  |  | SI | Shoulder external rotation (HBH) |
| Q40 | varchar |  |  | SI | Shoulder internal rotation (HBB) |
| Q41 | varchar |  |  | SI | Elbow extension |
| Q42 | varchar |  |  | SI | Elbow flexion |
| Q43 | varchar |  |  | SI | Neck flexion / extension |
| Q44 | varchar |  |  | SI | Neck rotation |
| Q45 | varchar |  |  | SI | Neck lateral flexion |
| Q46 | varchar |  |  | SI | Hip flexion |
| Q47 | varchar |  |  | SI | Hip extension |
| Q48 | varchar |  |  | SI | Hip abduction |
| Q49 | varchar |  |  | SI | Hip internal rotation |
| Q50 | varchar |  |  | SI | Hip external rotation |
| Q51 | varchar |  |  | SI | Knee flexion |
| Q52 | varchar |  |  | SI | Knee extension |
| Q53 | varchar |  |  | SI | Plantarflexion |
| Q54 | varchar |  |  | SI | Dorsiflexion |
| Q55 | varchar |  |  | SI | Lower Limb Movement |
| Q56 | varchar |  |  | SI | Stemmer Sign |
| Q57 | varchar |  |  | SI | Stemmer sign right |
| Q58 | varchar |  |  | SI | Stemmer Sign Left |
| Q59 | varchar |  |  | SI | Ankle brachial pressure index |
| Q60 | varchar |  |  | SI | Upper Limb Measurements (Bioimpedance and Volumete... |
| Q61 | varchar |  |  | SI | Dominant |
| Q62 | varchar |  |  | SI | Surgery |
| Q63 | varchar |  |  | SI | Rung |
| Q64 | varchar |  |  | SI | Hand position |
| Q65 | varchar |  |  | SI | Other (please specify) |
| Q67 | varchar |  |  | SI | Notes |
| Q69 | varchar |  |  | SI | Management plan |
| Q70 | varchar |  |  | SI | Referral to |
| Q71 | varchar |  |  | SI | Active |
| Q72 | varchar |  |  | SI | Passive |
| Q73 | varchar |  |  | SI | Active Left |
| Q74 | varchar |  |  | SI | Active Left |
| Q75 | varchar |  |  | SI | Active Left |
| Q76 | varchar |  |  | SI | Active Left |
| Q77 | varchar |  |  | SI | Active Left |
| Q78 | varchar |  |  | SI | Active Left |
| Q79 | varchar |  |  | SI | Active Right |
| Q80 | varchar |  |  | SI | Active Right |
| Q81 | varchar |  |  | SI | Active Right |
| Q82 | varchar |  |  | SI | Active Right |
| Q83 | varchar |  |  | SI | Active Right |
| Q84 | varchar |  |  | SI | Active Right |
| Q85 | varchar |  |  | SI | Passive Left |
| Q86 | varchar |  |  | SI | Passive Left |
| Q87 | varchar |  |  | SI | Passive Left |
| Q88 | varchar |  |  | SI | Passive Left |
| Q89 | varchar |  |  | SI | Passive Left |
| Q90 | varchar |  |  | SI | Passive Left |
| Q91 | varchar |  |  | SI | Passive Right |
| Q92 | varchar |  |  | SI | Passive Right |
| Q93 | varchar |  |  | SI | Passive Right |
| Q94 | varchar |  |  | SI | Passive Right |
| Q95 | varchar |  |  | SI | Passive Right |
| Q96 | varchar |  |  | SI | Passive Right |
| Q97 | varchar |  |  | SI | Neck flexion |
| Q98 | varchar |  |  | SI | Neck extension |
| Q99 | varchar |  |  | SI | Neck rotation |
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
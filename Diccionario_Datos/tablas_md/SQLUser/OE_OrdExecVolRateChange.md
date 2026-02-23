# SQLUser.OE_OrdExecVolRateChange

**Schema:** SQLUser
**Columnas:** 336
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VRCH_ParRef | varchar | PK |  | NO | OE_OrdExec Parent Reference |
| ChildQ66DR | - |  |  | SI | Child Reference: Bioimpedance and volumeter |
| Q01 | - |  |  | SI | Surgery date |
| Q02 | - |  |  | SI | Surgery details |
| Q03 | - |  |  | SI | Surgery |
| Q04 | - |  |  | SI | Node type |
| Q05 | - |  |  | SI | Radiotherapy |
| Q06 | - |  |  | SI | Start date |
| Q07 | - |  |  | SI | Finish date |
| Q08 | - |  |  | SI | No of treatments |
| Q09 | - |  |  | SI | Chemotherapy |
| Q10 | - |  |  | SI | Start date |
| Q100 | - |  |  | SI | Neck lateral flexion |
| Q101 | - |  |  | SI | Shoulder flexion |
| Q102 | - |  |  | SI | Shoulder abduction |
| Q103 | - |  |  | SI | Shoulder external rotation (HBH) |
| Q104 | - |  |  | SI | Shoulder internal rotation (HBH) |
| Q105 | - |  |  | SI | Elbow extension |
| Q106 | - |  |  | SI | Elbow flexion |
| Q107 | - |  |  | SI | Hip extension |
| Q108 | - |  |  | SI | Hip abduction |
| Q109 | - |  |  | SI | Hip internal rotation |
| Q11 | - |  |  | SI | Finish date |
| Q110 | - |  |  | SI | Hip external rotation |
| Q111 | - |  |  | SI | Knee flexion |
| Q112 | - |  |  | SI | Knee extension |
| Q113 | - |  |  | SI | Ankle plantar flexion |
| Q114 | - |  |  | SI | Neck Flexion, Active |
| Q114ObsDR | - |  |  | SI | Neck Flexion, Active DR |
| Q115 | - |  |  | SI | Neck Extension, Active |
| Q115ObsDR | - |  |  | SI | Neck Extension, Active DR |
| Q116 | - |  |  | SI | Neck flexion, Passive |
| Q116ObsDR | - |  |  | SI | Neck flexion, Passive DR |
| Q117 | - |  |  | SI | Neck extension, passive |
| Q117ObsDR | - |  |  | SI | Neck extension, passive DR |
| Q118 | - |  |  | SI | Neck rotation, active left |
| Q118ObsDR | - |  |  | SI | Neck rotation, active left DR |
| Q119 | - |  |  | SI | Neck rotation, active right |
| Q119ObsDR | - |  |  | SI | Neck rotation, active right DR |
| Q12 | - |  |  | SI | No of treatments |
| Q120 | - |  |  | SI | Neck rotation, passive left |
| Q120ObsDR | - |  |  | SI | Neck rotation, passive left DR |
| Q121 | - |  |  | SI | Neck rotation, passive right |
| Q121ObsDR | - |  |  | SI | Neck rotation, passive right DR |
| Q122 | - |  |  | SI | Neck lateral flexion, active left |
| Q122ObsDR | - |  |  | SI | Neck lateral flexion, active left DR |
| Q123 | - |  |  | SI | Neck lateral flexion, active right |
| Q123ObsDR | - |  |  | SI | Neck lateral flexion, active right DR |
| Q124 | - |  |  | SI | Neck lateral flexion, passive left |
| Q124ObsDR | - |  |  | SI | Neck lateral flexion, passive left DR |
| Q125 | - |  |  | SI | Neck lateral flexion, passive right |
| Q125ObsDR | - |  |  | SI | Neck lateral flexion, passive right DR |
| Q126 | - |  |  | SI | Shoulder flexion, active left |
| Q126ObsDR | - |  |  | SI | Shoulder flexion, active left DR |
| Q127 | - |  |  | SI | Shoulder flexion, active right |
| Q127ObsDR | - |  |  | SI | Shoulder flexion, active right DR |
| Q128 | - |  |  | SI | Shoulder flexion, passive left |
| Q128ObsDR | - |  |  | SI | Shoulder flexion, passive left DR |
| Q129 | - |  |  | SI | Shoulder flexion, passive right |
| Q129ObsDR | - |  |  | SI | Shoulder flexion, passive right DR |
| Q13 | - |  |  | SI | Hormonal therapy |
| Q130 | - |  |  | SI | Shoulder abduction, active left |
| Q130ObsDR | - |  |  | SI | Shoulder abduction, active left DR |
| Q131 | - |  |  | SI | Shoulder abduction, active right |
| Q131ObsDR | - |  |  | SI | Shoulder abduction, active right DR |
| Q132 | - |  |  | SI | Shoulder abduction, passive left |
| Q132ObsDR | - |  |  | SI | Shoulder abduction, passive left DR |
| Q133 | - |  |  | SI | Shoulder abduction, passive right |
| Q133ObsDR | - |  |  | SI | Shoulder abduction, passive right DR |
| Q134 | - |  |  | SI | Shoulder external rotation, active left |
| Q134ObsDR | - |  |  | SI | Shoulder external rotation, active left DR |
| Q135 | - |  |  | SI | Shoulder external rotation, active right |
| Q135ObsDR | - |  |  | SI | Shoulder external rotation, active right DR |
| Q136 | - |  |  | SI | Shoulder external rotation, passive left |
| Q136ObsDR | - |  |  | SI | Shoulder external rotation, passive left DR |
| Q137 | - |  |  | SI | Shoulder external rotation, passive right |
| Q137ObsDR | - |  |  | SI | Shoulder external rotation, passive right DR |
| Q138 | - |  |  | SI | Shoulder internal rotation, active left |
| Q138ObsDR | - |  |  | SI | Shoulder internal rotation, active left DR |
| Q139 | - |  |  | SI | Shoulder internal rotation, active right |
| Q139ObsDR | - |  |  | SI | Shoulder internal rotation, active right DR |
| Q14 | - |  |  | SI | Start date |
| Q140 | - |  |  | SI | Shoulder internal rotation, passive left |
| Q140ObsDR | - |  |  | SI | Shoulder internal rotation, passive left DR |
| Q141 | - |  |  | SI | Shoulder internal rotation, passive right |
| Q141ObsDR | - |  |  | SI | Shoulder internal rotation, passive right DR |
| Q142 | - |  |  | SI | Elbow extension, active left |
| Q142ObsDR | - |  |  | SI | Elbow extension, active left DR |
| Q143 | - |  |  | SI | Elbow extension, active right |
| Q143ObsDR | - |  |  | SI | Elbow extension, active right DR |
| Q144 | - |  |  | SI | Elbow extension, passive left |
| Q144ObsDR | - |  |  | SI | Elbow extension, passive left DR |
| Q145 | - |  |  | SI | Elbow extension, passive right |
| Q145ObsDR | - |  |  | SI | Elbow extension, passive right DR |
| Q146 | - |  |  | SI | Elbow flexion, active left |
| Q146ObsDR | - |  |  | SI | Elbow flexion, active left DR |
| Q147 | - |  |  | SI | Elbow flexion, active right |
| Q147ObsDR | - |  |  | SI | Elbow flexion, active right DR |
| Q148 | - |  |  | SI | Elbow flexion, passive left |
| Q148ObsDR | - |  |  | SI | Elbow flexion, passive left DR |
| Q149 | - |  |  | SI | Elbow flexion, passive right |
| Q149ObsDR | - |  |  | SI | Elbow flexion, passive right DR |
| Q15 | - |  |  | SI | Finish date |
| Q150 | - |  |  | SI | Hip flexion, active left |
| Q150ObsDR | - |  |  | SI | Hip flexion, active left DR |
| Q151 | - |  |  | SI | Hip flexion, active right |
| Q151ObsDR | - |  |  | SI | Hip flexion, active right DR |
| Q152 | - |  |  | SI | Hip flexion, passive left |
| Q152ObsDR | - |  |  | SI | Hip flexion, passive left DR |
| Q153 | - |  |  | SI | Hip flexion, passive right |
| Q153ObsDR | - |  |  | SI | Hip flexion, passive right DR |
| Q154 | - |  |  | SI | Hip extension, active left |
| Q154ObsDR | - |  |  | SI | Hip extension, active left DR |
| Q155 | - |  |  | SI | Hip extension, active right |
| Q155ObsDR | - |  |  | SI | Hip extension, active right DR |
| Q156 | - |  |  | SI | Hip extension, passive left |
| Q156ObsDR | - |  |  | SI | Hip extension, passive left DR |
| Q157 | - |  |  | SI | Hip extension, passive right |
| Q157ObsDR | - |  |  | SI | Hip extension, passive right DR |
| Q158 | - |  |  | SI | Hip abduction, active left |
| Q158ObsDR | - |  |  | SI | Hip abduction, active left DR |
| Q159 | - |  |  | SI | Hip abduction, active right |
| Q159ObsDR | - |  |  | SI | Hip abduction, active right DR |
| Q16 | - |  |  | SI | Medication |
| Q160 | - |  |  | SI | Hip abduction, passive left |
| Q160ObsDR | - |  |  | SI | Hip abduction, passive left DR |
| Q161 | - |  |  | SI | Hip abduction, passive right |
| Q161ObsDR | - |  |  | SI | Hip abduction, passive right DR |
| Q162 | - |  |  | SI | Hip internal rotation, active left |
| Q162ObsDR | - |  |  | SI | Hip internal rotation, active left DR |
| Q163 | - |  |  | SI | Hip internal rotation, active right |
| Q163ObsDR | - |  |  | SI | Hip internal rotation, active right DR |
| Q164 | - |  |  | SI | Hip internal rotation, passive left |
| Q164ObsDR | - |  |  | SI | Hip internal rotation, passive left DR |
| Q165 | - |  |  | SI | Hip internal rotation, passive right |
| Q165ObsDR | - |  |  | SI | Hip internal rotation, passive right DR |
| Q166 | - |  |  | SI | Hip external rotation, active left |
| Q166ObsDR | - |  |  | SI | Hip external rotation, active left DR |
| Q167 | - |  |  | SI | Hip external rotation, active right |
| Q167ObsDR | - |  |  | SI | Hip external rotation, active right DR |
| Q168 | - |  |  | SI | Hip external rotation, passive left |
| Q168ObsDR | - |  |  | SI | Hip external rotation, passive left DR |
| Q169 | - |  |  | SI | Hip external rotation, passive right |
| Q169ObsDR | - |  |  | SI | Hip external rotation, passive right DR |
| Q17 | - |  |  | SI | Dominant side |
| Q170 | - |  |  | SI | Knee flexion, active left |
| Q170ObsDR | - |  |  | SI | Knee flexion, active left DR |
| Q171 | - |  |  | SI | Knee flexion, active right |
| Q171ObsDR | - |  |  | SI | Knee flexion, active right DR |
| Q172 | - |  |  | SI | Knee flexion, passive left |
| Q172ObsDR | - |  |  | SI | Knee flexion, passive left DR |
| Q173 | - |  |  | SI | Knee flexion, passive right |
| Q173ObsDR | - |  |  | SI | Knee flexion, passive right DR |
| Q174 | - |  |  | SI | Knee extension, active left |
| Q174ObsDR | - |  |  | SI | Knee extension, active left DR |
| Q175 | - |  |  | SI | Knee extension, active right |
| Q175ObsDR | - |  |  | SI | Knee extension, active right DR |
| Q176 | - |  |  | SI | Knee extension, passive left |
| Q176ObsDR | - |  |  | SI | Knee extension, passive left DR |
| Q177 | - |  |  | SI | Knee extension, passive right |
| Q177ObsDR | - |  |  | SI | Knee extension, passive right DR |
| Q178 | - |  |  | SI | Ankle plantar flexion, active left |
| Q178ObsDR | - |  |  | SI | Ankle plantar flexion, active left DR |
| Q179 | - |  |  | SI | Ankle plantar flexion, active right |
| Q179ObsDR | - |  |  | SI | Ankle plantar flexion, active right DR |
| Q18 | - |  |  | SI | Comment |
| Q180 | - |  |  | SI | Ankle plantar flexion, passive left |
| Q180ObsDR | - |  |  | SI | Ankle plantar flexion, passive left DR |
| Q181 | - |  |  | SI | Ankle plantar flexion, passive right |
| Q181ObsDR | - |  |  | SI | Ankle plantar flexion, passive right DR |
| Q182 | - |  |  | SI | Ankle dorsiflexion, active left |
| Q182ObsDR | - |  |  | SI | Ankle dorsiflexion, active left DR |
| Q183 | - |  |  | SI | Ankle dorsiflexion, active right |
| Q183ObsDR | - |  |  | SI | Ankle dorsiflexion, active right DR |
| Q184 | - |  |  | SI | Ankle dorsiflexion, passive left |
| Q184ObsDR | - |  |  | SI | Ankle dorsiflexion, passive left DR |
| Q185 | - |  |  | SI | Ankle dorsiflexion, passive right |
| Q185ObsDR | - |  |  | SI | Ankle dorsiflexion, passive right DR |
| Q186 | - |  |  | SI | Date |
| Q187 | - |  |  | SI | Time |
| Q188 | - |  |  | SI | Neck |
| Q189 | - |  |  | SI | Shoulder |
| Q19 | - |  |  | SI | Pain assessment |
| Q190 | - |  |  | SI | Elbow |
| Q191 | - |  |  | SI | Hip |
| Q192 | - |  |  | SI | Knee |
| Q193 | - |  |  | SI | Foot |
| Q194 | - |  |  | SI | Ankle dorsiflexion |
| Q195 | - |  |  | SI | Hip flexion |
| Q196 | - |  |  | SI | Please enter the degree of movement observed for e... |
| Q20 | - |  |  | SI | (Present, site, character, pain score) |
| Q26 | - |  |  | SI | Other |
| Q27 | - |  |  | SI | General comments |
| Q28 | - |  |  | SI | (Seromas, wound healing, etc.) |
| Q29 | - |  |  | SI | Skin condition |
| Q30 | - |  |  | SI | Sensory changes |
| Q31 | - |  |  | SI | Skin care routine |
| Q32 | - |  |  | SI | Tissues in swollen areas |
| Q33 | - |  |  | SI | are predominantly |
| Q34 | - |  |  | SI | Comment |
| Q35 | - |  |  | SI | Body map |
| Q36 | - |  |  | SI | Upper Limb Movement |
| Q37 | - |  |  | SI | Shoulder flexion |
| Q38 | - |  |  | SI | Shoulder abduction |
| Q39 | - |  |  | SI | Shoulder external rotation (HBH) |
| Q40 | - |  |  | SI | Shoulder internal rotation (HBB) |
| Q41 | - |  |  | SI | Elbow extension |
| Q42 | - |  |  | SI | Elbow flexion |
| Q43 | - |  |  | SI | Neck flexion / extension |
| Q44 | - |  |  | SI | Neck rotation |
| Q45 | - |  |  | SI | Neck lateral flexion |
| Q46 | - |  |  | SI | Hip flexion |
| Q47 | - |  |  | SI | Hip extension |
| Q48 | - |  |  | SI | Hip abduction |
| Q49 | - |  |  | SI | Hip internal rotation |
| Q50 | - |  |  | SI | Hip external rotation |
| Q51 | - |  |  | SI | Knee flexion |
| Q52 | - |  |  | SI | Knee extension |
| Q53 | - |  |  | SI | Plantarflexion |
| Q54 | - |  |  | SI | Dorsiflexion |
| Q55 | - |  |  | SI | Lower Limb Movement |
| Q56 | - |  |  | SI | Stemmer Sign |
| Q57 | - |  |  | SI | Stemmer sign right |
| Q58 | - |  |  | SI | Stemmer Sign Left |
| Q59 | - |  |  | SI | Ankle brachial pressure index |
| Q60 | - |  |  | SI | Upper Limb Measurements (Bioimpedance and Volumete... |
| Q61 | - |  |  | SI | Dominant |
| Q62 | - |  |  | SI | Surgery |
| Q63 | - |  |  | SI | Rung |
| Q64 | - |  |  | SI | Hand position |
| Q65 | - |  |  | SI | Other (please specify) |
| Q67 | - |  |  | SI | Notes |
| Q69 | - |  |  | SI | Management plan |
| Q70 | - |  |  | SI | Referral to |
| Q71 | - |  |  | SI | Active |
| Q72 | - |  |  | SI | Passive |
| Q73 | - |  |  | SI | Active Left |
| Q74 | - |  |  | SI | Active Left |
| Q75 | - |  |  | SI | Active Left |
| Q76 | - |  |  | SI | Active Left |
| Q77 | - |  |  | SI | Active Left |
| Q78 | - |  |  | SI | Active Left |
| Q79 | - |  |  | SI | Active Right |
| Q80 | - |  |  | SI | Active Right |
| Q81 | - |  |  | SI | Active Right |
| Q82 | - |  |  | SI | Active Right |
| Q83 | - |  |  | SI | Active Right |
| Q84 | - |  |  | SI | Active Right |
| Q85 | - |  |  | SI | Passive Left |
| Q86 | - |  |  | SI | Passive Left |
| Q87 | - |  |  | SI | Passive Left |
| Q88 | - |  |  | SI | Passive Left |
| Q89 | - |  |  | SI | Passive Left |
| Q90 | - |  |  | SI | Passive Left |
| Q91 | - |  |  | SI | Passive Right |
| Q92 | - |  |  | SI | Passive Right |
| Q93 | - |  |  | SI | Passive Right |
| Q94 | - |  |  | SI | Passive Right |
| Q95 | - |  |  | SI | Passive Right |
| Q96 | - |  |  | SI | Passive Right |
| Q97 | - |  |  | SI | Neck flexion |
| Q98 | - |  |  | SI | Neck extension |
| Q99 | - |  |  | SI | Neck rotation |
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
| VRCH_ApplyRate | varchar |  |  | SI | ApplyRate |
| VRCH_BagChanged | varchar |  |  | SI | Bag Changed |
| VRCH_BolusAmt | double |  |  | SI | BolusAmt  |
| VRCH_BolusUOM_DR | bigint |  | FK | SI | BolusUOM |
| VRCH_CalcIVDose | varchar |  |  | SI | CalcIVDose   |
| VRCH_Childsub | double |  |  | NO | Childsub |
| VRCH_Comments | varchar |  |  | SI | Comments |
| VRCH_Date | date |  |  | SI | Date |
| VRCH_DeliveryRate | double |  |  | SI | DeliveryRate |
| VRCH_DeliveryUOM_DR | bigint |  | FK | SI | DeliveryUOM |
| VRCH_DropsPerMinute | double |  |  | SI | DropsPerMinute |
| VRCH_IVCalcMethod | varchar |  |  | SI | IV calculation method 85138 standard type IVCalcMe... |
| VRCH_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| VRCH_LastUpdateRateType | varchar |  |  | SI | Type of Admin Rate used during last update |
| VRCH_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| VRCH_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| VRCH_NewTime | double |  |  | SI | NewTime |
| VRCH_NewVolume | double |  |  | SI | NewVolume |
| VRCH_O2DeliveryMethod_DR | bigint |  | FK | SI | O2 Delivery Method |
| VRCH_O2Rate | double |  |  | SI | O2 Rate |
| VRCH_O2RateCalMethod | varchar |  |  | SI | O2 Rate Calculation Method |
| VRCH_O2RateUOM_DR | bigint |  | FK | SI | O2 Rate UOM |
| VRCH_OverseeUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| VRCH_PCASuspended | varchar |  |  | SI | PCASuspended |
| VRCH_PatientWeight | double |  |  | SI | PatientWeight |
| VRCH_Reason_DR | bigint |  | FK | SI | Des Ref PHCReasonIVRateChange |
| VRCH_RowId | varchar |  |  | NO | - |
| VRCH_Time | time |  |  | SI | Time |
| VRCH_TimeUnit | varchar |  |  | SI | TimeUnit |
| VRCH_TotalVolInfused | double |  |  | SI | Total Volume Infused  |
| VRCH_User_DR | bigint |  | FK | SI | Des Ref SSUser |
| VRCH_VolumeRemaining | double |  |  | SI | VolumeRemaining |
| VRCH_VolumeUnit | varchar |  |  | SI | VolumeUnit |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
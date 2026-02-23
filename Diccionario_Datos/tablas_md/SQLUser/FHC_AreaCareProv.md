# SQLUser.FHC_AreaCareProv

**Schema:** SQLUser
**Columnas:** 224
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CP_ParRef | bigint | PK |  | NO | FHC_Area Parent Reference |
| CP_CareProv_DR | varchar |  | FK | SI | Des Ref to CTCareProv |
| CP_Childsub | double |  |  | NO | Childsub |
| CP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CP_CreatedDate | date |  |  | SI | Created Date |
| CP_CreatedTime | time |  |  | SI | Created Time |
| CP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CP_DateFrom | date |  |  | SI | Date From |
| CP_DateTo | date |  |  | SI | Date To |
| CP_RowId | varchar |  |  | NO | - |
| CP_UpdatedDate | date |  |  | SI | Updated Date |
| CP_UpdatedTime | time |  |  | SI | Updated Time |
| CP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Focus of case history |
| Q04 | - |  |  | SI | Include general history questions |
| Q05 | - |  |  | SI | History obtained from |
| Q06 | - |  |  | SI | History obtained from - comments |
| Q07 | - |  |  | SI | Referral details |
| Q08 | - |  |  | SI | Detail of issue (in patient's / carer's own words) |
| Q09 | - |  |  | SI | Have you ever had any past difficulties like this ... |
| Q10 | - |  |  | SI | Details including any speech pathologist / other t... |
| Q100 | - |  |  | SI | Excessive Mucus |
| Q101 | - |  |  | SI | Excessive Mucus |
| Q102 | - |  |  | SI | Mucus comments |
| Q103 | - |  |  | SI | Mucus comments |
| Q104 | - |  |  | SI | Post nasal drip |
| Q105 | - |  |  | SI | Post nasal drip comments |
| Q106 | - |  |  | SI | Pain associated with condition? |
| Q107 | - |  |  | SI | Pain comments |
| Q108 | - |  |  | SI | Neck pain / ache / throbbing / radiating |
| Q109 | - |  |  | SI | Neck pain comments |
| Q11 | - |  |  | SI | Note: All significant medical history should be do... |
| Q110 | - |  |  | SI | Burning / Scratching / Tickling / Lump in your thr... |
| Q111 | - |  |  | SI | Throat comments |
| Q112 | - |  |  | SI | Food gets stuck |
| Q113 | - |  |  | SI | If yes, consider consistencies, material, when, fr... |
| Q114 | - |  |  | SI | Food stuck comments |
| Q115 | - |  |  | SI | Vomiting and/or regurgitation |
| Q116 | - |  |  | SI | Vomiting / Regurgitation comments |
| Q117 | - |  |  | SI | Reflux / Indigestion / Heartburn? |
| Q118 | - |  |  | SI | General detail including time of occurrence |
| Q119 | - |  |  | SI | Do you take medication for this? If yes, is it eff... |
| Q12 | - |  |  | SI | Existing impairment or history: |
| Q120 | - |  |  | SI | Indigestion medication detail |
| Q121 | - |  |  | SI | Coughing and/or throat clearing? |
| Q122 | - |  |  | SI | Coughing / Throat clearing comments |
| Q123 | - |  |  | SI | Wake up at night coughing |
| Q124 | - |  |  | SI | Night coughing comments |
| Q125 | - |  |  | SI | Choking episodes  (consistencies, airway obstructi... |
| Q126 | - |  |  | SI | Choking comments |
| Q127 | - |  |  | SI | Voice fatigue |
| Q128 | - |  |  | SI | Voice fatigue comments |
| Q129 | - |  |  | SI | Voice loss |
| Q13 | - |  |  | SI | Swallow |
| Q130 | - |  |  | SI | Voice loss comments	 |
| Q131 | - |  |  | SI | Voice / Speech changes associated with swallowing ... |
| Q132 | - |  |  | SI | Voice / Speech changes related to swallowing / ind... |
| Q133 | - |  |  | SI | Did you develop any other difficulties at the same... |
| Q134 | - |  |  | SI | Other difficulties - comments |
| Q135 | - |  |  | SI | Signs & symptoms comments |
| Q136 | - |  |  | SI | Exacerbation and Relief |
| Q137 | - |  |  | SI | Which of the following have you found / trialled t... |
| Q138 | - |  |  | SI | Medication |
| Q139 | - |  |  | SI | Medication comment |
| Q14 | - |  |  | SI | Swallow history details |
| Q140 | - |  |  | SI | Certain food / fluid types |
| Q141 | - |  |  | SI | Food / Fluid type comment |
| Q142 | - |  |  | SI | Rate of food intake |
| Q143 | - |  |  | SI | Rate of food intake comment |
| Q144 | - |  |  | SI | Changing chewing / size of mouthful |
| Q145 | - |  |  | SI | Changing chewing / size of mouthful comment |
| Q146 | - |  |  | SI | Hot food / liquid |
| Q147 | - |  |  | SI | Hot food / liquid comment |
| Q148 | - |  |  | SI | Cold food / liquid |
| Q149 | - |  |  | SI | Cold food / liquid comment |
| Q15 | - |  |  | SI | Speech |
| Q150 | - |  |  | SI | Eating / Drinking equipment trialled |
| Q151 | - |  |  | SI | Equipment comments |
| Q152 | - |  |  | SI | Equipment outcome |
| Q153 | - |  |  | SI | Equipment outcome comments |
| Q154 | - |  |  | SI | Posture / Position |
| Q155 | - |  |  | SI | Posture / Position comments |
| Q156 | - |  |  | SI | Situation / Environment |
| Q157 | - |  |  | SI | Situation / Environment comment |
| Q158 | - |  |  | SI | Therapy (eg. speech, acupuncture, physio) |
| Q159 | - |  |  | SI | Therapy comment |
| Q16 | - |  |  | SI | Speech history details |
| Q160 | - |  |  | SI | Other |
| Q161 | - |  |  | SI | Other things tried comments |
| Q162 | - |  |  | SI | Compensation |
| Q163 | - |  |  | SI | Have you done anything to compensate for this cond... |
| Q164 | - |  |  | SI | Additional detail |
| Q165 | - |  |  | SI | Do you want to change your current condition? |
| Q166 | - |  |  | SI | What would you like to change most? |
| Q167 | - |  |  | SI | Is there anything you'd like to get back to doing? |
| Q168 | - |  |  | SI | Get back to doing comments |
| Q169 | - |  |  | SI | Patient goals |
| Q17 | - |  |  | SI | Language |
| Q170 | - |  |  | SI | Thoughts on cause comments |
| Q18 | - |  |  | SI | Language history details |
| Q19 | - |  |  | SI | Voice |
| Q20 | - |  |  | SI | Voice history details |
| Q21 | - |  |  | SI | Vision |
| Q22 | - |  |  | SI | Vision details |
| Q23 | - |  |  | SI | Hearing |
| Q24 | - |  |  | SI | Hearing details |
| Q25 | - |  |  | SI | Cognitive communication |
| Q26 | - |  |  | SI | Cognitive communication history details |
| Q27 | - |  |  | SI | Augmentative and alternative communication (AAC) m... |
| Q28 | - |  |  | SI | AAC Details |
| Q29 | - |  |  | SI | Other AAC |
| Q30 | - |  |  | SI | Risk factors for developing aspiration pneumonia (... |
| Q31 | - |  |  | SI | Associated history comments |
| Q32 | - |  |  | SI | Current social supports in place? |
| Q33 | - |  |  | SI | Social support detail |
| Q34 | - |  |  | SI | Current social service support? |
| Q35 | - |  |  | SI | Social service detail |
| Q36 | - |  |  | SI | Occupation (current or previous) |
| Q37 | - |  |  | SI | Voice use (professional / social / vocal activitie... |
| Q38 | - |  |  | SI | Physical activity and leisure (current or previous... |
| Q39 | - |  |  | SI | Sleep patterns |
| Q40 | - |  |  | SI | Education |
| Q41 | - |  |  | SI | Social & lifestyle comments |
| Q42 | - |  |  | SI | This question end dated during initial configurati... |
| Q42a | - |  |  | SI | Dysphagia assessment not completed |
| Q43 | - |  |  | SI | Reason |
| Q44 | - |  |  | SI | Do you have any difficulty with your speech? |
| Q45 | - |  |  | SI | How would you describe your speech |
| Q46 | - |  |  | SI | Has it changed? If yes, what did your speech sound... |
| Q47 | - |  |  | SI | Consider loudness, rate, effort, precision |
| Q48 | - |  |  | SI | Speech change comments |
| Q49 | - |  |  | SI | Dysphagia to substance |
| Q50 | - |  |  | SI | Dysphagia to substance comments |
| Q51 | - |  |  | SI | How would you describe the onset? |
| Q52 | - |  |  | SI | Onset comments |
| Q53 | - |  |  | SI | How long have you been aware of this? |
| Q54 | - |  |  | SI | Has it ever returned to normal? |
| Q55 | - |  |  | SI | Returned to normal comments |
| Q56 | - |  |  | SI | How would you describe the frequency? |
| Q57 | - |  |  | SI | Frequency comments |
| Q58 | - |  |  | SI | Has it changed / progressed over time? If so, how? |
| Q59 | - |  |  | SI | Progression comments |
| Q60 | - |  |  | SI | When does the the dysphagia occur? |
| Q61 | - |  |  | SI | Dysphagia timing comments |
| Q62 | - |  |  | SI | Where does it feel like it's located? |
| Q63 | - |  |  | SI | Location comments |
| Q64 | - |  |  | SI | Has anyone ever commented or had trouble understan... |
| Q65 | - |  |  | SI | Difficulty being understood comments |
| Q66 | - |  |  | SI | Does this impact aspects of your life? i.e. work, ... |
| Q67 | - |  |  | SI | Quality of life comments |
| Q68 | - |  |  | SI | Have you seen any other health professionals about... |
| Q69 | - |  |  | SI | Other investigation comments |
| Q70 | - |  |  | SI | Have you been told anything about your condition /... |
| Q71 | - |  |  | SI | Condition / Prognosis comments |
| Q72 | - |  |  | SI | Do you have any thoughts about what has caused thi... |
| Q73 | - |  |  | SI | Additional case history detail |
| Q74 | - |  |  | SI | Current diet |
| Q75 | - |  |  | SI | Diet |
| Q76 | - |  |  | SI | Solids |
| Q77 | - |  |  | SI | Solids comment |
| Q78 | - |  |  | SI | Liquids |
| Q79 | - |  |  | SI | Liquids comment |
| Q80 | - |  |  | SI | Alternative feeding |
| Q81 | - |  |  | SI | Alternative feeding comments |
| Q82 | - |  |  | SI | Average daily water intake |
| Q83 | - |  |  | SI | Consumption of caffeinated drinks |
| Q84 | - |  |  | SI | Caffeinated drink comments |
| Q85 | - |  |  | SI | Has your diet changed because of this issue? If ye... |
| Q86 | - |  |  | SI | Diet change comments |
| Q87 | - |  |  | SI | What is your method of taking tablets? |
| Q88 | - |  |  | SI | Tablet comments |
| Q89 | - |  |  | SI | Detail of current diet (including fluids)? |
| Q90 | - |  |  | SI | Associated Signs & Symptoms |
| Q91 | - |  |  | SI | Do you experience any of the following? |
| Q92 | - |  |  | SI | Weight changes |
| Q93 | - |  |  | SI | Weight change comments |
| Q94 | - |  |  | SI | Appetite changes |
| Q95 | - |  |  | SI | Appetite change comments |
| Q96 | - |  |  | SI | Taste changes, including bad taste in mouth? |
| Q97 | - |  |  | SI | Taste change comments |
| Q98 | - |  |  | SI | Saliva symptoms |
| Q99 | - |  |  | SI | Saliva comments |
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
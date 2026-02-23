# SQLUser.PAC_OSVisitorStatus

**Schema:** SQLUser
**Columnas:** 233
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OVS_RowId | bigint | PK |  | NO | - |
| OVS_Code | varchar |  |  | NO | Code |
| OVS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OVS_CreatedDate | date |  |  | SI | Created Date |
| OVS_CreatedTime | time |  |  | SI | Created Time |
| OVS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OVS_Desc | varchar |  |  | NO | Description |
| OVS_Owner | varchar |  |  | SI | Owner |
| OVS_UpdatedDate | date |  |  | SI | Updated Date |
| OVS_UpdatedTime | time |  |  | SI | Updated Time |
| OVS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1a. Level of consciousness (LOC) |
| Q02 | - |  |  | SI | 1b. LOC Questions: The patient is asked the month ... |
| Q03 | - |  |  | SI | 1c. LOC Commands: The patient is asked to open and... |
| Q04 | - |  |  | SI | 2. Best Gaze: Only horizontal eye movements will b... |
| Q05 | - |  |  | SI | 3. Visual: Visual fields (upper and lower quadrant... |
| Q06 | - |  |  | SI | 4. Facial Palsy: Ask – or use pantomime to encoura... |
| Q07 | - |  |  | SI | 5a. Motor arm - Right |
| Q08 | - |  |  | SI | 5b. Motor arm - Left |
| Q09 | - |  |  | SI | 6a. Motor leg - Right |
| Q10 | - |  |  | SI | 6b. Motor leg - Left |
| Q100 | - |  |  | SI | The examiner must choose a score for the patient w... |
| Q101 | - |  |  | SI | but a score of 3 should be used only if the patien... |
| Q102 | - |  |  | SI | What is happening in this picture? |
| Q103 | - |  |  | SI | Name these items |
| Q104 | - |  |  | SI | Read this list of sentences |
| Q105 | - |  |  | SI | You know how. |
| Q106 | - |  |  | SI | Down to earth. |
| Q107 | - |  |  | SI | I got home from work. |
| Q108 | - |  |  | SI | They heard him speak on the radio last night. |
| Q109 | - |  |  | SI | 10. Dysarthria: If patient is thought to be normal... |
| Q11 | - |  |  | SI | 7. Limb ataxia |
| Q110 | - |  |  | SI | If the patient has severe aphasia, the clarity of ... |
| Q111 | - |  |  | SI | the examiner should record the score as untestable... |
| Q112 | - |  |  | SI | the examiner should record the score as untestable... |
| Q113 | - |  |  | SI | Repeat these words |
| Q114 | - |  |  | SI | MAMA |
| Q115 | - |  |  | SI | TIP - TOP |
| Q116 | - |  |  | SI | FIFTY - FIFTY |
| Q117 | - |  |  | SI | THANKS |
| Q118 | - |  |  | SI | HUCKLEBERRY |
| Q119 | - |  |  | SI | 11. Extinction and Inattention (formerly Neglect):... |
| Q12 | - |  |  | SI | 8. Sensory |
| Q120 | - |  |  | SI | If the patient has a severe visual loss preventing... |
| Q121 | - |  |  | SI | If the patient has aphasia but does appear to atte... |
| Q122 | - |  |  | SI | Since the abnormality is scored only if present, t... |
| Q123 | - |  |  | SI | Since the abnormality is scored only if present, t... |
| Q124 | - |  |  | SI | Near the table in the dining room. |
| Q125 | - |  |  | SI | BASEBALL PLAYER |
| Q126 | - |  |  | SI | Total Score |
| Q127 | - |  |  | SI | Assessment type |
| Q128 | - |  |  | SI | • Brott T, Adams Jr HP, Olinger CP, Marler JR, Bar... |
| Q129 | - |  |  | SI | • Lyden P, Brott T, Tilley B, Welch KM, Mascha EJ,... |
| Q13 | - |  |  | SI | 9. Best language |
| Q130 | - |  |  | SI | • National Institute for Neurological Diseases and... |
| Q131 | - |  |  | SI | 1a. Level of Consciousness: The investigator must ... |
| Q132 | - |  |  | SI | A 3 is scored only if the patient makes no movemen... |
| Q133 | - |  |  | SI | 1b. LOC Questions: The patient is asked the month ... |
| Q134 | - |  |  | SI | Patients unable to speak because of endotracheal i... |
| Q135 | - |  |  | SI | It is important that only the initial answer be gr... |
| Q136 | - |  |  | SI | 1c. LOC Commands: The patient is asked to open and... |
| Q137 | - |  |  | SI | Credit is given if an unequivocal attempt is made ... |
| Q138 | - |  |  | SI | and the result scored (i.e., follows none, one or ... |
| Q139 | - |  |  | SI | 1. Best Gaze: Only horizontal eye movements will b... |
| Q14 | - |  |  | SI | 10. Dysarthria |
| Q140 | - |  |  | SI | If the patient has a conjugate deviation of the ey... |
| Q141 | - |  |  | SI | Gaze is testable in all aphasic patients. Patients... |
| Q142 | - |  |  | SI | and a choice made by the investigator. Establishin... |
| Q143 | - |  |  | SI | 2. Visual: Visual fields (upper and lower quadrant... |
| Q144 | - |  |  | SI | but if they look at the side of the moving fingers... |
| Q145 | - |  |  | SI | Score 1 only if a clear-cut asymmetry, including q... |
| Q146 | - |  |  | SI | patient receives a 1, and the results are used to ... |
| Q147 | - |  |  | SI | 3. Facial Palsy: Ask – or use pantomime to encoura... |
| Q148 | - |  |  | SI | Score symmetry of grimace in response to noxious s... |
| Q149 | - |  |  | SI | tape or other physical barriers obscure the face, ... |
| Q15 | - |  |  | SI | 11. Extinction and inattention (formerly neglect) |
| Q150 | - |  |  | SI | 4. Motor Arm: The limb is placed in the appropriat... |
| Q151 | - |  |  | SI | The aphasic patient is encouraged using urgency in... |
| Q152 | - |  |  | SI | Only in the case of amputation or joint fusion at ... |
| Q153 | - |  |  | SI | 5. Motor Leg: The limb is placed in the appropriat... |
| Q154 | - |  |  | SI | The aphasic patient is encouraged using urgency in... |
| Q155 | - |  |  | SI | Only in the case of amputation or joint fusion at ... |
| Q156 | - |  |  | SI | 6. Limb Ataxia: This item is aimed at finding evid... |
| Q157 | - |  |  | SI | The finger-nose-finger and heel-shin tests are per... |
| Q158 | - |  |  | SI | Only in the case of amputation or joint fusion, th... |
| Q159 | - |  |  | SI | test by having the patient touch nose from extende... |
| Q16 | - |  |  | SI | 0: No stroke symptoms |
| Q160 | - |  |  | SI | 7. Sensory: Sensation or grimace to pinprick when ... |
| Q161 | - |  |  | SI | Only sensory loss attributed to stroke is scored a... |
| Q162 | - |  |  | SI | A score of 2, “severe or total sensory loss,” shou... |
| Q163 | - |  |  | SI | Stuporous and aphasic patients will, therefore, pr... |
| Q164 | - |  |  | SI | If the patient does not respond and is quadriplegi... |
| Q165 | - |  |  | SI | 8. Best Language: A great deal of information abou... |
| Q166 | - |  |  | SI | picture, to name the items on the attached naming ... |
| Q167 | - |  |  | SI | as well as to all of the commands in the preceding... |
| Q168 | - |  |  | SI | repeat, and produce speech. The intubated patient ... |
| Q169 | - |  |  | SI | The examiner must choose a score for the patient w... |
| Q17 | - |  |  | SI | 1 - 4: Minor stroke |
| Q170 | - |  |  | SI | 9. Dysarthria: If patient is thought to be normal,... |
| Q171 | - |  |  | SI | If the patient has severe aphasia, the clarity of ... |
| Q172 | - |  |  | SI | the examiner should record the score as untestable... |
| Q173 | - |  |  | SI | 10. Extinction and Inattention (formerly Neglect):... |
| Q174 | - |  |  | SI | If the patient has a severe visual loss preventing... |
| Q175 | - |  |  | SI | If the patient has aphasia but does appear to atte... |
| Q176 | - |  |  | SI | Since the abnormality is scored only if present, t... |
| Q177 | - |  |  | SI | 5a. Motor arm - Right |
| Q178 | - |  |  | SI | 5b. Motor arm - Left |
| Q179 | - |  |  | SI | 6a. Motor leg - Right |
| Q18 | - |  |  | SI | 5 - 15: Moderate stroke |
| Q180 | - |  |  | SI | 6b. Motor leg - Left |
| Q181 | - |  |  | SI | 7. Limb ataxia |
| Q182 | - |  |  | SI | 10. Dysarthria |
| Q19 | - |  |  | SI | 16 - 20: Moderate to severe stroke |
| Q20 | - |  |  | SI | 21 - 42:  Severe stroke |
| Q21 | - |  |  | SI | The NIHSS is a 15-item impairment scale, intended ... |
| Q22 | - |  |  | SI | The score for each ability is a number between 0 a... |
| Q23 | - |  |  | SI | The individual scores from each item are summed in... |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Time |
| Q26 | - |  |  | SI | Interval since stroke |
| Q27 | - |  |  | SI | Other interval |
| Q28 | - |  |  | SI | Extends arms (palms down) 90 degrees (if sitting) ... |
| Q29 | - |  |  | SI | Hold the leg at 30 degrees (always tested supine) ... |
| Q30 | - |  |  | SI | Test upper arms, legs, trunk and face. Compare sid... |
| Q31 | - |  |  | SI | Describe picture, name items and read sentences |
| Q32 | - |  |  | SI | Read or repeat several words |
| Q33 | - |  |  | SI | For full instructions, please refer to |
| Q34 | - |  |  | SI | Score |
| Q35 | - |  |  | SI | Classification |
| Q36 | - |  |  | SI | 0 |
| Q37 | - |  |  | SI | No stroke symptoms |
| Q38 | - |  |  | SI | 1 - 4 |
| Q39 | - |  |  | SI | Minor stroke |
| Q40 | - |  |  | SI | 5 - 15 |
| Q41 | - |  |  | SI | Moderate stroke |
| Q42 | - |  |  | SI | 16 - 20 |
| Q43 | - |  |  | SI | Moderate to severe stroke |
| Q44 | - |  |  | SI | 21 - 42 |
| Q45 | - |  |  | SI | Severe stroke |
| Q46 | - |  |  | SI | The maximum possible score is 42, with the minimum... |
| Q47 | - |  |  | SI | Administer stroke scale items in the order listed.... |
| Q48 | - |  |  | SI | Scores should reflect what the patient does, not w... |
| Q49 | - |  |  | SI | Except where indicated, the patient should not be ... |
| Q50 | - |  |  | SI | Instructions |
| Q51 | - |  |  | SI | 1a. Level of consciousness |
| Q52 | - |  |  | SI | 1a. Level of Consciousness: The investigator must ... |
| Q53 | - |  |  | SI | A 3 is scored only if the patient makes no movemen... |
| Q54 | - |  |  | SI | 1b. LOC Questions |
| Q55 | - |  |  | SI | 1b. LOC Questions: The patient is asked the month ... |
| Q56 | - |  |  | SI | Patients unable to speak because of endotracheal i... |
| Q57 | - |  |  | SI | It is important that only the initial answer be gr... |
| Q58 | - |  |  | SI | 1c. LOC Commands |
| Q59 | - |  |  | SI | 1c. LOC Commands: The patient is asked to open and... |
| Q60 | - |  |  | SI | Credit is given if an unequivocal attempt is made ... |
| Q61 | - |  |  | SI | and the result scored (i.e., follows none, one or ... |
| Q62 | - |  |  | SI | Patients with trauma, amputation, or other physica... |
| Q63 | - |  |  | SI | 2. Best Gaze: Only horizontal eye movements will b... |
| Q64 | - |  |  | SI | If the patient has a conjugate deviation of the ey... |
| Q65 | - |  |  | SI | Gaze is testable in all aphasic patients. Patients... |
| Q66 | - |  |  | SI | and a choice made by the investigator. Establishin... |
| Q67 | - |  |  | SI | bandages, pre - existing blindness, or other disor... |
| Q68 | - |  |  | SI | Establishing eye contact and then moving about the... |
| Q69 | - |  |  | SI | 3. Visual: Visual fields (upper and lower quadrant... |
| Q70 | - |  |  | SI | but if they look at the side of the moving fingers... |
| Q71 | - |  |  | SI | Score 1 only if a clear-cut asymmetry, including q... |
| Q72 | - |  |  | SI | patient receives a 1, and the results are used to ... |
| Q73 | - |  |  | SI | 4. Facial Palsy: Ask – or use pantomime to encoura... |
| Q74 | - |  |  | SI | Score symmetry of grimace in response to noxious s... |
| Q75 | - |  |  | SI | tape or other physical barriers obscure the face, ... |
| Q76 | - |  |  | SI | If facial  trauma / bandages, orotracheal tube, ta... |
| Q77 | - |  |  | SI | 5. Motor Arm: The limb is placed in the appropriat... |
| Q78 | - |  |  | SI | The aphasic patient is encouraged using urgency in... |
| Q79 | - |  |  | SI | Only in the case of amputation or joint fusion at ... |
| Q80 | - |  |  | SI | Only in the case of amputation or joint fusion at ... |
| Q81 | - |  |  | SI | 6. Motor Leg: The limb is placed in the appropriat... |
| Q82 | - |  |  | SI | The aphasic patient is encouraged using urgency in... |
| Q83 | - |  |  | SI | Only in the case of amputation or joint fusion at ... |
| Q84 | - |  |  | SI | Only in the case of amputation or joint fusion at ... |
| Q85 | - |  |  | SI | 7. Limb Ataxia: This item is aimed at finding evid... |
| Q86 | - |  |  | SI | The finger-nose-finger and heel-shin tests are per... |
| Q87 | - |  |  | SI | Only in the case of amputation or joint fusion, th... |
| Q88 | - |  |  | SI | test by having the patient touch nose from extende... |
| Q89 | - |  |  | SI | test by having the patient touch nose from extende... |
| Q90 | - |  |  | SI | 8. Sensory: Sensation or grimace to pinprick when ... |
| Q91 | - |  |  | SI | Only sensory loss attributed to stroke is scored a... |
| Q92 | - |  |  | SI | A score of 2, “severe or total sensory loss,” shou... |
| Q93 | - |  |  | SI | Stuporous and aphasic patients will, therefore, pr... |
| Q94 | - |  |  | SI | If the patient does not respond and is quadriplegi... |
| Q95 | - |  |  | SI | Patients in a coma (item 1a = 3) are automatically... |
| Q96 | - |  |  | SI | 9. Best Language: A great deal of information abou... |
| Q97 | - |  |  | SI | picture, to name the items on the attached naming ... |
| Q98 | - |  |  | SI | as well as to all of the commands in the preceding... |
| Q99 | - |  |  | SI | repeat, and produce speech. The intubated patient ... |
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
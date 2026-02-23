# SQLUser.PAC_WardNurseAllocation

**Schema:** SQLUser
**Columnas:** 338
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NUR_ParRef | bigint | PK |  | NO | PAC_Ward Parent Reference |
| NUR_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| NUR_Childsub | double |  |  | NO | Childsub |
| NUR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NUR_CreatedDate | date |  |  | SI | Created Date |
| NUR_CreatedTime | time |  |  | SI | Created Time |
| NUR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NUR_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| NUR_RowId | varchar |  |  | NO | - |
| NUR_UpdatedDate | date |  |  | SI | Updated Date |
| NUR_UpdatedTime | time |  |  | SI | Updated Time |
| NUR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Reason for collection |
| Q04 | - |  |  | SI | Data collection |
| Q05 | - |  |  | SI | For each item, please mark the box for Not True, S... |
| Q06 | - |  |  | SI | Please give your answers on the basis of your chil... |
| Q07 | - |  |  | SI | Please give your answers on the basis of your chil... |
| Q08 | - |  |  | SI | Q1. Considerate of other people’s feelings. |
| Q09 | - |  |  | SI | Q1. I try to be nice to other people. I care about... |
| Q10 | - |  |  | SI | Q2. Restless, overactive, cannot stay still for lo... |
| Q100 | - |  |  | SI | Parent completed SDQ |
| Q101 | - |  |  | SI | Total difficulties score |
| Q102 | - |  |  | SI | Conduct problems score |
| Q103 | - |  |  | SI | Hyperactivity score |
| Q104 | - |  |  | SI | Peer problems score |
| Q105 | - |  |  | SI | Prosocial score |
| Q106 | - |  |  | SI | Emotional problems score |
| Q107 | - |  |  | SI | 0 - 13 |
| Q108 | - |  |  | SI | 14 - 16 |
| Q109 | - |  |  | SI | 17 - 40 |
| Q11 | - |  |  | SI | Q2. I am restless, I cannot stay still for long. |
| Q110 | - |  |  | SI | 0 - 3 |
| Q111 | - |  |  | SI | 4 |
| Q112 | - |  |  | SI | 5 - 10 |
| Q113 | - |  |  | SI | 0 - 2 |
| Q114 | - |  |  | SI | 3 |
| Q115 | - |  |  | SI | 4 - 10 |
| Q116 | - |  |  | SI | 0 - 5 |
| Q117 | - |  |  | SI | 6 |
| Q118 | - |  |  | SI | 7 - 10 |
| Q119 | - |  |  | SI | 0 - 2 |
| Q12 | - |  |  | SI | Q3. Often complains of headaches, stomach-aches or... |
| Q120 | - |  |  | SI | 3 |
| Q121 | - |  |  | SI | 4 - 10 |
| Q122 | - |  |  | SI | 6 - 10 |
| Q123 | - |  |  | SI | 5 |
| Q124 | - |  |  | SI | 0 - 4 |
| Q125 | - |  |  | SI | 0 |
| Q126 | - |  |  | SI | 1 |
| Q127 | - |  |  | SI | 2 - 10 |
| Q128 | - |  |  | SI | Teacher completed SDQ |
| Q129 | - |  |  | SI | Total difficulties score |
| Q13 | - |  |  | SI | Q3. I get a lot of headaches, stomach-aches or sic... |
| Q130 | - |  |  | SI | 0 - 11 |
| Q131 | - |  |  | SI | 12 - 15 |
| Q132 | - |  |  | SI | 16 - 40 |
| Q133 | - |  |  | SI | Emotional problems score |
| Q134 | - |  |  | SI | 0 - 4 |
| Q135 | - |  |  | SI | 5 |
| Q136 | - |  |  | SI | 6 - 10 |
| Q137 | - |  |  | SI | Conduct problems score |
| Q138 | - |  |  | SI | 0 - 2 |
| Q139 | - |  |  | SI | 3 |
| Q14 | - |  |  | SI | Q4. Shares readily with other children (for exampl... |
| Q140 | - |  |  | SI | 4 - 10 |
| Q141 | - |  |  | SI | Hyperactivity score |
| Q142 | - |  |  | SI | 0 - 5 |
| Q143 | - |  |  | SI | 6 |
| Q144 | - |  |  | SI | 7 - 10 |
| Q145 | - |  |  | SI | Peer problems score |
| Q146 | - |  |  | SI | 0 - 3 |
| Q147 | - |  |  | SI | 4 |
| Q148 | - |  |  | SI | 5 - 10 |
| Q149 | - |  |  | SI | Prosocial score |
| Q15 | - |  |  | SI | Q4. I usually share with others, for examples CDs,... |
| Q150 | - |  |  | SI | 6 - 10 |
| Q151 | - |  |  | SI | 5 |
| Q152 | - |  |  | SI | 0 - 4 |
| Q153 | - |  |  | SI | Impact score |
| Q154 | - |  |  | SI | 0 |
| Q155 | - |  |  | SI | 1 |
| Q156 | - |  |  | SI | 2 - 10 |
| Q157 | - |  |  | SI | Self-completed SDQ |
| Q158 | - |  |  | SI | Total difficulties score |
| Q159 | - |  |  | SI | 0 - 15 |
| Q16 | - |  |  | SI | Q5. Often loses temper. |
| Q160 | - |  |  | SI | 16 - 19 |
| Q161 | - |  |  | SI | 20 - 40 |
| Q162 | - |  |  | SI | Emotional problem score |
| Q163 | - |  |  | SI | 0 - 5 |
| Q164 | - |  |  | SI | 6 |
| Q165 | - |  |  | SI | 7 - 10 |
| Q166 | - |  |  | SI | Conduct problems score |
| Q167 | - |  |  | SI | 0 - 3 |
| Q168 | - |  |  | SI | 4 |
| Q169 | - |  |  | SI | 5 - 10 |
| Q17 | - |  |  | SI | Q5. I get very angry and often lose my temper. |
| Q170 | - |  |  | SI | Hyperactivity score |
| Q171 | - |  |  | SI | 0 - 5 |
| Q172 | - |  |  | SI | 6 |
| Q173 | - |  |  | SI | 7 - 10 |
| Q174 | - |  |  | SI | Peer problems score |
| Q175 | - |  |  | SI | 0 -3 |
| Q176 | - |  |  | SI | 4 - 5 |
| Q177 | - |  |  | SI | 6 - 10 |
| Q178 | - |  |  | SI | Prosocial score |
| Q179 | - |  |  | SI | 6 - 10 |
| Q18 | - |  |  | SI | Q6. Rather solitary, prefers to play alone / would... |
| Q180 | - |  |  | SI | 5 |
| Q181 | - |  |  | SI | 0 - 4 |
| Q182 | - |  |  | SI | Impact score |
| Q183 | - |  |  | SI | 0 |
| Q184 | - |  |  | SI | 1 |
| Q185 | - |  |  | SI | 2 - 10 |
| Q186 | - |  |  | SI | There are several scoring methods used within the ... |
| Q187 | - |  |  | SI | Within normal limits: |
| Q188 | - |  |  | SI | The score is close to average - clinically signifi... |
| Q189 | - |  |  | SI | Borderline: |
| Q19 | - |  |  | SI | Q6. I would rather be alone than with people of my... |
| Q190 | - |  |  | SI | This score is slightly outside of normal limits wh... |
| Q191 | - |  |  | SI | Abnormal: |
| Q192 | - |  |  | SI | This score is outside of normal limits - there is ... |
| Q193 | - |  |  | SI | Please check the interpretation of the score in th... |
| Q194 | - |  |  | SI | Impact score |
| Q195 | - |  |  | SI | The Strengths and Difficulties Questionnaire (SDQ)... |
| Q196 | - |  |  | SI | B. Total Difficulties Score |
| Q197 | - |  |  | SI | Calculation: Depending on the data collection the ... |
| Q198 | - |  |  | SI | Within Normal Limit |
| Q199 | - |  |  | SI | Within Normal Limit |
| Q20 | - |  |  | SI | Q7. Generally well behaved / usually does what adu... |
| Q200 | - |  |  | SI | Within Normal Limit |
| Q201 | - |  |  | SI | Within Normal Limit |
| Q202 | - |  |  | SI | Within Normal Limit |
| Q203 | - |  |  | SI | Within Normal Limit |
| Q204 | - |  |  | SI | Within Normal Limit |
| Q205 | - |  |  | SI | Borderline |
| Q206 | - |  |  | SI | Borderline |
| Q207 | - |  |  | SI | Borderline |
| Q208 | - |  |  | SI | Borderline |
| Q209 | - |  |  | SI | Borderline |
| Q21 | - |  |  | SI | Q7. I usually do as I am told. |
| Q210 | - |  |  | SI | Borderline |
| Q211 | - |  |  | SI | Borderline |
| Q212 | - |  |  | SI | Abnormal |
| Q213 | - |  |  | SI | Abnormal |
| Q214 | - |  |  | SI | Abnormal |
| Q215 | - |  |  | SI | Abnormal |
| Q216 | - |  |  | SI | Abnormal |
| Q217 | - |  |  | SI | Abnormal |
| Q218 | - |  |  | SI | Abnormal |
| Q219 | - |  |  | SI | Within Normal Limit |
| Q22 | - |  |  | SI | Q8. Many worries or often seems worried. |
| Q220 | - |  |  | SI | Within Normal Limit |
| Q221 | - |  |  | SI | Within Normal Limit |
| Q222 | - |  |  | SI | Within Normal Limit |
| Q223 | - |  |  | SI | Within Normal Limit |
| Q224 | - |  |  | SI | Within Normal Limit |
| Q225 | - |  |  | SI | Within Normal Limit |
| Q226 | - |  |  | SI | Borderline |
| Q227 | - |  |  | SI | Borderline |
| Q228 | - |  |  | SI | Borderline |
| Q229 | - |  |  | SI | Borderline |
| Q23 | - |  |  | SI | Q8. I worry a lot. |
| Q230 | - |  |  | SI | Borderline |
| Q231 | - |  |  | SI | Borderline |
| Q232 | - |  |  | SI | Borderline |
| Q233 | - |  |  | SI | Abnormal |
| Q234 | - |  |  | SI | Abnormal |
| Q235 | - |  |  | SI | Abnormal |
| Q236 | - |  |  | SI | Abnormal |
| Q237 | - |  |  | SI | Abnormal |
| Q238 | - |  |  | SI | Abnormal |
| Q239 | - |  |  | SI | Abnormal |
| Q24 | - |  |  | SI | Q9. Helpful if someone is hurt, upset or feeling i... |
| Q240 | - |  |  | SI | Within Normal Limit |
| Q241 | - |  |  | SI | Within Normal Limit |
| Q242 | - |  |  | SI | Within Normal Limit |
| Q243 | - |  |  | SI | Within Normal Limit |
| Q244 | - |  |  | SI | Within Normal Limit |
| Q245 | - |  |  | SI | Within Normal Limit |
| Q246 | - |  |  | SI | Within Normal Limit |
| Q247 | - |  |  | SI | Borderline |
| Q248 | - |  |  | SI | Borderline |
| Q249 | - |  |  | SI | Borderline |
| Q25 | - |  |  | SI | Q9. I am helpful if someone is hurt, upset or feel... |
| Q250 | - |  |  | SI | Borderline |
| Q251 | - |  |  | SI | Borderline |
| Q252 | - |  |  | SI | Borderline |
| Q253 | - |  |  | SI | Borderline |
| Q254 | - |  |  | SI | Abnormal |
| Q255 | - |  |  | SI | Abnormal |
| Q256 | - |  |  | SI | Abnormal |
| Q257 | - |  |  | SI | Abnormal |
| Q258 | - |  |  | SI | Abnormal |
| Q259 | - |  |  | SI | Abnormal |
| Q26 | - |  |  | SI | Q10. Constantly fidgeting or squirming. |
| Q260 | - |  |  | SI | Abnormal |
| Q261 | - |  |  | SI | Total difficulties score |
| Q262 | - |  |  | SI | Emotional problem score |
| Q263 | - |  |  | SI | Conduct problems score |
| Q264 | - |  |  | SI | Hyperactivity score |
| Q265 | - |  |  | SI | Peer problems score |
| Q266 | - |  |  | SI | Prosocial score |
| Q267 | - |  |  | SI | Impact score |
| Q268 | - |  |  | SI | Total difficulties score |
| Q269 | - |  |  | SI | Emotional problems score |
| Q27 | - |  |  | SI | Q10. I am constantly fidgeting or squirming. |
| Q270 | - |  |  | SI | Conduct problems score |
| Q271 | - |  |  | SI | Hyperactivity score |
| Q272 | - |  |  | SI | Peer problems score |
| Q273 | - |  |  | SI | Prosocial score |
| Q274 | - |  |  | SI | Impact score |
| Q275 | - |  |  | SI | Total difficulties score |
| Q276 | - |  |  | SI | Emotional problems score |
| Q277 | - |  |  | SI | Conduct problems score |
| Q278 | - |  |  | SI | Hyperactivity score |
| Q279 | - |  |  | SI | Peer problems score |
| Q28 | - |  |  | SI | Q11. Has at least one good friend. |
| Q280 | - |  |  | SI | Prosocial score |
| Q281 | - |  |  | SI | Impact score |
| Q282 | - |  |  | SI | Goodman R (1997) The Strengths and Difficulties Qu... |
| Q283 | - |  |  | SI | Goodman R (1999) The extended version of the Stren... |
| Q284 | - |  |  | SI | https://www.sdqinfo.org/ |
| Q285 | - |  |  | SI | 1.&nbsp |
| Q286 | - |  |  | SI | 2.&nbsp |
| Q29 | - |  |  | SI | Q11. I have one good friend or more. |
| Q30 | - |  |  | SI | Q12. Often fights with other children or bullies t... |
| Q31 | - |  |  | SI | Q12. I fight a lot. I can make other people do wha... |
| Q32 | - |  |  | SI | Q13. Often unhappy, depressed or tearful. |
| Q33 | - |  |  | SI | Q13. I am often unhappy, depressed or tearful. |
| Q34 | - |  |  | SI | Q14. Generally liked by other children / young peo... |
| Q35 | - |  |  | SI | Q14. Other people my age generally like me. |
| Q36 | - |  |  | SI | Q15. Easily distracted, concentration wanders. |
| Q37 | - |  |  | SI | Q15. I am easily distracted, I find it difficult t... |
| Q38 | - |  |  | SI | Q16. Nervous or clingy in new situations, easily l... |
| Q39 | - |  |  | SI | Q16. I am nervous in new situations. I easily lose... |
| Q40 | - |  |  | SI | Q17. Kind to younger children. |
| Q41 | - |  |  | SI | Q17. I am kind to younger people. |
| Q42 | - |  |  | SI | Q18. Often lies or cheats. |
| Q43 | - |  |  | SI | Q18. I am often accused of lying or cheating. |
| Q44 | - |  |  | SI | Q19. Picked on or bullied by children / youth. |
| Q45 | - |  |  | SI | Q19. Other children or young people pick on me or ... |
| Q46 | - |  |  | SI | Q20. Often volunteers to help others (parents, tea... |
| Q47 | - |  |  | SI | Q20. I often volunteer to help others (parents, te... |
| Q48 | - |  |  | SI | Q21. Thinks things out before acting. |
| Q49 | - |  |  | SI | Q21. I think before I do things. |
| Q50 | - |  |  | SI | Q22. Steals from home, school or elsewhere. |
| Q51 | - |  |  | SI | Q22. I take things that are not mine from home, sc... |
| Q52 | - |  |  | SI | Q23. Gets along better with adults than with other... |
| Q53 | - |  |  | SI | Q23. I get along better with adults than with peop... |
| Q54 | - |  |  | SI | Q24. Many fears, easily scared. |
| Q55 | - |  |  | SI | Q24. I have many fears, I am easily scared. |
| Q56 | - |  |  | SI | Q25. Good attention span sees chores or homework t... |
| Q57 | - |  |  | SI | Q25. I finish the work I’m doing. My attention is ... |
| Q58 | - |  |  | SI | Q26. Overall, do you think that your child has dif... |
| Q59 | - |  |  | SI | Q26. Overall, do you think that you have difficult... |
| Q60 | - |  |  | SI | Q26. Over the last month, do you think that your c... |
| Q61 | - |  |  | SI | Q26. Over the last month, do you think that you ha... |
| Q62 | - |  |  | SI | Q27. How long have these difficulties been present... |
| Q63 | - |  |  | SI | Q27. How long have these difficulties been present... |
| Q64 | - |  |  | SI | Q28. Do the difficulties upset or distress your ch... |
| Q65 | - |  |  | SI | Q28. Do the difficulties upset or distress you? |
| Q66 | - |  |  | SI | Do the difficulties interfere with your child’s ev... |
| Q67 | - |  |  | SI | Do the difficulties interfere with your everyday l... |
| Q68 | - |  |  | SI | Q29. HOME LIFE |
| Q69 | - |  |  | SI | Q30. FRIENDSHIPS |
| Q70 | - |  |  | SI | Q31. CLASSROOM LEARNING |
| Q71 | - |  |  | SI | Q32. LEISURE ACTIVITIES. |
| Q72 | - |  |  | SI | Q33. Do the difficulties put a burden on you or th... |
| Q73 | - |  |  | SI | Q33. Do the difficulties make it harder for those ... |
| Q74 | - |  |  | SI | Q34. Since coming to the services, are your child’... |
| Q75 | - |  |  | SI | Q34. Since coming to the service, are your problem... |
| Q76 | - |  |  | SI | Q35. Has coming to the service been helpful in oth... |
| Q77 | - |  |  | SI | Q36. Over the last 6 months have your child’s teac... |
| Q78 | - |  |  | SI | Q37. Over the last 6 months have your child’s teac... |
| Q79 | - |  |  | SI | Q38. Over the last 6 months have your child’s teac... |
| Q80 | - |  |  | SI | Q39. Does your family complain about you having pr... |
| Q81 | - |  |  | SI | Q40. Do your teachers complain about you having pr... |
| Q82 | - |  |  | SI | Q41. Does your family complain about you being awk... |
| Q83 | - |  |  | SI | Q42. Do your teachers complain about you being awk... |
| Q84 | - |  |  | SI | A. Emotional Symptoms Scale |
| Q85 | - |  |  | SI | A. Conduct Problem Scale |
| Q86 | - |  |  | SI | A. Hyperactivity Scale |
| Q87 | - |  |  | SI | A. Peer Problem Scale |
| Q88 | - |  |  | SI | A. Prosocial Scale |
| Q89 | - |  |  | SI | A. Total Difficulties Score |
| Q90 | - |  |  | SI | Impact Score |
| Q91 | - |  |  | SI | B. Emotional Symptoms Scale |
| Q92 | - |  |  | SI | B. Conduct Problem Scale |
| Q93 | - |  |  | SI | B. Hyperactivity Scale |
| Q94 | - |  |  | SI | B. Peer Problem Scale |
| Q95 | - |  |  | SI | B. Prosocial Scale |
| Q96 | - |  |  | SI | Original three-band categorisation |
| Q97 | - |  |  | SI | Within Normal Limit |
| Q98 | - |  |  | SI | Borderline |
| Q99 | - |  |  | SI | Abnormal |
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
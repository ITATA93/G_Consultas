# SQLUser.CT_ResponsibleUnitCP

**Schema:** SQLUser
**Columnas:** 204
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CP_ParRef | bigint | PK |  | NO | CT_ResponsibleUnit Parent Reference |
| CP_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| CP_Childsub | double |  |  | NO | Childsub |
| CP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CP_CreatedDate | date |  |  | SI | Created Date |
| CP_CreatedTime | time |  |  | SI | Created Time |
| CP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CP_DateFrom | date |  |  | SI | Date From |
| CP_DateTo | date |  |  | SI | DateTo |
| CP_HospitalDR | bigint |  | FK | SI | Hospital DR |
| CP_RowId | varchar |  |  | NO | - |
| CP_UpdatedDate | date |  |  | SI | Updated Date |
| CP_UpdatedTime | time |  |  | SI | Updated Time |
| CP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | All of the tests should be performed in the same o... |
| Q04 | - |  |  | SI | 1. Do you think it would be safe for you to try to... |
| Q05 | - |  |  | SI | 2. Demonstrate and explain the procedure according... |
| Q06 | - |  |  | SI | 3. When the participant is properly seated, say: |
| Q07 | - |  |  | SI | “Ready? Stand” |
| Q08 | - |  |  | SI | 4. Count out loud as the participant arises each t... |
| Q09 | - |  |  | SI | 5. Stop if participant becomes tired or short of b... |
| Q10 | - |  |  | SI | 6. Stop the stopwatch when he/she has straightened... |
| Q100 | - |  |  | SI | Demonstrate |
| Q101 | - |  |  | SI | “Are you ready?” |
| Q102 | - |  |  | SI | “Are you ready?” |
| Q103 | - |  |  | SI | “Ready, begin.” |
| Q104 | - |  |  | SI | Demonstrate |
| Q105 | - |  |  | SI | “Are you ready?” |
| Q106 | - |  |  | SI | “Ready, begin.” |
| Q107 | - |  |  | SI | Remember that this test requires participants to w... |
| Q108 | - |  |  | SI | Demonstrate |
| Q109 | - |  |  | SI | “Ready, begin.” |
| Q11 | - |  |  | SI | 7. Also stop: |
| Q110 | - |  |  | SI | “Stop” |
| Q111 | - |  |  | SI | after 10 seconds or when the participant steps out... |
| Q112 | - |  |  | SI | Try to hold this position until I tell you to stop... |
| Q113 | - |  |  | SI | “Stop” |
| Q114 | - |  |  | SI | after 10 seconds or when the participant steps out... |
| Q115 | - |  |  | SI | “Ready, begin.” |
| Q116 | - |  |  | SI | 3. You may use your arms, bend your knees, or move... |
| Q117 | - |  |  | SI | Stop the stopwatch and say |
| Q118 | - |  |  | SI | “Stop” |
| Q119 | - |  |  | SI | after 10 seconds or when the participant steps out... |
| Q12 | - |  |  | SI | • If participant uses his/her arms |
| Q120 | - |  |  | SI | “Ready, begin.” |
| Q121 | - |  |  | SI | Instructions to the participants are shown in |
| Q122 | - |  |  | SI | bold italic |
| Q123 | - |  |  | SI | and should be given exactly as they are written in... |
| Q124 | - |  |  | SI | Please always click ''Apply'' then ''Update'' to g... |
| Q125 | - |  |  | SI | 0 - 9: One or more mobility limitation |
| Q126 | - |  |  | SI | 10 - 12: No mobility limitation |
| Q127 | - |  |  | SI | 0 - 9 |
| Q128 | - |  |  | SI | 10 - 12 |
| Q129 | - |  |  | SI | Score |
| Q13 | - |  |  | SI | • After 30 seconds, if participant has not complet... |
| Q130 | - |  |  | SI | Classification |
| Q131 | - |  |  | SI | One or more mobility limitation |
| Q132 | - |  |  | SI | No mobility limitation |
| Q133 | - |  |  | SI | The total score is comprised of the sum of Chair S... |
| Q134 | - |  |  | SI | The Modified Short Physical Performance Battery Sc... |
| Q135 | - |  |  | SI | The physical performance evaluation is a screening... |
| Q136 | - |  |  | SI | The score produced by the tool relates to the func... |
| Q137 | - |  |  | SI | Instructions to the participants are shown in bold... |
| Q138 | - |  |  | SI | 3. When I want you to start, I will say: “Ready? S... |
| Q139 | - |  |  | SI | 8. If the participant stops and appears to be fati... |
| Q14 | - |  |  | SI | • At your discretion, if concerned for participant... |
| Q140 | - |  |  | SI | 5. When the participant has his/her feet together,... |
| Q141 | - |  |  | SI | 6. Then let go and begin timing as you say: ''Read... |
| Q142 | - |  |  | SI | Stop the stopwatch and say ''Stop'' after 10 secon... |
| Q143 | - |  |  | SI | 5. When the participant has his/her feet together,... |
| Q144 | - |  |  | SI | 6. Then let go and begin timing as you say: “Ready... |
| Q145 | - |  |  | SI | Stop the stopwatch and say ''Stop'' after 10 secon... |
| Q146 | - |  |  | SI | If participant is unable to hold the position for ... |
| Q147 | - |  |  | SI | 5. When the participant has his/her feet together,... |
| Q148 | - |  |  | SI | 6. Then let go and begin timing as you say: ''Read... |
| Q149 | - |  |  | SI | Stop the stopwatch and say ''Stop'' after 10 secon... |
| Q15 | - |  |  | SI | 8. If the participant stops and appears to be fati... |
| Q150 | - |  |  | SI | When the participant acknowledges this instruction... |
| Q16 | - |  |  | SI | 9. If participant says “Yes,” continue timing. If ... |
| Q17 | - |  |  | SI | Pre-test: Pedir que cruce los brazos sobre el pech... |
| Q18 | - |  |  | SI | Tiempo empleado en levantarse 5 veces de la silla,... |
| Q19 | - |  |  | SI | If participant did not attempt test or failed, why... |
| Q20 | - |  |  | SI | Specify other |
| Q21 | - |  |  | SI | After completing the repeated chair stand test ask... |
| Q22 | - |  |  | SI | If the participant declined to try the test, was u... |
| Q23 | - |  |  | SI | The participant must be able to stand unassisted w... |
| Q24 | - |  |  | SI | Now let’s begin the evaluation. I would now like y... |
| Q25 | - |  |  | SI | If you cannot do a particular movement, or if you ... |
| Q26 | - |  |  | SI | Let me emphasize that I do not want you to try to ... |
| Q27 | - |  |  | SI | Side-by-Side Stand |
| Q28 | - |  |  | SI | 1. Now I will show you the first movement. |
| Q29 | - |  |  | SI | 2. I want you to try to stand with your feet toget... |
| Q30 | - |  |  | SI | 3. You may use your arms, bend your knees, or move... |
| Q31 | - |  |  | SI | 4. Try to hold this position until I tell you to s... |
| Q32 | - |  |  | SI | Stand next to the participant to help him/her into... |
| Q33 | - |  |  | SI | 5. When the participant has his/her feet together,... |
| Q34 | - |  |  | SI | 6. Then let go and begin timing as you say: |
| Q35 | - |  |  | SI | If participant is unable to hold the position for ... |
| Q36 | - |  |  | SI | Pies juntos durante 10 segundos |
| Q37 | - |  |  | SI | If 0 points, end Balance Tests |
| Q38 | - |  |  | SI | Number of seconds held if less than 10 sec |
| Q39 | - |  |  | SI | If participant did not attempt test or failed, why... |
| Q40 | - |  |  | SI | Specify other |
| Q41 | - |  |  | SI | Semi-Tandem Stand |
| Q42 | - |  |  | SI | 1. Now I will show you the second movement. |
| Q43 | - |  |  | SI | 2. Now I want you to try to stand with the side of... |
| Q44 | - |  |  | SI | 3. You may use your arms, bend your knees, or move... |
| Q45 | - |  |  | SI | 4. Stand next to the participant to help him/her i... |
| Q46 | - |  |  | SI | 5. When the participant has his/her feet together,... |
| Q47 | - |  |  | SI | 6. Then let go and begin timing as you say: |
| Q48 | - |  |  | SI | Stop the stopwatch and say |
| Q49 | - |  |  | SI | If participant is unable to hold the position for ... |
| Q50 | - |  |  | SI | Semi-tandem durante 10 segundos |
| Q51 | - |  |  | SI | If 0 points, end Balance Tests |
| Q52 | - |  |  | SI | Number of seconds held if less than 10 sec |
| Q53 | - |  |  | SI | If participant did not attempt test or failed, why... |
| Q54 | - |  |  | SI | Specify other |
| Q55 | - |  |  | SI | Tandem Stand |
| Q56 | - |  |  | SI | 1. Now I will show you the third movement. |
| Q57 | - |  |  | SI | 2. Now I want you to try to stand with the heel of... |
| Q58 | - |  |  | SI | 3. You may use your arms, bend your knees, or move... |
| Q59 | - |  |  | SI | 4. Stand next to the participant to help him/her i... |
| Q60 | - |  |  | SI | 5. When the participant has his/her feet together,... |
| Q61 | - |  |  | SI | 6. Then let go and begin timing as you say: |
| Q62 | - |  |  | SI | Stop the stopwatch and say |
| Q63 | - |  |  | SI | Tándem durante 10 segundos |
| Q64 | - |  |  | SI | Number of seconds held if less than 10 sec |
| Q65 | - |  |  | SI | If participant did not attempt test or failed, why... |
| Q66 | - |  |  | SI | Specify other |
| Q67 | - |  |  | SI | TOTAL BALANCE SCORE: |
| Q68 | - |  |  | SI | Balance Test Side-by-side points |
| Q69 | - |  |  | SI | Balance Test Semi-tandem points |
| Q70 | - |  |  | SI | Balance Test Tandem points |
| Q71 | - |  |  | SI | Total points |
| Q72 | - |  |  | SI | Note: the walking course should be 3 meters (9 fee... |
| Q73 | - |  |  | SI | At least 3 feet is recommended. The course should ... |
| Q74 | - |  |  | SI | If you use a cane or other walking aid and you fee... |
| Q75 | - |  |  | SI | Single Gait Speed Test |
| Q76 | - |  |  | SI | 1. This is our walking course. I want you to walk ... |
| Q77 | - |  |  | SI | Demonstrate the walk for the participant: Tip – be... |
| Q78 | - |  |  | SI | 2. Walk all the way past the other end of the tape... |
| Q79 | - |  |  | SI | Have the participant stand with both feet touching... |
| Q80 | - |  |  | SI | 3. When I want you to start, I will say: |
| Q81 | - |  |  | SI | When the participant acknowledges this instruction... |
| Q82 | - |  |  | SI | 4. Press the start/stop button to start the stopwa... |
| Q83 | - |  |  | SI | Walk behind and to the side of the participant. St... |
| Q84 | - |  |  | SI | Aides used during the walk test |
| Q85 | - |  |  | SI | Specify other |
| Q86 | - |  |  | SI | If participant did not attempt test or failed, why... |
| Q87 | - |  |  | SI | Specify other |
| Q88 | - |  |  | SI | Comments on gait speed test |
| Q89 | - |  |  | SI | Gait Speed Test Scoring |
| Q90 | - |  |  | SI | Time for the walk (seconds) |
| Q91 | - |  |  | SI | Tiempo empleado en caminar 4 metros a ritmo normal |
| Q92 | - |  |  | SI | Chair Stand Test Score |
| Q93 | - |  |  | SI | Total Balance Test Score |
| Q94 | - |  |  | SI | Gait Speed Test Score |
| Q95 | - |  |  | SI | Total Score |
| Q96 | - |  |  | SI | Please stand up straight as QUICKLY as you can fiv... |
| Q97 | - |  |  | SI | I’ll be timing you with a stopwatch. |
| Q98 | - |  |  | SI | and begin timing as you say Stand. |
| Q99 | - |  |  | SI | Can you continue?” |
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
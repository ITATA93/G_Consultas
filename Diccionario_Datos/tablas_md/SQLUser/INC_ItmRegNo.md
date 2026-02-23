# SQLUser.INC_ItmRegNo

**Schema:** SQLUser
**Columnas:** 218
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCIRN_INCI_ParRef | bigint | PK |  | NO | Par Ref to INCItm |
| INCIRN_ApprovalStatus | varchar |  |  | SI | Approval Status |
| INCIRN_ChildSub | numeric |  |  | NO | Childsub |
| INCIRN_Desc | varchar |  |  | NO | Registration Number |
| INCIRN_INCLB_DR | varchar |  | FK | SI | Des Ref to INCItmLcBt |
| INCIRN_INCRND_DR | bigint |  | FK | SI | Des Ref to INCRegNoDesignation |
| INCIRN_INGRI_DR | varchar |  | FK | SI | Des Ref to INGdRecItm |
| INCIRN_Lot | varchar |  |  | SI | Lot |
| INCIRN_RowId | varchar |  |  | NO | - |
| INCIRN_UsageStatus | varchar |  |  | SI | Usage Status |
| Q01 | - |  |  | SI | Affected limb |
| Q02 | - |  |  | SI | CAHAI version used |
| Q03 | - |  |  | SI | CAHAI-7 |
| Q04 | - |  |  | SI | CAHAI-8 |
| Q05 | - |  |  | SI | CAHAI-9 |
| Q06 | - |  |  | SI | CAHAI-13 |
| Q07 | - |  |  | SI | Task |
| Q08 | - |  |  | SI | Affected Limb Activity |
| Q09 | - |  |  | SI | 1. Open jar of coffee |
| Q10 | - |  |  | SI | Question 1 score |
| Q100 | - |  |  | SI | • medium resistance putty |
| Q101 | - |  |  | SI | • knife and fork |
| Q102 | - |  |  | SI | • built up handles the length of the utensil handl... |
| Q103 | - |  |  | SI | Score |
| Q104 | - |  |  | SI | Classification |
| Q107 | - |  |  | SI | The Chedoke Arm and Hand Activity Inventory (CAHAI... |
| Q108 | - |  |  | SI | There are 4 versions: CAHAI-7, CAHAI-8,CAHAI-9, CA... |
| Q109 | - |  |  | SI | 7 - 49 |
| Q11 | - |  |  | SI | 2. Call emergency number |
| Q110 | - |  |  | SI | 8 - 56 |
| Q111 | - |  |  | SI | 9 - 63 |
| Q112 | - |  |  | SI | 13 - 91 |
| Q113 | - |  |  | SI | Score |
| Q114 | - |  |  | SI | Date |
| Q115 | - |  |  | SI | Time |
| Q116 | - |  |  | SI | 1 TOTAL ASSISTANCE - The client expends less than ... |
| Q117 | - |  |  | SI | Score 1 if two people are required to assist in co... |
| Q118 | - |  |  | SI | Score 1 if you feel it is unsafe to try the task. |
| Q119 | - |  |  | SI | The lower the score, the greater the impairment |
| Q12 | - |  |  | SI | Question 2 score |
| Q120 | - |  |  | SI | ) |
| Q121 | - |  |  | SI | to determine what part of the task the affected li... |
| Q122 | - |  |  | SI | Task |
| Q123 | - |  |  | SI | 1. Open jar of coffee |
| Q124 | - |  |  | SI | Affected Limb Activity |
| Q125 | - |  |  | SI | Score |
| Q126 | - |  |  | SI | Task |
| Q127 | - |  |  | SI | 2. Call emergency number |
| Q128 | - |  |  | SI | Affected Limb Activity |
| Q129 | - |  |  | SI | Score |
| Q13 | - |  |  | SI | 3. Draw a line with a ruler |
| Q130 | - |  |  | SI | Task |
| Q131 | - |  |  | SI | 3. Draw a line with a ruler |
| Q132 | - |  |  | SI | Affected Limb Activity |
| Q133 | - |  |  | SI | Score |
| Q134 | - |  |  | SI | Task |
| Q135 | - |  |  | SI | 4. Pour a glass of water |
| Q136 | - |  |  | SI | Affected Limb Activity |
| Q137 | - |  |  | SI | Score |
| Q138 | - |  |  | SI | Task |
| Q139 | - |  |  | SI | 5. Wring out washcloth |
| Q14 | - |  |  | SI | Question 3 score |
| Q140 | - |  |  | SI | Score |
| Q141 | - |  |  | SI | Task |
| Q142 | - |  |  | SI | 6. Do up five buttons |
| Q143 | - |  |  | SI | Affected Limb Activity |
| Q144 | - |  |  | SI | Score |
| Q145 | - |  |  | SI | Task |
| Q146 | - |  |  | SI | 7. Dry back with towel |
| Q147 | - |  |  | SI | Affected Limb Activity |
| Q148 | - |  |  | SI | Score |
| Q149 | - |  |  | SI | Task |
| Q15 | - |  |  | SI | 4. Pour a glass of water |
| Q150 | - |  |  | SI | 8. Put toothpaste on toothbrush |
| Q151 | - |  |  | SI | Affected Limb Activity |
| Q152 | - |  |  | SI | Score |
| Q153 | - |  |  | SI | Task |
| Q154 | - |  |  | SI | 9. Cut medium resistance putty |
| Q155 | - |  |  | SI | Affected Limb Activity |
| Q156 | - |  |  | SI | Score |
| Q157 | - |  |  | SI | Task |
| Q158 | - |  |  | SI | 10. Zip up the zipper |
| Q159 | - |  |  | SI | Affected Limb Activity |
| Q16 | - |  |  | SI | Question 4 score |
| Q160 | - |  |  | SI | Score |
| Q161 | - |  |  | SI | 11. Clean a pair of eyeglasses |
| Q162 | - |  |  | SI | Affected Limb Activity |
| Q163 | - |  |  | SI | Score |
| Q164 | - |  |  | SI | Task |
| Q165 | - |  |  | SI | 12. Place container on table |
| Q166 | - |  |  | SI | Score |
| Q167 | - |  |  | SI | Task |
| Q168 | - |  |  | SI | 13. Carry bag up the stairs |
| Q169 | - |  |  | SI | Score |
| Q17 | - |  |  | SI | 5. Wring out washcloth |
| Q170 | - |  |  | SI | Task |
| Q18 | - |  |  | SI | Question 5 score |
| Q19 | - |  |  | SI | 6. Do up five buttons |
| Q20 | - |  |  | SI | Question 6 score |
| Q21 | - |  |  | SI | 7. Dry back with towel |
| Q22 | - |  |  | SI | Question 7 score |
| Q23 | - |  |  | SI | 8. Put toothpaste on toothbrush |
| Q24 | - |  |  | SI | Question 8 score |
| Q25 | - |  |  | SI | 9. Cut medium resistance putty |
| Q26 | - |  |  | SI | Question 9 score |
| Q27 | - |  |  | SI | 10. Zip up the zipper |
| Q28 | - |  |  | SI | Question 10 score |
| Q29 | - |  |  | SI | 11. Clean a pair of eyeglasses |
| Q30 | - |  |  | SI | Question 11 score |
| Q31 | - |  |  | SI | 12. Place container on table |
| Q32 | - |  |  | SI | Question 12 score |
| Q33 | - |  |  | SI | 13. Carry bag up the stairs |
| Q34 | - |  |  | SI | Question 13 score |
| Q35 | - |  |  | SI | / 49 (CAHAI-7) |
| Q36 | - |  |  | SI | / 56 (CAHAI-8) |
| Q37 | - |  |  | SI | / 63 (CAHAI-9) |
| Q38 | - |  |  | SI | / 91 (CAHAI-13) |
| Q39 | - |  |  | SI | General Instructions for Administering the CAHAI |
| Q40 | - |  |  | SI | The purpose of this measure is to evaluate the fun... |
| Q41 | - |  |  | SI | It is NOT designed to measure the client’s ability... |
| Q42 | - |  |  | SI | Explain to your clients that some tasks are diffic... |
| Q43 | - |  |  | SI | Encourage them to give their best effort using BOT... |
| Q44 | - |  |  | SI | Standard starting position |
| Q45 | - |  |  | SI | Posture: |
| Q46 | - |  |  | SI | seated in chair without armrests or in wheelchair ... |
| Q47 | - |  |  | SI | Height of table: |
| Q48 | - |  |  | SI | at the level of the last costal rib |
| Q49 | - |  |  | SI | Distance from table: |
| Q50 | - |  |  | SI | client's elbow comes to the table edge |
| Q51 | - |  |  | SI | Hands: |
| Q52 | - |  |  | SI | resting on the table Variations from the standard ... |
| Q53 | - |  |  | SI | To ensure the client's understanding: |
| Q54 | - |  |  | SI | Every effort should be made to ensure the client u... |
| Q55 | - |  |  | SI | • each task should be demonstrated once, twice if ... |
| Q56 | - |  |  | SI | • the client may be cued to use both hands twice |
| Q57 | - |  |  | SI | • the client may be reminded not to rest elbows on... |
| Q58 | - |  |  | SI | Scoring |
| Q59 | - |  |  | SI | Score the performance of the affected upper limb u... |
| Q60 | - |  |  | SI | 7 COMPLETE INDEPENDENCE - All of the tasks are per... |
| Q61 | - |  |  | SI | 6 MODIFIED INDEPENDENCE - Activity requires any on... |
| Q62 | - |  |  | SI | 5 SUPERVISION - The client requires no more help t... |
| Q63 | - |  |  | SI | 4 MINIMAL ASSISTANCE - With physical contact the c... |
| Q64 | - |  |  | SI | 3 MODERATE ASSISTANCE - Weak limb manipulates and ... |
| Q65 | - |  |  | SI | 2 MAXIMAL ASSISTANCE - Weak limb stabilizes during... |
| Q66 | - |  |  | SI | Observe the performance of the affected upper limb... |
| Q67 | - |  |  | SI | 1) Use the Task Component Chart (available via |
| Q68 | - |  |  | SI | e.g. affected hand turning the lid or affected han... |
| Q69 | - |  |  | SI | 2) Identify the specific components of manipulatio... |
| Q70 | - |  |  | SI | 3) Use the 7 point Activity Scale to determine the... |
| Q71 | - |  |  | SI | If different performances are observed then assign... |
| Q72 | - |  |  | SI | Score 6 if more than reasonable time is required. ... |
| Q73 | - |  |  | SI | Score 6 if assistive devices (e.g. built up handle... |
| Q74 | - |  |  | SI | Score 6 if there are safety concerns in doing uppe... |
| Q75 | - |  |  | SI | Score 5 if you need to cue throughout the clients'... |
| Q76 | - |  |  | SI | Score 4 if client touches table very briefly |
| Q77 | - |  |  | SI | Score 3 if client continually uses table for suppo... |
| Q78 | - |  |  | SI | Score 1 if client uses only one arm / hand |
| Q79 | - |  |  | SI | Equipment |
| Q80 | - |  |  | SI | List A |
| Q81 | - |  |  | SI | • height adjustable table |
| Q82 | - |  |  | SI | • chair / wheelchair without armrests |
| Q83 | - |  |  | SI | • dycem |
| Q84 | - |  |  | SI | • 200g jar of coffee |
| Q85 | - |  |  | SI | • push-button telephone |
| Q86 | - |  |  | SI | • 12''/30cm ruler |
| Q87 | - |  |  | SI | • 8.5'' x 11'' paper |
| Q88 | - |  |  | SI | • pencil |
| Q89 | - |  |  | SI | • 2.3L plastic pitcher with lid |
| Q90 | - |  |  | SI | • 250 ml plastic cup |
| Q91 | - |  |  | SI | • wash cloth |
| Q92 | - |  |  | SI | • wash basin (24.5 cm. in diameter, height 8 cm.) |
| Q93 | - |  |  | SI | • Pull-on vest with 5 buttons (one side male & one... |
| Q94 | - |  |  | SI | • bath towel (65cm X 100cm) |
| Q95 | - |  |  | SI | List B |
| Q96 | - |  |  | SI | • 75ml toothpaste with screw lid, >50% full |
| Q97 | - |  |  | SI | • toothbrush |
| Q98 | - |  |  | SI | List C |
| Q99 | - |  |  | SI | • dinner plate (Melamine or heavy plastic, 25 cm. ... |
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
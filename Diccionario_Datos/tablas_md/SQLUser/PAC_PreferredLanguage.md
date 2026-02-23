# SQLUser.PAC_PreferredLanguage

**Schema:** SQLUser
**Columnas:** 225
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PREFL_RowId | bigint | PK |  | NO | - |
| PREFL_Code | varchar |  |  | NO | Code |
| PREFL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PREFL_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| PREFL_CreatedDate | date |  |  | SI | Created Date |
| PREFL_CreatedTime | time |  |  | SI | Created Time |
| PREFL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PREFL_DateFrom | date |  |  | SI | Date From |
| PREFL_DateTo | date |  |  | SI | Date To |
| PREFL_Desc | varchar |  |  | NO | Description |
| PREFL_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| PREFL_Dialect | varchar |  |  | SI | Dialect |
| PREFL_ISOCode | varchar |  |  | SI | ISO Code |
| PREFL_Owner | varchar |  |  | SI | Owner |
| PREFL_UpdatedDate | date |  |  | SI | Updated Date |
| PREFL_UpdatedTime | time |  |  | SI | Updated Time |
| PREFL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PREFL_VEMDCode | varchar |  |  | SI | VEMDCode |
| Q01 | - |  |  | SI | Theatre to Recovery |
| Q02 | - |  |  | SI | Recovery to Ward	 |
| Q03 | - |  |  | SI | Confirm patient identity with receiving practition... |
| Q04 | - |  |  | SI | Type of anaesthetic |
| Q05 | - |  |  | SI | Local anaesthetic wound infiltration	 |
| Q06 | - |  |  | SI | Level of consciousness |
| Q07 | - |  |  | SI | Airway maintained |
| Q08 | - |  |  | SI | Breathing |
| Q09 | - |  |  | SI | O2 administered via mask / cannula |
| Q10 | - |  |  | SI | Ensure observations are within normal parameters |
| Q100 | - |  |  | SI | Recovery to Ward |
| Q101 | - |  |  | SI | Recovery to Ward |
| Q102 | - |  |  | SI | Recovery to Ward |
| Q103 | - |  |  | SI | Recovery to Ward |
| Q104 | - |  |  | SI | Recovery to Ward |
| Q105 | - |  |  | SI | Recovery to Ward |
| Q106 | - |  |  | SI | Recovery to Ward |
| Q107 | - |  |  | SI | Recovery to Ward |
| Q108 | - |  |  | SI | Recovery to Ward |
| Q109 | - |  |  | SI | Recovery to Ward |
| Q11 | - |  |  | SI | Relevant anticoagulants prescribed if applicable |
| Q110 | - |  |  | SI | Recovery to Ward |
| Q111 | - |  |  | SI | Recovery to Ward |
| Q112 | - |  |  | SI | Recovery to Ward |
| Q113 | - |  |  | SI | Recovery to Ward |
| Q114 | - |  |  | SI | Recovery to Ward |
| Q115 | - |  |  | SI | Recovery to Ward |
| Q116 | - |  |  | SI | Recovery to Ward |
| Q117 | - |  |  | SI | Recovery to Ward |
| Q118 | - |  |  | SI | Recovery to Ward |
| Q119 | - |  |  | SI | Recovery to Ward |
| Q12 | - |  |  | SI | Time of next dose confirmed	 |
| Q120 | - |  |  | SI | Recovery to Ward |
| Q121 | - |  |  | SI | Recovery to Ward |
| Q122 | - |  |  | SI | Recovery to Ward |
| Q123 | - |  |  | SI | Recovery to Ward |
| Q124 | - |  |  | SI | Recovery to Ward |
| Q125 | - |  |  | SI | Recovery to Ward |
| Q126 | - |  |  | SI | Recovery to Ward |
| Q127 | - |  |  | SI | Recovery to Ward |
| Q128 | - |  |  | SI | Recovery to Ward |
| Q129 | - |  |  | SI | Recovery to Ward |
| Q13 | - |  |  | SI | IV access, Sites and fluid management reviewed and... |
| Q130 | - |  |  | SI | Recovery to Ward |
| Q131 | - |  |  | SI | Recovery to Ward |
| Q132 | - |  |  | SI | Recovery to Ward |
| Q133 | - |  |  | SI | Recovery to Ward |
| Q134 | - |  |  | SI | Confirm patient identity with receiving practition... |
| Q135 | - |  |  | SI | Type of anaesthetic |
| Q136 | - |  |  | SI | Local anaesthetic wound infiltration |
| Q137 | - |  |  | SI | Level of consciousness |
| Q138 | - |  |  | SI | Airway maintained |
| Q139 | - |  |  | SI | Breathing |
| Q14 | - |  |  | SI | PCA IV site reviewed (if applicable) |
| Q140 | - |  |  | SI | O2 administered via mask / cannula |
| Q141 | - |  |  | SI | Ensure observations are within normal parameters |
| Q142 | - |  |  | SI | Relevant anticoagulants prescribed if applicable |
| Q143 | - |  |  | SI | Time of next dose confirmed |
| Q144 | - |  |  | SI | IV access, Sites and fluid management reviewed and... |
| Q145 | - |  |  | SI | PCA IV site reviewed (if applicable) |
| Q146 | - |  |  | SI | VIP score |
| Q147 | - |  |  | SI | Skin integrity / pressure areas checked |
| Q148 | - |  |  | SI | Dressing type recorded |
| Q149 | - |  |  | SI | Review of wound sites undertaken together |
| Q15 | - |  |  | SI | VIP score	 |
| Q150 | - |  |  | SI | Details of wound closure material used. |
| Q151 | - |  |  | SI | Drain sites & numbers reviewed together |
| Q152 | - |  |  | SI | Check insertion site & TR Band / Femstop observati... |
| Q153 | - |  |  | SI | Specific post-op care instructions discussed |
| Q154 | - |  |  | SI | Cardiac monitoring for approx 2 hours |
| Q155 | - |  |  | SI | Patient advised to stay flat for how long? |
| Q156 | - |  |  | SI | ECG recorded (cardiac patients) |
| Q157 | - |  |  | SI | Comments |
| Q158 | - |  |  | SI | Anaesthetist |
| Q159 | - |  |  | SI | Recovery nurse |
| Q15ObsDR | - |  |  | SI | VIP score	 DR |
| Q16 | - |  |  | SI | Skin integrity / pressure areas checked |
| Q160 | - |  |  | SI | Total analgesia given in recovery |
| Q161 | - |  |  | SI | Total anti-emetics given in recovery |
| Q162 | - |  |  | SI | Ward nurse |
| Q163 | - |  |  | SI | Total analgesia given in recovery |
| Q164 | - |  |  | SI | Total anti-emetics given in recovery |
| Q165 | - |  |  | SI | Ward nurse |
| Q17 | - |  |  | SI | Dressing type recorded	 |
| Q18 | - |  |  | SI | Review of wound sites undertaken together |
| Q19 | - |  |  | SI | Details of wound closure material used. |
| Q20 | - |  |  | SI | Drain sites & numbers reviewed together |
| Q21 | - |  |  | SI | Check insertion site & TR Band / Femstop observati... |
| Q22 | - |  |  | SI | Specific post-op care instructions discussed	 |
| Q23 | - |  |  | SI | Cardiac monitoring for approx 2 hours	 |
| Q24 | - |  |  | SI | Patient advised to stay flat for how long?	 |
| Q25 | - |  |  | SI | ECG recorded (cardiac patients) |
| Q26 | - |  |  | SI | Comments |
| Q27 | - |  |  | SI | Anaesthetist |
| Q28 | - |  |  | SI | Recovery nurse |
| Q29 | - |  |  | SI | Confirm patient identity with receiving practition... |
| Q30 | - |  |  | SI | Type of anaesthetic |
| Q31 | - |  |  | SI | Local anaesthetic wound infiltration |
| Q32 | - |  |  | SI | Level of consciousness |
| Q33 | - |  |  | SI | Airway maintained |
| Q34 | - |  |  | SI | Breathing |
| Q35 | - |  |  | SI | O2 administered via mask / cannula |
| Q36 | - |  |  | SI | Ensure observations are within normal parameters |
| Q37 | - |  |  | SI | Relevant anticoagulants prescribed if applicable |
| Q38 | - |  |  | SI | Time of next dose confirmed	 |
| Q39 | - |  |  | SI | IV access, sites and fluid management reviewed & f... |
| Q40 | - |  |  | SI | PCA IV site reviewed (if applicable) |
| Q41 | - |  |  | SI | VIP score	 |
| Q41ObsDR | - |  |  | SI | VIP score	 DR |
| Q42 | - |  |  | SI | Skin integrity / pressure areas checked |
| Q43 | - |  |  | SI | Dressing type recorded	 |
| Q44 | - |  |  | SI | Review of wound sites undertaken together |
| Q45 | - |  |  | SI | Details of wound closure material used. |
| Q46 | - |  |  | SI | Drain sites and numbers reviewed together |
| Q47 | - |  |  | SI | Check insertion site and TR Band / Femstop observa... |
| Q48 | - |  |  | SI | Specific post-op care instructions discussed |
| Q49 | - |  |  | SI | Cardiac monitoring for approx 2 hours |
| Q50 | - |  |  | SI | Patient advised to stay flat for how long? |
| Q51 | - |  |  | SI | ECG recorded (cardiac patients) |
| Q52 | - |  |  | SI | Comments 	 |
| Q53 | - |  |  | SI | Total analgesia given in recovery |
| Q54 | - |  |  | SI | Total anti-emetics given in recovery |
| Q55 | - |  |  | SI | Recovery nurse |
| Q56 | - |  |  | SI | Ward nurse |
| Q57 | - |  |  | SI | Date |
| Q58 | - |  |  | SI | Time |
| Q59 | - |  |  | SI | Date of handover |
| Q60 | - |  |  | SI | Time of handover |
| Q61 | - |  |  | SI | Theatre nurse |
| Q62 | - |  |  | SI | Theatre to Recovery |
| Q63 | - |  |  | SI | Theatre to Recovery |
| Q64 | - |  |  | SI | Theatre to Recovery |
| Q65 | - |  |  | SI | Theatre to Recovery |
| Q66 | - |  |  | SI | Theatre to Recovery |
| Q67 | - |  |  | SI | Theatre to Recovery |
| Q68 | - |  |  | SI | Theatre to Recovery |
| Q69 | - |  |  | SI | Theatre to Recovery |
| Q70 | - |  |  | SI | Theatre to Recovery |
| Q71 | - |  |  | SI | Theatre to Recovery |
| Q72 | - |  |  | SI | Theatre to Recovery |
| Q73 | - |  |  | SI | Theatre to Recovery |
| Q74 | - |  |  | SI | Theatre to Recovery |
| Q75 | - |  |  | SI | Theatre to Recovery |
| Q76 | - |  |  | SI | Theatre to Recovery |
| Q77 | - |  |  | SI | Theatre to Recovery |
| Q78 | - |  |  | SI | Theatre to Recovery |
| Q79 | - |  |  | SI | Theatre to Recovery |
| Q80 | - |  |  | SI | Theatre to Recovery |
| Q81 | - |  |  | SI | Theatre to Recovery |
| Q82 | - |  |  | SI | Theatre to Recovery |
| Q83 | - |  |  | SI | Theatre to Recovery |
| Q84 | - |  |  | SI | Theatre to Recovery |
| Q85 | - |  |  | SI | Theatre to Recovery |
| Q86 | - |  |  | SI | Theatre to Recovery |
| Q87 | - |  |  | SI | Theatre to Recovery |
| Q88 | - |  |  | SI | Theatre to Recovery |
| Q89 | - |  |  | SI | Theatre to Recovery |
| Q90 | - |  |  | SI | Theatre to Recovery |
| Q91 | - |  |  | SI | Theatre to Recovery |
| Q92 | - |  |  | SI | Theatre to Recovery |
| Q93 | - |  |  | SI | Recovery to Ward |
| Q94 | - |  |  | SI | Recovery to Ward |
| Q95 | - |  |  | SI | Recovery to Ward |
| Q96 | - |  |  | SI | Recovery to Ward |
| Q97 | - |  |  | SI | Recovery to Ward |
| Q98 | - |  |  | SI | Recovery to Ward |
| Q99 | - |  |  | SI | Recovery to Ward |
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
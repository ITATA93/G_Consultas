# SQLUser.ORC_LaryngoscopicView

**Schema:** SQLUser
**Columnas:** 224
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LARVIE_RowId | bigint | PK |  | NO | - |
| ChildQ82DR | - |  |  | SI | Child Reference: Oxygen saturation screening |
| LARVIE_Code | varchar |  |  | NO | Code |
| LARVIE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LARVIE_CreatedDate | date |  |  | SI | Created Date |
| LARVIE_CreatedTime | time |  |  | SI | Created Time |
| LARVIE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LARVIE_DateFrom | date |  |  | SI | Date From |
| LARVIE_DateTo | date |  |  | SI | Date To |
| LARVIE_Desc | varchar |  |  | NO | Description |
| LARVIE_Owner | varchar |  |  | SI | Owner |
| LARVIE_UpdatedDate | date |  |  | SI | Updated Date |
| LARVIE_UpdatedTime | time |  |  | SI | Updated Time |
| LARVIE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Examination date |
| Q02 | - |  |  | SI | Examination time |
| Q03 | - |  |  | SI | Examiner |
| Q04 | - |  |  | SI | Skin |
| Q05 | - |  |  | SI | Variance comment |
| Q06 | - |  |  | SI | Anterior fontanelle |
| Q07 | - |  |  | SI | Variance comment |
| Q08 | - |  |  | SI | Posterior fontanelle |
| Q09 | - |  |  | SI | Variance comment |
| Q10 | - |  |  | SI | Left hip |
| Q100 | - |  |  | SI | Bony structure |
| Q101 | - |  |  | SI | Variance comment |
| Q102 | - |  |  | SI | Skin integrity along the spine |
| Q103 | - |  |  | SI | Variance comment |
| Q104 | - |  |  | SI | Notes |
| Q105 | - |  |  | SI | Colour |
| Q106 | - |  |  | SI | Variance comment |
| Q107 | - |  |  | SI | Overall integrity |
| Q108 | - |  |  | SI | Variance comment |
| Q109 | - |  |  | SI | Notes |
| Q11 | - |  |  | SI | Variance comment |
| Q110 | - |  |  | SI | Tone |
| Q111 | - |  |  | SI | Variance comment |
| Q112 | - |  |  | SI | Behaviour |
| Q113 | - |  |  | SI | Variance comment |
| Q114 | - |  |  | SI | Activity |
| Q115 | - |  |  | SI | Variance comment |
| Q116 | - |  |  | SI | Posture |
| Q117 | - |  |  | SI | Variance comment |
| Q118 | - |  |  | SI | Notes |
| Q119 | - |  |  | SI | Moro |
| Q12 | - |  |  | SI | Right hip |
| Q120 | - |  |  | SI | Variance comment |
| Q121 | - |  |  | SI | Suck |
| Q122 | - |  |  | SI | Variance comment |
| Q123 | - |  |  | SI | Grasp |
| Q124 | - |  |  | SI | Variance comment |
| Q125 | - |  |  | SI | Notes |
| Q126 | - |  |  | SI | Barlow test |
| Q127 | - |  |  | SI | Variance comment |
| Q128 | - |  |  | SI | Ortolani test |
| Q129 | - |  |  | SI | Variance comment |
| Q13 | - |  |  | SI | Variance comment |
| Q130 | - |  |  | SI | Notes |
| Q131 | - |  |  | SI | Limbs |
| Q132 | - |  |  | SI | Hands |
| Q133 | - |  |  | SI | Variance comment |
| Q134 | - |  |  | SI | Feet |
| Q135 | - |  |  | SI | Variance comment |
| Q136 | - |  |  | SI | Digits |
| Q137 | - |  |  | SI | Variance comment |
| Q138 | - |  |  | SI | Notes |
| Q139 | - |  |  | SI | Feeding |
| Q14 | - |  |  | SI | Developmental Dysplasia of the Hip (DDH) risk fact... |
| Q140 | - |  |  | SI | Notes |
| Q141 | - |  |  | SI | Referral required |
| Q142 | - |  |  | SI | Notes |
| Q143 | - |  |  | SI | Normal Newborn Pulse Oximetry |
| Q144 | - |  |  | SI | • ≥ 95% in each limb |
| Q145 | - |  |  | SI | • ≤3% difference between limbs |
| Q146 | - |  |  | SI | Abnormal Newborn Pulse Oximetry |
| Q147 | - |  |  | SI | • <90% in either limb |
| Q148 | - |  |  | SI | • >3% difference between limbs |
| Q149 | - |  |  | SI | • 90 - 94% on 2 sequential measures 2 hours apart |
| Q15 | - |  |  | SI | Umbilicus |
| Q150 | - |  |  | SI | Date |
| Q151 | - |  |  | SI | Time |
| Q152 | - |  |  | SI | Variance comment |
| Q153 | - |  |  | SI | Notes |
| Q154 | - |  |  | SI | Notes |
| Q155 | - |  |  | SI | Head |
| Q156 | - |  |  | SI | Eyes |
| Q157 | - |  |  | SI | Chest |
| Q158 | - |  |  | SI | Lungs |
| Q159 | - |  |  | SI | Abdomen |
| Q16 | - |  |  | SI | Variance comment |
| Q160 | - |  |  | SI | Genitourinary |
| Q161 | - |  |  | SI | Spine |
| Q162 | - |  |  | SI | Skin |
| Q163 | - |  |  | SI | Central Nervous System |
| Q164 | - |  |  | SI | Reflex Group |
| Q165 | - |  |  | SI | Hips and Limbs |
| Q166 | - |  |  | SI | Proportions and Symmetry |
| Q167 | - |  |  | SI | Feeding Status |
| Q168 | - |  |  | SI | Referral and Recommendations |
| Q17 | - |  |  | SI | Left testes |
| Q18 | - |  |  | SI | Variance comment |
| Q19 | - |  |  | SI | Right testes |
| Q20 | - |  |  | SI | Variance comment |
| Q21 | - |  |  | SI | Vulva |
| Q22 | - |  |  | SI | Variance comment |
| Q23 | - |  |  | SI | Heart |
| Q24 | - |  |  | SI | Variance comment |
| Q25 | - |  |  | SI | Chest |
| Q26 | - |  |  | SI | Variance comment |
| Q27 | - |  |  | SI | Abdomen |
| Q28 | - |  |  | SI | Variance comment |
| Q29 | - |  |  | SI | Eyes |
| Q30 | - |  |  | SI | Variance comment |
| Q31 | - |  |  | SI | Ears |
| Q32 | - |  |  | SI | Variance comment |
| Q33 | - |  |  | SI | Mouth and palate |
| Q34 | - |  |  | SI | Variance comment |
| Q35 | - |  |  | SI | Spine |
| Q36 | - |  |  | SI | Variance comment |
| Q37 | - |  |  | SI | Anus |
| Q38 | - |  |  | SI | Variance comment |
| Q39 | - |  |  | SI | Left upper limb |
| Q40 | - |  |  | SI | Variance comment |
| Q41 | - |  |  | SI | Right upper limb |
| Q42 | - |  |  | SI | Variance comment |
| Q43 | - |  |  | SI | Left lower limb |
| Q44 | - |  |  | SI | Variance comment |
| Q45 | - |  |  | SI | Right lower limb |
| Q46 | - |  |  | SI | Variance comment	 |
| Q47 | - |  |  | SI | Left femoral pulse |
| Q48 | - |  |  | SI | Variance comment |
| Q49 | - |  |  | SI | Right femoral pulse |
| Q50 | - |  |  | SI | Variance comment |
| Q51 | - |  |  | SI | Comments |
| Q52 | - |  |  | SI | *NAD, Nil Abnormalities Detected |
| Q53 | - |  |  | SI | Pre ductal saturations (%) |
| Q54 | - |  |  | SI | Post ductal saturations  (%) |
| Q55 | - |  |  | SI | Saturation result |
| Q56 | - |  |  | SI | Red eye reflex |
| Q57 | - |  |  | SI | Variance comment |
| Q58 | - |  |  | SI | Age at time of discharge examination |
| Q59 | - |  |  | SI | Age factor |
| Q60 | - |  |  | SI | Birth weight (g) |
| Q61 | - |  |  | SI | Sutures |
| Q62 | - |  |  | SI | Variance comment |
| Q63 | - |  |  | SI | Face |
| Q64 | - |  |  | SI | Variance comment |
| Q65 | - |  |  | SI | Nose |
| Q66 | - |  |  | SI | Variance comment |
| Q67 | - |  |  | SI | Neck |
| Q68 | - |  |  | SI | Variance comment |
| Q69 | - |  |  | SI | Head symmetry |
| Q70 | - |  |  | SI | Variance comment |
| Q71 | - |  |  | SI | Head circumference (cm) |
| Q71ObsDR | - |  |  | SI | Head circumference (cm) DR |
| Q72 | - |  |  | SI | Notes |
| Q73 | - |  |  | SI | Opacities |
| Q74 | - |  |  | SI | Variance comment |
| Q75 | - |  |  | SI | Praecordium |
| Q76 | - |  |  | SI | Variance comment |
| Q77 | - |  |  | SI | Rhythm |
| Q78 | - |  |  | SI | Variance comment |
| Q79 | - |  |  | SI | Murmurs |
| Q80 | - |  |  | SI | Variance comment |
| Q81 | - |  |  | SI | Heart rate (bpm) |
| Q81ObsDR | - |  |  | SI | Heart rate (bpm) DR |
| Q83 | - |  |  | SI | Other result |
| Q84 | - |  |  | SI | Notes |
| Q85 | - |  |  | SI | Air entry |
| Q86 | - |  |  | SI | Variance comment |
| Q87 | - |  |  | SI | Respiratory effort |
| Q88 | - |  |  | SI | Variance comment |
| Q89 | - |  |  | SI | Sounds |
| Q90 | - |  |  | SI | Variance comment |
| Q91 | - |  |  | SI | Respiratory rate (br/min) |
| Q91ObsDR | - |  |  | SI | Respiratory rate (br/min) DR |
| Q92 | - |  |  | SI | Notes |
| Q93 | - |  |  | SI | Shape |
| Q94 | - |  |  | SI | Variance comment |
| Q95 | - |  |  | SI | Organomegaly |
| Q96 | - |  |  | SI | Variance comment |
| Q97 | - |  |  | SI | External genitalia |
| Q98 | - |  |  | SI | Variance comment |
| Q99 | - |  |  | SI | Notes |
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
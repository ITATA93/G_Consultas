# SQLUser.CT_LocalAuthority

**Schema:** SQLUser
**Columnas:** 216
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOCAUTH_RowId | bigint | PK |  | NO | - |
| LOCAUTH_Code | varchar |  |  | NO | Code |
| LOCAUTH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOCAUTH_CreatedDate | date |  |  | SI | Created Date |
| LOCAUTH_CreatedTime | time |  |  | SI | Created Time |
| LOCAUTH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOCAUTH_Desc | varchar |  |  | NO | Description |
| LOCAUTH_Owner | varchar |  |  | SI | Owner |
| LOCAUTH_UpdatedDate | date |  |  | SI | Updated Date |
| LOCAUTH_UpdatedTime | time |  |  | SI | Updated Time |
| LOCAUTH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Right Eye |
| Q02 | - |  |  | SI | Left Eye |
| Q03 | - |  |  | SI | Adnexa & Lids |
| Q04 | - |  |  | SI | Lacrimal gland |
| Q05 | - |  |  | SI | Lacrimal gland RE 2 |
| Q06 | - |  |  | SI | Lacrimal drainage |
| Q07 | - |  |  | SI | Lacrimal Drainage 2 |
| Q08 | - |  |  | SI | Lymphnodes |
| Q09 | - |  |  | SI | Lymphnodes 2 |
| Q10 | - |  |  | SI | Lids |
| Q100 | - |  |  | SI | Cortical |
| Q101 | - |  |  | SI | Cortical |
| Q102 | - |  |  | SI | Post subscapular cataract |
| Q103 | - |  |  | SI | Post subscapular cataract |
| Q104 | - |  |  | SI | Nucleus |
| Q105 | - |  |  | SI | Nucleus |
| Q106 | - |  |  | SI | Brown cataract |
| Q107 | - |  |  | SI | Brown cataract |
| Q108 | - |  |  | SI | Lens type 2 |
| Q109 | - |  |  | SI | Good capsular support |
| Q11 | - |  |  | SI | Adnexa |
| Q110 | - |  |  | SI | Lens Type - Psuedophakia |
| Q111 | - |  |  | SI | IOL |
| Q112 | - |  |  | SI | Good Capsular support |
| Q113 | - |  |  | SI | IOL |
| Q114 | - |  |  | SI | Lens Type - Phakic |
| Q115 | - |  |  | SI | IOL |
| Q116 | - |  |  | SI | IOL |
| Q117 | - |  |  | SI | IOL |
| Q118 | - |  |  | SI | Lens movement |
| Q119 | - |  |  | SI | Lens movement 2 |
| Q11ObsDR | - |  |  | SI | Adnexa DR |
| Q12 | - |  |  | SI | Adnexa L |
| Q120 | - |  |  | SI | Pseudo exfoliation |
| Q121 | - |  |  | SI | Scleritis |
| Q122 | - |  |  | SI | Scleritis 2 |
| Q123 | - |  |  | SI | Other abnormalities |
| Q124 | - |  |  | SI | Other abnormalities 2 |
| Q125 | - |  |  | SI | Notes |
| Q126 | - |  |  | SI | Right Eye |
| Q127 | - |  |  | SI | Left Eye |
| Q128 | - |  |  | SI | Scleritis |
| Q129 | - |  |  | SI | Scleritis 2 |
| Q12ObsDR | - |  |  | SI | Adnexa L DR |
| Q13 | - |  |  | SI | Notes |
| Q130 | - |  |  | SI | Clarity |
| Q131 | - |  |  | SI | Infiltrates |
| Q132 | - |  |  | SI | Lens type |
| Q133 | - |  |  | SI | Clarity |
| Q134 | - |  |  | SI | Cortical |
| Q135 | - |  |  | SI | Post subscapular cataract |
| Q136 | - |  |  | SI | Nucleus |
| Q137 | - |  |  | SI | Brown cataract |
| Q138 | - |  |  | SI | Good capsular support |
| Q139 | - |  |  | SI | IOL |
| Q14 | - |  |  | SI | Conjunctiva |
| Q140 | - |  |  | SI | IOL |
| Q141 | - |  |  | SI | IOL |
| Q142 | - |  |  | SI | Lenticule location |
| Q143 | - |  |  | SI | Lacrimal gland |
| Q144 | - |  |  | SI | Lids |
| Q145 | - |  |  | SI | Adnexa |
| Q146 | - |  |  | SI | Conjunctiva |
| Q147 | - |  |  | SI | Pupils |
| Q148 | - |  |  | SI | Date |
| Q149 | - |  |  | SI | Time |
| Q15 | - |  |  | SI | Image Annotation |
| Q150 | - |  |  | SI | Image annotation |
| Q151 | - |  |  | SI | Contact lens |
| Q152 | - |  |  | SI | Cells |
| Q153 | - |  |  | SI | Cells 2 |
| Q16 | - |  |  | SI | Left Eye |
| Q17 | - |  |  | SI | Conjunctiva |
| Q17ObsDR | - |  |  | SI | Conjunctiva DR |
| Q18 | - |  |  | SI | Conjunctiva L |
| Q18ObsDR | - |  |  | SI | Conjunctiva L DR |
| Q19 | - |  |  | SI | Bulbar |
| Q20 | - |  |  | SI | Bulbar 2 |
| Q200 | - |  |  | SI | Lids RE 2 |
| Q201 | - |  |  | SI | Right Eye |
| Q202 | - |  |  | SI | Dye Type |
| Q203 | - |  |  | SI | Dye Type |
| Q204 | - |  |  | SI | Dye Type 2 |
| Q21 | - |  |  | SI | Palpebral |
| Q22 | - |  |  | SI | Palpebral 2 |
| Q23 | - |  |  | SI | Notes |
| Q24 | - |  |  | SI | Gonioscopy |
| Q26 | - |  |  | SI | Image Annotation |
| Q300 | - |  |  | SI | Pseudo exfoliation 2 |
| Q301 | - |  |  | SI | Notes |
| Q302 | - |  |  | SI | Image annotation |
| Q33 | - |  |  | SI | Notes |
| Q34 | - |  |  | SI | Right Eye |
| Q35 | - |  |  | SI | Left Eye |
| Q36 | - |  |  | SI | Pupils |
| Q37 | - |  |  | SI | Pupil R |
| Q37ObsDR | - |  |  | SI | Pupil R DR |
| Q38 | - |  |  | SI | pupil L |
| Q38ObsDR | - |  |  | SI | pupil L DR |
| Q39 | - |  |  | SI | Notes |
| Q40 | - |  |  | SI | Cornea |
| Q41 | - |  |  | SI | Right Eye |
| Q42 | - |  |  | SI | Left Eye |
| Q43 | - |  |  | SI | Cornea R |
| Q43ObsDR | - |  |  | SI | Cornea R DR |
| Q44 | - |  |  | SI | Cornea L |
| Q44ObsDR | - |  |  | SI | Cornea L DR |
| Q45 | - |  |  | SI | Keratoconus |
| Q46 | - |  |  | SI | Keratoconus 2 |
| Q47 | - |  |  | SI | Graft type |
| Q48 | - |  |  | SI | Graft type 2 |
| Q49 | - |  |  | SI | Epithelium |
| Q50 | - |  |  | SI | Epithelium 2 |
| Q51 | - |  |  | SI | Stroma |
| Q52 | - |  |  | SI | Stroma 2 |
| Q53 | - |  |  | SI | Clarity |
| Q54 | - |  |  | SI | Clarity |
| Q55 | - |  |  | SI | Infiltrates |
| Q56 | - |  |  | SI | Infiltrates |
| Q57 | - |  |  | SI | Sutures |
| Q58 | - |  |  | SI | Infiltrate 2 |
| Q59 | - |  |  | SI | Lenticule location |
| Q60 | - |  |  | SI | Lenticule location |
| Q61 | - |  |  | SI | Endothelium |
| Q62 | - |  |  | SI | Endothelium 2 |
| Q63 | - |  |  | SI | Contact lens |
| Q63ObsDR | - |  |  | SI | Contact lens DR |
| Q64 | - |  |  | SI | Contact Lens L |
| Q64ObsDR | - |  |  | SI | Contact Lens L DR |
| Q65 | - |  |  | SI | Dry eye evaluation |
| Q66 | - |  |  | SI | Dry eye evaluation 2 |
| Q67 | - |  |  | SI | Tear film |
| Q68 | - |  |  | SI | Tear film 2 |
| Q69 | - |  |  | SI | Notes |
| Q70 | - |  |  | SI | RAPD - Grading |
| Q71 | - |  |  | SI | RAPD - Grading 2 |
| Q72 | - |  |  | SI | Iris |
| Q72ObsDR | - |  |  | SI | Iris DR |
| Q73 | - |  |  | SI | Iris 2 |
| Q73ObsDR | - |  |  | SI | Iris 2 DR |
| Q74 | - |  |  | SI | Iris Pathology |
| Q75 | - |  |  | SI | Iris Pathology 2 |
| Q76 | - |  |  | SI | Anterior Chamber |
| Q77 | - |  |  | SI | Right Eye |
| Q78 | - |  |  | SI | Left Eye |
| Q79 | - |  |  | SI | Depth |
| Q80 | - |  |  | SI | Depth 2 |
| Q81 | - |  |  | SI | Cells |
| Q82 | - |  |  | SI | Cells 2 |
| Q83 | - |  |  | SI | Type |
| Q84 | - |  |  | SI | Type 2 |
| Q85 | - |  |  | SI | Air bubbles |
| Q86 | - |  |  | SI | Air bubbles 2 |
| Q87 | - |  |  | SI | Flare |
| Q88 | - |  |  | SI | Flar 2 |
| Q89 | - |  |  | SI | Notes |
| Q91 | - |  |  | SI | Infiltrates |
| Q92 | - |  |  | SI | Sutures |
| Q93 | - |  |  | SI | Lenticule location |
| Q94 | - |  |  | SI | Lens |
| Q95 | - |  |  | SI | Right Eye |
| Q96 | - |  |  | SI | Left Eye |
| Q97 | - |  |  | SI | Lens type |
| Q98 | - |  |  | SI | Clarity |
| Q99 | - |  |  | SI | Clarity |
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
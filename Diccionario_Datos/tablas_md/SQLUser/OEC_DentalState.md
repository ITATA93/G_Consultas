# SQLUser.OEC_DentalState

**Schema:** SQLUser
**Columnas:** 313
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DENST_RowId | bigint | PK |  | NO | - |
| DENST_Code | varchar |  |  | NO | Code |
| DENST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DENST_Color | varchar |  |  | SI | Color |
| DENST_Colos | varchar |  |  | SI | Colos |
| DENST_CreatedDate | date |  |  | SI | Created Date |
| DENST_CreatedTime | time |  |  | SI | Created Time |
| DENST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DENST_Crown | varchar |  |  | SI | Crown |
| DENST_DateFrom | date |  |  | SI | DateFrom |
| DENST_DateTo | date |  |  | SI | DateTo |
| DENST_Desc | varchar |  |  | NO | Description |
| DENST_Face1 | varchar |  |  | SI | Face1 |
| DENST_Face2 | varchar |  |  | SI | Face2 |
| DENST_Face3 | varchar |  |  | SI | Face3 |
| DENST_Face4 | varchar |  |  | SI | Face4 |
| DENST_Face5 | varchar |  |  | SI | Face5 |
| DENST_Image | varchar |  |  | SI | Image |
| DENST_Owner | varchar |  |  | SI | Owner |
| DENST_Root | varchar |  |  | SI | Root |
| DENST_RootImage | varchar |  |  | SI | Root Image |
| DENST_ToothArea_DR | bigint |  | FK | SI | Des Ref ToothArea |
| DENST_UpdatedDate | date |  |  | SI | Updated Date |
| DENST_UpdatedTime | time |  |  | SI | Updated Time |
| DENST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DENST_WholeTooth | varchar |  |  | SI | WholeTooth |
| Q01 | - |  |  | SI | Right Eye |
| Q02 | - |  |  | SI | Left Eye |
| Q03 | - |  |  | SI | Adnexa & Lids |
| Q04 | - |  |  | SI | Lacrimal gland RE |
| Q05 | - |  |  | SI | Lacrimal gland RE 2 |
| Q06 | - |  |  | SI | Lachrymal Drainage |
| Q07 | - |  |  | SI | Lachrymal Drainage 2 |
| Q08 | - |  |  | SI | Lymphnodes |
| Q09 | - |  |  | SI | Lymphnodes 2 |
| Q10 | - |  |  | SI | Lids RE |
| Q100 | - |  |  | SI | Cortical |
| Q101 | - |  |  | SI | Cortical L |
| Q102 | - |  |  | SI | Post subscapular cataract |
| Q103 | - |  |  | SI | Post subscapular cataract 2 |
| Q104 | - |  |  | SI | Nucleus |
| Q105 | - |  |  | SI | Nucleus 2 |
| Q106 | - |  |  | SI | Brown cataract |
| Q107 | - |  |  | SI | Brown cataract 2 |
| Q108 | - |  |  | SI | Lens type 2_old |
| Q109 | - |  |  | SI | Good capsular support |
| Q11 | - |  |  | SI | Adnexa R |
| Q110 | - |  |  | SI | Lens Type - Psuedophakia |
| Q111 | - |  |  | SI | IOL |
| Q112 | - |  |  | SI | Capsular support 2 |
| Q113 | - |  |  | SI | IOL 2 |
| Q114 | - |  |  | SI | Lens Type - Phakic |
| Q115 | - |  |  | SI | IOL |
| Q116 | - |  |  | SI | IOL - Phasic 2 |
| Q117 | - |  |  | SI | IOL |
| Q118 | - |  |  | SI | Lens movement |
| Q119 | - |  |  | SI | Lens movement 2 |
| Q11ObsDR | - |  |  | SI | Adnexa R DR |
| Q12 | - |  |  | SI | Adnexa L |
| Q120 | - |  |  | SI | Pseudo exfoliation |
| Q121 | - |  |  | SI | Pseudo exfoliation 2 |
| Q122 | - |  |  | SI | Notes |
| Q123 | - |  |  | SI | Image Annotation |
| Q124 | - |  |  | SI | Retina |
| Q125 | - |  |  | SI | Right Eye |
| Q126 | - |  |  | SI | Left Eye |
| Q127 | - |  |  | SI | Cupping |
| Q128 | - |  |  | SI | Cupping 2 |
| Q129 | - |  |  | SI | Shape |
| Q12ObsDR | - |  |  | SI | Adnexa L DR |
| Q13 | - |  |  | SI | Notes |
| Q130 | - |  |  | SI | Shape 2 |
| Q131 | - |  |  | SI | Size |
| Q132 | - |  |  | SI | Size 2 |
| Q133 | - |  |  | SI | Colour |
| Q134 | - |  |  | SI | Colour 2 |
| Q135 | - |  |  | SI | Other Abnormalities |
| Q136 | - |  |  | SI | Other Abnormalities 2 |
| Q137 | - |  |  | SI | Retina |
| Q138 | - |  |  | SI | Retina 2 |
| Q139 | - |  |  | SI | Notes |
| Q14 | - |  |  | SI | Conjuctiva |
| Q140 | - |  |  | SI | Abnormal movements |
| Q141 | - |  |  | SI | Notes |
| Q142 | - |  |  | SI | Conjuctiva appearance |
| Q143 | - |  |  | SI | Conjuctiva appearance 2 |
| Q144 | - |  |  | SI | Bleb Surgery |
| Q145 | - |  |  | SI | Site |
| Q146 | - |  |  | SI | Site 2 |
| Q147 | - |  |  | SI | Height |
| Q148 | - |  |  | SI | Height 2 |
| Q149 | - |  |  | SI | Extension |
| Q15 | - |  |  | SI | Right Eye |
| Q150 | - |  |  | SI | Extension 2 |
| Q151 | - |  |  | SI | Appearance |
| Q152 | - |  |  | SI | Appearance 2 |
| Q153 | - |  |  | SI | Tube surgery 2 |
| Q154 | - |  |  | SI | Position |
| Q155 | - |  |  | SI | Position 2 |
| Q156 | - |  |  | SI | Site |
| Q157 | - |  |  | SI | Site 2 |
| Q158 | - |  |  | SI | Conjunctiva |
| Q159 | - |  |  | SI | Conjunctiva 2 |
| Q16 | - |  |  | SI | Left Eye |
| Q160 | - |  |  | SI | Lacrimal gland |
| Q161 | - |  |  | SI | Lids |
| Q162 | - |  |  | SI | Lids 2 |
| Q163 | - |  |  | SI | Anomalies |
| Q164 | - |  |  | SI | Appearance |
| Q165 | - |  |  | SI | Appearance 2 |
| Q166 | - |  |  | SI | Conjuctiva |
| Q167 | - |  |  | SI | Anomalies 2 |
| Q168 | - |  |  | SI | Right Eye |
| Q169 | - |  |  | SI | Left Eye |
| Q17 | - |  |  | SI | Conjuctiva R |
| Q170 | - |  |  | SI | Notes |
| Q171 | - |  |  | SI | Dye type |
| Q172 | - |  |  | SI | Dye type 2 |
| Q173 | - |  |  | SI | Bleb site |
| Q174 | - |  |  | SI | Bleb site |
| Q175 | - |  |  | SI | Bleb height |
| Q176 | - |  |  | SI | Bleb height |
| Q177 | - |  |  | SI | Bleb extension |
| Q178 | - |  |  | SI | Bleb extension |
| Q179 | - |  |  | SI | Bleb appearance |
| Q17ObsDR | - |  |  | SI | Conjuctiva R DR |
| Q18 | - |  |  | SI | Conjuctiva L |
| Q180 | - |  |  | SI | Bleb appearance |
| Q181 | - |  |  | SI | Tube surgery |
| Q182 | - |  |  | SI | Tube 2 |
| Q183 | - |  |  | SI | Tube position |
| Q184 | - |  |  | SI | Tube position |
| Q185 | - |  |  | SI | Tube site |
| Q186 | - |  |  | SI | Tube site |
| Q187 | - |  |  | SI | Bleb Surgery 2 |
| Q188 | - |  |  | SI | Surgery done |
| Q189 | - |  |  | SI | Surgery done 2 |
| Q18ObsDR | - |  |  | SI | Conjuctiva L DR |
| Q19 | - |  |  | SI | Bulbar |
| Q190 | - |  |  | SI | Graft type |
| Q191 | - |  |  | SI | Clarity |
| Q192 | - |  |  | SI | Clarity |
| Q193 | - |  |  | SI | Infiltrates |
| Q194 | - |  |  | SI | Shape |
| Q195 | - |  |  | SI | shape 2 |
| Q196 | - |  |  | SI | Anisocoria |
| Q197 | - |  |  | SI | Anisocoria 2 |
| Q198 | - |  |  | SI | Pupil |
| Q199 | - |  |  | SI | PCO |
| Q20 | - |  |  | SI | Bulbar 2 |
| Q200 | - |  |  | SI | PCO 2 |
| Q201 | - |  |  | SI | PCO grading |
| Q202 | - |  |  | SI | PCO grading 2 |
| Q203 | - |  |  | SI | Lens type |
| Q204 | - |  |  | SI | Lens type |
| Q205 | - |  |  | SI | Clarity |
| Q206 | - |  |  | SI | Cortical |
| Q207 | - |  |  | SI | Post subscapular cataract |
| Q208 | - |  |  | SI | Nucleus |
| Q209 | - |  |  | SI | Brown cataract |
| Q21 | - |  |  | SI | Palpebral |
| Q210 | - |  |  | SI | Good capsular support |
| Q211 | - |  |  | SI | IOL |
| Q212 | - |  |  | SI | PCO |
| Q213 | - |  |  | SI | PCO grading |
| Q214 | - |  |  | SI | IOL |
| Q215 | - |  |  | SI | Normal movements |
| Q216 | - |  |  | SI | Cornea |
| Q217 | - |  |  | SI | Gonioscopy Outcome |
| Q218 | - |  |  | SI | Gonioscopy Outcome 2 |
| Q219 | - |  |  | SI | Image Annotation |
| Q22 | - |  |  | SI | Palpebral 2 |
| Q220 | - |  |  | SI | Bleb Surgery |
| Q221 | - |  |  | SI | Bleb Surgery |
| Q222 | - |  |  | SI | Surgery done |
| Q223 | - |  |  | SI | Tube surgery |
| Q224 | - |  |  | SI | Image Annotation |
| Q225 | - |  |  | SI | Cupping 2 |
| Q226 | - |  |  | SI | retina size 2 |
| Q227 | - |  |  | SI | Colour |
| Q228 | - |  |  | SI | retina other abnormalities 2 |
| Q229 | - |  |  | SI | Anterior chamber |
| Q229ObsDR | - |  |  | SI | Anterior chamber DR |
| Q23 | - |  |  | SI | Notes |
| Q230 | - |  |  | SI | Anterior chamber 2 |
| Q230ObsDR | - |  |  | SI | Anterior chamber 2 DR |
| Q231 | - |  |  | SI | Abnormal eyes movements |
| Q24 | - |  |  | SI | Sclera |
| Q25 | - |  |  | SI | Right Eye |
| Q26 | - |  |  | SI | Left Eye |
| Q27 | - |  |  | SI | Sclera R |
| Q27ObsDR | - |  |  | SI | Sclera R DR |
| Q28 | - |  |  | SI | Sclera L |
| Q28ObsDR | - |  |  | SI | Sclera L DR |
| Q29 | - |  |  | SI | Scleritis |
| Q30 | - |  |  | SI | Scleritis 2 |
| Q31 | - |  |  | SI | Other abnormalities |
| Q32 | - |  |  | SI | Other abnormalities 2 |
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
| Q60 | - |  |  | SI | Lenticule location 2 |
| Q61 | - |  |  | SI | Endothelium |
| Q62 | - |  |  | SI | Endothelium 2 |
| Q63 | - |  |  | SI | Contact Lens |
| Q63ObsDR | - |  |  | SI | Contact Lens DR |
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
| Q74 | - |  |  | SI | Pathology |
| Q75 | - |  |  | SI | Pathology 2 |
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
| Q90 | - |  |  | SI | Clarity |
| Q91 | - |  |  | SI | Infiltrates |
| Q92 | - |  |  | SI | Sutures |
| Q93 | - |  |  | SI | Lenticule location |
| Q94 | - |  |  | SI | Lens |
| Q95 | - |  |  | SI | Right Eye |
| Q96 | - |  |  | SI | Left Eye |
| Q97 | - |  |  | SI | Lens type_OLD |
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
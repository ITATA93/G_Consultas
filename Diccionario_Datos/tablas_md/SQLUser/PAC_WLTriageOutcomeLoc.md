# SQLUser.PAC_WLTriageOutcomeLoc

**Schema:** SQLUser
**Columnas:** 295
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | bigint | PK |  | NO | PAC_WLTriageOutcome Parent Reference |
| LOC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLoc |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_CreatedDate | date |  |  | SI | Created Date |
| LOC_CreatedTime | time |  |  | SI | Created Time |
| LOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOC_RowId | varchar |  |  | NO | - |
| LOC_UpdatedDate | date |  |  | SI | Updated Date |
| LOC_UpdatedTime | time |  |  | SI | Updated Time |
| LOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Intensive Care Unit (ICU) admission |
| Q04 | - |  |  | SI | Age in years |
| Q05 | - |  |  | SI | Length of stay before ICU admission, days |
| Q06 | - |  |  | SI | Intra-hospital location before ICU admission |
| Q07 | - |  |  | SI | Comorbidities |
| Q08 | - |  |  | SI | Use of major therapeutic options before ICU admiss... |
| Q09 | - |  |  | SI | ICU admission: Planned or Unplanned |
| Q10 | - |  |  | SI | Cardiovascular |
| Q100 | - |  |  | SI | Probability of Death 54% |
| Q101 | - |  |  | SI | 70 |
| Q102 | - |  |  | SI | Probability of Death 57% |
| Q103 | - |  |  | SI | 71 |
| Q104 | - |  |  | SI | Probability of Death 58% |
| Q105 | - |  |  | SI | 72 |
| Q106 | - |  |  | SI | Probability of Death 60% |
| Q107 | - |  |  | SI | 73 |
| Q108 | - |  |  | SI | Probability of Death 62% |
| Q109 | - |  |  | SI | 74 |
| Q11 | - |  |  | SI | Hepatic |
| Q110 | - |  |  | SI | Probability of Death 64% |
| Q111 | - |  |  | SI | 75 |
| Q112 | - |  |  | SI | Probability of Death 66% |
| Q113 | - |  |  | SI | 76 |
| Q114 | - |  |  | SI | Probability of Death 67% |
| Q115 | - |  |  | SI | 77 |
| Q116 | - |  |  | SI | Probability of Death 69% |
| Q117 | - |  |  | SI | 78 |
| Q118 | - |  |  | SI | Probability of Death 71% |
| Q119 | - |  |  | SI | 79 |
| Q12 | - |  |  | SI | Digestive |
| Q120 | - |  |  | SI | Probability of Death 72% |
| Q121 | - |  |  | SI | 80 |
| Q122 | - |  |  | SI | Probability of Death 74% |
| Q123 | - |  |  | SI | 81 |
| Q124 | - |  |  | SI | Probability of Death 75% |
| Q125 | - |  |  | SI | 82 |
| Q126 | - |  |  | SI | Probability of Death 76% |
| Q127 | - |  |  | SI | 83 |
| Q128 | - |  |  | SI | Probability of Death 78% |
| Q129 | - |  |  | SI | 84 |
| Q13 | - |  |  | SI | Neurologic |
| Q130 | - |  |  | SI | Probability of Death 79% |
| Q131 | - |  |  | SI | 85 |
| Q132 | - |  |  | SI | Probability of Death 80% |
| Q133 | - |  |  | SI | 86 |
| Q134 | - |  |  | SI | Probability of Death 81% |
| Q135 | - |  |  | SI | 87 |
| Q136 | - |  |  | SI | Probability of Death 82% |
| Q137 | - |  |  | SI | 88 |
| Q138 | - |  |  | SI | Probability of Death 83% |
| Q139 | - |  |  | SI | 89 |
| Q14 | - |  |  | SI | Surgical status at ICU admission |
| Q140 | - |  |  | SI | Probability of Death 84% |
| Q141 | - |  |  | SI | 90 |
| Q142 | - |  |  | SI | Probability of Death 85% |
| Q143 | - |  |  | SI | 91-92 |
| Q144 | - |  |  | SI | Probability of Death 86% |
| Q145 | - |  |  | SI | 93 |
| Q146 | - |  |  | SI | Probability of Death 87% |
| Q147 | - |  |  | SI | 94 |
| Q148 | - |  |  | SI | Probability of Death 88% |
| Q149 | - |  |  | SI | 95-96 |
| Q15 | - |  |  | SI | Anatomical site of surgery |
| Q150 | - |  |  | SI | Probability of Death 89% |
| Q151 | - |  |  | SI | 97-98 |
| Q152 | - |  |  | SI | Probability of Death 90% |
| Q153 | - |  |  | SI | 99-100 |
| Q154 | - |  |  | SI | Probability of Death 91% |
| Q155 | - |  |  | SI | 101-102 |
| Q156 | - |  |  | SI | Probability of Death 92% |
| Q157 | - |  |  | SI | 103-105 |
| Q158 | - |  |  | SI | Probability of Death 93% |
| Q159 | - |  |  | SI | 106-108 |
| Q16 | - |  |  | SI | Acute infection at ICU admission |
| Q160 | - |  |  | SI | Probability of Death 94% |
| Q161 | - |  |  | SI | 109-112 |
| Q162 | - |  |  | SI | Probability of Death 95% |
| Q163 | - |  |  | SI | 113-117 |
| Q164 | - |  |  | SI | Probability of Death 96% |
| Q165 | - |  |  | SI | 118-123 |
| Q166 | - |  |  | SI | Probability of Death 97% |
| Q167 | - |  |  | SI | 124-134 |
| Q168 | - |  |  | SI | Probability of Death 98% |
| Q169 | - |  |  | SI | 135-159 |
| Q17 | - |  |  | SI | Estimated Glasgow Coma Score (lowest), points |
| Q170 | - |  |  | SI | Probability of Death 99% |
| Q171 | - |  |  | SI | >159 |
| Q172 | - |  |  | SI | Probability of Death 100% |
| Q173 | - |  |  | SI | The Simplified Acute Physiology Score III (SAPS 3)... |
| Q174 | - |  |  | SI | 16-21: Probability of Death 0% |
| Q175 | - |  |  | SI | 22-28: Probability of Death 1% |
| Q176 | - |  |  | SI | 29-32: Probability of Death 2% |
| Q177 | - |  |  | SI | 33-34: Probability of Death 3% |
| Q178 | - |  |  | SI | 35-36: Probability of Death 4% |
| Q179 | - |  |  | SI | 37-38: Probability of Death 5% |
| Q18 | - |  |  | SI | Total bilirubin (highest), mg/dL (µmol/L) |
| Q180 | - |  |  | SI | 39-40: Probability of Death 6% |
| Q181 | - |  |  | SI | 41: Probability of Death 7% |
| Q182 | - |  |  | SI | 42: Probability of Death 8% |
| Q183 | - |  |  | SI | 43: Probability of Death 9% |
| Q184 | - |  |  | SI | 44: Probability of Death 10% |
| Q185 | - |  |  | SI | 45: Probability of Death 11% |
| Q186 | - |  |  | SI | 46: Probability of Death 12% |
| Q187 | - |  |  | SI | 47: Probability of Death 13% |
| Q188 | - |  |  | SI | 48: Probability of Death 15% |
| Q189 | - |  |  | SI | 49: Probability of Death 16% |
| Q19 | - |  |  | SI | Body temperature (highest), degrees celsius |
| Q190 | - |  |  | SI | 50: Probability of Death 17% |
| Q191 | - |  |  | SI | 51: Probability of Death 19% |
| Q192 | - |  |  | SI | 52: Probability of Death 20% |
| Q193 | - |  |  | SI | 53: Probability of Death 22% |
| Q194 | - |  |  | SI | 54: Probability of Death 24% |
| Q195 | - |  |  | SI | 55: Probability of Death 26% |
| Q196 | - |  |  | SI | 56: Probability of Death 28% |
| Q197 | - |  |  | SI | 57: Probability of Death 30% |
| Q198 | - |  |  | SI | 58: Probability of Death 32% |
| Q199 | - |  |  | SI | 59: Probability of Death 34% |
| Q20 | - |  |  | SI | Creatinine (highest), mg/dL (µmol/L) |
| Q200 | - |  |  | SI | 60: Probability of Death 36% |
| Q201 | - |  |  | SI | 61: Probability of Death 38% |
| Q202 | - |  |  | SI | 62: Probability of Death 40% |
| Q203 | - |  |  | SI | 63: Probability of Death 42% |
| Q204 | - |  |  | SI | 64: Probability of Death 44% |
| Q205 | - |  |  | SI | 65: Probability of Death 46% |
| Q206 | - |  |  | SI | 66: Probability of Death 48% |
| Q207 | - |  |  | SI | 67: Probability of Death 50% |
| Q208 | - |  |  | SI | 68: Probability of Death 52% |
| Q209 | - |  |  | SI | 69: Probability of Death 54% |
| Q21 | - |  |  | SI | Heart rate (highest), beats / minute |
| Q210 | - |  |  | SI | 70: Probability of Death 57% |
| Q211 | - |  |  | SI | 71: Probability of Death 58% |
| Q212 | - |  |  | SI | 72: Probability of Death 60% |
| Q213 | - |  |  | SI | 73: Probability of Death 62% |
| Q214 | - |  |  | SI | 74: Probability of Death 64% |
| Q215 | - |  |  | SI | 75: Probability of Death 66% |
| Q216 | - |  |  | SI | 76: Probability of Death 67% |
| Q217 | - |  |  | SI | 77: Probability of Death 69% |
| Q218 | - |  |  | SI | 78: Probability of Death 71% |
| Q219 | - |  |  | SI | 79: Probability of Death 72% |
| Q22 | - |  |  | SI | Leukocytes (lowest), G/L |
| Q220 | - |  |  | SI | 80: Probability of Death 74% |
| Q221 | - |  |  | SI | 81: Probability of Death 75% |
| Q222 | - |  |  | SI | 82: Probability of Death 76% |
| Q223 | - |  |  | SI | 83: Probability of Death 78% |
| Q224 | - |  |  | SI | 84: Probability of Death 79% |
| Q225 | - |  |  | SI | 85: Probability of Death 80% |
| Q226 | - |  |  | SI | 86: Probability of Death 81% |
| Q227 | - |  |  | SI | 87: Probability of Death 82% |
| Q228 | - |  |  | SI | 88: Probability of Death 83% |
| Q229 | - |  |  | SI | 89: Probability of Death 84% |
| Q23 | - |  |  | SI | Hydrogen ion concentration (lowest), pH |
| Q230 | - |  |  | SI | 90: Probability of Death 85% |
| Q231 | - |  |  | SI | 91-92: Probability of Death 86% |
| Q232 | - |  |  | SI | 93: Probability of Death 87% |
| Q233 | - |  |  | SI | 94: Probability of Death 88% |
| Q234 | - |  |  | SI | 95-96: Probability of Death 89% |
| Q235 | - |  |  | SI | 97-98: Probability of Death 90% |
| Q236 | - |  |  | SI | 99-100: Probability of Death 91% |
| Q237 | - |  |  | SI | 101-102: Probability of Death 92% |
| Q238 | - |  |  | SI | 103-105: Probability of Death 93% |
| Q239 | - |  |  | SI | 106-108: Probability of Death 94% |
| Q24 | - |  |  | SI | Platelets (lowest), G/L |
| Q240 | - |  |  | SI | 109-112: Probability of Death 95% |
| Q241 | - |  |  | SI | 113-117: Probability of Death 96% |
| Q242 | - |  |  | SI | 118:-123: Probability of Death 97% |
| Q243 | - |  |  | SI | 124-134: Probability of Death 98% |
| Q244 | - |  |  | SI | 135-159:  Probability of Death 99% |
| Q245 | - |  |  | SI | >159: Probability of Death 100% |
| Q25 | - |  |  | SI | Systolic blood pressure (lowest), mmHg |
| Q26 | - |  |  | SI | Oxygenation |
| Q27 | - |  |  | SI | Score |
| Q28 | - |  |  | SI | Classification |
| Q29 | - |  |  | SI | 16-21 |
| Q30 | - |  |  | SI | Probability of Death 0% |
| Q31 | - |  |  | SI | 22-28 |
| Q32 | - |  |  | SI | Probability of Death 1% |
| Q33 | - |  |  | SI | 29-32 |
| Q34 | - |  |  | SI | Probability of Death 2% |
| Q35 | - |  |  | SI | 33-34 |
| Q36 | - |  |  | SI | Probability of Death 3% |
| Q37 | - |  |  | SI | 35-36 |
| Q38 | - |  |  | SI | Probability of Death 4% |
| Q39 | - |  |  | SI | 37-38 |
| Q40 | - |  |  | SI | Probability of Death 5% |
| Q41 | - |  |  | SI | 39-40 |
| Q42 | - |  |  | SI | Probability of Death 6% |
| Q43 | - |  |  | SI | 41 |
| Q44 | - |  |  | SI | Probability of Death 7% |
| Q45 | - |  |  | SI | 42 |
| Q46 | - |  |  | SI | Probability of Death 8% |
| Q47 | - |  |  | SI | 43 |
| Q48 | - |  |  | SI | Probability of Death 9% |
| Q49 | - |  |  | SI | 44 |
| Q50 | - |  |  | SI | Probability of Death 10% |
| Q51 | - |  |  | SI | 45 |
| Q52 | - |  |  | SI | Probability of Death 11% |
| Q53 | - |  |  | SI | 46 |
| Q54 | - |  |  | SI | Probability of Death 12% |
| Q55 | - |  |  | SI | 47 |
| Q56 | - |  |  | SI | Probability of Death 13% |
| Q57 | - |  |  | SI | 48 |
| Q58 | - |  |  | SI | Probability of Death 15% |
| Q59 | - |  |  | SI | 49 |
| Q60 | - |  |  | SI | Probability of Death 16% |
| Q61 | - |  |  | SI | 50 |
| Q62 | - |  |  | SI | Probability of Death 17% |
| Q63 | - |  |  | SI | 51 |
| Q64 | - |  |  | SI | Probability of Death 19% |
| Q65 | - |  |  | SI | 52 |
| Q66 | - |  |  | SI | Probability of Death 20% |
| Q67 | - |  |  | SI | 53 |
| Q68 | - |  |  | SI | Probability of Death 22% |
| Q69 | - |  |  | SI | 54 |
| Q70 | - |  |  | SI | Probability of Death 24% |
| Q71 | - |  |  | SI | 55 |
| Q72 | - |  |  | SI | Probability of Death 26% |
| Q73 | - |  |  | SI | 56 |
| Q74 | - |  |  | SI | Probability of Death 28% |
| Q75 | - |  |  | SI | 57 |
| Q76 | - |  |  | SI | Probability of Death 30% |
| Q77 | - |  |  | SI | 58 |
| Q78 | - |  |  | SI | Probability of Death 32% |
| Q79 | - |  |  | SI | 59 |
| Q80 | - |  |  | SI | Probability of Death 34% |
| Q81 | - |  |  | SI | 60 |
| Q82 | - |  |  | SI | Probability of Death 36% |
| Q83 | - |  |  | SI | 61 |
| Q84 | - |  |  | SI | Probability of Death 38% |
| Q85 | - |  |  | SI | 62 |
| Q86 | - |  |  | SI | Probability of Death 40% |
| Q87 | - |  |  | SI | 63 |
| Q88 | - |  |  | SI | Probability of Death 42% |
| Q89 | - |  |  | SI | 64 |
| Q90 | - |  |  | SI | Probability of Death 44% |
| Q91 | - |  |  | SI | 65 |
| Q92 | - |  |  | SI | Probability of Death 46% |
| Q93 | - |  |  | SI | 66 |
| Q94 | - |  |  | SI | Probability of Death 48% |
| Q95 | - |  |  | SI | 67 |
| Q96 | - |  |  | SI | Probability of Death 50% |
| Q97 | - |  |  | SI | 68 |
| Q98 | - |  |  | SI | Probability of Death 52% |
| Q99 | - |  |  | SI | 69 |
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
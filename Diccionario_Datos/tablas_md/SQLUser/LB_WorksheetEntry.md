# SQLUser.LB_WorksheetEntry

**Schema:** SQLUser
**Columnas:** 190
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBWSE_ParRef | bigint | PK |  | NO | - |
| LBWSE_Episode_DR | bigint |  | FK | SI | The Lab episode for this entry row |
| LBWSE_QCLink_DR | varchar |  | FK | SI | Linked QC |
| LBWSE_RowID | varchar |  |  | NO | - |
| LBWSE_SequenceNumber | numeric |  |  | SI | Sort order of the worksheet entries |
| Q01 | - |  |  | SI | Hombro |
| Q02 | - |  |  | SI | Flexión hombro izquierdo activo |
| Q03 | - |  |  | SI | Flexión hombro izquierdo pasivo |
| Q04 | - |  |  | SI | Flexión hombro derecho activo |
| Q05 | - |  |  | SI | Flexión hombro derecho pasivo |
| Q06 | - |  |  | SI | Extensión hombro izquierdo activo |
| Q07 | - |  |  | SI | Extensión hombro izquierdo pasivo |
| Q08 | - |  |  | SI | Extensión hombro derecho activo |
| Q09 | - |  |  | SI | Extención hombro derecho pasivo |
| Q10 | - |  |  | SI | Rot. Int hombro izquierdo activo |
| Q11 | - |  |  | SI | Rot Int hombro izquierdo pasivo |
| Q12 | - |  |  | SI | Rot Int hombro derecho activo |
| Q120 | - |  |  | SI | Observaciones |
| Q121 | - |  |  | SI | Fuerza hombro Flexión izquierda |
| Q122 | - |  |  | SI | Fuerza hombro Flexión derecha |
| Q123 | - |  |  | SI | Fuerza hombro Extensión izquierda |
| Q124 | - |  |  | SI | Fuerza hombro Extensión derecha |
| Q125 | - |  |  | SI | Fuerza hombro Rot Int izquierda |
| Q126 | - |  |  | SI | Fuerza hombro Rot Int derecha |
| Q127 | - |  |  | SI | Fuerza hombro Rot Ext izquierda |
| Q128 | - |  |  | SI | Fuerza hombro Rot Ext derecha |
| Q129 | - |  |  | SI | Fuerza hombro Abduccion izquierda |
| Q13 | - |  |  | SI | Rot Itn hombro derecho pasivo |
| Q130 | - |  |  | SI | Fuerza hombro Abducción derecha |
| Q131 | - |  |  | SI | Fuerza hombro Aducción izquierda |
| Q132 | - |  |  | SI | Fuerza hombro Aducción derecha |
| Q133 | - |  |  | SI | Fuerza codo Flexión izquierda |
| Q134 | - |  |  | SI | Fuerza codo Flexión derecha |
| Q135 | - |  |  | SI | Fuerza codo Extensión izquierda |
| Q136 | - |  |  | SI | Fuerza codo Extensión derecha |
| Q137 | - |  |  | SI | Fuerza muñeca Flexión izquierda |
| Q138 | - |  |  | SI | Fuerza muñeca Flexión derecha |
| Q139 | - |  |  | SI | Fuerza muñeca Extensión izquierda |
| Q14 | - |  |  | SI | Rot Ext hombro izquierdo activo |
| Q140 | - |  |  | SI | Fuerza muñeca Extensión derecha |
| Q141 | - |  |  | SI | Fuerza muñeca Lateral Ext izquierda |
| Q142 | - |  |  | SI | Fuerza muñeca Lateral Ext derecho |
| Q143 | - |  |  | SI | Fuerza muñeca Lateral Int izquierda |
| Q144 | - |  |  | SI | Fuerza muñeca Lateral Int derecha |
| Q145 | - |  |  | SI | Fuerza muñeca Supinación izquierda |
| Q146 | - |  |  | SI | Fuerza muñeca Supinación derecha |
| Q147 | - |  |  | SI | Fuerza muñeca Pronación izquierda |
| Q148 | - |  |  | SI | Fuerza muñeca Pronación derecha |
| Q15 | - |  |  | SI | Rot Ext hombro izquierdo pasivo |
| Q16 | - |  |  | SI | Rot Ext hombro derecho activo |
| Q17 | - |  |  | SI | Rot Ext hombro derecho pasivo |
| Q178 | - |  |  | SI | eva hombro flexion derecha |
| Q179 | - |  |  | SI | eva hombro flexion izquierdo |
| Q18 | - |  |  | SI | Abducción hombro izquierdo activo |
| Q180 | - |  |  | SI | eva hombro extension derecha |
| Q181 | - |  |  | SI | eva hombro extension izquierda |
| Q182 | - |  |  | SI | eva hombro rot int derecha |
| Q183 | - |  |  | SI | eva hombro rot int izquierda |
| Q184 | - |  |  | SI | eva hombro rot ext derecha |
| Q185 | - |  |  | SI | eva hombro rot ext izquierda |
| Q186 | - |  |  | SI | eva hombro abducion derecha |
| Q187 | - |  |  | SI | eva hombro abducion izquierdo |
| Q188 | - |  |  | SI | eva hombro aduccion derecha |
| Q189 | - |  |  | SI | eva hombro aduccion izquierda |
| Q19 | - |  |  | SI | Abducción hombro izquierdo pasivo |
| Q190 | - |  |  | SI | eva codo flexión derecha |
| Q191 | - |  |  | SI | eva codo flexión izquierda |
| Q192 | - |  |  | SI | eva codo extension derecha |
| Q193 | - |  |  | SI | eva codo extension izquierda |
| Q194 | - |  |  | SI | eva muñeca flexion izquierda |
| Q195 | - |  |  | SI | eva muñeca flexion derecha |
| Q196 | - |  |  | SI | eva muñeca extension izquierda |
| Q197 | - |  |  | SI | eva muñeca extension derecha |
| Q198 | - |  |  | SI | eva muñeca lateral ext izquierda |
| Q199 | - |  |  | SI | eva muñeca lateral ext derecha |
| Q20 | - |  |  | SI | Abducción hombro derecho activo |
| Q200 | - |  |  | SI | eva muñeca lateral int izquierda |
| Q201 | - |  |  | SI | eva muñeca lateral int derecha |
| Q202 | - |  |  | SI | eva muñeca supinacion izquierda |
| Q203 | - |  |  | SI | eva muñeca supinacion derecha |
| Q204 | - |  |  | SI | eva muñeca pronacion izquierda |
| Q205 | - |  |  | SI | eva muñeca pronacion derecha |
| Q21 | - |  |  | SI | Abducción hombro derecho pasivo |
| Q22 | - |  |  | SI | Aducción hombro izquierdo activo |
| Q23 | - |  |  | SI | Aducción hombro izquierdo pasivo |
| Q236 | - |  |  | SI | eva hombro flexion derecha pasivo |
| Q237 | - |  |  | SI | eva hombro flexion izquierda pasivo |
| Q238 | - |  |  | SI | eva hombro extension izquierda pasivo |
| Q239 | - |  |  | SI | eva hombro extension derecha pasivo |
| Q24 | - |  |  | SI | Aducción hombro derecho activo |
| Q240 | - |  |  | SI | eva hombro rot int izquierda pasivo |
| Q241 | - |  |  | SI | eva hombro rot int derecha pasivo |
| Q242 | - |  |  | SI | eva hombro rot ext izquierda pasivo |
| Q243 | - |  |  | SI | eva hombro rot ext derecha pasivo |
| Q244 | - |  |  | SI | eva hombro abducion izquierda pasivo |
| Q245 | - |  |  | SI | eva hombro abducion derecha pasivo |
| Q246 | - |  |  | SI | eva hombro adducion izquierda pasivo |
| Q247 | - |  |  | SI | eva hombro adducion derecha pasivo |
| Q248 | - |  |  | SI | eva codo flexion izq pasivo |
| Q249 | - |  |  | SI | eva codo flexión derecho pasivo |
| Q25 | - |  |  | SI | Aducción hombro derecho pasivo |
| Q250 | - |  |  | SI | eva codo extensión izquierda pasivo |
| Q251 | - |  |  | SI | eva codo flexión derecha pasivo |
| Q252 | - |  |  | SI | eva muñeca flexión izquierda pasivo |
| Q253 | - |  |  | SI | eva muñeca flexión derecha pasivo |
| Q254 | - |  |  | SI | eva muñeca extensión izquierda pasivo |
| Q255 | - |  |  | SI | eva muñeca extensión derecha pasivo |
| Q256 | - |  |  | SI | eva muñeca lateral ext. izquierda pasivo |
| Q257 | - |  |  | SI | eva muñeca lateral ext. derecha pasivo |
| Q258 | - |  |  | SI | eva muñeca lateral int. izquierda pasivo |
| Q259 | - |  |  | SI | eva muñeca lateral int. derecha pasivo |
| Q26 | - |  |  | SI | Codo |
| Q260 | - |  |  | SI | eva muñeca supinación izquierda pasivo |
| Q261 | - |  |  | SI | eva muñeca supinación derecha pasivo |
| Q262 | - |  |  | SI | eva muñeca pronación izquierda pasivo |
| Q263 | - |  |  | SI | eva muñeca pronación derecha pasivo |
| Q27 | - |  |  | SI | Flexión codo izquierdo activo |
| Q28 | - |  |  | SI | Flexión codo izquierdo pasivo |
| Q29 | - |  |  | SI | Flexión codo derecho activo |
| Q30 | - |  |  | SI | Flexión codo derecho pasivo |
| Q31 | - |  |  | SI | Extensión codo izquierdo activo |
| Q32 | - |  |  | SI | Extensión codo izquierdo pasivo |
| Q33 | - |  |  | SI | Extensión codo derecho activo |
| Q34 | - |  |  | SI | Extension codo derecho pasivo |
| Q35 | - |  |  | SI | Muñeca |
| Q36 | - |  |  | SI | Flexión muñeca izquierda activa |
| Q37 | - |  |  | SI | Flexión muñeca izquierda pasiva |
| Q38 | - |  |  | SI | Flexión muñeca derecha activa |
| Q39 | - |  |  | SI | Flexión muñeca derecha pasiva |
| Q40 | - |  |  | SI | Extensión muñeca izquierda activa |
| Q41 | - |  |  | SI | Extensión muñeca izquierda pasiva |
| Q42 | - |  |  | SI | Extensión muñeca derecha activa |
| Q43 | - |  |  | SI | Extensión muñeca derecha pasiva |
| Q44 | - |  |  | SI | Lateral Ext muñeca izquierda activa |
| Q45 | - |  |  | SI | Lateral Ext muñeca izquierda pasiva |
| Q46 | - |  |  | SI | Lateral Ext muñeca derecha activo |
| Q47 | - |  |  | SI | Lateral Ext muñeca derecha pasiva |
| Q48 | - |  |  | SI | Lateral Int muñeca izquierda activa |
| Q49 | - |  |  | SI | Lateral Int muñeca izquierda pasiva |
| Q50 | - |  |  | SI | Lateral Int muñeca derecha activa |
| Q51 | - |  |  | SI | Lateral Int muñeca derecha pasiva |
| Q52 | - |  |  | SI | Supinación muñeca izquierda activa |
| Q53 | - |  |  | SI | Supinación muñeca izquierda pasiva |
| Q54 | - |  |  | SI | Supinación muñeca derecha activa |
| Q55 | - |  |  | SI | Supinación muñeca derecha pasiva |
| Q56 | - |  |  | SI | Pronación muñeca izquierda activa |
| Q57 | - |  |  | SI | Pronación muñeca izquierda pasiva |
| Q58 | - |  |  | SI | Pronación muñeca derecha activa |
| Q59 | - |  |  | SI | Pronación muñeca derecha pasiva |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
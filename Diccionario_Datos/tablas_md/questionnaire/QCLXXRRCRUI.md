# questionnaire.QCLXXRRCRUI

> VISUALIZAR RESULTADOS RUI

**Schema:** questionnaire
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* VISUALIZAR RESULTADOS RUI

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | Hematocrito |
| Q02 | date |  |  | SI | Fecha Hematocrito |
| Q03 | numeric |  |  | SI | Hemoglobina |
| Q04 | date |  |  | SI | Fecha Hemoglobina |
| Q05 | numeric |  |  | SI | Glicemia |
| Q06 | date |  |  | SI | Fecha Glicemia |
| Q07 | numeric |  |  | SI | Hemoglobina glicosilada |
| Q08 | date |  |  | SI | Fecha Hemoglobina glicosilada |
| Q09 | numeric |  |  | SI | Colesterol Total |
| Q10 | date |  |  | SI | Fecha Colesterol Total |
| Q11 | numeric |  |  | SI | Triglicéridos |
| Q12 | date |  |  | SI | Fecha Triglicéridos |
| Q13 | numeric |  |  | SI | Colesterol HDL |
| Q14 | date |  |  | SI | Fecha Colesterol HDL |
| Q15 | numeric |  |  | SI | Colesterol LDL |
| Q16 | date |  |  | SI | Fecha Colesterol LDL |
| Q17 | numeric |  |  | SI | GOT |
| Q18 | date |  |  | SI | Fecha GOT |
| Q19 | numeric |  |  | SI | GPT |
| Q20 | date |  |  | SI | Fecha GPT |
| Q21 | numeric |  |  | SI | Creatinemia |
| Q22 | date |  |  | SI | Fecha Creatininemia |
| Q23 | numeric |  |  | SI | Velocidad de Filtración Glomerular (Cockcroft-Gaul... |
| Q24 | date |  |  | SI | Fecha Velocidad de Filtración Glomerular (Cockcrof... |
| Q25 | numeric |  |  | SI | Electrolitos plasmáticos: Sodio |
| Q26 | date |  |  | SI | Fecha Electrolitos plasmáticos: Sodio |
| Q27 | numeric |  |  | SI | Electrolitos plasmáticos: Potasio |
| Q28 | date |  |  | SI | Fecha Electrolitos plasmáticos: Potasio |
| Q29 | numeric |  |  | SI | Electrolitos plasmáticos: Cloro |
| Q30 | date |  |  | SI | Fecha Electrolitos plasmáticos: Cloro |
| Q31 | numeric |  |  | SI | Relación Albúmina / Creatininuria (RAC) |
| Q32 | date |  |  | SI | Fecha Relación Albúmina / Creatininuria (RAC) |
| Q33 | numeric |  |  | SI | TSH |
| Q34 | date |  |  | SI | Fecha TSH |
| Q35 | varchar |  |  | SI | Baciloscopía |
| Q36 | date |  |  | SI | Fecha Baciloscopía |
| Q37 | varchar |  |  | SI | RPR |
| Q38 | date |  |  | SI | Fecha RPR |
| Q39 | varchar |  |  | SI | VDRL |
| Q40 | date |  |  | SI | Fecha VDRL |
| Q41 | varchar |  |  | SI | Fondo de Ojo |
| Q42 | date |  |  | SI | Fecha Fondo de ojo |
| Q43 | numeric |  |  | SI | Velocidad de Filtración Glomerular (MDRD-4) |
| Q44 | date |  |  | SI | Fecha Velocidad de Filtración Glomerular (MDRD-4) |
| Q45 | varchar |  |  | SI | Reg. Hematocrito  |
| Q45ObsDR | varchar |  | FK | SI | Reg. Hematocrito  DR |
| Q46 | varchar |  |  | SI | Reg. Hemoglobina |
| Q46ObsDR | varchar |  | FK | SI | Reg. Hemoglobina DR |
| Q47 | varchar |  |  | SI | Reg. Glicemia |
| Q47ObsDR | varchar |  | FK | SI | Reg. Glicemia DR |
| Q48 | varchar |  |  | SI | Reg. Hemoglobina glicosilada |
| Q48ObsDR | varchar |  | FK | SI | Reg. Hemoglobina glicosilada DR |
| Q49 | varchar |  |  | SI | Reg. Colesterol Total |
| Q49ObsDR | varchar |  | FK | SI | Reg. Colesterol Total DR |
| Q50 | varchar |  |  | SI | Reg. Triglicéridos |
| Q50ObsDR | varchar |  | FK | SI | Reg. Triglicéridos DR |
| Q51 | varchar |  |  | SI | Reg. Colesterol HDL |
| Q51ObsDR | varchar |  | FK | SI | Reg. Colesterol HDL DR |
| Q52 | varchar |  |  | SI | Reg. Colesterol LDL |
| Q53 | varchar |  |  | SI | Reg. GOT |
| Q53ObsDR | varchar |  | FK | SI | Reg. GOT DR |
| Q54 | varchar |  |  | SI | Reg. GPT |
| Q54ObsDR | varchar |  | FK | SI | Reg. GPT DR |
| Q55 | varchar |  |  | SI | Reg. Creatinemia |
| Q55ObsDR | varchar |  | FK | SI | Reg. Creatinemia DR |
| Q56 | varchar |  |  | SI | Reg. VFG (Cockcroft-Gault) |
| Q56ObsDR | varchar |  | FK | SI | Reg. VFG (Cockcroft-Gault) DR |
| Q57 | varchar |  |  | SI | Reg. VFG (MDRD-4) |
| Q57ObsDR | varchar |  | FK | SI | Reg. VFG (MDRD-4) DR |
| Q58 | varchar |  |  | SI | Reg. Sodio |
| Q58ObsDR | varchar |  | FK | SI | Reg. Sodio DR |
| Q59 | varchar |  |  | SI | Reg. Potasio |
| Q59ObsDR | varchar |  | FK | SI | Reg. Potasio DR |
| Q60 | varchar |  |  | SI | Reg. Cloro |
| Q60ObsDR | varchar |  | FK | SI | Reg. Cloro DR |
| Q61 | varchar |  |  | SI | Reg. RAC |
| Q61ObsDR | varchar |  | FK | SI | Reg. RAC DR |
| Q62 | varchar |  |  | SI | Reg. TSH |
| Q62ObsDR | varchar |  | FK | SI | Reg. TSH DR |
| Q63 | varchar |  |  | SI | Reg. Baciloscopía |
| Q63ObsDR | varchar |  | FK | SI | Reg. Baciloscopía DR |
| Q64 | varchar |  |  | SI | Reg. RPR |
| Q64ObsDR | varchar |  | FK | SI | Reg. RPR DR |
| Q65 | varchar |  |  | SI | Reg. VDRL |
| Q65ObsDR | varchar |  | FK | SI | Reg. VDRL DR |
| Q66 | varchar |  |  | SI | Reg. Fondo de Ojo |
| Q66ObsDR | varchar |  | FK | SI | Reg. Fondo de Ojo DR |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
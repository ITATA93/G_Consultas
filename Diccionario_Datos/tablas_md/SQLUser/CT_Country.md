# SQLUser.CT_Country

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCOU_RowId | bigint | PK |  | NO | - |
| CTCOU_Active | varchar |  |  | SI | Active |
| CTCOU_Code | varchar |  |  | NO | Country Code |
| CTCOU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTCOU_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| CTCOU_CreatedDate | date |  |  | SI | Created Date |
| CTCOU_CreatedTime | time |  |  | SI | Created Time |
| CTCOU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTCOU_DateActiveFrom | date |  |  | SI | Date Active From |
| CTCOU_DateActiveTo | date |  |  | SI | Date Active To |
| CTCOU_Desc | varchar |  |  | NO | Country Description |
| CTCOU_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| CTCOU_Iso3166Alpha2Code | varchar |  |  | SI | ISO-3166 Alpha-2 Code |
| CTCOU_Iso3166Alpha3Code | varchar |  |  | SI | ISO-3166 Alpha-3 Code |
| CTCOU_Iso3166Code | varchar |  |  | SI | ISO-3166 Code |
| CTCOU_NationalCode | varchar |  |  | SI | National Code |
| CTCOU_Owner | varchar |  |  | SI | Owner |
| CTCOU_UpdatedDate | date |  |  | SI | Updated Date |
| CTCOU_UpdatedTime | time |  |  | SI | Updated Time |
| CTCOU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Hematocrito |
| Q02 | - |  |  | SI | Fecha Hematocrito |
| Q03 | - |  |  | SI | Hemoglobina |
| Q04 | - |  |  | SI | Fecha Hemoglobina |
| Q05 | - |  |  | SI | Glicemia |
| Q06 | - |  |  | SI | Fecha Glicemia |
| Q07 | - |  |  | SI | Hemoglobina glicosilada |
| Q08 | - |  |  | SI | Fecha Hemoglobina glicosilada |
| Q09 | - |  |  | SI | Colesterol Total |
| Q10 | - |  |  | SI | Fecha Colesterol Total |
| Q11 | - |  |  | SI | Triglicéridos |
| Q12 | - |  |  | SI | Fecha Triglicéridos |
| Q13 | - |  |  | SI | Colesterol HDL |
| Q14 | - |  |  | SI | Fecha Colesterol HDL |
| Q15 | - |  |  | SI | Colesterol LDL |
| Q16 | - |  |  | SI | Fecha Colesterol LDL |
| Q17 | - |  |  | SI | GOT |
| Q18 | - |  |  | SI | Fecha GOT |
| Q19 | - |  |  | SI | GPT |
| Q20 | - |  |  | SI | Fecha GPT |
| Q21 | - |  |  | SI | Creatinemia |
| Q22 | - |  |  | SI | Fecha Creatininemia |
| Q23 | - |  |  | SI | Velocidad de Filtración Glomerular (Cockcroft-Gaul... |
| Q24 | - |  |  | SI | Fecha Velocidad de Filtración Glomerular (Cockcrof... |
| Q25 | - |  |  | SI | Electrolitos plasmáticos: Sodio |
| Q26 | - |  |  | SI | Fecha Electrolitos plasmáticos: Sodio |
| Q27 | - |  |  | SI | Electrolitos plasmáticos: Potasio |
| Q28 | - |  |  | SI | Fecha Electrolitos plasmáticos: Potasio |
| Q29 | - |  |  | SI | Electrolitos plasmáticos: Cloro |
| Q30 | - |  |  | SI | Fecha Electrolitos plasmáticos: Cloro |
| Q31 | - |  |  | SI | Relación Albúmina / Creatininuria (RAC) |
| Q32 | - |  |  | SI | Fecha Relación Albúmina / Creatininuria (RAC) |
| Q33 | - |  |  | SI | TSH |
| Q34 | - |  |  | SI | Fecha TSH |
| Q35 | - |  |  | SI | Baciloscopía |
| Q36 | - |  |  | SI | Fecha Baciloscopía |
| Q37 | - |  |  | SI | RPR |
| Q38 | - |  |  | SI | Fecha RPR |
| Q39 | - |  |  | SI | VDRL |
| Q40 | - |  |  | SI | Fecha VDRL |
| Q41 | - |  |  | SI | Fondo de Ojo |
| Q42 | - |  |  | SI | Fecha Fondo de ojo |
| Q43 | - |  |  | SI | Velocidad de Filtración Glomerular (MDRD-4) |
| Q44 | - |  |  | SI | Fecha Velocidad de Filtración Glomerular (MDRD-4) |
| Q45 | - |  |  | SI | Reg. Hematocrito |
| Q45ObsDR | - |  |  | SI | Reg. Hematocrito  DR |
| Q46 | - |  |  | SI | Reg. Hemoglobina |
| Q46ObsDR | - |  |  | SI | Reg. Hemoglobina DR |
| Q47 | - |  |  | SI | Reg. Glicemia |
| Q47ObsDR | - |  |  | SI | Reg. Glicemia DR |
| Q48 | - |  |  | SI | Reg. Hemoglobina glicosilada |
| Q48ObsDR | - |  |  | SI | Reg. Hemoglobina glicosilada DR |
| Q49 | - |  |  | SI | Reg. Colesterol Total |
| Q49ObsDR | - |  |  | SI | Reg. Colesterol Total DR |
| Q50 | - |  |  | SI | Reg. Triglicéridos |
| Q50ObsDR | - |  |  | SI | Reg. Triglicéridos DR |
| Q51 | - |  |  | SI | Reg. Colesterol HDL |
| Q51ObsDR | - |  |  | SI | Reg. Colesterol HDL DR |
| Q52 | - |  |  | SI | Reg. Colesterol LDL |
| Q53 | - |  |  | SI | Reg. GOT |
| Q53ObsDR | - |  |  | SI | Reg. GOT DR |
| Q54 | - |  |  | SI | Reg. GPT |
| Q54ObsDR | - |  |  | SI | Reg. GPT DR |
| Q55 | - |  |  | SI | Reg. Creatinemia |
| Q55ObsDR | - |  |  | SI | Reg. Creatinemia DR |
| Q56 | - |  |  | SI | Reg. VFG (Cockcroft-Gault) |
| Q56ObsDR | - |  |  | SI | Reg. VFG (Cockcroft-Gault) DR |
| Q57 | - |  |  | SI | Reg. VFG (MDRD-4) |
| Q57ObsDR | - |  |  | SI | Reg. VFG (MDRD-4) DR |
| Q58 | - |  |  | SI | Reg. Sodio |
| Q58ObsDR | - |  |  | SI | Reg. Sodio DR |
| Q59 | - |  |  | SI | Reg. Potasio |
| Q59ObsDR | - |  |  | SI | Reg. Potasio DR |
| Q60 | - |  |  | SI | Reg. Cloro |
| Q60ObsDR | - |  |  | SI | Reg. Cloro DR |
| Q61 | - |  |  | SI | Reg. RAC |
| Q61ObsDR | - |  |  | SI | Reg. RAC DR |
| Q62 | - |  |  | SI | Reg. TSH |
| Q62ObsDR | - |  |  | SI | Reg. TSH DR |
| Q63 | - |  |  | SI | Reg. Baciloscopía |
| Q63ObsDR | - |  |  | SI | Reg. Baciloscopía DR |
| Q64 | - |  |  | SI | Reg. RPR |
| Q64ObsDR | - |  |  | SI | Reg. RPR DR |
| Q65 | - |  |  | SI | Reg. VDRL |
| Q65ObsDR | - |  |  | SI | Reg. VDRL DR |
| Q66 | - |  |  | SI | Reg. Fondo de Ojo |
| Q66ObsDR | - |  |  | SI | Reg. Fondo de Ojo DR |
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
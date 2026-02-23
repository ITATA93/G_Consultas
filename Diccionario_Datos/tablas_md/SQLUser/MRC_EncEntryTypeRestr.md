# SQLUser.MRC_EncEntryTypeRestr

**Schema:** SQLUser
**Columnas:** 237
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ERESTR_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| ERESTR_Childsub | double |  |  | NO | Childsub |
| ERESTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ERESTR_CreatedDate | date |  |  | SI | Created Date |
| ERESTR_CreatedTime | time |  |  | SI | Created Time |
| ERESTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ERESTR_FromAge | integer |  |  | SI | Age From |
| ERESTR_FromAgePeriod | varchar |  |  | SI | Age From |
| ERESTR_Gender | bigint |  |  | SI | Gender |
| ERESTR_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| ERESTR_RowId | varchar |  |  | NO | - |
| ERESTR_ToAge | integer |  |  | SI | Age To |
| ERESTR_ToAgePeriod | varchar |  |  | SI | Age To |
| ERESTR_UpdatedDate | date |  |  | SI | Updated Date |
| ERESTR_UpdatedTime | time |  |  | SI | Updated Time |
| ERESTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Establecimiento de Salud (código y descripción) |
| Q02 | - |  |  | SI | código establecimiento de salud |
| Q03 | - |  |  | SI | Mes de Atención |
| Q04 | - |  |  | SI | Año de Atención |
| Q05 | - |  |  | SI | actividades,totales RBC, comunas comunidades, diag... |
| Q06 | - |  |  | SI | actividades,totales RBC, organizaciones asociadas ... |
| Q07 | - |  |  | SI | actividades,totales RBC, organizaciones comunitari... |
| Q08 | - |  |  | SI | actividades,totales RBC, comunidad educativa, diag... |
| Q09 | - |  |  | SI | participantes,totales RBC, comunas comunidades, di... |
| Q10 | - |  |  | SI | participantes,totales RBC, organizaciones asociada... |
| Q100 | - |  |  | SI | participantes,totales R1, cuidadores, actividades ... |
| Q101 | - |  |  | SI | actividades,totales RR, profesionales de salud, ac... |
| Q102 | - |  |  | SI | actividades,totales RR, empleadores y compañeros d... |
| Q103 | - |  |  | SI | actividades,totales RR, comunidad educativa, activ... |
| Q104 | - |  |  | SI | actividades,totales RR, monitores, actividades par... |
| Q105 | - |  |  | SI | actividades,totales RR, red de apoyo, actividades ... |
| Q106 | - |  |  | SI | actividades,totales RR, cuidadores, actividades pa... |
| Q107 | - |  |  | SI | participantes,totales RR, profesionales de salud, ... |
| Q108 | - |  |  | SI | participantes,totales RR, empleadores y compañeros... |
| Q109 | - |  |  | SI | participantes,totales RR, comunidad educativa, act... |
| Q11 | - |  |  | SI | participantes,totales RBC, organizaciones comunita... |
| Q110 | - |  |  | SI | participantes,totales RR, monitores, actividades p... |
| Q111 | - |  |  | SI | participantes,totales RR, red de apoyo, actividade... |
| Q112 | - |  |  | SI | participantes,totales RR, cuidadores, actividades ... |
| Q113 | - |  |  | SI | actividades,otros totales, profesionales de salud,... |
| Q114 | - |  |  | SI | actividades,otros totales, empleadores y compañero... |
| Q115 | - |  |  | SI | actividades,otros totales, comunidad educativa, ac... |
| Q116 | - |  |  | SI | actividades,otros totales, monitores, actividades ... |
| Q117 | - |  |  | SI | actividades,otros totales, red de apoyo, actividad... |
| Q118 | - |  |  | SI | actividades,otros totales, cuidadores, actividades... |
| Q119 | - |  |  | SI | participantes,otros totales, profesionales de salu... |
| Q12 | - |  |  | SI | participantes,totales RBC, comunidad educativa, di... |
| Q120 | - |  |  | SI | participantes,otros totales, empleadores y compañe... |
| Q121 | - |  |  | SI | participantes,otros totales, comunidad educativa, ... |
| Q122 | - |  |  | SI | participantes,otros totales, monitores, actividade... |
| Q123 | - |  |  | SI | participantes,otros totales, red de apoyo, activid... |
| Q124 | - |  |  | SI | participantes,otros totales, cuidadores, actividad... |
| Q125 | - |  |  | SI | actividades,totales RBC, organizaciones de psd, as... |
| Q126 | - |  |  | SI | actividades,totales RBC, organizaciones para/por p... |
| Q127 | - |  |  | SI | participantes,totales RBC, organizaciones de psd, ... |
| Q128 | - |  |  | SI | participantes,totales RBC, organizaciones para/por... |
| Q129 | - |  |  | SI | actividades,totales R1, organizaciones de psd, ase... |
| Q13 | - |  |  | SI | actividades,totales R1, comunas comunidades, diagn... |
| Q130 | - |  |  | SI | actividades,totales R1, organizaciones para/por ps... |
| Q131 | - |  |  | SI | participantes,totales R1, organizaciones de psd, a... |
| Q132 | - |  |  | SI | participantes,totales R1, organizaciones para/por ... |
| Q133 | - |  |  | SI | actividades,totales RR, organizaciones de psd, ase... |
| Q134 | - |  |  | SI | actividades,totales RR, organizaciones para/por ps... |
| Q135 | - |  |  | SI | participantes,totales RR, organizaciones de psd, a... |
| Q136 | - |  |  | SI | participantes,totales RR, organizaciones para/por ... |
| Q137 | - |  |  | SI | actividades,otros totales, organizaciones de psd, ... |
| Q138 | - |  |  | SI | actividades,otros totales, organizaciones para/por... |
| Q139 | - |  |  | SI | participantes,otros totales, organizaciones de psd... |
| Q14 | - |  |  | SI | actividades,totales R1, organizaciones asociadas a... |
| Q140 | - |  |  | SI | participantes,otros totales, organizaciones para/p... |
| Q142 | - |  |  | SI | actividades, totales RBC, Organizaciones Comunitar... |
| Q143 | - |  |  | SI | participantes, totales RBC, Organizaciones Comunit... |
| Q144 | - |  |  | SI | actividades, totales R1, Organizaciones Comunitari... |
| Q145 | - |  |  | SI | participantes, totales R1, Organizaciones Comunita... |
| Q146 | - |  |  | SI | actividades, totales RR, Organizaciones Comunitari... |
| Q147 | - |  |  | SI | participantes, totales RR, Organizaciones Comunita... |
| Q148 | - |  |  | SI | actividades, otros totales, Organizaciones Comunit... |
| Q149 | - |  |  | SI | participantes, otros totales, Organizaciones Comun... |
| Q15 | - |  |  | SI | actividades,totales R1, organizaciones comunitaria... |
| Q150 | - |  |  | SI | actividades, UAPORRINO, comunas comunidades, diagn... |
| Q151 | - |  |  | SI | participantes, UAPORRINO, comunas comunidades, dia... |
| Q152 | - |  |  | SI | actividades UAPORRINO, organizaciones asociadas a ... |
| Q153 | - |  |  | SI | participantes, UAPORRINO, organizaciones asociadas... |
| Q154 | - |  |  | SI | actividades, UAPORRINO, organizaciones comunitaria... |
| Q155 | - |  |  | SI | participantes, UAPORRINO, organizaciones comunitar... |
| Q156 | - |  |  | SI | actividades, UAPORRINO, comunidad educativa, diagn... |
| Q157 | - |  |  | SI | participantes, UAPORRINO, comunidad educativa, dia... |
| Q158 | - |  |  | SI | actividades UAPORRINO, comunas comunidades, activi... |
| Q159 | - |  |  | SI | participantes, UAPORRINO, comunas comunidades, act... |
| Q16 | - |  |  | SI | actividades,totales R1, comunidad educativa, diagn... |
| Q160 | - |  |  | SI | actividades, UAPORRINO, empleadores y compañeros d... |
| Q161 | - |  |  | SI | participantes, UAPORRINO, empleadores y compañeros... |
| Q162 | - |  |  | SI | actividades, UAPORRINO, comunidad educativa, activ... |
| Q163 | - |  |  | SI | participantes, UAPORRINO, comunidad educativa, act... |
| Q164 | - |  |  | SI | actividades, UAPORRINO, red de apoyo, actividades ... |
| Q165 | - |  |  | SI | participantes, UAPORRINO, red de apoyo, actividade... |
| Q166 | - |  |  | SI | actividades, UAPORRINO, cuidadores, actividades de... |
| Q167 | - |  |  | SI | participantes, UAPORRINO,  cuidadores, actividades... |
| Q168 | - |  |  | SI | actividades, UAPORRINO, profesionales de la salud,... |
| Q169 | - |  |  | SI | participantes, UAPORRINO, profesionales de salud, ... |
| Q17 | - |  |  | SI | participantes,totales R1, comunas comunidades, dia... |
| Q170 | - |  |  | SI | actividades, UAPORRINO, empleadores y compañeros d... |
| Q171 | - |  |  | SI | participantes, UAPORRINO, empleadores y compañeros... |
| Q172 | - |  |  | SI | actividades, UAPORRINO, comunidad educativa, activ... |
| Q173 | - |  |  | SI | participantes, UAPORRINO, comunidad educativa, act... |
| Q174 | - |  |  | SI | actividades, UAPORRINO, monitores, actividades par... |
| Q175 | - |  |  | SI | participantes, UAPORRINO, monitores, actividades p... |
| Q176 | - |  |  | SI | actividades, UAPORRINO, red de apoyo, actividades ... |
| Q177 | - |  |  | SI | participantes, UAPORRINO, red de apoyo, actividade... |
| Q178 | - |  |  | SI | actividades, UAPORRINO, cuidadores, actividades pa... |
| Q179 | - |  |  | SI | participantes, UAPORRINO, cuidadores, actividades ... |
| Q18 | - |  |  | SI | participantes,totales R1, organizaciones asociadas... |
| Q180 | - |  |  | SI | actividades, UAPORRINO, cuidadores, Organizaciones... |
| Q181 | - |  |  | SI | participantes, UAPORRINO, cuidadores, Organizacion... |
| Q19 | - |  |  | SI | participantes,totales R1, organizaciones comunitar... |
| Q20 | - |  |  | SI | participantes,totales R1, comunidad educativa, dia... |
| Q21 | - |  |  | SI | actividades,totales RR, comunas comunidades, diagn... |
| Q22 | - |  |  | SI | actividades,totales RR, organizaciones asociadas a... |
| Q23 | - |  |  | SI | actividades,totales RR, organizaciones comunitaria... |
| Q24 | - |  |  | SI | actividades,totales RR, comunidad educativa, diagn... |
| Q25 | - |  |  | SI | participantes,totales RR, comunas comunidades, dia... |
| Q26 | - |  |  | SI | participantes,totales RR, organizaciones asociadas... |
| Q27 | - |  |  | SI | participantes,totales RR, organizaciones comunitar... |
| Q28 | - |  |  | SI | participantes,totales RR, comunidad educativa, dia... |
| Q29 | - |  |  | SI | actividades,OTROS totales, comunas comunidades, di... |
| Q30 | - |  |  | SI | actividades,OTROS totales, organizaciones asociada... |
| Q31 | - |  |  | SI | actividades,OTROS totales, organizaciones comunita... |
| Q32 | - |  |  | SI | actividades,OTROS totales, comunidad educativa, di... |
| Q33 | - |  |  | SI | participantes,OTROS totales, comunas comunidades, ... |
| Q34 | - |  |  | SI | participantes,OTROS totales, organizaciones asocia... |
| Q35 | - |  |  | SI | participantes,OTROS totales, organizaciones comuni... |
| Q36 | - |  |  | SI | participantes,OTROS totales, comunidad educativa, ... |
| Q37 | - |  |  | SI | actividades,totales RBC, comunas comunidades, acti... |
| Q38 | - |  |  | SI | actividades,totales RBC, empleadores y compañeros ... |
| Q39 | - |  |  | SI | actividades,totales RBC, comunidad educativa, acti... |
| Q40 | - |  |  | SI | actividades,totales RBC, red de apoyo, actividades... |
| Q41 | - |  |  | SI | actividades,totales RBC, cuidadores, actividades d... |
| Q42 | - |  |  | SI | participantes,totales RBC, comunas comunidades, ac... |
| Q43 | - |  |  | SI | participantes,totales RBC, empleadores y compañero... |
| Q44 | - |  |  | SI | participantes,totales RBC, comunidad educativa, ac... |
| Q45 | - |  |  | SI | participantes,totales RBC, red de apoyo, actividad... |
| Q46 | - |  |  | SI | participantes,totales RBC, cuidadores, actividades... |
| Q47 | - |  |  | SI | actividades,totales R1, comunas comunidades, activ... |
| Q48 | - |  |  | SI | actividades,totales R1, empleadores y compañeros d... |
| Q49 | - |  |  | SI | actividades,totales R1, comunidad educativa, activ... |
| Q50 | - |  |  | SI | actividades,totales R1, red de apoyo, actividades ... |
| Q51 | - |  |  | SI | actividades,totales R1, cuidadores, actividades de... |
| Q52 | - |  |  | SI | participantes,totales R1, comunas comunidades, act... |
| Q53 | - |  |  | SI | participantes,totales R1, empleadores y compañeros... |
| Q54 | - |  |  | SI | participantes,totales R1, comunidad educativa, act... |
| Q55 | - |  |  | SI | participantes,totales R1, red de apoyo, actividade... |
| Q56 | - |  |  | SI | participantes,totales R1, cuidadores, actividades ... |
| Q57 | - |  |  | SI | actividades,totales RR, comunas comunidades, activ... |
| Q58 | - |  |  | SI | actividades,totales RR, empleadores y compañeros d... |
| Q59 | - |  |  | SI | actividades,totales RR, comunidad educativa, activ... |
| Q60 | - |  |  | SI | actividades,totales RR, red de apoyo, actividades ... |
| Q61 | - |  |  | SI | actividades,totales RR, cuidadores, actividades de... |
| Q62 | - |  |  | SI | participantes,totales RR, comunas comunidades, act... |
| Q63 | - |  |  | SI | participantes,totales RR, empleadores y compañeros... |
| Q64 | - |  |  | SI | participantes,totales RR, comunidad educativa, act... |
| Q65 | - |  |  | SI | participantes,totales RR, red de apoyo, actividade... |
| Q66 | - |  |  | SI | participantes,totales RR, cuidadores, actividades ... |
| Q67 | - |  |  | SI | actividades,otros totales, comunas comunidades, ac... |
| Q68 | - |  |  | SI | actividades,otros totales, empleadores y compañero... |
| Q69 | - |  |  | SI | actividades,otros totales, comunidad educativa, ac... |
| Q70 | - |  |  | SI | actividades,otros totales, red de apoyo, actividad... |
| Q71 | - |  |  | SI | actividades,otros totales, cuidadores, actividades... |
| Q72 | - |  |  | SI | participantes,otros totales, comunas comunidades, ... |
| Q73 | - |  |  | SI | participantes,otros totales, empleadores y compañe... |
| Q74 | - |  |  | SI | participantes,otros totales, comunidad educativa, ... |
| Q75 | - |  |  | SI | participantes,otros totales, red de apoyo, activid... |
| Q76 | - |  |  | SI | participantes,otros totales, cuidadores, actividad... |
| Q77 | - |  |  | SI | actividades,totales RBC, profesionales de salud, a... |
| Q78 | - |  |  | SI | actividades,totales RBC, empleadores y compañeros ... |
| Q79 | - |  |  | SI | actividades,totales RBC, comunidad educativa, acti... |
| Q80 | - |  |  | SI | actividades,totales RBC, monitores, actividades pa... |
| Q81 | - |  |  | SI | actividades,totales RBC, red de apoyo, actividades... |
| Q82 | - |  |  | SI | actividades,totales RBC, cuidadores, actividades p... |
| Q83 | - |  |  | SI | participantes,totales RBC, profesionales de salud,... |
| Q84 | - |  |  | SI | participantes,totales RBC, empleadores y compañero... |
| Q85 | - |  |  | SI | participantes,totales RBC, comunidad educativa, ac... |
| Q86 | - |  |  | SI | participantes,totales RBC, monitores, actividades ... |
| Q87 | - |  |  | SI | participantes,totales RBC, red de apoyo, actividad... |
| Q88 | - |  |  | SI | participantes,totales RBC, cuidadores, actividades... |
| Q89 | - |  |  | SI | actividades,totales R1, profesionales de salud, ac... |
| Q90 | - |  |  | SI | actividades,totales R1, empleadores y compañeros d... |
| Q91 | - |  |  | SI | actividades,totales R1, comunidad educativa, activ... |
| Q92 | - |  |  | SI | actividades,totales R1, monitores, actividades par... |
| Q93 | - |  |  | SI | actividades,totales R1, red de apoyo, actividades ... |
| Q94 | - |  |  | SI | actividades,totales R1, cuidadores, actividades pa... |
| Q95 | - |  |  | SI | participantes,totales R1, profesionales de salud, ... |
| Q96 | - |  |  | SI | participantes,totales R1, empleadores y compañeros... |
| Q97 | - |  |  | SI | participantes,totales R1, comunidad educativa, act... |
| Q98 | - |  |  | SI | participantes,totales R1, monitores, actividades p... |
| Q99 | - |  |  | SI | participantes,totales R1, red de apoyo, actividade... |
| QHR | - |  |  | SI | Establecimiento de Salud |
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
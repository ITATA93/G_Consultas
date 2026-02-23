# SQLUser.LBC_ProtocolObservation

**Schema:** SQLUser
**Columnas:** 217
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPTO_ParRef | bigint | PK |  | NO | Parent Protocol |
| LBCPTO_CreatedDate | date |  |  | SI | Created Date |
| LBCPTO_CreatedTime | time |  |  | SI | Created Time |
| LBCPTO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPTO_Notes | varchar |  |  | SI | Notes |
| LBCPTO_Observation_DR | bigint |  | FK | SI | Lab Obserrvation |
| LBCPTO_RowID | varchar |  |  | NO | - |
| LBCPTO_Source_DR | varchar |  | FK | SI | Source Material |
| LBCPTO_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPTO_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPTO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Establecimiento de Salud (código y descripción) |
| Q02 | - |  |  | SI | código establecimiento de salud |
| Q03 | - |  |  | SI | Mes de Atención |
| Q04 | - |  |  | SI | Año de Atención |
| Q05 | - |  |  | SI | Total actividades, comunas, comunidades, eventos m... |
| Q06 | - |  |  | SI | Total actividades, espacios amigables en aps, even... |
| Q07 | - |  |  | SI | Total actividades, lugares de trabajo, eventos mas... |
| Q08 | - |  |  | SI | Total actividades, establecimientos educacion, eve... |
| Q09 | - |  |  | SI | actividad fisica, comunas, comunidades, eventos ma... |
| Q10 | - |  |  | SI | actividad fisica, espacios amigables en aps, event... |
| Q100 | - |  |  | SI | ambiente libre tabaco, establecimientos educacion,... |
| Q101 | - |  |  | SI | factores psicosociales, comunas comunidades, jorna... |
| Q102 | - |  |  | SI | factores psicosociales, espacios amigables en aps,... |
| Q103 | - |  |  | SI | factores psicosociales, lugares de trabajo, jornad... |
| Q104 | - |  |  | SI | factores psicosociales, establecimientos educacion... |
| Q105 | - |  |  | SI | factores ambientales, comunas comunidades, jornada... |
| Q106 | - |  |  | SI | factores ambientales, espacios amigables en aps, j... |
| Q107 | - |  |  | SI | factores ambientales, lugares de trabajo, jornadas... |
| Q108 | - |  |  | SI | factores ambientales, establecimientos educacion, ... |
| Q109 | - |  |  | SI | derechos humanos, comunas comunidades, jornadas y ... |
| Q11 | - |  |  | SI | actividad fisica, lugares de trabajo, eventos masi... |
| Q110 | - |  |  | SI | derechos humanos, espacios amigables en aps, jorna... |
| Q111 | - |  |  | SI | derechos humanos, lugares de trabajo, jornadas y s... |
| Q112 | - |  |  | SI | derechos humanos, establecimientos educacion, jorn... |
| Q113 | - |  |  | SI | salud sexual, comunas comunidades, jornadas y semi... |
| Q114 | - |  |  | SI | salud sexual, espacios amigables en aps, jornadas ... |
| Q115 | - |  |  | SI | salud sexual, lugares de trabajo, jornadas y semin... |
| Q116 | - |  |  | SI | salud sexual, establecimientos educacion, jornadas... |
| Q117 | - |  |  | SI | determinantes sociales, comunas comunidades, jorna... |
| Q118 | - |  |  | SI | determinantes sociales, espacios amigables en aps,... |
| Q119 | - |  |  | SI | determinantes sociales, lugares de trabajo, jornad... |
| Q12 | - |  |  | SI | actividad fisica, establecimientos educacion, even... |
| Q120 | - |  |  | SI | determinantes sociales, establecimientos educacion... |
| Q121 | - |  |  | SI | Total participantes, comunas comunidades, jornadas... |
| Q122 | - |  |  | SI | Total participantes, espacios amigables en aps, jo... |
| Q123 | - |  |  | SI | Total participantes, lugares de trabajo, jornadas ... |
| Q124 | - |  |  | SI | Total participantes, establecimientos educacion, j... |
| Q125 | - |  |  | SI | Total actividades, comunas comunidades, educacion ... |
| Q126 | - |  |  | SI | Total actividades, espacios amigables en aps, educ... |
| Q127 | - |  |  | SI | Total actividades, lugares de trabajo, educacion g... |
| Q128 | - |  |  | SI | Total actividades, establecimientos educacion, edu... |
| Q129 | - |  |  | SI | actividad fisica, comunas comunidades, educacion g... |
| Q13 | - |  |  | SI | alimentacion, comunas, comunidades, eventos masivo... |
| Q130 | - |  |  | SI | actividad fisica, espacios amigables en aps, educa... |
| Q131 | - |  |  | SI | actividad fisica, lugares de trabajo, educacion gr... |
| Q132 | - |  |  | SI | actividad fisica, establecimientos educacion, educ... |
| Q133 | - |  |  | SI | alimentacion, comunas comunidades, educacion grupa... |
| Q134 | - |  |  | SI | alimentacion, espacios amigables en aps, educacion... |
| Q135 | - |  |  | SI | alimentacion, lugares de trabajo, educacion grupal |
| Q136 | - |  |  | SI | alimentacion, establecimientos educacion, educacio... |
| Q137 | - |  |  | SI | ambiente libre tabaco, comunas comunidades, educac... |
| Q138 | - |  |  | SI | ambiente libre tabaco, espacios amigables en aps, ... |
| Q139 | - |  |  | SI | ambiente libre tabaco, lugares de trabajo, educaci... |
| Q14 | - |  |  | SI | alimentacion, espacios amigables en aps, eventos m... |
| Q140 | - |  |  | SI | ambiente libre tabaco, establecimientos educacion,... |
| Q141 | - |  |  | SI | factores psicosociales, comunas comunidades, educa... |
| Q142 | - |  |  | SI | factores psicosociales, espacios amigables en aps,... |
| Q143 | - |  |  | SI | factores psicosociales, lugares de trabajo, educac... |
| Q144 | - |  |  | SI | factores psicosociales, establecimientos educacion... |
| Q145 | - |  |  | SI | factores ambientales, comunas comunidades, educaci... |
| Q146 | - |  |  | SI | factores ambientales, espacios amigables en aps, e... |
| Q147 | - |  |  | SI | factores ambientales, lugares de trabajo, educacio... |
| Q148 | - |  |  | SI | factores ambientales, establecimientos educacion, ... |
| Q149 | - |  |  | SI | derechos humanos, comunas comunidades, educacion g... |
| Q15 | - |  |  | SI | alimentacion, lugares de trabajo, eventos masivos |
| Q150 | - |  |  | SI | derechos humanos, espacios amigables en aps, educa... |
| Q151 | - |  |  | SI | derechos humanos, lugares de trabajo, educacion gr... |
| Q152 | - |  |  | SI | derechos humanos, establecimientos educacion, educ... |
| Q153 | - |  |  | SI | salud sexual, comunas comunidades, educacion grupa... |
| Q154 | - |  |  | SI | salud sexual, espacios amigables en aps, educacion... |
| Q155 | - |  |  | SI | salud sexual, lugares de trabajo, educacion grupal |
| Q156 | - |  |  | SI | salud sexual, establecimientos educacion, educacio... |
| Q157 | - |  |  | SI | determinantes sociales, comunas comunidades, educa... |
| Q158 | - |  |  | SI | determinantes sociales, espacios amigables en aps,... |
| Q159 | - |  |  | SI | determinantes sociales, lugares de trabajo, educac... |
| Q16 | - |  |  | SI | alimentacion, establecimientos educacion, eventos ... |
| Q160 | - |  |  | SI | determinantes sociales, establecimientos educacion... |
| Q161 | - |  |  | SI | Total participantes, comunas comunidades, educacio... |
| Q162 | - |  |  | SI | Total participantes, espacios amigables en aps, ed... |
| Q163 | - |  |  | SI | Total participantes, lugares de trabajo, educacion... |
| Q164 | - |  |  | SI | Total participantes, establecimientos educacion, e... |
| Q17 | - |  |  | SI | ambiente libre tabaco, comunas comunidades, evento... |
| Q18 | - |  |  | SI | amiente libre tabaco, espacios amigables en aps, e... |
| Q19 | - |  |  | SI | ambiente libre tabaco, lugares de trabajo, eventos... |
| Q20 | - |  |  | SI | ambiente libre tabaco, establecimientos educacion,... |
| Q21 | - |  |  | SI | factores psicosociales, comunas comunidades, event... |
| Q22 | - |  |  | SI | factores psicosociales, espacios amigables en aps,... |
| Q23 | - |  |  | SI | factores psicosociales, lugares de trabajo, evento... |
| Q24 | - |  |  | SI | factores psicosociales, establecimientos educacion... |
| Q25 | - |  |  | SI | factores ambientales, comunas comunidades, eventos... |
| Q26 | - |  |  | SI | factores ambientales, espacios amigables en aps, e... |
| Q27 | - |  |  | SI | factores ambientales, lugares de trabajo, eventos ... |
| Q28 | - |  |  | SI | factores ambientales, establecimientos educacion, ... |
| Q29 | - |  |  | SI | derechos humanos, comunas comunidades, eventos mas... |
| Q30 | - |  |  | SI | derechos humanos, espacios amigables en aps, event... |
| Q31 | - |  |  | SI | derechos humanos, lugares de trabajo, eventos masi... |
| Q32 | - |  |  | SI | derechos humanos, establecimientos educacion, even... |
| Q33 | - |  |  | SI | salud sexual, comunas comunidades, eventos masivos |
| Q34 | - |  |  | SI | salud sexual, espacios amigables en aps, eventos m... |
| Q35 | - |  |  | SI | salud sexual, lugares de trabajo, eventos masivos |
| Q36 | - |  |  | SI | salud sexual, establecimientos educacion, eventos ... |
| Q37 | - |  |  | SI | determinantes sociales, comunas comunidades, event... |
| Q38 | - |  |  | SI | determinantes sociales, espacios amigables en aps,... |
| Q39 | - |  |  | SI | determinantes sociales, lugares de trabajo, evento... |
| Q40 | - |  |  | SI | determinantes sociales, establecimientos educacion... |
| Q41 | - |  |  | SI | Total participantes, comunas comunidades, eventos ... |
| Q42 | - |  |  | SI | Total participantes, espacios amigables en aps, ev... |
| Q43 | - |  |  | SI | Total participantes, lugares de trabajo, eventos m... |
| Q44 | - |  |  | SI | Total participantes, establecimientos educacion, e... |
| Q45 | - |  |  | SI | Total actividades, comunas comunidades, reuniones ... |
| Q46 | - |  |  | SI | Total actividades, espacios amigables en aps, reun... |
| Q47 | - |  |  | SI | Total actividades, lugares de trabajo, reuniones p... |
| Q48 | - |  |  | SI | Total actividades, establecimientos educacion, reu... |
| Q49 | - |  |  | SI | actividad fisica, comunas comunidades, reuniones p... |
| Q50 | - |  |  | SI | actividad fisica, espacios amigables en aps, reuni... |
| Q51 | - |  |  | SI | actividad fisica, lugares de trabajo, reuniones pl... |
| Q52 | - |  |  | SI | actividad fisica, establecimientos educacion, reun... |
| Q53 | - |  |  | SI | alimentacion, comunas comunidades, reuniones plani... |
| Q54 | - |  |  | SI | alimentacion, espacios amigables en aps, reuniones... |
| Q55 | - |  |  | SI | alimentacion, lugares de trabajo, reuniones planif... |
| Q56 | - |  |  | SI | alimentacion, establecimientos educacion, reunione... |
| Q57 | - |  |  | SI | ambiente libre tabaco, comunas comunidades, reunio... |
| Q58 | - |  |  | SI | mbiente libre tabaco, espacios amigables en aps, r... |
| Q59 | - |  |  | SI | ambiente libre tabaco, lugares de trabajo, reunion... |
| Q60 | - |  |  | SI | ambiente libre tabaco, establecimientos educacion,... |
| Q61 | - |  |  | SI | factores psicosociales, comunas comunidades, reuni... |
| Q62 | - |  |  | SI | factores psicosociales, espacios amigables en aps,... |
| Q63 | - |  |  | SI | factores psicosociales, lugares de trabajo, reunio... |
| Q64 | - |  |  | SI | factores psicosociales, establecimientos educacion... |
| Q65 | - |  |  | SI | factores ambientales, comunas comunidades, reunion... |
| Q66 | - |  |  | SI | factores ambientales, espacios amigables en aps, r... |
| Q67 | - |  |  | SI | factores ambientales, lugares de trabajo, reunione... |
| Q68 | - |  |  | SI | factores ambientales, establecimientos educacion, ... |
| Q69 | - |  |  | SI | derechos humanos, comunas comunidades, reuniones p... |
| Q70 | - |  |  | SI | derechos humanos, espacios amigables en aps, reuni... |
| Q71 | - |  |  | SI | derechos humanos, lugares de trabajo, reuniones pl... |
| Q72 | - |  |  | SI | derechos humanos, establecimientos educacion, reun... |
| Q73 | - |  |  | SI | salud sexual, comunas comunidades, reuniones plani... |
| Q74 | - |  |  | SI | salud sexual, espacios amigables en aps, reuniones... |
| Q75 | - |  |  | SI | salud sexual, lugares de trabajo, reuniones planif... |
| Q76 | - |  |  | SI | salud sexual, establecimientos educacion, reunione... |
| Q77 | - |  |  | SI | determinantes sociales, comunas comunidades, reuni... |
| Q78 | - |  |  | SI | determinantes sociales, espacios amigables en aps,... |
| Q79 | - |  |  | SI | determinantes sociales, lugares de trabajo, reunio... |
| Q80 | - |  |  | SI | determinantes sociales, establecimientos educacion... |
| Q81 | - |  |  | SI | Total participantes, comunas comunidades, reunione... |
| Q82 | - |  |  | SI | Total participantes, espacios amigables en aps, re... |
| Q83 | - |  |  | SI | Total participantes, lugares de trabajo, reuniones... |
| Q84 | - |  |  | SI | Total participantes, establecimientos educacion, r... |
| Q85 | - |  |  | SI | Total actividades, comunas comunidades, jornadas y... |
| Q86 | - |  |  | SI | Total actividades, espacios amigables en aps, jorn... |
| Q87 | - |  |  | SI | Total actividades, lugares de trabajo, jornadas y ... |
| Q88 | - |  |  | SI | Total actividades, establecimientos educacion, jor... |
| Q89 | - |  |  | SI | actividad fisica, comunas comunidades, jornadas y ... |
| Q90 | - |  |  | SI | actividad fisica, espacios amigables en aps, jorna... |
| Q91 | - |  |  | SI | actividad fisica, lugares de trabajo, jornadas y s... |
| Q92 | - |  |  | SI | actividad fisica, establecimientos educacion, jorn... |
| Q93 | - |  |  | SI | alimentacion, comunas comunidades, jornadas y semi... |
| Q94 | - |  |  | SI | alimentacion, espacios amigables en aps, jornadas ... |
| Q95 | - |  |  | SI | alimentacion, lugares de trabajo, jornadas y semin... |
| Q96 | - |  |  | SI | alimentacion, establecimientos educacion, jornadas... |
| Q97 | - |  |  | SI | ambiente libre tabaco, comunas comunidades, jornad... |
| Q98 | - |  |  | SI | ambiente libre tabaco, espacios amigables en aps, ... |
| Q99 | - |  |  | SI | ambiente libre tabaco, lugares de trabajo, jornada... |
| QHR | - |  |  | SI | Establecimiento de Salud (código y descripción) |
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
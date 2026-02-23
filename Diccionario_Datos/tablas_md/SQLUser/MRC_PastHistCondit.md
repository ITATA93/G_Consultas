# SQLUser.MRC_PastHistCondit

**Schema:** SQLUser
**Columnas:** 155
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAST_RowId | bigint | PK |  | NO | - |
| PAST_CTLOC_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| PAST_Code | varchar |  |  | NO | Code |
| PAST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAST_CreatedDate | date |  |  | SI | Created Date |
| PAST_CreatedTime | time |  |  | SI | Created Time |
| PAST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAST_Desc | varchar |  |  | NO | Description |
| PAST_Owner | varchar |  |  | SI | Owner |
| PAST_UpdatedDate | date |  |  | SI | Updated Date |
| PAST_UpdatedTime | time |  |  | SI | Updated Time |
| PAST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Causal Interv |
| Q02 | - |  |  | SI | Persona responsable paciente |
| Q03 | - |  |  | SI | Relación |
| Q04 | - |  |  | SI | Edad |
| Q05 | - |  |  | SI | Escolaridad |
| Q06 | - |  |  | SI | Actividad |
| Q07 | - |  |  | SI | Prog. |
| Q08 | - |  |  | SI | Grupo Familiar |
| Q09 | - |  |  | SI | Adultos |
| Q10 | - |  |  | SI | Niños |
| Q100 | - |  |  | SI | DATOS DE IDENTIFICACIÓN |
| Q101 | - |  |  | SI | SITUACIÓN ECONÓMICA GRUPO FAMILIAR |
| Q102 | - |  |  | SI | VIVIENDA |
| Q103 | - |  |  | SI | ELECTRICIDAD CONCET |
| Q104 | - |  |  | SI | ENERGIA PARA COCINAR |
| Q105 | - |  |  | SI | DISP.EXCRETAS |
| Q106 | - |  |  | SI | DINÁMICA FAMILIAR |
| Q107 | - |  |  | SI | RESOLUCIÓN DE CONFLICTOS |
| Q108 | - |  |  | SI | CLIMA EFECTIVO |
| Q109 | - |  |  | SI | ESTIMULACIÓN PSICOMOTORA |
| Q11 | - |  |  | SI | Nº Allegados |
| Q110 | - |  |  | SI | INTEGRACIÓN |
| Q111 | - |  |  | SI | CUMPLIMIENTO DE INDICACIONES DE SALUD |
| Q112 | - |  |  | SI | DIAGNÓSTICO SOCIAL |
| Q113 | - |  |  | SI | IDENTIFICACIÓN DEL RIESGO |
| Q12 | - |  |  | SI | Familia Nuclear |
| Q13 | - |  |  | SI | Fam. Extendida |
| Q17 | - |  |  | SI | Completa |
| Q18 | - |  |  | SI | Incompleta |
| Q19 | - |  |  | SI | J/H |
| Q20 | - |  |  | SI | RELACION CON PACIENTE |
| Q21 | - |  |  | SI | TRAB. ESTABLE |
| Q22 | - |  |  | SI | ESPORADICO |
| Q23 | - |  |  | SI | CESANTE |
| Q24 | - |  |  | SI | INACTIVO |
| Q25 | - |  |  | SI | ESTUDIANTE |
| Q26 | - |  |  | SI | S/P |
| Q27 | - |  |  | SI | INP |
| Q28 | - |  |  | SI | AFP |
| Q29 | - |  |  | SI | OTROS VIGENTES |
| Q30 | - |  |  | SI | GRUPO FONASA |
| Q31 | - |  |  | SI | ISAPRE |
| Q32 | - |  |  | SI | TCD |
| Q33 | - |  |  | SI | OTROS |
| Q34 | - |  |  | SI | INGRESO J/H |
| Q35 | - |  |  | SI | OTROS INGRESOS $ |
| Q36 | - |  |  | SI | TOTAL $ |
| Q37 | - |  |  | SI | ING P. CAP. $ |
| Q38 | - |  |  | SI | BENEF RED SOCIAL Nº |
| Q39 | - |  |  | SI | SUF |
| Q40 | - |  |  | SI | ALIM. ESC |
| Q41 | - |  |  | SI | J. INF |
| Q42 | - |  |  | SI | C.ABIER |
| Q43 | - |  |  | SI | L. ESPER |
| Q44 | - |  |  | SI | NO CORRESP |
| Q45 | - |  |  | SI | TIPO |
| Q46 | - |  |  | SI | PROPIA |
| Q47 | - |  |  | SI | ARRIENDO |
| Q48 | - |  |  | SI | ALLEGADOS |
| Q49 | - |  |  | SI | OTROS |
| Q50 | - |  |  | SI | RED |
| Q51 | - |  |  | SI | COLGADO |
| Q52 | - |  |  | SI | SUSPENDIDO |
| Q53 | - |  |  | SI | NO DISPONIBLE |
| Q54 | - |  |  | SI | GAS |
| Q55 | - |  |  | SI | PARAFINA |
| Q56 | - |  |  | SI | ELECTRICIDAD |
| Q57 | - |  |  | SI | LEÑA |
| Q58 | - |  |  | SI | OTRO |
| Q59 | - |  |  | SI | ALCANTARILLADO |
| Q60 | - |  |  | SI | FOSA SEPT |
| Q61 | - |  |  | SI | LETRINA |
| Q62 | - |  |  | SI | Nº DORMITORIOS |
| Q63 | - |  |  | SI | Nº CAMAS |
| Q64 | - |  |  | SI | Toma de Desiciones Compartida |
| Q65 | - |  |  | SI | ASUMIDA POR |
| Q66 | - |  |  | SI | Tareas Parentales Compartidas |
| Q67 | - |  |  | SI | Asumida por |
| Q68 | - |  |  | SI | Resol. Conflictos C/Dialog. |
| Q69 | - |  |  | SI | Con Agresividad |
| Q70 | - |  |  | SI | No Se Enfrentan |
| Q71 | - |  |  | SI | Clima Afectivo calido |
| Q72 | - |  |  | SI | Cilam Afectivo Frio |
| Q73 | - |  |  | SI | Indiferente |
| Q74 | - |  |  | SI | Hostil |
| Q75 | - |  |  | SI | Suficiente |
| Q76 | - |  |  | SI | Insuficiente |
| Q77 | - |  |  | SI | Deprivada |
| Q78 | - |  |  | SI | Integración Familiar |
| Q79 | - |  |  | SI | Institucional |
| Q80 | - |  |  | SI | Social |
| Q81 | - |  |  | SI | Partcicipación Comuniataria |
| Q82 | - |  |  | SI | Siempre |
| Q83 | - |  |  | SI | A veces |
| Q84 | - |  |  | SI | Nunca |
| Q85 | - |  |  | SI | Antecedentes Salud Familiar (Especificar) |
| Q86 | - |  |  | SI | ARS por si solo |
| Q87 | - |  |  | SI | Ingreso Insuficiente |
| Q88 | - |  |  | SI | Vivienda Inadecuada |
| Q89 | - |  |  | SI | Disfun. Familiar |
| Q90 | - |  |  | SI | S/ Escolar o Básica Incompleta |
| Q91 | - |  |  | SI | Jerarquización De Problemas ( Especificar) |
| Q92 | - |  |  | SI | Indicaciones De Tratamiento (Especificar) |
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
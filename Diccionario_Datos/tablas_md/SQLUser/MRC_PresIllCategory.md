# SQLUser.MRC_PresIllCategory

**Schema:** SQLUser
**Columnas:** 202
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRESIC_RowId | bigint | PK |  | NO | - |
| PRESIC_Code | varchar |  |  | NO | Code |
| PRESIC_CreatedDate | date |  |  | SI | Created Date |
| PRESIC_CreatedTime | time |  |  | SI | Created Time |
| PRESIC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRESIC_DateFrom | date |  |  | SI | Date from |
| PRESIC_DateTo | date |  |  | SI | Date To |
| PRESIC_Desc | varchar |  |  | NO | Description |
| PRESIC_UpdatedDate | date |  |  | SI | Updated Date |
| PRESIC_UpdatedTime | time |  |  | SI | Updated Time |
| PRESIC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Consulta Espontanea |
| Q02 | - |  |  | SI | Derivación desde un Estab. de APS |
| Q03 | - |  |  | SI | Derivación desde Otro centro de tratamiento de dro... |
| Q04 | - |  |  | SI | Derivación desde la Red de Servicios de  Urgencia |
| Q05 | - |  |  | SI | Derivación desde Otros estab. de la Red de Salud G... |
| Q06 | - |  |  | SI | Derivación desde un Juzgado |
| Q07 | - |  |  | SI | Derivación desde un establecimiento educacional |
| Q08 | - |  |  | SI | Voluntario |
| Q09 | - |  |  | SI | Condicionado por |
| Q10 | - |  |  | SI | Obligado por demanda judicial |
| Q100 | - |  |  | SI | Contemplación |
| Q101 | - |  |  | SI | Preparación |
| Q102 | - |  |  | SI | Acción |
| Q103 | - |  |  | SI | Mantenimiento |
| Q104 | - |  |  | SI | Recaída |
| Q105 | - |  |  | SI | Observaciones: |
| Q106 | - |  |  | SI | 6 o más meses en los últimos 3 años |
| Q107 | - |  |  | SI | 1 a 5 meses en los últimos 3 años |
| Q108 | - |  |  | SI | Ningún período de abstinencia |
| Q109 | - |  |  | SI | Observaciones: |
| Q11 | - |  |  | SI | Observaciones: |
| Q110 | - |  |  | SI | Consumo de riesgo |
| Q111 | - |  |  | SI | Consumo Perjudicial |
| Q112 | - |  |  | SI | Dependencia |
| Q113 | - |  |  | SI | Observaciones: |
| Q114 | - |  |  | SI | Leve |
| Q115 | - |  |  | SI | Moderado |
| Q116 | - |  |  | SI | Severo |
| Q117 | - |  |  | SI | Sin Compromiso |
| Q118 | - |  |  | SI | Observaciones: |
| Q119 | - |  |  | SI | Trastorno mental Orgánico |
| Q12 | - |  |  | SI | Ninguno |
| Q120 | - |  |  | SI | Trastorno esquizofrénico |
| Q121 | - |  |  | SI | Trastornos del Animo, depresivos |
| Q122 | - |  |  | SI | Trastorno del Animo, bipolar |
| Q123 | - |  |  | SI | Trastorno del Animo, otros y no especificados |
| Q124 | - |  |  | SI | Trastorno de Angustia severos |
| Q125 | - |  |  | SI | Trastornos de personalidad |
| Q126 | - |  |  | SI | Retardo Mental |
| Q127 | - |  |  | SI | Trastorno conductual y emocionales de la infancia ... |
| Q128 | - |  |  | SI | Trastorno por déficit de atención |
| Q129 | - |  |  | SI | Sin Trastorno Psiquiátrico |
| Q13 | - |  |  | SI | Lugar: |
| Q130 | - |  |  | SI | En estudio |
| Q131 | - |  |  | SI | Hepatitis alcohólica subaguda |
| Q132 | - |  |  | SI | Hepatitis crónica |
| Q133 | - |  |  | SI | Enfermedades somáticas |
| Q134 | - |  |  | SI | Hepatitis B, C, D |
| Q135 | - |  |  | SI | ETS |
| Q136 | - |  |  | SI | VIH - SIDA |
| Q137 | - |  |  | SI | Otras Enfermedades o Condiciones de Riesgo Vital |
| Q138 | - |  |  | SI | Infecciosas relacionadas con uso de sustancias |
| Q139 | - |  |  | SI | Traumatismos y secuelas secundarios |
| Q14 | - |  |  | SI | 1 o 3 |
| Q140 | - |  |  | SI | Otras enfermedades o condiciones Físicas Limitante... |
| Q141 | - |  |  | SI | En estudio |
| Q142 | - |  |  | SI | Sin Enfermedad Física Aparente |
| Q143 | - |  |  | SI | Depresión |
| Q144 | - |  |  | SI | EQZ u otra psicosis |
| Q145 | - |  |  | SI | Trastorno de alimentación |
| Q146 | - |  |  | SI | Alcoholismo |
| Q147 | - |  |  | SI | Consumo de drogas |
| Q148 | - |  |  | SI | Trastorno ansioso |
| Q149 | - |  |  | SI | Epilepsia |
| Q15 | - |  |  | SI | Duración: |
| Q150 | - |  |  | SI | Otros |
| Q151 | - |  |  | SI | Observaciones: |
| Q16 | - |  |  | SI | Más de tres |
| Q17 | - |  |  | SI | Resultados: |
| Q18 | - |  |  | SI | Observaciones: |
| Q19 | - |  |  | SI | Alcohol |
| Q20 | - |  |  | SI | Alcohol |
| Q21 | - |  |  | SI | Marihuana |
| Q22 | - |  |  | SI | Marihuana |
| Q23 | - |  |  | SI | Cocaína |
| Q24 | - |  |  | SI | Cocaína |
| Q25 | - |  |  | SI | Oral |
| Q26 | - |  |  | SI | Pasta Base |
| Q27 | - |  |  | SI | Pasta Base |
| Q28 | - |  |  | SI | Crack |
| Q29 | - |  |  | SI | Crack |
| Q30 | - |  |  | SI | Éxtasis |
| Q31 | - |  |  | SI | Éxtasis |
| Q32 | - |  |  | SI | Inhalantes |
| Q33 | - |  |  | SI | Inhalantes |
| Q34 | - |  |  | SI | LSD |
| Q35 | - |  |  | SI | LSD |
| Q36 | - |  |  | SI | Hongos |
| Q37 | - |  |  | SI | Hongos |
| Q38 | - |  |  | SI | Otros alucinógenos |
| Q39 | - |  |  | SI | Otros alucinógenos |
| Q40 | - |  |  | SI | Heroína |
| Q41 | - |  |  | SI | Heroína |
| Q42 | - |  |  | SI | Metadona |
| Q43 | - |  |  | SI | Metadona |
| Q44 | - |  |  | SI | Otros Opioides Analgesicos: Morfina, Codeína, Mepe... |
| Q45 | - |  |  | SI | Otros Opioides Analgesicos: Morfina, Codeína, Mepe... |
| Q46 | - |  |  | SI | Anfetaminas |
| Q47 | - |  |  | SI | Anfetaminas |
| Q48 | - |  |  | SI | Meta-anfetaminas |
| Q49 | - |  |  | SI | Meta-anfetaminas |
| Q50 | - |  |  | SI | Otros estimulantes |
| Q51 | - |  |  | SI | Otros estimulantes |
| Q52 | - |  |  | SI | Sedantes: Diazepam, Valium, Clonazepam, Ravotril, ... |
| Q53 | - |  |  | SI | Sedantes: Diazepam, Valium, Clonazepam, Ravotril, ... |
| Q54 | - |  |  | SI | Hipnóticos |
| Q55 | - |  |  | SI | Hipnóticos |
| Q56 | - |  |  | SI | Esteroides Anabólicos |
| Q57 | - |  |  | SI | Esteroides Anabólicos |
| Q58 | - |  |  | SI | Tabaco |
| Q59 | - |  |  | SI | Otros |
| Q60 | - |  |  | SI | Otros |
| Q61 | - |  |  | SI | Oral |
| Q62 | - |  |  | SI | Oral |
| Q63 | - |  |  | SI | Respiratoria |
| Q64 | - |  |  | SI | Respiratoria |
| Q65 | - |  |  | SI | Inyectable |
| Q66 | - |  |  | SI | Inyectable |
| Q67 | - |  |  | SI | Otras Vías |
| Q68 | - |  |  | SI | Otras Vías |
| Q69 | - |  |  | SI | <12 años |
| Q70 | - |  |  | SI | <12 años |
| Q71 | - |  |  | SI | Entre 12 y 14 años. |
| Q72 | - |  |  | SI | Entre 12 y 14 años. |
| Q73 | - |  |  | SI | 15 y mas |
| Q74 | - |  |  | SI | 15 y mas |
| Q75 | - |  |  | SI | Diaria |
| Q76 | - |  |  | SI | Diaria |
| Q77 | - |  |  | SI | Fines de semana |
| Q78 | - |  |  | SI | Tabaco |
| Q79 | - |  |  | SI | Fines de semana |
| Q80 | - |  |  | SI | Ocasional |
| Q81 | - |  |  | SI | Observaciones: |
| Q82 | - |  |  | SI | Observaciones: |
| Q83 | - |  |  | SI | Ocasional |
| Q84 | - |  |  | SI | Fisiológicas |
| Q85 | - |  |  | SI | Fisiológicas |
| Q86 | - |  |  | SI | Emocionales |
| Q87 | - |  |  | SI | Emocionales |
| Q88 | - |  |  | SI | De desempeño y adaptación |
| Q89 | - |  |  | SI | De desempeño y adaptación |
| Q90 | - |  |  | SI | Recreacional |
| Q91 | - |  |  | SI | Observaciones: |
| Q92 | - |  |  | SI | Experimental |
| Q93 | - |  |  | SI | Ocasional |
| Q94 | - |  |  | SI | Habitual |
| Q95 | - |  |  | SI | Abusivo |
| Q96 | - |  |  | SI | Dependiente |
| Q97 | - |  |  | SI | Ha sufrido intoxicación |
| Q98 | - |  |  | SI | Observaciones: |
| Q99 | - |  |  | SI | Pre - contemplación |
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
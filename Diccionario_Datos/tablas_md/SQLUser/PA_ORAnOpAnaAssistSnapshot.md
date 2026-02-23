# SQLUser.PA_ORAnOpAnaAssistSnapshot

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAANAS_ParRef | bigint | PK |  | NO | PA_ORAnaestOper Parent Reference |
| PAANAS_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| PAANAS_Childsub | double |  |  | NO | Childsub |
| PAANAS_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Pregunta Sorpresa (a/entre Profesionales) |
| Q02 | - |  |  | SI | ¿Le sorprendería que este paciente muriese a lo la... |
| Q03 | - |  |  | SI | Demanda |
| Q04 | - |  |  | SI | ¿Ha habido alguna expresión de limitación de esfue... |
| Q05 | - |  |  | SI | Indicadores Clínicos Generales de Progresión |
| Q06 | - |  |  | SI | Los últimos 6 meses |
| Q07 | - |  |  | SI | No relacionado con proceso intercurrente reciente/... |
| Q08 | - |  |  | SI | Declive nutricional |
| Q09 | - |  |  | SI | Pérdida de peso mayor a 10% |
| Q10 | - |  |  | SI | Declive funcional |
| Q11 | - |  |  | SI | Deterioro Barthel o Karnofsky mayor a 30% Pérdida ... |
| Q12 | - |  |  | SI | Dependencia Severa |
| Q13 | - |  |  | SI | Barthel menor a 20 o Karnofsky menor a 50 |
| Q14 | - |  |  | SI | Datos clínicos por anamnesis |
| Q15 | - |  |  | SI | Síndromes Geriátricos |
| Q16 | - |  |  | SI | Caídas, Úlceras por presión, Disfagia, Delirium, I... |
| Q17 | - |  |  | SI | Datos clínicos anamnesis. Dos o más síndromes geri... |
| Q18 | - |  |  | SI | Síntomas Persistentes |
| Q19 | - |  |  | SI | Dolor, debilidad, anorexia, disnea, digestivos... |
| Q20 | - |  |  | SI | Dos o más síntomas persistentes o refractarios en ... |
| Q21 | - |  |  | SI | Multimorbilidad |
| Q22 | - |  |  | SI | Cáncer, EPOC, ICC, Insuficiencia hepática, ERC, AC... |
| Q23 | - |  |  | SI | Dos o más enfermedades |
| Q24 | - |  |  | SI | Uso de Recursos |
| Q25 | - |  |  | SI | Valoración de la demanda o intensidad e intervenci... |
| Q26 | - |  |  | SI | Dos o más hospitalizaciones urgentes o no planific... |
| Q27 | - |  |  | SI | Indicadores Específicos |
| Q28 | - |  |  | SI | Severidad y/o progresión de la enfermedad |
| Q29 | - |  |  | SI | Al menos 1 enfermedad con indicador de severidad/p... |
| Q30 | - |  |  | SI | Clasificación |
| Q31 | - |  |  | SI | Pregunta Sorpresa (PS) |
| Q32 | - |  |  | SI | Parámetros NECPAL |
| Q33 | - |  |  | SI | ¿Cómo interpretar el resultado? |
| Q34 | - |  |  | SI | El instrumento es positivo, es decir, su paciente ... |
| Q35 | - |  |  | SI | Enfermedad Oncológica |
| Q36 | - |  |  | SI | Cáncer metatástico o locoregional avanzado. |
| Q37 | - |  |  | SI | En progresión (en tumores sólidos). |
| Q38 | - |  |  | SI | Síntomas persistentes mal cotrolados o refractario... |
| Q39 | - |  |  | SI | Enfermedad Pulmonar Crónica |
| Q40 | - |  |  | SI | Disnea de reposo o de mínimos esfuerzos entre exac... |
| Q41 | - |  |  | SI | Confinado a domicilio con limitación marcha. |
| Q42 | - |  |  | SI | Criterios espirométricos de obstrucción severa (VE... |
| Q43 | - |  |  | SI | Criterios gastrométricos basales de oxigenoterapia... |
| Q44 | - |  |  | SI | Necesidad corticoterapia continuada. |
| Q45 | - |  |  | SI | Insuficiencia cardíaca sintomática asociada. |
| Q46 | - |  |  | SI | Enfermedad Cardíaca Crónica |
| Q47 | - |  |  | SI | Disnea de reposo o de mínimos esfuerzos entre exac... |
| Q48 | - |  |  | SI | Insuficiencia cardiaca NYHA estadio III o IV, enfe... |
| Q49 | - |  |  | SI | Ecocardiografía basal: FE menor 30% o HTAP severa ... |
| Q50 | - |  |  | SI | Insuficiencia renal asociada (VFG menor 30l/min). |
| Q51 | - |  |  | SI | Asociación con insuficiencia renal e hiponatremia ... |
| Q52 | - |  |  | SI | Demencia |
| Q53 | - |  |  | SI | GDS mayor o igual de 6c. |
| Q54 | - |  |  | SI | Progresión declive cognitivo, funcional y/o nutric... |
| Q55 | - |  |  | SI | Fragilidad |
| Q56 | - |  |  | SI | Puntaje mayor o igual a 3 en el cuestionario FRAIL... |
| Q57 | - |  |  | SI | Evaluación geriátrica integral sugestiva de fragil... |
| Q58 | - |  |  | SI | Enfermedad Neurológica Vascular (ACV) |
| Q59 | - |  |  | SI | Durante la fase aguda y subaguda (menos de 3 meses... |
| Q60 | - |  |  | SI | Durante la fase crónica (más de 3 meses post-aCV):... |
| Q61 | - |  |  | SI | Enfermedad Neurológica Degenerativa: Esclerosis la... |
| Q62 | - |  |  | SI | Deterioro progresivo de la función física y/o cogn... |
| Q63 | - |  |  | SI | Síntomas complejos y difíciles de controlar. |
| Q64 | - |  |  | SI | Disfagia/trastorno del habla persistente. |
| Q65 | - |  |  | SI | Dificultades crecientes de comunicación. |
| Q66 | - |  |  | SI | Neumonía por aspiración recurrente, disnea o insuf... |
| Q67 | - |  |  | SI | Enfermedad Hepática Crónica |
| Q68 | - |  |  | SI | Cirrosis avanzada estadio Child C (determinado fue... |
| Q69 | - |  |  | SI | MELD-Na mayor de 30 o ascitis refractaria, síndrom... |
| Q70 | - |  |  | SI | Carcinoma hepatocelular en estadio C o D. |
| Q71 | - |  |  | SI | Enfermedad Renal Crónica |
| Q72 | - |  |  | SI | Enfermedad renal crónica etapa V (VFG menor 15) en... |
| Q73 | - |  |  | SI | Finalización diálisis o fallo trasplante. |
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
# questionnaire.QTCECLAP

**Schema:** questionnaire
**Columnas:** 173
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01CP | numeric | PK |  | SI | Consulta N° |
| Q02CP | varchar | PK |  | SI | Consulta Espontánea |
| Q03CP | varchar | PK |  | SI | Derivado |
| Q04CP | varchar | PK |  | SI | Traido |
| Q05CP | date | PK |  | SI | Fecha |
| Q07CP | varchar | PK |  | SI | Años |
| Q08CP | varchar | PK |  | SI | Meses |
| Q09CP | varchar | PK |  | SI | Estado Civil |
| Q100T | varchar | PK |  | SI | Observaciones |
| Q101VS | varchar | PK |  | SI | ACEPTACIÓN |
| Q102VS | varchar | PK |  | SI | PAREJA |
| Q103VS | numeric | PK |  | SI | EDAD DE LA PAREJA |
| Q104VS | numeric | PK |  | SI | MESES |
| Q105VS | varchar | PK |  | SI | VIOLENCIA EN LA PAREJA |
| Q106VS | varchar | PK |  | SI | AMIGOS/AS |
| Q107VS | numeric | PK |  | SI | ACTIVIDAD FÍSICA (Horas por semana) |
| Q108VS | numeric | PK |  | SI | TV (Horas por día) |
| Q109VS | numeric | PK |  | SI | COMPUTADORA (Horas por Día) |
| Q10CP | varchar | PK |  | SI | Etnia |
| Q110VS | numeric | PK |  | SI | JUEGOS Y REDES VIRTUALES (Horas por Día) |
| Q111VS | varchar | PK |  | SI | OTRAS ACTIVIDADES (Incluso Grupales) |
| Q112VS | varchar | PK |  | SI | ¿CUÁLES? |
| Q113AP | varchar | PK |  | SI | Resultado Antecedentes Personales |
| Q113VS | varchar | PK |  | SI | Observaciones |
| Q114AP | varchar | PK |  | SI | Resultado Antecedentes Familiares |
| Q115F | varchar | PK |  | SI | PAREJA |
| Q116FV | varchar | PK |  | SI | Resultado Familia y Vivienda |
| Q117E | varchar | PK |  | SI | Resultado Educación |
| Q118T | varchar | PK |  | SI | Resultado Trabajo |
| Q119 | varchar | PK |  | SI | PAREJA |
| Q119VS | varchar | PK |  | SI | Resultado Vida Social |
| Q11CP | varchar | PK |  | SI | Acompañante |
| Q120 | numeric | PK |  | SI | Años en el mayor nivel |
| Q120TFC | varchar | PK |  | SI | Total de Alertas |
| Q121 | varchar | PK |  | SI | Ocupación Pareja |
| Q124X | varchar | PK |  | SI | Resultado Antecedentes Personales 2 |
| Q125X | varchar | PK |  | SI | Resultado Antecedentes Familiares 2 |
| Q126X | varchar | PK |  | SI | Resultado Familia y Vivienda 2  |
| Q127X | varchar | PK |  | SI | Resultado Educación 2  |
| Q128X | varchar | PK |  | SI | Resultado Trabajo 2  |
| Q129X | varchar | PK |  | SI | Resultado Vida Social 2 |
| Q131AP | varchar | PK |  | SI | Peso al Nacer |
| Q132AP | varchar | PK |  | SI | Cual Migrante |
| Q133AP | varchar | PK |  | SI | Otras Etnias |
| Q134E | numeric | PK |  | SI | Código Violencia Escolar |
| Q135E | varchar | PK |  | SI | PAREJA (Nivel de Instrucción) |
| Q136E | numeric | PK |  | SI | AÑOS REPETIDOS |
| Q13CP | varchar | PK |  | SI | Descripción de Motivo de la Consulta |
| Q14AP | varchar | PK |  | SI | Accidentes |
| Q15AP | varchar | PK |  | SI | Llamativamente Frecuentes |
| Q16AP | varchar | PK |  | SI | PERINATALES Normales |
| Q17AP | varchar | PK |  | SI | CRECIMIENTO Normal |
| Q18AP | varchar | PK |  | SI | DESARROLLO Normal |
| Q19AP | varchar | PK |  | SI | ALERGIA |
| Q20AP | varchar | PK |  | SI | VACUNAS COMPLETAS |
| Q21AP | varchar | PK |  | SI | ENFERMEDADES CRÓNICAS |
| Q22AP | varchar | PK |  | SI | DISCAPACIDAD |
| Q23AP | varchar | PK |  | SI | ENFERMEDADES INFECTO CONTAGIOSAS |
| Q24AP | varchar | PK |  | SI | INTOXICACIONES |
| Q25AP | varchar | PK |  | SI | CIRUGÍA HOSPITALIZAC. |
| Q26AP | varchar | PK |  | SI | USO DE MEDICAMENTOS |
| Q27AP | varchar | PK |  | SI | PROBLEMAS PSICOLÓGICOS |
| Q28AP | varchar | PK |  | SI | VIOLENCIA |
| Q29AP | numeric | PK |  | SI | Código |
| Q30AP | varchar | PK |  | SI | EDUCACIÓN PREESCOLAR |
| Q31AP | varchar | PK |  | SI | JUDICIALES |
| Q32AP | varchar | PK |  | SI | OTROS |
| Q33AP | varchar | PK |  | SI | Observaciones |
| Q34AF | varchar | PK |  | SI | DIABETES |
| Q35AF | varchar | PK |  | SI | OBESIDAD |
| Q36AF | varchar | PK |  | SI | CARDIOVASC.(HTA,cardiopatía,etc) |
| Q37AF | varchar | PK |  | SI | ALERGIA |
| Q38AF | varchar | PK |  | SI | INFECCIONES |
| Q39AF | varchar | PK |  | SI | CÁNCER |
| Q40AF | varchar | PK |  | SI | PROBLEMAS PSICOLÓGICOS |
| Q41AF | varchar | PK |  | SI | ALCOHOL, DROGAS Y OTROS |
| Q42AF | varchar | PK |  | SI | VIOLENCIA INTRAFAMILIAR |
| Q43AF | varchar | PK |  | SI | MADRE Y/O PADRE ADOLESCENTE |
| Q44AF | varchar | PK |  | SI | JUDICIALES |
| Q45AF | varchar | PK |  | SI | OTROS |
| Q46AF | varchar | PK |  | SI | Observaciones |
| Q47F | varchar | PK |  | SI | SOLO |
| Q48F | varchar | PK |  | SI | EN LA CASA |
| Q49F | varchar | PK |  | SI | EN LA CALLE |
| Q50F | varchar | PK |  | SI | EN INST. PROTECTORA |
| Q51F | varchar | PK |  | SI | PRIVADO DE LIBERTAD |
| Q52F | varchar | PK |  | SI | MADRE |
| Q53F | varchar | PK |  | SI | PADRE |
| Q54F | varchar | PK |  | SI | MADRASTRA |
| Q55F | varchar | PK |  | SI | PADRASTRO |
| Q56F | varchar | PK |  | SI | HERMANOS |
| Q57F | varchar | PK |  | SI | PAREJA |
| Q58F | varchar | PK |  | SI | HIJO |
| Q59F | varchar | PK |  | SI | OTROS |
| Q60F | varchar | PK |  | SI | PADRE O SUSTITUTO |
| Q61F | numeric | PK |  | SI | AÑOS EN EL MAYOR NIVEL |
| Q62F | varchar | PK |  | SI | MADRE O SUSTITUTO |
| Q63F | numeric | PK |  | SI | AÑOS EN EL MAYOR NIVEL |
| Q64FT | varchar | PK |  | SI | PADRE O SUSTITUTO |
| Q65FT | varchar | PK |  | SI | MADRE O SUSTITUTO |
| Q66FT | varchar | PK |  | SI | PAREJA |
| Q67FT | varchar | PK |  | SI | OCUPACIÓN PAREJA |
| Q68FT | varchar | PK |  | SI | OCUPACIÓN PADRES |
| Q69FT | varchar | PK |  | SI | APOYO SOCIAL O SUBSIDIO |
| Q70FT | varchar | PK |  | SI | PERCEPCIÓN DEL ADOLESCENTE SOBRE SU FAMILIA |
| Q71V | varchar | PK |  | SI | ENERGÍA ELECTRICA |
| Q72V | varchar | PK |  | SI | AGUA |
| Q73V | varchar | PK |  | SI | EXCRETAS |
| Q74V | varchar | PK |  | SI | HACINAMIENTO |
| Q75V | varchar | PK |  | SI | OBSERVACIONES |
| Q76E | varchar | PK |  | SI | ESTUDIA |
| Q77E | varchar | PK |  | SI | CENTRO AL QUE CONCURRE |
| Q78E | varchar | PK |  | SI | NIVEL |
| Q79E | numeric | PK |  | SI | GRADO CURSO |
| Q80E | numeric | PK |  | SI | AÑOS APROBADOS |
| Q81E | varchar | PK |  | SI | PROBLEMAS EN LA ESCUELA |
| Q82E | numeric | PK |  | SI | AÑOS REPETIDOS (ANTIGUO) |
| Q83E | varchar | PK |  | SI | CAUSA |
| Q84E | varchar | PK |  | SI | VIOLENCIA ESCOLAR |
| Q85E | varchar | PK |  | SI | DESERCIÓN/EXCLUSIÓN |
| Q86E | varchar | PK |  | SI | CAUSA |
| Q87E | varchar | PK |  | SI | EDUCACIÓN NO FORMAL |
| Q88E | varchar | PK |  | SI | ¿Cuál? |
| Q89E | varchar | PK |  | SI | Observaciones |
| Q90T | varchar | PK |  | SI | ACTIVIDAD |
| Q91T | numeric | PK |  | SI | EDAD INICIO TRABAJO |
| Q92T | numeric | PK |  | SI | TRABAJO (Horas por semana) |
| Q93T | varchar | PK |  | SI | TRABAJO INFANTIL |
| Q94T | varchar | PK |  | SI | TRABAJO JUVENIL |
| Q95T | varchar | PK |  | SI | HORARIO DE TRABAJO |
| Q96T | varchar | PK |  | SI | RAZÓN DE TRABAJO |
| Q97T | varchar | PK |  | SI | TRABAJO LEGALIZADO |
| Q98T | varchar | PK |  | SI | TRABAJO INSALUBRE |
| Q99T | varchar | PK |  | SI | TIPO DE TRABAJO |
| QE130 | varchar | PK |  | SI | Establecimiento |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
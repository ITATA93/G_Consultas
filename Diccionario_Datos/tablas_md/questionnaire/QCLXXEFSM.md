# questionnaire.QCLXXEFSM

**Schema:** questionnaire
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date | PK |  | SI | Fecha de Ingreso a la Unidad |
| Q02 | time | PK |  | SI | Hora de Ingreso a la Unidad |
| Q03 | date | PK |  | SI | Fecha de realización del Ingreso |
| Q04 | time | PK |  | SI | Hora de realización del Ingreso |
| Q05 | varchar | PK |  | SI | Tipo de Ingreso |
| Q06 | varchar | PK |  | SI | Otro tipo de ingreso |
| Q07 | varchar | PK |  | SI | Derivado desde |
| Q08 | varchar | PK |  | SI | Establecimiento |
| Q09 | varchar | PK |  | SI | Motivo de Ingreso |
| Q09a | varchar | PK |  | SI | Motivo de Consulta |
| Q10 | varchar | PK |  | SI | Anamnesis Próxima |
| Q11a | varchar | PK |  | SI | Patrón de Consumo (Texto Libre) |
| Q12 | bit | PK |  | SI | Sin historia de consumo de drogas. |
| Q13a | varchar | PK |  | SI | Conductas Desadaptativas e Infracciones a la ley. ... |
| Q14 | bit | PK |  | SI | Sin antecedente de conductas desadaptativas o infr... |
| Q15 | varchar | PK |  | SI | Antecedentes perinatales  |
| Q15a | varchar | PK |  | SI | Lactancia Materna |
| Q16 | bit | PK |  | SI | Sin antecedentes perinatales de importancia. |
| Q17 | bit | PK |  | SI | Lactancia materna hasta por lo menos los seis prim... |
| Q18 | bit | PK |  | SI | No recibe lactancia materna. |
| Q19 | varchar | PK |  | SI | Temperamento |
| Q21 | bit | PK |  | SI | Desarrollo psicomotor adecuado para la edad |
| Q22 | varchar | PK |  | SI | Apego y personas significativas durante la crianza |
| Q23 | varchar | PK |  | SI | Educación pre-escolar y escolar |
| Q24 | varchar | PK |  | SI | Otros Antecedentes y Observaciones. |
| Q25 | varchar | PK |  | SI | PAS |
| Q25ObsDR | varchar | PK | FK | SI | PAS DR |
| Q26 | varchar | PK |  | SI | PAD |
| Q26ObsDR | varchar | PK | FK | SI | PAD DR |
| Q27 | varchar | PK |  | SI | Frecuencia Cardíaca (lpm) |
| Q27ObsDR | varchar | PK | FK | SI | Frecuencia Cardíaca (lpm) DR |
| Q28 | varchar | PK |  | SI | Frecuencia respiratoria (prm) |
| Q28ObsDR | varchar | PK | FK | SI | Frecuencia respiratoria (prm) DR |
| Q29 | varchar | PK |  | SI | Saturación O2 (%) |
| Q29ObsDR | varchar | PK | FK | SI | Saturación O2 (%) DR |
| Q30 | varchar | PK |  | SI | Examen físico (Campo de texto) |
| Q31 | varchar | PK |  | SI | Posición y Decúbito |
| Q32 | bit | PK |  | SI | Posición activa, indiferente.  |
| Q33 | varchar | PK |  | SI | Marcha |
| Q34 | bit | PK |  | SI | Deambulación normal |
| Q35 | varchar | PK |  | SI | Facie |
| Q36 | bit | PK |  | SI | Facie no característica |
| Q37 | varchar | PK |  | SI | Grado de Conciencia |
| Q38 | varchar | PK |  | SI | Grado de conciencia (otro) |
| Q40 | varchar | PK |  | SI | Percepción |
| Q41 | varchar | PK |  | SI | Memoria de corto plazo |
| Q42 | varchar | PK |  | SI | Memoria de largo plazo |
| Q43 | varchar | PK |  | SI | Inteligencia abstracta |
| Q44 | varchar | PK |  | SI | Inteligencia concreta |
| Q45 | varchar | PK |  | SI | Otros (conciencia y estado psíquico) |
| Q46 | bit | PK |  | SI | Paciente vigil, lúcido y cooperador. Conciencia al... |
| Q47 | bit | PK |  | SI | Orientado en tiempo, espacio y persona. |
| Q48 | bit | PK |  | SI | Percepción normal. |
| Q49 | bit | PK |  | SI | Memoria normal, de corto y largo plazo. |
| Q50 | bit | PK |  | SI | Inteligencia abstracta y concreta adecuadas. |
| Q51 | varchar | PK |  | SI | Constitución |
| Q52 | varchar | PK |  | SI | Estado nutricional |
| Q53 | varchar | PK |  | SI | Peso (kgs.) |
| Q53ObsDR | varchar | PK | FK | SI | Peso (kgs.) DR |
| Q54 | varchar | PK |  | SI | Talla (cms.) |
| Q54ObsDR | varchar | PK | FK | SI | Talla (cms.) DR |
| Q56 | varchar | PK |  | SI | Fanéreos (Cabello y uñas) |
| Q57 | bit | PK |  | SI | Piel de turgor, elasticidad e hidratación normal. |
| Q58 | bit | PK |  | SI | Sin lesiones cutáneas. |
| Q59 | bit | PK |  | SI | Fanéreos sin alteraciones. |
| Q60 | varchar | PK |  | SI | Sistema linfático |
| Q61 | bit | PK |  | SI | Sin adenopatías al examen físico. |
| Q62 | varchar | PK |  | SI | Cabeza y cuello |
| Q63 | bit | PK |  | SI | Cabeza sin alteraciones a la examinación. |
| Q64 | bit | PK |  | SI | Cuello de movilidad normal, sin elementos patológi... |
| Q65 | bit | PK |  | SI | Pulsos carotídeos de amplitud normal, simétricos. ... |
| Q66 | varchar | PK |  | SI | Cardiopulmonar |
| Q67 | bit | PK |  | SI | Cardíaco: Ritmo regular en dos tiempos, sin soplos... |
| Q68 | bit | PK |  | SI | Pulmonar: Murmullo pulmonar presente, simétrico. S... |
| Q69 | varchar | PK |  | SI | Abdomen |
| Q70 | bit | PK |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidor... |
| Q71 | varchar | PK |  | SI | Extremidades |
| Q72 | bit | PK |  | SI | Extremidades de fuerza, tono y movilidad conservad... |
| Q73 | bit | PK |  | SI | Pulsos de amplitud normal, simétricos. |
| Q74 | varchar | PK |  | SI | Examen Neurológico (Texto libre) |
| Q76 | bit | PK |  | SI | Examen neurológico normal, sin hallazgos. |
| Q77 | varchar | PK |  | SI | Examen Mental (texto libre) |
| Q84 | bigint | PK |  | SI | Imágenes digitales: Genograma |
| Q84TxtOnly | bigint | PK |  | SI | Imágenes digitales: Genograma Plain Text Only |
| Q85 | varchar | PK |  | SI | Abordaje familiar y Estrategias de Afrontamiento |
| Q87a | varchar | PK |  | SI | Hipótesis Diagnóstica. (Texto Libre) |
| Q88 | varchar | PK |  | SI | Plan de Intervención / Tratamiento al Ingreso |
| Q89 | varchar | PK |  | SI | Profesional de Salud |
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
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
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
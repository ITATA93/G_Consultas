# questionnaire.QTCEINGSMEN

> Ingreso Médico Salud Mental

**Schema:** questionnaire
**Columnas:** 134
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Médico Salud Mental

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Ingreso a la Unidad |
| Q02 | time |  |  | SI | Hora de Ingreso a la Unidad |
| Q03 | date |  |  | SI | Fecha de realización del Ingreso |
| Q04 | time |  |  | SI | Hora de realización del Ingreso |
| Q05 | varchar |  |  | SI | Tipo de Ingreso |
| Q06 | varchar |  |  | SI | Otro tipo de ingreso |
| Q07 | varchar |  |  | SI | Derivado desde |
| Q08 | varchar |  |  | SI | Establecimiento |
| Q09 | varchar |  |  | SI | Motivo de Ingreso |
| Q09a | varchar |  |  | SI | Motivo de Consulta |
| Q10 | varchar |  |  | SI | Anamnesis Próxima |
| Q11a | varchar |  |  | SI | Patrón de Consumo (Texto Libre) |
| Q12 | bit |  |  | SI | Sin historia de consumo de drogas. |
| Q13a | varchar |  |  | SI | Conductas Desadaptativas e Infracciones a la ley. ... |
| Q14 | bit |  |  | SI | Sin antecedente de conductas desadaptativas o infr... |
| Q15 | varchar |  |  | SI | Antecedentes perinatales  |
| Q15a | varchar |  |  | SI | Lactancia Materna |
| Q16 | bit |  |  | SI | Sin antecedentes perinatales de importancia. |
| Q17 | bit |  |  | SI | Lactancia materna hasta por lo menos los seis prim... |
| Q18 | bit |  |  | SI | No recibe lactancia materna. |
| Q19 | varchar |  |  | SI | Temperamento |
| Q21 | bit |  |  | SI | Desarrollo psicomotor adecuado para la edad |
| Q22 | varchar |  |  | SI | Apego y personas significativas durante la crianza |
| Q23 | varchar |  |  | SI | Educación pre-escolar y escolar |
| Q24 | varchar |  |  | SI | Otros Antecedentes y Observaciones. |
| Q25 | varchar |  |  | SI | PAS |
| Q25ObsDR | varchar |  | FK | SI | PAS DR |
| Q26 | varchar |  |  | SI | PAD |
| Q26ObsDR | varchar |  | FK | SI | PAD DR |
| Q27 | varchar |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q27ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca (lpm) DR |
| Q28 | varchar |  |  | SI | Frecuencia respiratoria (prm) |
| Q28ObsDR | varchar |  | FK | SI | Frecuencia respiratoria (prm) DR |
| Q29 | varchar |  |  | SI | Saturación O2 (%) |
| Q29ObsDR | varchar |  | FK | SI | Saturación O2 (%) DR |
| Q30 | varchar |  |  | SI | Examen físico (Campo de texto) |
| Q31 | varchar |  |  | SI | Posición y Decúbito |
| Q32 | bit |  |  | SI | Posición activa, indiferente.  |
| Q33 | varchar |  |  | SI | Marcha |
| Q34 | bit |  |  | SI | Deambulación normal |
| Q35 | varchar |  |  | SI | Facie |
| Q36 | bit |  |  | SI | Facie no característica |
| Q37 | varchar |  |  | SI | Grado de Conciencia |
| Q38 | varchar |  |  | SI | Grado de conciencia (otro) |
| Q40 | varchar |  |  | SI | Percepción |
| Q41 | varchar |  |  | SI | Memoria de corto plazo |
| Q42 | varchar |  |  | SI | Memoria de largo plazo |
| Q43 | varchar |  |  | SI | Inteligencia abstracta |
| Q44 | varchar |  |  | SI | Inteligencia concreta |
| Q45 | varchar |  |  | SI | Otros (conciencia y estado psíquico) |
| Q46 | bit |  |  | SI | Paciente vigil, lúcido y cooperador. Conciencia al... |
| Q47 | bit |  |  | SI | Orientado en tiempo, espacio y persona. |
| Q48 | bit |  |  | SI | Percepción normal. |
| Q49 | bit |  |  | SI | Memoria normal, de corto y largo plazo. |
| Q50 | bit |  |  | SI | Inteligencia abstracta y concreta adecuadas. |
| Q51 | varchar |  |  | SI | Constitución |
| Q52 | varchar |  |  | SI | Estado nutricional |
| Q53 | varchar |  |  | SI | Peso (kgs.) |
| Q53ObsDR | varchar |  | FK | SI | Peso (kgs.) DR |
| Q54 | varchar |  |  | SI | Talla (cms.) |
| Q54ObsDR | varchar |  | FK | SI | Talla (cms.) DR |
| Q56 | varchar |  |  | SI | Fanéreos (Cabello y uñas) |
| Q57 | bit |  |  | SI | Piel de turgor, elasticidad e hidratación normal. |
| Q58 | bit |  |  | SI | Sin lesiones cutáneas. |
| Q59 | bit |  |  | SI | Fanéreos sin alteraciones. |
| Q60 | varchar |  |  | SI | Sistema linfático |
| Q61 | bit |  |  | SI | Sin adenopatías al examen físico. |
| Q62 | varchar |  |  | SI | Cabeza y cuello |
| Q63 | bit |  |  | SI | Cabeza sin alteraciones a la examinación. |
| Q64 | bit |  |  | SI | Cuello de movilidad normal, sin elementos patológi... |
| Q65 | bit |  |  | SI | Pulsos carotídeos de amplitud normal, simétricos. ... |
| Q66 | varchar |  |  | SI | Cardiopulmonar |
| Q67 | bit |  |  | SI | Cardíaco: Ritmo regular en dos tiempos, sin soplos... |
| Q68 | bit |  |  | SI | Pulmonar: Murmullo pulmonar presente, simétrico. S... |
| Q69 | varchar |  |  | SI | Abdomen |
| Q70 | bit |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidor... |
| Q71 | varchar |  |  | SI | Extremidades |
| Q72 | bit |  |  | SI | Extremidades de fuerza, tono y movilidad conservad... |
| Q73 | bit |  |  | SI | Pulsos de amplitud normal, simétricos. |
| Q74 | varchar |  |  | SI | Examen Neurológico (Texto libre) |
| Q76 | bit |  |  | SI | Examen neurológico normal, sin hallazgos. |
| Q77 | varchar |  |  | SI | Examen Mental (texto libre) |
| Q84 | bigint |  |  | SI | Imágenes digitales: Genograma |
| Q84TxtOnly | bigint |  |  | SI | Imágenes digitales: Genograma Plain Text Only |
| Q85 | varchar |  |  | SI | Abordaje familiar y Estrategias de Afrontamiento |
| Q87a | varchar |  |  | SI | Hipótesis Diagnóstica. (Texto Libre) |
| Q88 | varchar |  |  | SI | Plan de Intervención / Tratamiento al Ingreso |
| Q89 | varchar |  |  | SI | Profesional de Salud |
| Q95 | varchar |  |  | SI | HISTORIA DEL DESARROLLO |
| Q96 | varchar |  |  | SI | Antecedentes Clínicos |
| Q97 | varchar |  |  | SI | EXAMEN  FISICO |
| Q98 | varchar |  |  | SI | EXAMEN FISICO SEGMENTARIO |
| Q99 | varchar |  |  | SI | Carácter del ingreso |
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
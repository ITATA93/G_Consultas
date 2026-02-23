# SQLUser.ARC_InsTypeMultiplier

**Schema:** SQLUser
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MULT_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ11DR | - |  |  | SI | Child Reference: Patrón de consumo |
| MULT_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| MULT_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| MULT_Childsub | double |  |  | NO | Childsub |
| MULT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MULT_CreatedDate | date |  |  | SI | Created Date |
| MULT_CreatedTime | time |  |  | SI | Created Time |
| MULT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MULT_DateFrom | date |  |  | SI | Date From |
| MULT_DateTo | date |  |  | SI | Date To |
| MULT_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| MULT_EpisodeType | varchar |  |  | SI | EpisodeType |
| MULT_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| MULT_ItmMast_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| MULT_Multiplier | double |  |  | SI | Multiplier |
| MULT_Rank | double |  |  | SI | Rank |
| MULT_RowId | varchar |  |  | NO | - |
| MULT_ServCat_DR | bigint |  | FK | SI | Des Ref ARCServCat |
| MULT_UpdatedDate | date |  |  | SI | Updated Date |
| MULT_UpdatedTime | time |  |  | SI | Updated Time |
| MULT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q11a | - |  |  | SI | Patrón de Consumo |
| Q12 | - |  |  | SI | Sin historia de consumo de drogas. |
| Q13a | - |  |  | SI | Conductas Desadaptativas e Infracciones a la ley |
| Q14 | - |  |  | SI | Sin antecedente de conductas desadaptativas o infr... |
| Q15 | - |  |  | SI | Antecedentes perinatales |
| Q15a | - |  |  | SI | Lactancia Materna |
| Q16 | - |  |  | SI | Sin antecedentes perinatales de importancia. |
| Q17 | - |  |  | SI | Lactancia materna hasta por lo menos los seis prim... |
| Q18 | - |  |  | SI | No recibe lactancia materna. |
| Q19 | - |  |  | SI | Temperamento |
| Q21 | - |  |  | SI | Desarrollo psicomotor adecuado para la edad |
| Q22 | - |  |  | SI | Apego y personas significativas durante la crianza |
| Q23 | - |  |  | SI | Educación pre-escolar y escolar |
| Q24 | - |  |  | SI | Otros Antecedentes y Observaciones. |
| Q25 | - |  |  | SI | PAS |
| Q25ObsDR | - |  |  | SI | PAS DR |
| Q26 | - |  |  | SI | PAD |
| Q26ObsDR | - |  |  | SI | PAD DR |
| Q27 | - |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q27ObsDR | - |  |  | SI | Frecuencia Cardíaca (lpm) DR |
| Q28 | - |  |  | SI | Frecuencia respiratoria (prm) |
| Q28ObsDR | - |  |  | SI | Frecuencia respiratoria (prm) DR |
| Q29 | - |  |  | SI | Saturación O2 (%) |
| Q29ObsDR | - |  |  | SI | Saturación O2 (%) DR |
| Q30 | - |  |  | SI | Examen físico |
| Q31 | - |  |  | SI | Posición y Decúbito |
| Q32 | - |  |  | SI | Posición activa, indiferente. |
| Q33 | - |  |  | SI | Marcha |
| Q34 | - |  |  | SI | Deambulación normal |
| Q35 | - |  |  | SI | Facie |
| Q36 | - |  |  | SI | Facie no característica |
| Q37 | - |  |  | SI | Grado de Conciencia |
| Q38 | - |  |  | SI | Grado de conciencia (otro) |
| Q40 | - |  |  | SI | Percepción |
| Q41 | - |  |  | SI | Memoria de corto plazo |
| Q42 | - |  |  | SI | Memoria de largo plazo |
| Q43 | - |  |  | SI | Inteligencia abstracta |
| Q44 | - |  |  | SI | Inteligencia concreta |
| Q45 | - |  |  | SI | Otros (conciencia y estado psíquico) |
| Q46 | - |  |  | SI | Paciente vigil, lúcido y cooperador. Conciencia al... |
| Q47 | - |  |  | SI | Orientado en tiempo, espacio y persona. |
| Q48 | - |  |  | SI | Percepción normal. |
| Q49 | - |  |  | SI | Memoria normal, de corto y largo plazo. |
| Q50 | - |  |  | SI | Inteligencia abstracta y concreta adecuadas. |
| Q51 | - |  |  | SI | Constitución |
| Q52 | - |  |  | SI | Estado nutricional |
| Q53 | - |  |  | SI | Peso (kgs.) |
| Q53ObsDR | - |  |  | SI | Peso (kgs.) DR |
| Q54 | - |  |  | SI | Talla (cms.) |
| Q54ObsDR | - |  |  | SI | Talla (cms.) DR |
| Q56 | - |  |  | SI | Fanéreos (Cabello y uñas) |
| Q57 | - |  |  | SI | Piel de turgor, elasticidad e hidratación normal. |
| Q58 | - |  |  | SI | Sin lesiones cutáneas. |
| Q59 | - |  |  | SI | Fanéreos sin alteraciones. |
| Q60 | - |  |  | SI | Sistema linfático |
| Q61 | - |  |  | SI | Sin adenopatías al examen físico. |
| Q62 | - |  |  | SI | Cabeza y cuello |
| Q63 | - |  |  | SI | Cabeza sin alteraciones a la examinación. |
| Q64 | - |  |  | SI | Cuello de movilidad normal, sin elementos patológi... |
| Q65 | - |  |  | SI | Pulsos carotídeos de amplitud normal, simétricos. ... |
| Q66 | - |  |  | SI | Cardiopulmonar |
| Q67 | - |  |  | SI | Cardíaco: Ritmo regular en dos tiempos, sin soplos... |
| Q68 | - |  |  | SI | Pulmonar: Murmullo pulmonar presente, simétrico. S... |
| Q69 | - |  |  | SI | Abdomen |
| Q70 | - |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidor... |
| Q71 | - |  |  | SI | Extremidades |
| Q72 | - |  |  | SI | Extremidades de fuerza, tono y movilidad conservad... |
| Q73 | - |  |  | SI | Pulsos de amplitud normal, simétricos. |
| Q74 | - |  |  | SI | Examen Neurológico |
| Q76 | - |  |  | SI | Examen neurológico normal, sin hallazgos. |
| Q77 | - |  |  | SI | Examen Mental |
| Q85 | - |  |  | SI | Abordaje familiar y Estrategias de Afrontamiento |
| Q89 | - |  |  | SI | Profesional de Salud |
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
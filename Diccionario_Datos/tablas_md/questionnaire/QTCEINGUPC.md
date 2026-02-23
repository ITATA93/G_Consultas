# questionnaire.QTCEINGUPC

> INGRESO UNIDAD DE PACIENTE CRÍTICO

**Schema:** questionnaire
**Columnas:** 142
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* INGRESO UNIDAD DE PACIENTE CRÍTICO

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Ingreso |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Información Entregada por |
| Q04 | varchar |  |  | SI | Procedencia |
| Q05 | varchar |  |  | SI | Procedencia |
| Q06 | varchar |  |  | SI | Nombre del Contacto |
| Q07 | varchar |  |  | SI | Fono de Contacto |
| Q08 | varchar |  |  | SI | Profesión o Actividad del Paciente |
| Q09 | varchar |  |  | SI | Anamnesis Próxima |
| Q10 | varchar |  |  | SI | Capacidad Funcional |
| Q11 | varchar |  |  | SI | Hábitos |
| Q12 | varchar |  |  | SI | Respiratorio |
| Q13 | varchar |  |  | SI | Cardiovascular |
| Q14 | varchar |  |  | SI | Digestivo |
| Q15 | varchar |  |  | SI | Enfermedades Infecciosas |
| Q16 | varchar |  |  | SI | Diabetes |
| Q17 | varchar |  |  | SI | Endocrinologia y Nutrición |
| Q18 | varchar |  |  | SI | Cabeza y Cuello |
| Q19 | varchar |  |  | SI | Reumatología |
| Q20 | varchar |  |  | SI | Neurología |
| Q21 | varchar |  |  | SI | Psiquiatría |
| Q22 | varchar |  |  | SI | Genitourinario |
| Q23 | varchar |  |  | SI | Oncología/Hematología |
| Q24 | varchar |  |  | SI | Medicamentos de Uso Reciente |
| Q25 | varchar |  |  | SI | Otros - Informaciones complementarias |
| Q26 | varchar |  |  | SI | Estado de conciencia |
| Q27 | bit |  |  | SI | Paciente conciente, lúcido y orientado en tiempo y... |
| Q28 | varchar |  |  | SI | Facie |
| Q29 | bit |  |  | SI | Facie no característica |
| Q30 | varchar |  |  | SI | Posición y Marcha |
| Q31 | bit |  |  | SI | Posición en cama activa |
| Q32 | bit |  |  | SI | Posición de pie: Postura recta, firme y sin oscila... |
| Q33 | varchar |  |  | SI | Piel |
| Q34 | varchar |  |  | SI | Piel |
| Q35 | bit |  |  | SI | Rosada, sin ictericia o cianosis de extremidades. |
| Q36 | varchar |  |  | SI | Respiración |
| Q37 | varchar |  |  | SI | Respiración |
| Q38 | bit |  |  | SI | Paciente eupnéico, respiración tranquila |
| Q39 | varchar |  |  | SI | P. Arterial Sistólica (mmHg) |
| Q39ObsDR | varchar |  | FK | SI | P. Arterial Sistólica (mmHg) DR |
| Q40 | varchar |  |  | SI | P. Arterial Diastólica (mmHg) |
| Q40ObsDR | varchar |  | FK | SI | P. Arterial Diastólica (mmHg) DR |
| Q41 | varchar |  |  | SI | Temperatura Axilar |
| Q41ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q42 | varchar |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q42ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca (lpm) DR |
| Q43 | varchar |  |  | SI | Frecuencia Respiratoria (rpm) |
| Q43ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria (rpm) DR |
| Q44 | varchar |  |  | SI | Saturación O2 (%) |
| Q44ObsDR | varchar |  | FK | SI | Saturación O2 (%) DR |
| Q45 | varchar |  |  | SI | FiO2 (%) |
| Q45ObsDR | varchar |  | FK | SI | FiO2 (%) DR |
| Q46 | varchar |  |  | SI | Escala de Dolor (EVA) |
| Q46ObsDR | varchar |  | FK | SI | Escala de Dolor (EVA) DR |
| Q47 | varchar |  |  | SI | Peso (Kg.) |
| Q47ObsDR | varchar |  | FK | SI | Peso (Kg.) DR |
| Q48 | varchar |  |  | SI | Talla |
| Q48ObsDR | varchar |  | FK | SI | Talla DR |
| Q49 | varchar |  |  | SI | Descripción Examen Físico |
| Q50 | varchar |  |  | SI | Orofaringe |
| Q51 | varchar |  |  | SI | Dientes |
| Q52 | varchar |  |  | SI | Cuello |
| Q53 | bit |  |  | SI | Cabeza normal. Ojos, oídos y orofaringe sin hallaz... |
| Q54 | bit |  |  | SI | Tiroides normal. Carótidas sin soplos, pulsos norm... |
| Q55 | varchar |  |  | SI | Tórax |
| Q56 | bit |  |  | SI | Tórax simétrico, sin deformaciones o lesiones |
| Q57 | bit |  |  | SI | Mamas: Tejido glandular, piel, pezón y areola sin ... |
| Q59 | varchar |  |  | SI | Pulmonar |
| Q60 | bit |  |  | SI | Pulmonar: Murmullo pulmonar simétrico, normal, sin... |
| Q62 | varchar |  |  | SI | Cardiaco |
| Q63 | bit |  |  | SI | Cardiaco: Ritmo regular en dos tiempos. No se ausc... |
| Q65 | varchar |  |  | SI | Abdomen |
| Q66 | bit |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q67 | varchar |  |  | SI | Región anogenital |
| Q68 | bit |  |  | SI | Pene y escroto sin lesiones. Testículos de forma y... |
| Q69 | bit |  |  | SI | Vulva sin hallazgos patológicos. Flujo ausente. |
| Q70 | bit |  |  | SI | Tacto rectal sin hallazgos |
| Q72 | varchar |  |  | SI | Extremidades |
| Q73 | bit |  |  | SI | Extremidades de movilidad normal, sin lesiones, si... |
| Q75 | varchar |  |  | SI | Pulsos |
| Q76 | bit |  |  | SI | Pulsos periféricos simétricos, de amplitud normal. |
| Q81 | varchar |  |  | SI | Neurológico |
| Q82 | varchar |  |  | SI | Glasgow |
| Q82ObsDR | varchar |  | FK | SI | Glasgow DR |
| Q83 | bit |  |  | SI | Examen neurológico sin hallazgos. |
| Q84 | varchar |  |  | SI | Ilustración |
| Q85 | varchar |  |  | SI | Exámenes de Laboratorio |
| Q86 | varchar |  |  | SI | Hemoglucotest |
| Q86ObsDR | varchar |  | FK | SI | Hemoglucotest DR |
| Q87 | varchar |  |  | SI | Exámenes de Imagen |
| Q88 | varchar |  |  | SI | Otros Exámenes Complementarios |
| Q89 | varchar |  |  | SI | Conclusiones |
| Q90 | varchar |  |  | SI | Plan de Manejo al Ingreso |
| Q91 | varchar |  |  | SI | Profesional(es) |
| Q92 | varchar |  |  | SI | Servicio Clínico |
| Q93 | varchar |  |  | SI | Electrocardiograma |
| Q94 | varchar |  |  | SI | Conclusión |
| Q95 | varchar |  |  | SI | Plan |
| Q96 | varchar |  |  | SI | Habla |
| Q97 | varchar |  |  | SI | Pupilas |
| Q98 | varchar |  |  | SI | Signos Meníngeos |
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
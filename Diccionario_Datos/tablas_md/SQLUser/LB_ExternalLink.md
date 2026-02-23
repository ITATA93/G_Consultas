# SQLUser.LB_ExternalLink

**Schema:** SQLUser
**Columnas:** 148
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEL_RowID | bigint | PK |  | NO | - |
| ChildQ58DR | - |  |  | SI | Child Reference: Pulmonar |
| LBEL_Comment | varchar |  |  | SI | Comment |
| LBEL_Episode_DR | bigint |  | FK | SI | Link to Lab Episode |
| LBEL_Link | varchar |  |  | SI | Link |
| LBEL_TestSet_DR | bigint |  | FK | SI | Link to Lab Test Set |
| LBEL_Title | varchar |  |  | SI | Link title |
| Q01 | - |  |  | SI | Fecha de Ingreso |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Información Entregada por |
| Q04 | - |  |  | SI | Procedencia |
| Q05 | - |  |  | SI | Procedencia |
| Q06 | - |  |  | SI | Nombre del Contacto |
| Q07 | - |  |  | SI | Fono de Contacto |
| Q08 | - |  |  | SI | Profesión o Actividad del Paciente |
| Q09 | - |  |  | SI | Anamnesis Próxima |
| Q10 | - |  |  | SI | Capacidad Funcional |
| Q11 | - |  |  | SI | Hábitos |
| Q12 | - |  |  | SI | Respiratorio |
| Q13 | - |  |  | SI | Cardiovascular |
| Q14 | - |  |  | SI | Digestivo |
| Q15 | - |  |  | SI | Enfermedades Infecciosas |
| Q16 | - |  |  | SI | Diabetes |
| Q17 | - |  |  | SI | Endocrinologia y Nutrición |
| Q18 | - |  |  | SI | Cabeza y Cuello |
| Q19 | - |  |  | SI | Reumatología |
| Q20 | - |  |  | SI | Neurología |
| Q21 | - |  |  | SI | Psiquiatría |
| Q22 | - |  |  | SI | Genitourinario |
| Q23 | - |  |  | SI | Oncología/Hematología |
| Q24 | - |  |  | SI | Medicamentos de Uso Reciente |
| Q25 | - |  |  | SI | Otros - Informaciones complementarias |
| Q26 | - |  |  | SI | Estado de conciencia |
| Q27 | - |  |  | SI | Paciente conciente, lúcido y orientado en tiempo y... |
| Q28 | - |  |  | SI | Facie |
| Q29 | - |  |  | SI | Facie no característica |
| Q30 | - |  |  | SI | Posición y Marcha |
| Q31 | - |  |  | SI | Posición en cama activa |
| Q32 | - |  |  | SI | Posición de pie: Postura recta, firme y sin oscila... |
| Q33 | - |  |  | SI | Piel |
| Q34 | - |  |  | SI | Piel |
| Q35 | - |  |  | SI | Rosada, sin ictericia o cianosis de extremidades. |
| Q36 | - |  |  | SI | Respiración |
| Q37 | - |  |  | SI | Respiración |
| Q38 | - |  |  | SI | Paciente eupnéico, respiración tranquila |
| Q39 | - |  |  | SI | P. Arterial Sistólica (mmHg) |
| Q39ObsDR | - |  |  | SI | P. Arterial Sistólica (mmHg) DR |
| Q40 | - |  |  | SI | P. Arterial Diastólica (mmHg) |
| Q40ObsDR | - |  |  | SI | P. Arterial Diastólica (mmHg) DR |
| Q41 | - |  |  | SI | Temperatura Axilar |
| Q41ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q42 | - |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q42ObsDR | - |  |  | SI | Frecuencia Cardíaca (lpm) DR |
| Q43 | - |  |  | SI | Frecuencia Respiratoria (rpm) |
| Q43ObsDR | - |  |  | SI | Frecuencia Respiratoria (rpm) DR |
| Q44 | - |  |  | SI | Saturación O2 (%) |
| Q44ObsDR | - |  |  | SI | Saturación O2 (%) DR |
| Q45 | - |  |  | SI | FiO2 (%) |
| Q45ObsDR | - |  |  | SI | FiO2 (%) DR |
| Q46 | - |  |  | SI | Escala de Dolor (EVA) |
| Q46ObsDR | - |  |  | SI | Escala de Dolor (EVA) DR |
| Q47 | - |  |  | SI | Peso (Kg.) |
| Q47ObsDR | - |  |  | SI | Peso (Kg.) DR |
| Q48 | - |  |  | SI | Talla |
| Q48ObsDR | - |  |  | SI | Talla DR |
| Q49 | - |  |  | SI | Descripción Examen Físico |
| Q50 | - |  |  | SI | Orofaringe |
| Q51 | - |  |  | SI | Dientes |
| Q52 | - |  |  | SI | Cuello |
| Q53 | - |  |  | SI | Cabeza normal. Ojos, oídos y orofaringe sin hallaz... |
| Q54 | - |  |  | SI | Tiroides normal. Carótidas sin soplos, pulsos norm... |
| Q55 | - |  |  | SI | Tórax |
| Q56 | - |  |  | SI | Tórax simétrico, sin deformaciones o lesiones |
| Q57 | - |  |  | SI | Mamas: Tejido glandular, piel, pezón y areola sin ... |
| Q59 | - |  |  | SI | Pulmonar |
| Q60 | - |  |  | SI | Pulmonar: Murmullo pulmonar simétrico, normal, sin... |
| Q62 | - |  |  | SI | Cardiaco |
| Q63 | - |  |  | SI | Cardiaco: Ritmo regular en dos tiempos. No se ausc... |
| Q65 | - |  |  | SI | Abdomen |
| Q66 | - |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q67 | - |  |  | SI | Región anogenital |
| Q68 | - |  |  | SI | Pene y escroto sin lesiones. Testículos de forma y... |
| Q69 | - |  |  | SI | Vulva sin hallazgos patológicos. Flujo ausente. |
| Q70 | - |  |  | SI | Tacto rectal sin hallazgos |
| Q72 | - |  |  | SI | Extremidades |
| Q73 | - |  |  | SI | Extremidades de movilidad normal, sin lesiones, si... |
| Q75 | - |  |  | SI | Pulsos |
| Q76 | - |  |  | SI | Pulsos periféricos simétricos, de amplitud normal. |
| Q81 | - |  |  | SI | Neurológico |
| Q82 | - |  |  | SI | Glasgow |
| Q82ObsDR | - |  |  | SI | Glasgow DR |
| Q83 | - |  |  | SI | Examen neurológico sin hallazgos. |
| Q84 | - |  |  | SI | Ilustración |
| Q85 | - |  |  | SI | Exámenes de Laboratorio |
| Q86 | - |  |  | SI | Hemoglucotest |
| Q86ObsDR | - |  |  | SI | Hemoglucotest DR |
| Q87 | - |  |  | SI | Exámenes de Imagen |
| Q88 | - |  |  | SI | Otros Exámenes Complementarios |
| Q89 | - |  |  | SI | Conclusiones |
| Q90 | - |  |  | SI | Plan de Manejo al Ingreso |
| Q91 | - |  |  | SI | Profesional(es) |
| Q92 | - |  |  | SI | Servicio Clínico |
| Q93 | - |  |  | SI | Electrocardiograma |
| Q94 | - |  |  | SI | Conclusión |
| Q95 | - |  |  | SI | Plan |
| Q96 | - |  |  | SI | Habla |
| Q97 | - |  |  | SI | Pupilas |
| Q98 | - |  |  | SI | Signos Meníngeos |
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
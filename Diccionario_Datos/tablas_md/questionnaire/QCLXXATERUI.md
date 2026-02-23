# questionnaire.QCLXXATERUI

> REGISTRO ATENCIÓN RUI

**Schema:** questionnaire
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* REGISTRO ATENCIÓN RUI

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Fecha Atención |
| Q01ObsDR | varchar |  | FK | SI | Fecha Atención DR |
| Q02 | date |  |  | SI | Fecha Última Atención |
| Q03 | varchar |  |  | SI | Tipo de Actividad Agendada |
| Q04 | varchar |  |  | SI | Tipo de Actividad Realizada |
| Q05 | varchar |  |  | SI | ACTIVIDAD |
| Q06 | varchar |  |  | SI | CUIDADO INTEGRAL |
| Q07 | varchar |  |  | SI | Anamnesis |
| Q08 | varchar |  |  | SI | Control / Compensación |
| Q09 | varchar |  |  | SI | Reacciones Adversas a Medicamentos |
| Q10 | varchar |  |  | SI | Observaciones de la Reación |
| Q11 | varchar |  |  | SI | Examen Físico |
| Q12 | varchar |  |  | SI | EXAMEN FÍSICO |
| Q13 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q13ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q14 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q14ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q15 | varchar |  |  | SI | Frecuencia Cardíaca |
| Q15ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca DR |
| Q16 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q16ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q17 | varchar |  |  | SI | Saturación de Oxígeno |
| Q17ObsDR | varchar |  | FK | SI | Saturación de Oxígeno DR |
| Q18 | varchar |  |  | SI | Peso |
| Q18ObsDR | varchar |  | FK | SI | Peso DR |
| Q19 | varchar |  |  | SI | Talla |
| Q19ObsDR | varchar |  | FK | SI | Talla DR |
| Q20 | varchar |  |  | SI | IMC |
| Q21 | varchar |  |  | SI | Hemoglucotest |
| Q21ObsDR | varchar |  | FK | SI | Hemoglucotest DR |
| Q22 | varchar |  |  | SI | Circunferencia Craneana |
| Q22ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q23 | varchar |  |  | SI | Circunferencia Cintura |
| Q23ObsDR | varchar |  | FK | SI | Circunferencia Cintura DR |
| Q24 | varchar |  |  | SI | Estado Nutricional |
| Q25 | varchar |  |  | SI | Síntomas de disnea |
| Q26 | varchar |  |  | SI | Resultado Riesgo Ulceración |
| Q27 | varchar |  |  | SI | Úlcera activa del pie |
| Q28 | varchar |  |  | SI | Grado de Úlcera |
| Q29 | date |  |  | SI | Fecha Estado Nutricional |
| Q30 | date |  |  | SI | Fecha Síntomas de disnea |
| Q31 | date |  |  | SI | Fecha Evaluación del pie DM |
| Q32 | date |  |  | SI | Fecha Úlcera activa del pie |
| Q33 | date |  |  | SI | Fecha Grado Wagner úlcera |
| Q34 | date |  |  | SI | Fecha Parámetros Clínicos |
| Q35 | numeric |  |  | SI | Espirometría Basal VEF1/CVF |
| Q36 | date |  |  | SI | Fecha Espirometría Basal VEF1/CVF |
| Q37 | numeric |  |  | SI | Espirometría post BD VEF1/CVF |
| Q38 | date |  |  | SI | Fecha Espirometría post BD VEF1/CVF |
| Q39 | numeric |  |  | SI | Flujometría Basal |
| Q40 | date |  |  | SI | Fecha Flujometría Basal |
| Q41 | numeric |  |  | SI | Flujometría pot BD |
| Q42 | date |  |  | SI | Fecha Flujometría pot BD |
| Q43 | numeric |  |  | SI | Pirometría |
| Q44 | date |  |  | SI | Fecha Pimometría |
| Q45 | numeric |  |  | SI | Test de Provocación con Ejercicio |
| Q46 | date |  |  | SI | Fecha Test de Provocación con Ejercicio |
| Q47 | varchar |  |  | SI | Resultado Test Marcha 6 Min |
| Q48 | date |  |  | SI | Fecha Test de Marcha |
| Q49 | varchar |  |  | SI | Resultado COPD Assessment Test CAT |
| Q50 | date |  |  | SI | Fecha Resultado COPD Assessment Test CAT |
| Q51 | varchar |  |  | SI | EQ5D |
| Q52 | date |  |  | SI | Fecha EQ5D |
| Q53 | varchar |  |  | SI | Electrocardiograma Descripción |
| Q53ObsDR | varchar |  | FK | SI | Electrocardiograma Descripción DR |
| Q54 | date |  |  | SI | Fecha Electrocardiograma |
| Q55 | varchar |  |  | SI | Cuestionario Pediátrico de Síntomas (PSC) 5-9 años |
| Q56 | date |  |  | SI | Fecha Cuestionario Pediátrico de Síntomas (PSC) 5-... |
| Q57 | varchar |  |  | SI | Cuestionario Pediátrico de Síntomas (PSC-Y) 10-14 ... |
| Q58 | date |  |  | SI | Fecha Cuestionario Pediátrico de Síntomas (PSC-Y) ... |
| Q59 | varchar |  |  | SI | Cuestionario de Salud General GHQ-12 |
| Q60 | date |  |  | SI | Fecha Cuestionario de Salud General GHQ-12 |
| Q61 | varchar |  |  | SI | PEDS-QL |
| Q62 | date |  |  | SI | Fecha PEDS-QL |
| Q63 | varchar |  |  | SI | Plan de Cuidado Integral  |
| Q64 | varchar |  |  | SI | Compromiso Acordado |
| Q65 | varchar |  |  | SI | Cumplimiento de cada uno de los acuerdos de plan d... |
| Q66 | varchar |  |  | SI | Consejería Familiar |
| Q67 | varchar |  |  | SI | Consejeria Breve Tabaquismo |
| Q68 | varchar |  |  | SI | Monitoreo a Distancia |
| Q69 | varchar |  |  | SI | Próximo Control con |
| Q70 | varchar |  |  | SI | Próximo Control |
| Q71 | date |  |  | SI | Fecha Próximo Control  |
| Q72 | varchar |  |  | SI | Electrocardiograma |
| Q72ObsDR | varchar |  | FK | SI | Electrocardiograma DR |
| Q74 | time |  |  | SI | Hora Ultimo Registro Atención RUI |
| Q75 | varchar |  |  | SI | La Etiqueta de Caida |
| Q76 | varchar |  |  | SI | EVALUACIÓN DEL PIE DIABÉTICO |
| Q77 | varchar |  |  | SI | EVALUACIÓN ENFERMEDAD RESPIRATORIA CRÓNICA  |
| Q78 | varchar |  |  | SI | OTROS PROCEDIMIENTOS DIAGNÓSTICOS |
| Q79 | varchar |  |  | SI | PLAN DE CUIDADO INTEGRAL |
| Q80 | varchar |  |  | SI | OTROS PROCEDIMIENTOS DIAGNÓSTICOS |
| Q83 | varchar |  |  | SI | Problemas Identificados y Priorizados |
| Q84 | varchar |  |  | SI | Objetivos y Resultados Esperados |
| Q85 | varchar |  |  | SI | Opciones Ofrecidas |
| Q86 | varchar |  |  | SI | Acuerdos / Actividades |
| Q87 | varchar |  |  | SI | Seguimiento de los acuerdos |
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
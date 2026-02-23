# questionnaire.QTCEEXMEPR

> Examen de Medicina Preventiva

**Schema:** questionnaire
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen de Medicina Preventiva

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ22 | varchar |  |  | SI | - |
| CQ33 | varchar |  |  | SI | - |
| CQ34 | varchar |  |  | SI | - |
| CQ70 | varchar |  |  | SI | - |
| CQ74 | varchar |  |  | SI | - |
| CQ75 | varchar |  |  | SI | - |
| CQ76 | varchar |  |  | SI | - |
| Q1 | varchar |  |  | SI | ¿Consumo bebidas alcohólicas? |
| Q10 | varchar |  |  | SI | Circunferencia abdominal Mujer >= 88 cm. |
| Q11 | varchar |  |  | SI | Circunferencia abdominal Hombre >= 102 cm. |
| Q12 | varchar |  |  | SI | Presión arterial sistólica |
| Q12ObsDR | varchar |  | FK | SI | Presión arterial sistólica DR |
| Q13 | varchar |  |  | SI | Presión arterial sistólica >= 140 mm/Hg |
| Q14 | varchar |  |  | SI | Presión arterial diastólica |
| Q14ObsDR | varchar |  | FK | SI | Presión arterial diastólica DR |
| Q15 | varchar |  |  | SI | Presión arterial diastólica >= 90 mm/Hg |
| Q16 | varchar |  |  | SI | Glicemia en ayunas (mg/dl) |
| Q16ObsDR | varchar |  | FK | SI | Glicemia en ayunas (mg/dl) DR |
| Q17 | varchar |  |  | SI | Glicemia en ayunas entre 100-125 mg/dl |
| Q18 | varchar |  |  | SI | Glicemia en ayunas >= 126 mg/dl |
| Q19 | varchar |  |  | SI | Hombres que tienen sexo con otros hombres, trabaja... |
| Q2 | varchar |  |  | SI | AUDIT Antíguo |
| Q20 | varchar |  |  | SI | VDRL |
| Q20ObsDR | varchar |  | FK | SI | VDRL DR |
| Q21 | varchar |  |  | SI | RPR |
| Q21ObsDR | varchar |  | FK | SI | RPR DR |
| Q22 | varchar |  |  | SI | ¿Ha tenido tos productiva por más de 15 días? |
| Q23 | date |  |  | SI | Fecha resultado PAP |
| Q24 | varchar |  |  | SI | PAP vigente |
| Q25 | varchar |  |  | SI | Resultado de PAP |
| Q25ObsDR | varchar |  | FK | SI | Resultado de PAP DR |
| Q26 | varchar |  |  | SI | Resultado colesterol total |
| Q26ObsDR | varchar |  | FK | SI | Resultado colesterol total DR |
| Q27 | varchar |  |  | SI | Colesterol total entre 200-239 mg/dl |
| Q28 | varchar |  |  | SI | Colesterol total >= 240 mg/dl |
| Q29 | varchar |  |  | SI | Mamografía realizada |
| Q2ObsDR | varchar |  | FK | SI | AUDIT Antíguo DR |
| Q3 | varchar |  |  | SI | Tabaquismo |
| Q30 | varchar |  |  | SI | Resultado mamografía |
| Q30ObsDR | varchar |  | FK | SI | Resultado mamografía DR |
| Q31 | varchar |  |  | SI | Debe generar Indicación de Baciloscopía |
| Q32 | date |  |  | SI | Fecha Vencimiento EMPA |
| Q33 | varchar |  |  | SI | Resultado Audit |
| Q34 | varchar |  |  | SI | Resultado Audit-C |
| Q35 | varchar |  |  | SI | Consejería según tipo de consumo |
| Q36 | varchar |  |  | SI | Consejería breve |
| Q37 | varchar |  |  | SI | Consejería en alimentación y actividad física |
| Q38 | date |  |  | SI | Fecha PAD |
| Q39 | varchar |  |  | SI | Refiere a perfil de Presión Arterial |
| Q4 | varchar |  |  | SI | Peso (kg.) |
| Q40 | varchar |  |  | SI | Refiere a PTGO |
| Q41 | varchar |  |  | SI | Referir a programa ITS |
| Q42 | varchar |  |  | SI | Baciloscopía |
| Q43 | date |  |  | SI | Fecha último Papanicolau |
| Q44 | varchar |  |  | SI | Resultado PAP |
| Q45 | varchar |  |  | SI | Toma de PAP |
| Q46 | varchar |  |  | SI | Refiere a consejería en alimentación saludable y a... |
| Q47 | varchar |  |  | SI | Refiere a confirmación Diagnóstica |
| Q48 | date |  |  | SI | Fecha última mamografía |
| Q49 | varchar |  |  | SI | Mamografía vigente |
| Q4ObsDR | varchar |  | FK | SI | Peso (kg.) DR |
| Q5 | varchar |  |  | SI | Talla (cms.) |
| Q50 | varchar |  |  | SI | Mamografía alterada |
| Q51 | varchar |  |  | SI | Mamografía a otras edades realizada |
| Q52 | varchar |  |  | SI | Mamografía a otras edades alterada |
| Q53 | varchar |  |  | SI | Observaciones |
| Q54 | date |  |  | SI | Fecha ingreso observaciones |
| Q55 | date |  |  | SI | Fecha realización EMP |
| Q56 | varchar |  |  | SI | RUT |
| Q57 | varchar |  |  | SI | Profesional |
| Q58 | varchar |  |  | SI | Especialidad |
| Q59 | varchar |  |  | SI | Código Especialidad |
| Q5ObsDR | varchar |  | FK | SI | Talla (cms.) DR |
| Q6 | varchar |  |  | SI | Índice de masa corporal (IMC) |
| Q60 | date |  |  | SI | Fecha registro resultado exámenes |
| Q61 | varchar |  |  | SI | Profesional |
| Q62 | varchar |  |  | SI | RUT |
| Q63 | varchar |  |  | SI | Especialidad |
| Q64 | varchar |  |  | SI | Código Especialidad |
| Q65 | date |  |  | SI | Fecha informa paciente |
| Q66 | varchar |  |  | SI | Profesional |
| Q67 | varchar |  |  | SI | RUT |
| Q68 | varchar |  |  | SI | Especialidad |
| Q69 | varchar |  |  | SI | Código Especialidad |
| Q7 | varchar |  |  | SI | Sobrepeso |
| Q70 | varchar |  |  | SI | Resultado CRAFFT |
| Q71 | varchar |  |  | SI | Refiere a confirmación diagnóstica |
| Q72 | varchar |  |  | SI | VDRL |
| Q73 | varchar |  |  | SI | RPR |
| Q74 | varchar |  |  | SI | Prueba ASSIST |
| Q75 | varchar |  |  | SI | Prueba CRAFFT |
| Q76 | varchar |  |  | SI | Prueba AUDIT  |
| Q8 | varchar |  |  | SI | Obesidad |
| Q9 | numeric |  |  | SI | Circunferencia de cintura (cm.) |
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
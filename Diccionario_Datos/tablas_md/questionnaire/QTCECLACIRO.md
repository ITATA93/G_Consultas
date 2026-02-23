# questionnaire.QTCECLACIRO

**Schema:** questionnaire
**Columnas:** 149
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date | PK |  | SI | Fecha Inicio |
| Q02 | time | PK |  | SI | Hora |
| Q03 | varchar | PK |  | SI | Información entregada por |
| Q04 | varchar | PK |  | SI | Procedencia |
| Q05 | varchar | PK |  | SI | Procedencia |
| Q06 | varchar | PK |  | SI | Anamnesis próxima |
| Q07 | varchar | PK |  | SI | Fatores de riesgo |
| Q08 | bit | PK |  | SI | consciente, orientado, cooperativo, eupneico y sin... |
| Q09 | varchar | PK |  | SI | Capacidad Funcional |
| Q10 | varchar | PK |  | SI | Lugar de consulta frecuente |
| Q100 | bigint | PK |  | SI | HTML |
| Q100TxtOnly | bigint | PK |  | SI | HTML Plain Text Only |
| Q101 | varchar | PK |  | SI | Examen mamario normal |
| Q102 | varchar | PK |  | SI | Examen Mamario |
| Q11 | varchar | PK |  | SI | Condiciones familiares o sociales para el cuidado ... |
| Q12 | varchar | PK |  | SI | Dieta y Nutrición |
| Q13 | varchar | PK |  | SI | Pérdida reciente de peso |
| Q14 | varchar | PK |  | SI | Chequeo pre-operatorio |
| Q15 | varchar | PK |  | SI | Medicamentos de uso regular |
| Q16 | varchar | PK |  | SI | Notas complementarias |
| Q17 | varchar | PK |  | SI | Estado fiísico general |
| Q18 | bit | PK |  | SI | eupneico, afebril, rosado, anictérico y acianótico |
| Q19 | varchar | PK |  | SI | Disnea |
| Q20 | varchar | PK |  | SI | Sindrome febril |
| Q21 | varchar | PK |  | SI | Palidez |
| Q22 | varchar | PK |  | SI | Ictericia |
| Q23 | bit | PK |  | SI | Examen Neurológico Normal |
| Q25 | varchar | PK |  | SI | Examen Neurológico |
| Q26 | bit | PK |  | SI | Marcha y equilibrio normales |
| Q27 | bit | PK |  | SI | Fimose |
| Q28 | bit | PK |  | SI | Hemorroidas |
| Q29 | bit | PK |  | SI | Celulitis |
| Q30 | bit | PK |  | SI | Abseceso |
| Q31 | bit | PK |  | SI | matidez a la percusión hacia la base pulmonar, que... |
| Q32 | bit | PK |  | SI | Masa abdominal |
| Q33 | bit | PK |  | SI | tórax con expansión unilateral, timpánico del mism... |
| Q34 | varchar | PK |  | SI | Consciente |
| Q35 | varchar | PK |  | SI | Orientado |
| Q36 | varchar | PK |  | SI | Cooperador |
| Q37 | varchar | PK |  | SI | Signos de dolor |
| Q38 | varchar | PK |  | SI | Indiferente |
| Q39 | varchar | PK |  | SI | Agresivo |
| Q40 | varchar | PK |  | SI | Peso |
| Q40ObsDR | varchar | PK | FK | SI | Peso DR |
| Q41 | varchar | PK |  | SI | Talla |
| Q41ObsDR | varchar | PK | FK | SI | Talla DR |
| Q42 | varchar | PK |  | SI | Temperatura |
| Q42ObsDR | varchar | PK | FK | SI | Temperatura DR |
| Q43 | varchar | PK |  | SI | Frecuencia Cardiaca |
| Q43ObsDR | varchar | PK | FK | SI | Frecuencia Cardiaca DR |
| Q44 | varchar | PK |  | SI | Frecuencia Respiratoria |
| Q44ObsDR | varchar | PK | FK | SI | Frecuencia Respiratoria DR |
| Q45 | varchar | PK |  | SI | Presión Arterial Sistólica |
| Q45ObsDR | varchar | PK | FK | SI | Presión Arterial Sistólica DR |
| Q46 | varchar | PK |  | SI | Presión Arterial Diastólica |
| Q46ObsDR | varchar | PK | FK | SI | Presión Arterial Diastólica DR |
| Q47 | varchar | PK |  | SI | Presión Arterial Media |
| Q47ObsDR | varchar | PK | FK | SI | Presión Arterial Media DR |
| Q48 | varchar | PK |  | SI | Saturación oxígeno spo |
| Q48ObsDR | varchar | PK | FK | SI | Saturación oxígeno spo DR |
| Q49 | varchar | PK |  | SI | Observaciones |
| Q50 | bit | PK |  | SI |  dientes en buen estado, orofaringe normal. |
| Q51 | varchar | PK |  | SI | Cabeza e cuello |
| Q52 | varchar | PK |  | SI | Observaciones |
| Q53 | varchar | PK |  | SI | Palpación abd. |
| Q54 | varchar | PK |  | SI | Percución abd. |
| Q55 | varchar | PK |  | SI | Ausculta abd |
| Q56 | varchar | PK |  | SI | Localización de las anormalidades abdominales |
| Q57 | varchar | PK |  | SI | Localización de las anormalidades toráxicas más in... |
| Q58 | bit | PK |  | SI | Pie diabético cirurgico |
| Q59 | varchar | PK |  | SI | Inspeción t. |
| Q60 | varchar | PK |  | SI | Examen Pulmonar |
| Q61 | bit | PK |  | SI | Eupneico, murmurio pulmonar normal, sin ruidos agr... |
| Q62 | varchar | PK |  | SI | Percusión t. |
| Q63 | varchar | PK |  | SI | Auscultación t. |
| Q64 | bit | PK |  | SI | cicatriz quirúrgica con enpastamiento, eritema y d... |
| Q65 | bit | PK |  | SI | cisto pilonidal o absceso perianal |
| Q66 | varchar | PK |  | SI | Exámen Cardiaco Normal |
| Q67 | varchar | PK |  | SI | Examen Cardiaco |
| Q68 | bit | PK |  | SI | Ritmo regular, en dos tiempos, sin soplos, ruidos ... |
| Q69 | bit | PK |  | SI | Choque o prechoque hemorragico |
| Q70 | bit | PK |  | SI | colostomia |
| Q71 | varchar | PK |  | SI | Examen Abdominal Normal |
| Q72 | varchar | PK |  | SI | Examen Abdominal |
| Q73 | bit | PK |  | SI | Abdomen blando, depresible, indoloro, sin vicerome... |
| Q74 | varchar | PK |  | SI | Inspeción abd. |
| Q75 | varchar | PK |  | SI | Examen Genitoanal Normal |
| Q76 | varchar | PK |  | SI | Examen Genitoanal |
| Q77 | bit | PK |  | SI | Genitales, ano y carecteres sexuales adecuados par... |
| Q78 | varchar | PK |  | SI | Examen de Extremidades Normal |
| Q79 | varchar | PK |  | SI | Examen de Extremidades  |
| Q80 | varchar | PK |  | SI | Conclusion del la Evaluación |
| Q81 | bit | PK |  | SI | Enfermedad de notificación obligatoria |
| Q82 | bit | PK |  | SI | Enfermedad infectocontagiosa |
| Q83 | bit | PK |  | SI | Enfermedad Crónica reagudizada |
| Q84 | bit | PK |  | SI | Enfermedad aguda o nueva para el paciente |
| Q85 | bit | PK |  | SI | Problema GES |
| Q86 | varchar | PK |  | SI | Plan |
| Q87 | bit | PK |  | SI | Notificar atención a garantia de un problema GES |
| Q88 | bit | PK |  | SI | Notificar nuevo problema GES |
| Q89 | bit | PK |  | SI | Solicitar examenes de laboratorio |
| Q90 | bit | PK |  | SI | Solicitar examenes de imagen |
| Q91 | bit | PK |  | SI | Solicitar examen anatomopatologico |
| Q92 | bit | PK |  | SI | Periodo de observacion de la evolucion en la unida... |
| Q93 | bit | PK |  | SI | Hospitalización |
| Q94 | bit | PK |  | SI | Solicitar evaluación por especialidad |
| Q95 | bit | PK |  | SI | Retorno programado |
| Q96 | varchar | PK |  | SI | Exámenes laboratorio |
| Q97 | varchar | PK |  | SI | Exámenes Imágenes |
| Q98 | varchar | PK |  | SI | Exámenes histopatológicos |
| Q99 | varchar | PK |  | SI | Imagen |
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
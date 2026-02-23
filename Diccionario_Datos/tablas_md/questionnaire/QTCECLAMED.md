# questionnaire.QTCECLAMED

> CLINICA

**Schema:** questionnaire
**Columnas:** 161
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(CLINICA)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Ingreso |
| Q02 | time |  |  | SI | Hora de Ingreso |
| Q03 | varchar |  |  | SI | Información entregada por |
| Q04 | varchar |  |  | SI | Procedencia |
| Q05 | varchar |  |  | SI | Procedencia |
| Q06 | varchar |  |  | SI | Anamnesis Próxima |
| Q07 | varchar |  |  | SI | Chequeo de Antecedentes  |
| Q08 | varchar |  |  | SI | Acciones Preventivas |
| Q09 | varchar |  |  | SI | Condición basal del paciente |
| Q10 | varchar |  |  | SI | Red de Salud mayormente utilizada |
| Q100 | bigint |  |  | SI | HTML |
| Q100TxtOnly | bigint |  |  | SI | HTML Plain Text Only |
| Q101 | varchar |  |  | SI | Presión arterial sistólica PAS |
| Q101ObsDR | varchar |  | FK | SI | Presión arterial sistólica PAS DR |
| Q102 | varchar |  |  | SI | Presión arterial diastólica PAD |
| Q102ObsDR | varchar |  | FK | SI | Presión arterial diastólica PAD DR |
| Q103 | varchar |  |  | SI | Presión arterial media PAM |
| Q103ObsDR | varchar |  | FK | SI | Presión arterial media PAM DR |
| Q104 | varchar |  |  | SI | Talla |
| Q104ObsDR | varchar |  | FK | SI | Talla DR |
| Q105 | varchar |  |  | SI | Peso |
| Q105ObsDR | varchar |  | FK | SI | Peso DR |
| Q106 | varchar |  |  | SI | Índice de masa corporal IMC |
| Q106ObsDR | varchar |  | FK | SI | Índice de masa corporal IMC DR |
| Q107 | varchar |  |  | SI | Frecuencia cardiaca |
| Q107ObsDR | varchar |  | FK | SI | Frecuencia cardiaca DR |
| Q108 | varchar |  |  | SI | Frecuencia respiratoria |
| Q108ObsDR | varchar |  | FK | SI | Frecuencia respiratoria DR |
| Q109 | varchar |  |  | SI | Temperatura |
| Q109ObsDR | varchar |  | FK | SI | Temperatura DR |
| Q11 | varchar |  |  | SI | Condiciones familiares o sociales |
| Q110 | varchar |  |  | SI | Saturación oxígeno SPO2 |
| Q110ObsDR | varchar |  | FK | SI | Saturación oxígeno SPO2 DR |
| Q12 | varchar |  |  | SI | Dieta e nutrición |
| Q13 | varchar |  |  | SI | Perdida reciente de peso |
| Q14 | varchar |  |  | SI | Reserva1 |
| Q15 | varchar |  |  | SI | Medicamientos de uso frequente o habitual |
| Q16 | varchar |  |  | SI | Notas complementares |
| Q17 | varchar |  |  | SI | Estado fisico general |
| Q18 | varchar |  |  | SI | Actitud |
| Q19 | varchar |  |  | SI | Disnea |
| Q20 | varchar |  |  | SI | Fiebre |
| Q21 | varchar |  |  | SI | Palidez |
| Q22 | varchar |  |  | SI | Ictericia |
| Q23 | varchar |  |  | SI | Sistema Nervioso |
| Q25 | varchar |  |  | SI | Sistema nervioso |
| Q26 | bit |  |  | SI | Marcha y equilibrio normales |
| Q27 | bit |  |  | SI | Ausencia de rigidez nucal |
| Q28 | bit |  |  | SI | Pupilas reativas e simétricas |
| Q29 | bit |  |  | SI | Tonus muscular simétrico |
| Q30 | bit |  |  | SI | Ausencia de paresias o parestesias |
| Q31 | bit |  |  | SI | Sequelas de Accidente Vascular Encefálico |
| Q32 | bit |  |  | SI | Reflejos normales |
| Q33 | bit |  |  | SI | Columna vertebral normal |
| Q34 | varchar |  |  | SI | Ojos |
| Q35 | varchar |  |  | SI | Ojos |
| Q36 | bit |  |  | SI | Ojos de aspecto normal, bilateralmiente |
| Q37 | bit |  |  | SI | Conjuntivas hiperemiadas y con exudacion |
| Q38 | bit |  |  | SI | Blefaritis |
| Q39 | bit |  |  | SI | ojoreser |
| Q40 | varchar |  |  | SI | Oido |
| Q41 | varchar |  |  | SI | Oido |
| Q42 | bit |  |  | SI | Condutos auditivos externos y timpanos de aspecto ... |
| Q43 | bit |  |  | SI | Conduto auditivo externo direito hiperemiado e ede... |
| Q44 | bit |  |  | SI | Conducto auditivo externo izquierdo hiperemiado y ... |
| Q45 | varchar |  |  | SI | Timpano derecho abaulado y hiperemiado |
| Q46 | bit |  |  | SI | Timpano derecho roto |
| Q47 | bit |  |  | SI | Timpano izquierdo abaulado y hiperemiado |
| Q48 | bit |  |  | SI | Timpano izquierdo roto |
| Q49 | varchar |  |  | SI | Secrecion purulenta en el conducto auditivo derech... |
| Q50 | bit |  |  | SI | Secrecion purulenta en el conducto auditivo izquie... |
| Q51 | varchar |  |  | SI | Nariz, Boca, Pescoco |
| Q52 | varchar |  |  | SI | Nariz, Boca y Pescoco |
| Q53 | bit |  |  | SI | Denticion completa |
| Q54 | bit |  |  | SI | Dientes en buen estado |
| Q55 | bit |  |  | SI | Dientes en malo estado |
| Q56 | bit |  |  | SI | Orofaringe normal |
| Q57 | bit |  |  | SI | Orofaringe hiperemiada |
| Q58 | bit |  |  | SI | Amigdalas hipertrofiadas y hiperemiadas  |
| Q59 | varchar |  |  | SI | Pulmones |
| Q60 | varchar |  |  | SI | Pulmones |
| Q61 | bit |  |  | SI | Eupneico, murmurio vesicular fisiologico |
| Q62 | bit |  |  | SI | Taquipneico |
| Q63 | bit |  |  | SI | Dispneico |
| Q64 | bit |  |  | SI | Roncos |
| Q65 | bit |  |  | SI | Sibilos expiratorios |
| Q66 | varchar |  |  | SI | Coracion |
| Q67 | varchar |  |  | SI | Coracion |
| Q68 | bit |  |  | SI | Ritmo regular, en dos tiempos, sin soplos, ruidos ... |
| Q69 | bit |  |  | SI | Ritmo regular en dos tiempos con soplo sistolico |
| Q70 | bit |  |  | SI | Taquicardia |
| Q71 | varchar |  |  | SI | Abdomen |
| Q72 | varchar |  |  | SI | Abdomen |
| Q73 | bit |  |  | SI | Abdomen depresible, sin defensa o puntos dolorosos |
| Q74 | bit |  |  | SI | Ausencia de masas o viceromegalias |
| Q75 | varchar |  |  | SI | Genitoanal |
| Q76 | varchar |  |  | SI | Genitoanal |
| Q77 | bit |  |  | SI | Genitalia, anus y carecteres sexuais esperados par... |
| Q78 | varchar |  |  | SI | Extremidades |
| Q79 | varchar |  |  | SI | Extremidades  |
| Q80 | varchar |  |  | SI | Conclusion |
| Q81 | bit |  |  | SI | Enfermedad de notificacion compulsoria |
| Q82 | bit |  |  | SI | Enfermidad con alto riesgo en contaminacion comuni... |
| Q83 | bit |  |  | SI | Condicion cronica para el paciente, com acutizacio... |
| Q84 | bit |  |  | SI | Condicion aguda o nueva para el paciente |
| Q85 | bit |  |  | SI | Condicion de Garantia GES |
| Q86 | varchar |  |  | SI | Plan |
| Q87 | bit |  |  | SI | Notificar atendimiento a garantia GES |
| Q88 | bit |  |  | SI | Notificar nueva garantia GES |
| Q89 | bit |  |  | SI | Solicitar examenes de laboratorio |
| Q90 | bit |  |  | SI | Solicitar examenes de imagen |
| Q91 | bit |  |  | SI | Solicitar examen anatomopatologico |
| Q92 | bit |  |  | SI | Periodo de observacion de la evolucion en la unida... |
| Q93 | bit |  |  | SI | Hospitalizacion |
| Q94 | bit |  |  | SI | Solicitar parecer especializado |
| Q95 | bit |  |  | SI | Retorno programado |
| Q96 | varchar |  |  | SI | Examenes laboratorio |
| Q97 | varchar |  |  | SI | Examenes Imagenes |
| Q98 | varchar |  |  | SI | Examenes histopatologicos |
| Q99 | varchar |  |  | SI | imagen |
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
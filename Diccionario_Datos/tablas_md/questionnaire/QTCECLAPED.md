# questionnaire.QTCECLAPED

> PEDIATRIA

**Schema:** questionnaire
**Columnas:** 178
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(PEDIATRIA)*

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
| Q07 | varchar |  |  | SI | Antecedentes Perinatales |
| Q08 | varchar |  |  | SI | Inmunizaciones |
| Q09 | varchar |  |  | SI | Condición funcional basal |
| Q10 | varchar |  |  | SI | Red de Salud, Contacto habitual |
| Q100 | varchar |  |  | SI | Orejas |
| Q101 | varchar |  |  | SI | Nariz |
| Q102 | varchar |  |  | SI | Boca |
| Q103 | varchar |  |  | SI | Cuello |
| Q104 | varchar |  |  | SI | Tórax |
| Q105 | varchar |  |  | SI | Murmurio vesicular |
| Q106 | varchar |  |  | SI | Tonos cardiacos |
| Q107 | varchar |  |  | SI | Abdomen |
| Q108 | varchar |  |  | SI | Cordón |
| Q109 | varchar |  |  | SI | Caderas |
| Q11 | varchar |  |  | SI | Condiciones familiares o sociales |
| Q110 | varchar |  |  | SI | Genitales femininos |
| Q111 | varchar |  |  | SI | Genitales masculinos |
| Q112 | varchar |  |  | SI | Extremidades |
| Q113 | varchar |  |  | SI | Pies |
| Q114 | numeric |  |  | SI | Edad gestacional en semanas según FUR |
| Q115 | numeric |  |  | SI | Edad gestacional en semanas según examen físico |
| Q116 | numeric |  |  | SI | Edad gestacional en semanas según examen neurológi... |
| Q117 | varchar |  |  | SI | Pediatra Responsable |
| Q118 | varchar |  |  | SI | Becado |
| Q119 | numeric |  |  | SI | Horas de vida |
| Q12 | varchar |  |  | SI | Crecimiento |
| Q120 | varchar |  |  | SI | Reserva1 |
| Q121 | varchar |  |  | SI | Temperatura Axilar |
| Q121ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q122 | varchar |  |  | SI | Talla |
| Q122ObsDR | varchar |  | FK | SI | Talla DR |
| Q123 | varchar |  |  | SI | Índice de masa corporal IMC |
| Q123ObsDR | varchar |  | FK | SI | Índice de masa corporal IMC DR |
| Q124 | varchar |  |  | SI | Saturación oxígeno SPO2 |
| Q124ObsDR | varchar |  | FK | SI | Saturación oxígeno SPO2 DR |
| Q125 | varchar |  |  | SI | Frecuencia cardiaca |
| Q125ObsDR | varchar |  | FK | SI | Frecuencia cardiaca DR |
| Q126 | varchar |  |  | SI | Frecuencia respiratória |
| Q126ObsDR | varchar |  | FK | SI | Frecuencia respiratória DR |
| Q127 | varchar |  |  | SI | Peso |
| Q127ObsDR | varchar |  | FK | SI | Peso DR |
| Q128 | varchar |  |  | SI | Reserva2 |
| Q129 | varchar |  |  | SI | Local |
| Q13 | varchar |  |  | SI | Pérdida reciente de peso |
| Q130 | varchar |  |  | SI | Temperatura Rectal |
| Q130ObsDR | varchar |  | FK | SI | Temperatura Rectal DR |
| Q14 | varchar |  |  | SI | Desarollo Sicomotor |
| Q15 | varchar |  |  | SI | Medicamentos de uso frecuente o habitual |
| Q16 | varchar |  |  | SI | Notas complementarias |
| Q17 | varchar |  |  | SI | Estado físico general |
| Q18 | varchar |  |  | SI | Actitud |
| Q19 | varchar |  |  | SI | Disnea |
| Q20 | varchar |  |  | SI | Febril |
| Q21 | varchar |  |  | SI | Pálido |
| Q22 | varchar |  |  | SI | Ictérico |
| Q23 | varchar |  |  | SI | Sistema Nervioso Central |
| Q25 | varchar |  |  | SI | Sistema Nervioso Central |
| Q26 | bit |  |  | SI | Reflejos y tono muscular normal |
| Q27 | bit |  |  | SI | Ausencia de rigidez nucal |
| Q28 | bit |  |  | SI | Pupilas isocóricas reativas  |
| Q29 | varchar |  |  | SI | Fontanela Bregmática |
| Q30 | varchar |  |  | SI | Columna vertebral |
| Q31 | bit |  |  | SI | Circunferencia craneana dentro de los límites norm... |
| Q32 | varchar |  |  | SI | Reflejos presentes |
| Q33 | varchar |  |  | SI | Respiración |
| Q34 | varchar |  |  | SI | Ojos |
| Q35 | varchar |  |  | SI | Ojos |
| Q36 | bit |  |  | SI | Ojos de aspecto normal, bilateralmiente |
| Q37 | bit |  |  | SI | Conjuntivas hiperhémicas, con exudado |
| Q38 | bit |  |  | SI | Blefaritis |
| Q39 | varchar |  |  | SI | Ojo |
| Q40 | varchar |  |  | SI | Oido |
| Q41 | varchar |  |  | SI | Oido |
| Q42 | bit |  |  | SI | Condutos auditivos externos y timpanos de aspecto ... |
| Q43 | bit |  |  | SI | Conduto auditivo externo direito hiperemiado e ede... |
| Q44 | bit |  |  | SI | Conducto auditivo externo izquierdo hiperemiado y ... |
| Q45 | bit |  |  | SI | Timpano derecho abaulado y hiperemiado |
| Q46 | bit |  |  | SI | Timpano derecho roto |
| Q47 | bit |  |  | SI | Timpano izquierdo abaulado y hiperemiado |
| Q48 | bit |  |  | SI | Timpano izquierdo roto |
| Q49 | bit |  |  | SI | Secrecion purulenta en el conducto auditivo derech... |
| Q50 | bit |  |  | SI | Secrecion purulenta en el conducto auditivo izquie... |
| Q51 | varchar |  |  | SI | Nariz, Boca, Pescoco |
| Q52 | varchar |  |  | SI | Nariz, Boca y Pescoco |
| Q53 | bit |  |  | SI | Denticion esperada para a edad |
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
| Q81 | bit |  |  | SI | Enfermedad de notificacion obligatoria |
| Q82 | bit |  |  | SI | Enfermedad con alto riesgo en contaminacion comuni... |
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
| Q99 | varchar |  |  | SI | Piel |
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
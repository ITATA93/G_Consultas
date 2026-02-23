# questionnaire.QTCECLAOBS

> GO

**Schema:** questionnaire
**Columnas:** 171
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(GO)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha ingreso |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Información entregada por |
| Q04 | varchar |  |  | SI | Procedencia |
| Q05 | varchar |  |  | SI | Procedencia |
| Q06 | varchar |  |  | SI | Anamnesis |
| Q07 | varchar |  |  | SI | Menarca |
| Q08 | varchar |  |  | SI | Acciones preventivas |
| Q09 | varchar |  |  | SI | Condición funcional básica |
| Q10 | varchar |  |  | SI | Red de Salud, conctato habitual |
| Q100 | bigint |  |  | SI | Texto especial, imagen y foto |
| Q100TxtOnly | bigint |  |  | SI | Texto especial, imagen y foto Plain Text Only |
| Q101 | bit |  |  | SI | Útero de forma, tamano, consistencia y mobilidad n... |
| Q102 | bit |  |  | SI | Útero de mobilidad moderadamiente dolorosa |
| Q103 | bit |  |  | SI | Útero de mobilidad extremadamiente dolorosa |
| Q104 | bit |  |  | SI | Útero aumentado de volumen pero dentro de los limi... |
| Q105 | bit |  |  | SI | Massa o empastamiento anexial |
| Q106 | date |  |  | SI | FUR operativa |
| Q107 | varchar |  |  | SI | Criterio elejido para la FUR |
| Q108 | varchar |  |  | SI | Crecimiento uterino y edad gestacional |
| Q109 | varchar |  |  | SI | Circunferencia abdominal fetal ecografica |
| Q11 | varchar |  |  | SI | Condiciones familiares o sociales |
| Q110 | varchar |  |  | SI | Ecodoppler |
| Q111 | varchar |  |  | SI | Volumen de líquido amniótico  |
| Q112 | bit |  |  | SI | Feto reactivo en cardiotocografia, con FCF normal |
| Q113 | varchar |  |  | SI | Examen obstétrico |
| Q114 | varchar |  |  | SI | Observaciones |
| Q115 | varchar |  |  | SI | Residuo vaginal |
| Q116 | varchar |  |  | SI | label |
| Q117 | varchar |  |  | SI | Ciclos |
| Q118 | varchar |  |  | SI | Periodo |
| Q119 | varchar |  |  | SI | Fertilidad |
| Q12 | varchar |  |  | SI | Nutrición |
| Q120 | varchar |  |  | SI | Partos |
| Q121 | varchar |  |  | SI | Temperatura |
| Q121ObsDR | varchar |  | FK | SI | Temperatura DR |
| Q122 | varchar |  |  | SI | Talla |
| Q122ObsDR | varchar |  | FK | SI | Talla DR |
| Q124 | varchar |  |  | SI | Saturación oxígeno SPO2 |
| Q124ObsDR | varchar |  | FK | SI | Saturación oxígeno SPO2 DR |
| Q125 | varchar |  |  | SI | Frecuencia cardiaca |
| Q125ObsDR | varchar |  | FK | SI | Frecuencia cardiaca DR |
| Q126 | varchar |  |  | SI | Frecuencia respiratoria |
| Q126ObsDR | varchar |  | FK | SI | Frecuencia respiratoria DR |
| Q13 | varchar |  |  | SI | Pérdida reciente de peso |
| Q14 | varchar |  |  | SI | Evaluación de Historia Ginecológica |
| Q15 | varchar |  |  | SI | Medicamentos de uso frequente o habitual |
| Q16 | varchar |  |  | SI | Evaluación y chequeo de antecedentes |
| Q17 | varchar |  |  | SI | Exame fisico general |
| Q18 | varchar |  |  | SI | Actitud |
| Q19 | varchar |  |  | SI | Disnea |
| Q20 | varchar |  |  | SI | Fiebre |
| Q21 | varchar |  |  | SI | Palidez |
| Q22 | varchar |  |  | SI | Ictericia |
| Q23 | varchar |  |  | SI | Lista neurológica |
| Q25 | varchar |  |  | SI | Examen neurológico |
| Q26 | bit |  |  | SI | Marcha y equilibrio normales |
| Q27 | varchar |  |  | SI | Region inguinal  |
| Q28 | varchar |  |  | SI | Vulva |
| Q29 | varchar |  |  | SI | Perineo |
| Q30 | varchar |  |  | SI | Condicón funcional específica |
| Q31 | varchar |  |  | SI | Lista especialidad |
| Q32 | bit |  |  | SI | Reflexos normales |
| Q33 | bit |  |  | SI | Reflexos patelares exaltados |
| Q34 | varchar |  |  | SI | Perinatal |
| Q35 | varchar |  |  | SI | Biópsias |
| Q36 | varchar |  |  | SI | Cirurgias |
| Q37 | varchar |  |  | SI | Deformaciones anatómicas importantes por |
| Q38 | varchar |  |  | SI | Menopausa |
| Q39 | bit |  |  | SI | Vagina con complacencia y elasticidad normales |
| Q40 | varchar |  |  | SI | Lista de locales |
| Q41 | varchar |  |  | SI | Sustentación uterovaginal |
| Q42 | varchar |  |  | SI | Evaluación especialidad |
| Q43 | varchar |  |  | SI | Membros inferiores |
| Q44 | varchar |  |  | SI | Lista antecedentes generales |
| Q45 | varchar |  |  | SI | Examen ginecológico |
| Q46 | bit |  |  | SI | Cuello uterino de tamano normal  |
| Q47 | bit |  |  | SI | Cuello uterino hipertrófico |
| Q48 | bit |  |  | SI | Colposcopia sin alteraciones displásicas de color,... |
| Q49 | bit |  |  | SI | Colposcopia con alteraciones displásicas de relevo... |
| Q50 | bit |  |  | SI | Colposcopia con alteraciones displásicas de color,... |
| Q51 | varchar |  |  | SI | Lista cara y cuello |
| Q52 | varchar |  |  | SI | Examen nariz, boca y cuello |
| Q53 | bit |  |  | SI | Dentición completa |
| Q54 | bit |  |  | SI | Dientes en buen estado |
| Q55 | bit |  |  | SI | Dientes en malo estado |
| Q56 | bit |  |  | SI | Orofaringe normal |
| Q57 | bit |  |  | SI | Orofaringe hiperémica |
| Q58 | varchar |  |  | SI | Blumberg  |
| Q59 | varchar |  |  | SI | Lista pulmonar |
| Q60 | varchar |  |  | SI | Examen pulmonar |
| Q61 | bit |  |  | SI | Eupneico, murmurio vesicular fisiologico |
| Q62 | bit |  |  | SI | Taquipneico |
| Q63 | bit |  |  | SI | Dispneico |
| Q64 | bit |  |  | SI | Roncos |
| Q65 | bit |  |  | SI | Sibilos en espiración |
| Q66 | varchar |  |  | SI | Lista cardíaca |
| Q67 | varchar |  |  | SI | Examen cardíaco |
| Q68 | bit |  |  | SI | Ritmo regular, en dos tiempos, sin soplos, ruidos ... |
| Q69 | bit |  |  | SI | Ritmo regular en dos tiempos con soplo sistolico |
| Q70 | bit |  |  | SI | Taquicardia |
| Q71 | varchar |  |  | SI | Lista abdominal |
| Q72 | varchar |  |  | SI | Examen abdominal |
| Q73 | bit |  |  | SI | Abdome depresible, sin resistencia a la palpación ... |
| Q74 | bit |  |  | SI | Ausencia de viceromegalias o masas palpables |
| Q75 | varchar |  |  | SI | Lista ginecológica completa |
| Q76 | bit |  |  | SI | Utero aumentado de volumen proyectandose hacia fue... |
| Q77 | varchar |  |  | SI | Exame mamas |
| Q78 | varchar |  |  | SI | Lista extremidades |
| Q79 | varchar |  |  | SI | Exame extremidades  |
| Q80 | varchar |  |  | SI | Conclusion |
| Q81 | bit |  |  | SI | Contacto preventivo sin allajos importantes |
| Q82 | bit |  |  | SI | Gestación de evolución normal, con bajo riesgo |
| Q83 | bit |  |  | SI | Enbarazo de alto riesgo con acompanhamiente obstét... |
| Q84 | bit |  |  | SI | Condicion aguda o nueva para el paciente |
| Q85 | bit |  |  | SI | Riesgo de prematuirdad en condiciones de GES |
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
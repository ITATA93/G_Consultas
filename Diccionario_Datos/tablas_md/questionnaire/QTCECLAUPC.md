# questionnaire.QTCECLAUPC

> CRITICO

**Schema:** questionnaire
**Columnas:** 162
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(CRITICO)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Data Inicio |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Informante |
| Q04 | varchar |  |  | SI | Procedencia |
| Q05 | varchar |  |  | SI | Procedencia |
| Q06 | varchar |  |  | SI | Anamnesis próxima |
| Q07 | varchar |  |  | SI | Chequeo Antecedentes Vasculares |
| Q08 | varchar |  |  | SI | Chequeo de Miocardio |
| Q09 | varchar |  |  | SI | Capacidad Funcional |
| Q10 | varchar |  |  | SI | Chequeo Ritmo Cardíaco |
| Q100 | bigint |  |  | SI | HTML |
| Q100TxtOnly | bigint |  |  | SI | HTML Plain Text Only |
| Q101 | varchar |  |  | SI | Temperatura |
| Q101ObsDR | varchar |  | FK | SI | Temperatura DR |
| Q102 | varchar |  |  | SI | Presión arterial sistólica PAS |
| Q102ObsDR | varchar |  | FK | SI | Presión arterial sistólica PAS DR |
| Q103 | varchar |  |  | SI | Presión arterial diastólica PAD |
| Q103ObsDR | varchar |  | FK | SI | Presión arterial diastólica PAD DR |
| Q104 | varchar |  |  | SI | Presión arterial media PAM |
| Q104ObsDR | varchar |  | FK | SI | Presión arterial media PAM DR |
| Q105 | varchar |  |  | SI | Talla |
| Q105ObsDR | varchar |  | FK | SI | Talla DR |
| Q106 | varchar |  |  | SI | Peso |
| Q106ObsDR | varchar |  | FK | SI | Peso DR |
| Q107 | varchar |  |  | SI | Índice de masa corporal |
| Q107ObsDR | varchar |  | FK | SI | Índice de masa corporal DR |
| Q108 | varchar |  |  | SI | Frecuencia cardiaca |
| Q108ObsDR | varchar |  | FK | SI | Frecuencia cardiaca DR |
| Q109 | varchar |  |  | SI | Frecuencia respiratoria |
| Q109ObsDR | varchar |  | FK | SI | Frecuencia respiratoria DR |
| Q11 | varchar |  |  | SI | Condiciones familiares o sociales |
| Q110 | varchar |  |  | SI | Saturación oxígeno |
| Q110ObsDR | varchar |  | FK | SI | Saturación oxígeno DR |
| Q12 | varchar |  |  | SI | Chequeo Válvulas Cardíacas |
| Q13 | varchar |  |  | SI | Estado nutricional |
| Q14 | varchar |  |  | SI | Chequeo Enf. Coronaria |
| Q15 | varchar |  |  | SI | Medicamentos de uso habitual |
| Q16 | varchar |  |  | SI | Observaciones en antecedentes |
| Q17 | varchar |  |  | SI | Observaciones en examen físico general |
| Q18 | varchar |  |  | SI | Actitud |
| Q19 | varchar |  |  | SI | Repiración |
| Q20 | varchar |  |  | SI | Piel y mucosas |
| Q21 | varchar |  |  | SI | Abdomen |
| Q22 | varchar |  |  | SI | Dolor |
| Q23 | varchar |  |  | SI | Sistema Nervoso  |
| Q25 | varchar |  |  | SI | Observaciones en Sistema Nervoso  |
| Q26 | varchar |  |  | SI | Glasgow |
| Q26ObsDR | varchar |  | FK | SI | Glasgow DR |
| Q27 | varchar |  |  | SI | Chequeo Hipertensión Arterial |
| Q28 | varchar |  |  | SI | Chequeo Historia Renal y Vía Urinaria |
| Q29 | varchar |  |  | SI | Chequeo de antecedentes de coagulación |
| Q30 | varchar |  |  | SI | Diabetes |
| Q31 | varchar |  |  | SI | Chequeo de antecedentes respiratoreos |
| Q32 | varchar |  |  | SI | Chequeo aparelho digestivo |
| Q33 | varchar |  |  | SI | Chequeo de antecedentes neurológicos |
| Q34 | varchar |  |  | SI | Cabeza y cuello |
| Q35 | varchar |  |  | SI | Chequeo de antecedentes |
| Q36 | varchar |  |  | SI | Ojos |
| Q37 | varchar |  |  | SI | Chequeo antecedentes comportamento |
| Q38 | varchar |  |  | SI | Chequeo antecedentes a. reprodutor femenino |
| Q39 | varchar |  |  | SI | Chequeo antecedentes tireoide y suprarenales |
| Q40 | varchar |  |  | SI | Oido |
| Q41 | varchar |  |  | SI | Oido |
| Q42 | varchar |  |  | SI | Membro inferior izquierdo |
| Q43 | varchar |  |  | SI | Miembros superiores |
| Q44 | varchar |  |  | SI | Abdomen |
| Q45 | varchar |  |  | SI | Cuello |
| Q46 | varchar |  |  | SI | Viceromegalia |
| Q47 | varchar |  |  | SI | Chequeo antecedentes de Cancer |
| Q48 | varchar |  |  | SI | Chequeo enfermedades reumáticas |
| Q49 | varchar |  |  | SI | Chequeo de infecciones crónicas |
| Q50 | varchar |  |  | SI | Observaciones en los Chequeos de Antecedentes |
| Q51 | varchar |  |  | SI | Nariz |
| Q52 | varchar |  |  | SI | Observaciones en Cabeza y Cuello |
| Q53 | varchar |  |  | SI | Boca |
| Q54 | varchar |  |  | SI | Reflejos |
| Q55 | varchar |  |  | SI | Signos meningeos |
| Q56 | varchar |  |  | SI | Motor |
| Q57 | varchar |  |  | SI | Pupilas |
| Q58 | varchar |  |  | SI | Habla |
| Q59 | varchar |  |  | SI | Examen físico segmentar |
| Q60 | varchar |  |  | SI | Observaciones en Respiratorio |
| Q61 | bit |  |  | SI | Eupneico, murmurio vesicular fisiologico |
| Q62 | bit |  |  | SI | Taquipneico |
| Q63 | bit |  |  | SI | Dispneico |
| Q64 | varchar |  |  | SI | Descrición del examen físico |
| Q65 | varchar |  |  | SI | Respiratorio |
| Q66 | varchar |  |  | SI | Cardiovascular |
| Q67 | varchar |  |  | SI | Observaciones en Cardiovascular |
| Q68 | bit |  |  | SI | Ritmo regular, en dos tiempos, sin soplos, ruidos ... |
| Q69 | bit |  |  | SI | Ritmo regular en dos tiempos con soplo sistolico |
| Q70 | bit |  |  | SI | Taquicardia |
| Q71 | varchar |  |  | SI | Abdomen |
| Q72 | varchar |  |  | SI | Observaciones en Abdomen |
| Q73 | bit |  |  | SI | Abdomen depresible, sin defensa o puntos dolorosos |
| Q74 | bit |  |  | SI | Ausencia de masas o viceromegalias |
| Q75 | varchar |  |  | SI | Genitoanal |
| Q76 | varchar |  |  | SI | Observaciones en Genitoanal |
| Q77 | bit |  |  | SI | Genitalia, anus y carecteres sexuais esperados par... |
| Q78 | varchar |  |  | SI | Extremidades |
| Q79 | varchar |  |  | SI | Observación de Extremidades  |
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
# SQLUser.LBC_Collection

**Schema:** SQLUser
**Columnas:** 176
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCOL_RowID | bigint | PK |  | NO | - |
| LBCCOL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCOL_Comments | varchar |  |  | SI | Comments |
| LBCCOL_CreatedDate | date |  |  | SI | Created Date |
| LBCCOL_CreatedTime | time |  |  | SI | Created Time |
| LBCCOL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCOL_Owner | varchar |  |  | SI | Owner |
| LBCCOL_Priority | double |  |  | SI | Priority - the lowest value will be the default Sp... |
| LBCCOL_TestItem_DR | bigint |  | FK | SI | TestItem DR |
| LBCCOL_TestSetItem_DR | varchar |  | FK | SI | TestSetItem DR |
| LBCCOL_TestSet_DR | bigint |  | FK | SI | TestSet DR |
| LBCCOL_Type | varchar |  |  | SI | Type
Note: TS is TestSetRevision, TSI is TestSetR... |
| LBCCOL_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCOL_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCOL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Data Inicio |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Informante |
| Q04 | - |  |  | SI | Procedencia |
| Q05 | - |  |  | SI | Procedencia |
| Q06 | - |  |  | SI | Anamnesis próxima |
| Q07 | - |  |  | SI | Chequeo Antecedentes Vasculares |
| Q08 | - |  |  | SI | Chequeo de Miocardio |
| Q09 | - |  |  | SI | Capacidad Funcional |
| Q10 | - |  |  | SI | Chequeo Ritmo Cardíaco |
| Q100 | - |  |  | SI | HTML |
| Q100TxtOnly | - |  |  | SI | HTML Plain Text Only |
| Q101 | - |  |  | SI | Temperatura |
| Q101ObsDR | - |  |  | SI | Temperatura DR |
| Q102 | - |  |  | SI | Presión arterial sistólica PAS |
| Q102ObsDR | - |  |  | SI | Presión arterial sistólica PAS DR |
| Q103 | - |  |  | SI | Presión arterial diastólica PAD |
| Q103ObsDR | - |  |  | SI | Presión arterial diastólica PAD DR |
| Q104 | - |  |  | SI | Presión arterial media PAM |
| Q104ObsDR | - |  |  | SI | Presión arterial media PAM DR |
| Q105 | - |  |  | SI | Talla |
| Q105ObsDR | - |  |  | SI | Talla DR |
| Q106 | - |  |  | SI | Peso |
| Q106ObsDR | - |  |  | SI | Peso DR |
| Q107 | - |  |  | SI | Índice de masa corporal |
| Q107ObsDR | - |  |  | SI | Índice de masa corporal DR |
| Q108 | - |  |  | SI | Frecuencia cardiaca |
| Q108ObsDR | - |  |  | SI | Frecuencia cardiaca DR |
| Q109 | - |  |  | SI | Frecuencia respiratoria |
| Q109ObsDR | - |  |  | SI | Frecuencia respiratoria DR |
| Q11 | - |  |  | SI | Condiciones familiares o sociales |
| Q110 | - |  |  | SI | Saturación oxígeno |
| Q110ObsDR | - |  |  | SI | Saturación oxígeno DR |
| Q12 | - |  |  | SI | Chequeo Válvulas Cardíacas |
| Q13 | - |  |  | SI | Estado nutricional |
| Q14 | - |  |  | SI | Chequeo Enf. Coronaria |
| Q15 | - |  |  | SI | Medicamentos de uso habitual |
| Q16 | - |  |  | SI | Observaciones en antecedentes |
| Q17 | - |  |  | SI | Observaciones en examen físico general |
| Q18 | - |  |  | SI | Actitud |
| Q19 | - |  |  | SI | Repiración |
| Q20 | - |  |  | SI | Piel y mucosas |
| Q21 | - |  |  | SI | Abdomen |
| Q22 | - |  |  | SI | Dolor |
| Q23 | - |  |  | SI | Sistema Nervoso |
| Q25 | - |  |  | SI | Observaciones en Sistema Nervoso |
| Q26 | - |  |  | SI | Glasgow |
| Q26ObsDR | - |  |  | SI | Glasgow DR |
| Q27 | - |  |  | SI | Chequeo Hipertensión Arterial |
| Q28 | - |  |  | SI | Chequeo Historia Renal y Vía Urinaria |
| Q29 | - |  |  | SI | Chequeo de antecedentes de coagulación |
| Q30 | - |  |  | SI | Diabetes |
| Q31 | - |  |  | SI | Chequeo de antecedentes respiratoreos |
| Q32 | - |  |  | SI | Chequeo aparelho digestivo |
| Q33 | - |  |  | SI | Chequeo de antecedentes neurológicos |
| Q34 | - |  |  | SI | Cabeza y cuello |
| Q35 | - |  |  | SI | Chequeo de antecedentes |
| Q36 | - |  |  | SI | Ojos |
| Q37 | - |  |  | SI | Chequeo antecedentes comportamento |
| Q38 | - |  |  | SI | Chequeo antecedentes a. reprodutor femenino |
| Q39 | - |  |  | SI | Chequeo antecedentes tireoide y suprarenales |
| Q40 | - |  |  | SI | Oido |
| Q41 | - |  |  | SI | Oido |
| Q42 | - |  |  | SI | Membro inferior izquierdo |
| Q43 | - |  |  | SI | Miembros superiores |
| Q44 | - |  |  | SI | Abdomen |
| Q45 | - |  |  | SI | Cuello |
| Q46 | - |  |  | SI | Viceromegalia |
| Q47 | - |  |  | SI | Chequeo antecedentes de Cancer |
| Q48 | - |  |  | SI | Chequeo enfermedades reumáticas |
| Q49 | - |  |  | SI | Chequeo de infecciones crónicas |
| Q50 | - |  |  | SI | Observaciones en los Chequeos de Antecedentes |
| Q51 | - |  |  | SI | Nariz |
| Q52 | - |  |  | SI | Observaciones en Cabeza y Cuello |
| Q53 | - |  |  | SI | Boca |
| Q54 | - |  |  | SI | Reflejos |
| Q55 | - |  |  | SI | Signos meningeos |
| Q56 | - |  |  | SI | Motor |
| Q57 | - |  |  | SI | Pupilas |
| Q58 | - |  |  | SI | Habla |
| Q59 | - |  |  | SI | Examen físico segmentar |
| Q60 | - |  |  | SI | Observaciones en Respiratorio |
| Q61 | - |  |  | SI | Eupneico, murmurio vesicular fisiologico |
| Q62 | - |  |  | SI | Taquipneico |
| Q63 | - |  |  | SI | Dispneico |
| Q64 | - |  |  | SI | Descrición del examen físico |
| Q65 | - |  |  | SI | Respiratorio |
| Q66 | - |  |  | SI | Cardiovascular |
| Q67 | - |  |  | SI | Observaciones en Cardiovascular |
| Q68 | - |  |  | SI | Ritmo regular, en dos tiempos, sin soplos, ruidos ... |
| Q69 | - |  |  | SI | Ritmo regular en dos tiempos con soplo sistolico |
| Q70 | - |  |  | SI | Taquicardia |
| Q71 | - |  |  | SI | Abdomen |
| Q72 | - |  |  | SI | Observaciones en Abdomen |
| Q73 | - |  |  | SI | Abdomen depresible, sin defensa o puntos dolorosos |
| Q74 | - |  |  | SI | Ausencia de masas o viceromegalias |
| Q75 | - |  |  | SI | Genitoanal |
| Q76 | - |  |  | SI | Observaciones en Genitoanal |
| Q77 | - |  |  | SI | Genitalia, anus y carecteres sexuais esperados par... |
| Q78 | - |  |  | SI | Extremidades |
| Q79 | - |  |  | SI | Observación de Extremidades |
| Q80 | - |  |  | SI | Conclusion |
| Q81 | - |  |  | SI | Enfermedad de notificacion compulsoria |
| Q82 | - |  |  | SI | Enfermidad con alto riesgo en contaminacion comuni... |
| Q83 | - |  |  | SI | Condicion cronica para el paciente, com acutizacio... |
| Q84 | - |  |  | SI | Condicion aguda o nueva para el paciente |
| Q85 | - |  |  | SI | Condicion de Garantia GES |
| Q86 | - |  |  | SI | Plan |
| Q87 | - |  |  | SI | Notificar atendimiento a garantia GES |
| Q88 | - |  |  | SI | Notificar nueva garantia GES |
| Q89 | - |  |  | SI | Solicitar examenes de laboratorio |
| Q90 | - |  |  | SI | Solicitar examenes de imagen |
| Q91 | - |  |  | SI | Solicitar examen anatomopatologico |
| Q92 | - |  |  | SI | Periodo de observacion de la evolucion en la unida... |
| Q93 | - |  |  | SI | Hospitalizacion |
| Q94 | - |  |  | SI | Solicitar parecer especializado |
| Q95 | - |  |  | SI | Retorno programado |
| Q96 | - |  |  | SI | Examenes laboratorio |
| Q97 | - |  |  | SI | Examenes Imagenes |
| Q98 | - |  |  | SI | Examenes histopatologicos |
| Q99 | - |  |  | SI | imagen |
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
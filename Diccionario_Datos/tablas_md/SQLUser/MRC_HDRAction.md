# SQLUser.MRC_HDRAction

**Schema:** SQLUser
**Columnas:** 202
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HDRA_ParRef | bigint | PK |  | NO | HDR config Parent Reference |
| HDRA_ActionContext | varchar |  |  | SI | Action Context |
| HDRA_ActionGroups | varchar |  |  | SI | Action Group |
| HDRA_ActionType_DR | bigint |  | FK | SI | Action Type DR |
| HDRA_CanCreateRecord | varchar |  |  | SI | Can Create Record |
| HDRA_Chart_DR | bigint |  | FK | SI | EPR Chart |
| HDRA_Childsub | double |  |  | NO | Childsub |
| HDRA_Code | varchar |  |  | NO | Code	 |
| HDRA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HDRA_CreatedDate | date |  |  | SI | Created Date |
| HDRA_CreatedTime | time |  |  | SI | Created Time |
| HDRA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HDRA_DateFrom | date |  |  | SI | DateFrom |
| HDRA_DateTo | date |  |  | SI | DateTo |
| HDRA_Desc | varchar |  |  | NO | Description  |
| HDRA_DispOrdDet | varchar |  |  | SI | Always Display Order Details |
| HDRA_Filter | varchar |  |  | SI | Filter |
| HDRA_InfoPaneSize | double |  |  | SI | Info Pane Size (Percentage) |
| HDRA_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| HDRA_RowId | varchar |  |  | NO | - |
| HDRA_Seq | integer |  |  | SI | DateTo |
| HDRA_UpdatedDate | date |  |  | SI | Updated Date |
| HDRA_UpdatedTime | time |  |  | SI | Updated Time |
| HDRA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| HDRA_WorkFlow | bigint |  |  | SI | Workflow |
| Q01 | - |  |  | SI | Fecha de Ingreso |
| Q02 | - |  |  | SI | Hora de Ingreso |
| Q03 | - |  |  | SI | Información entregada por |
| Q04 | - |  |  | SI | Procedencia |
| Q05 | - |  |  | SI | Procedencia |
| Q06 | - |  |  | SI | Anamnesis Próxima |
| Q07 | - |  |  | SI | Antecedentes Perinatales |
| Q08 | - |  |  | SI | Inmunizaciones |
| Q09 | - |  |  | SI | Condición funcional basal |
| Q10 | - |  |  | SI | Red de Salud, Contacto habitual |
| Q100 | - |  |  | SI | Orejas |
| Q101 | - |  |  | SI | Nariz |
| Q102 | - |  |  | SI | Boca |
| Q103 | - |  |  | SI | Cuello |
| Q104 | - |  |  | SI | Tórax |
| Q105 | - |  |  | SI | Murmurio vesicular |
| Q106 | - |  |  | SI | Tonos cardiacos |
| Q107 | - |  |  | SI | Abdomen |
| Q108 | - |  |  | SI | Cordón |
| Q109 | - |  |  | SI | Caderas |
| Q11 | - |  |  | SI | Condiciones familiares o sociales |
| Q110 | - |  |  | SI | Genitales femininos |
| Q111 | - |  |  | SI | Genitales masculinos |
| Q112 | - |  |  | SI | Extremidades |
| Q113 | - |  |  | SI | Pies |
| Q114 | - |  |  | SI | Edad gestacional en semanas según FUR |
| Q115 | - |  |  | SI | Edad gestacional en semanas según examen físico |
| Q116 | - |  |  | SI | Edad gestacional en semanas según examen neurológi... |
| Q117 | - |  |  | SI | Pediatra Responsable |
| Q118 | - |  |  | SI | Becado |
| Q119 | - |  |  | SI | Horas de vida |
| Q12 | - |  |  | SI | Crecimiento |
| Q120 | - |  |  | SI | Reserva1 |
| Q121 | - |  |  | SI | Temperatura Axilar |
| Q121ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q122 | - |  |  | SI | Talla |
| Q122ObsDR | - |  |  | SI | Talla DR |
| Q123 | - |  |  | SI | Índice de masa corporal IMC |
| Q123ObsDR | - |  |  | SI | Índice de masa corporal IMC DR |
| Q124 | - |  |  | SI | Saturación oxígeno SPO2 |
| Q124ObsDR | - |  |  | SI | Saturación oxígeno SPO2 DR |
| Q125 | - |  |  | SI | Frecuencia cardiaca |
| Q125ObsDR | - |  |  | SI | Frecuencia cardiaca DR |
| Q126 | - |  |  | SI | Frecuencia respiratória |
| Q126ObsDR | - |  |  | SI | Frecuencia respiratória DR |
| Q127 | - |  |  | SI | Peso |
| Q127ObsDR | - |  |  | SI | Peso DR |
| Q128 | - |  |  | SI | Reserva2 |
| Q129 | - |  |  | SI | Local |
| Q13 | - |  |  | SI | Pérdida reciente de peso |
| Q130 | - |  |  | SI | Temperatura Rectal |
| Q130ObsDR | - |  |  | SI | Temperatura Rectal DR |
| Q14 | - |  |  | SI | Desarollo Sicomotor |
| Q15 | - |  |  | SI | Medicamentos de uso frecuente o habitual |
| Q16 | - |  |  | SI | Notas complementarias |
| Q17 | - |  |  | SI | Estado físico general |
| Q18 | - |  |  | SI | Actitud |
| Q19 | - |  |  | SI | Disnea |
| Q20 | - |  |  | SI | Febril |
| Q21 | - |  |  | SI | Pálido |
| Q22 | - |  |  | SI | Ictérico |
| Q23 | - |  |  | SI | Sistema Nervioso Central |
| Q25 | - |  |  | SI | Sistema Nervioso Central |
| Q26 | - |  |  | SI | Reflejos y tono muscular normal |
| Q27 | - |  |  | SI | Ausencia de rigidez nucal |
| Q28 | - |  |  | SI | Pupilas isocóricas reativas |
| Q29 | - |  |  | SI | Fontanela Bregmática |
| Q30 | - |  |  | SI | Columna vertebral |
| Q31 | - |  |  | SI | Circunferencia craneana dentro de los límites norm... |
| Q32 | - |  |  | SI | Reflejos presentes |
| Q33 | - |  |  | SI | Respiración |
| Q34 | - |  |  | SI | Ojos |
| Q35 | - |  |  | SI | Ojos |
| Q36 | - |  |  | SI | Ojos de aspecto normal, bilateralmiente |
| Q37 | - |  |  | SI | Conjuntivas hiperhémicas, con exudado |
| Q38 | - |  |  | SI | Blefaritis |
| Q39 | - |  |  | SI | Ojo |
| Q40 | - |  |  | SI | Oido |
| Q41 | - |  |  | SI | Oido |
| Q42 | - |  |  | SI | Condutos auditivos externos y timpanos de aspecto ... |
| Q43 | - |  |  | SI | Conduto auditivo externo direito hiperemiado e ede... |
| Q44 | - |  |  | SI | Conducto auditivo externo izquierdo hiperemiado y ... |
| Q45 | - |  |  | SI | Timpano derecho abaulado y hiperemiado |
| Q46 | - |  |  | SI | Timpano derecho roto |
| Q47 | - |  |  | SI | Timpano izquierdo abaulado y hiperemiado |
| Q48 | - |  |  | SI | Timpano izquierdo roto |
| Q49 | - |  |  | SI | Secrecion purulenta en el conducto auditivo derech... |
| Q50 | - |  |  | SI | Secrecion purulenta en el conducto auditivo izquie... |
| Q51 | - |  |  | SI | Nariz, Boca, Pescoco |
| Q52 | - |  |  | SI | Nariz, Boca y Pescoco |
| Q53 | - |  |  | SI | Denticion esperada para a edad |
| Q54 | - |  |  | SI | Dientes en buen estado |
| Q55 | - |  |  | SI | Dientes en malo estado |
| Q56 | - |  |  | SI | Orofaringe normal |
| Q57 | - |  |  | SI | Orofaringe hiperemiada |
| Q58 | - |  |  | SI | Amigdalas hipertrofiadas y hiperemiadas |
| Q59 | - |  |  | SI | Pulmones |
| Q60 | - |  |  | SI | Pulmones |
| Q61 | - |  |  | SI | Eupneico, murmurio vesicular fisiologico |
| Q62 | - |  |  | SI | Taquipneico |
| Q63 | - |  |  | SI | Dispneico |
| Q64 | - |  |  | SI | Roncos |
| Q65 | - |  |  | SI | Sibilos expiratorios |
| Q66 | - |  |  | SI | Coracion |
| Q67 | - |  |  | SI | Coracion |
| Q68 | - |  |  | SI | Ritmo regular, en dos tiempos, sin soplos, ruidos ... |
| Q69 | - |  |  | SI | Ritmo regular en dos tiempos con soplo sistolico |
| Q70 | - |  |  | SI | Taquicardia |
| Q71 | - |  |  | SI | Abdomen |
| Q72 | - |  |  | SI | Abdomen |
| Q73 | - |  |  | SI | Abdomen depresible, sin defensa o puntos dolorosos |
| Q74 | - |  |  | SI | Ausencia de masas o viceromegalias |
| Q75 | - |  |  | SI | Genitoanal |
| Q76 | - |  |  | SI | Genitoanal |
| Q77 | - |  |  | SI | Genitalia, anus y carecteres sexuais esperados par... |
| Q78 | - |  |  | SI | Extremidades |
| Q79 | - |  |  | SI | Extremidades |
| Q80 | - |  |  | SI | Conclusion |
| Q81 | - |  |  | SI | Enfermedad de notificacion obligatoria |
| Q82 | - |  |  | SI | Enfermedad con alto riesgo en contaminacion comuni... |
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
| Q99 | - |  |  | SI | Piel |
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
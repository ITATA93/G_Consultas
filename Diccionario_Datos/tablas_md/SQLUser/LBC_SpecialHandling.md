# SQLUser.LBC_SpecialHandling

**Schema:** SQLUser
**Columnas:** 223
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSH_RowID | bigint | PK |  | NO | - |
| LBCSH_Code | varchar |  |  | NO | Code |
| LBCSH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSH_CreatedDate | date |  |  | SI | Created Date |
| LBCSH_CreatedTime | time |  |  | SI | Created Time |
| LBCSH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSH_DateFrom | date |  |  | SI | Date From |
| LBCSH_DateTo | date |  |  | SI | Date To |
| LBCSH_Desc | varchar |  |  | SI | Description |
| LBCSH_HideForCollection | varchar |  |  | SI | Hide for Collection |
| LBCSH_HideForProcessing | varchar |  |  | SI | Hide for Processing |
| LBCSH_HideForReceive | varchar |  |  | SI | Hide for Receive |
| LBCSH_HideForStorage | varchar |  |  | SI | Hide for Storage |
| LBCSH_HideForTransfers | varchar |  |  | SI | Hide for Transfers |
| LBCSH_Notes | varchar |  |  | SI | Notes |
| LBCSH_Owner | varchar |  |  | SI | Owner |
| LBCSH_PopUpNotes | varchar |  |  | SI | Pup-up notes flag |
| LBCSH_Sequence | integer |  |  | SI | Sequence |
| LBCSH_Type | varchar |  |  | SI | Special Handling Type
StandardType: LabSpecialHan... |
| LBCSH_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSH_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Intervención propuesta |
| Q02 | - |  |  | SI | Fecha de Evaluación |
| Q03 | - |  |  | SI | Hora de Evaluación |
| Q04 | - |  |  | SI | Capacidad Funcional |
| Q05 | - |  |  | SI | Antecedentes Anestésicos relevantes |
| Q06 | - |  |  | SI | Cabeza |
| Q07 | - |  |  | SI | Dentadura |
| Q08 | - |  |  | SI | Uso de Prótesis |
| Q09 | - |  |  | SI | Descripción Cabeza |
| Q10 | - |  |  | SI | Cuello |
| Q100 | - |  |  | SI | Recuento TP |
| Q101 | - |  |  | SI | Recuento TTPA |
| Q102 | - |  |  | SI | Comentarios Recuento TP |
| Q103 | - |  |  | SI | Comentarios Recuento TTPA |
| Q104 | - |  |  | SI | Paciente con Proceso Infeccioso Activo |
| Q105 | - |  |  | SI | Paciente con Proceso Infeccioso Activo (Texto Libr... |
| Q106 | - |  |  | SI | Posición Materna |
| Q107 | - |  |  | SI | Dilatación Cervical (cm) |
| Q108 | - |  |  | SI | Segunda cirugía |
| Q109 | - |  |  | SI | Farmacológicos |
| Q11 | - |  |  | SI | Movilidad del cuello |
| Q110 | - |  |  | SI | Comentarios Farmacológicos |
| Q111 | - |  |  | SI | Ecocardiograma |
| Q112 | - |  |  | SI | Comentarios Electrocardiograma |
| Q113 | - |  |  | SI | FUR |
| Q114 | - |  |  | SI | Farmacológicos |
| Q115 | - |  |  | SI | Antecedentes Reumatológicos |
| Q116 | - |  |  | SI | Observaciones Reumatológicas |
| Q117 | - |  |  | SI | Antecedentes Quirurgicos |
| Q118 | - |  |  | SI | METS |
| Q119 | - |  |  | SI | Horas de Ayuno |
| Q12 | - |  |  | SI | Apertura bucal |
| Q120 | - |  |  | SI | Profesional Evaluador |
| Q121 | - |  |  | SI | Anestesiólogo Tratante Toma Conocimiento |
| Q122 | - |  |  | SI | Postoperatorio |
| Q123 | - |  |  | SI | Edentado |
| Q124 | - |  |  | SI | Pieza Dental Suelta |
| Q125 | - |  |  | SI | INR |
| Q126 | - |  |  | SI | Creatinina |
| Q127 | - |  |  | SI | Sin Antecedentes Relevantes |
| Q128 | - |  |  | SI | Resto Sin Antecedentes |
| Q129 | - |  |  | SI | METS |
| Q13 | - |  |  | SI | Endentado |
| Q130 | - |  |  | SI | Plan Anestésico |
| Q131 | - |  |  | SI | Monitorización invasiva |
| Q132 | - |  |  | SI | Paciente rechaza anestesia regional |
| Q133 | - |  |  | SI | Accesos Vasculares |
| Q134 | - |  |  | SI | Comentarios INR |
| Q135 | - |  |  | SI | Comentarios Creatinina |
| Q136 | - |  |  | SI | Plan Anestésico |
| Q137 | - |  |  | SI | Reumatológicos |
| Q138 | - |  |  | SI | Comentarios Reumatológicos |
| Q139 | - |  |  | SI | Alergias relevantes para la cirugía |
| Q14 | - |  |  | SI | Descripción Dentadura |
| Q140 | - |  |  | SI | Comentario Alergias |
| Q141 | - |  |  | SI | Antecedentes relevantes para la cirugía |
| Q142 | - |  |  | SI | Comentario&nbsp |
| Q143 | - |  |  | SI | Antecedentes Social/Hábitos |
| Q144 | - |  |  | SI | Comentarios&nbsp |
| Q145 | - |  |  | SI | Comentario Capacidad Funcional |
| Q146 | - |  |  | SI | Condiciones de Intubación |
| Q147 | - |  |  | SI | Vía aérea difícil |
| Q148 | - |  |  | SI | Observaciones Cardiovasculares |
| Q149 | - |  |  | SI | Observaciones Respiratorios |
| Q15 | - |  |  | SI | Distancia Tiro-Mentoneana |
| Q150 | - |  |  | SI | Observaciones Neurológicos |
| Q151 | - |  |  | SI | Observaciones Endocrinos |
| Q152 | - |  |  | SI | Observaciones Renales |
| Q153 | - |  |  | SI | Observaciones Hepáticos |
| Q154 | - |  |  | SI | Observaciones Digestivos |
| Q155 | - |  |  | SI | Observaciones Hemato - Oncológicos |
| Q156 | - |  |  | SI | Observaciones Obstétricos |
| Q157 | - |  |  | SI | Observaciones Pediátricos |
| Q158 | - |  |  | SI | Observaciones Anestésicos |
| Q159 | - |  |  | SI | Observaciones Farmacológicos |
| Q16 | - |  |  | SI | Ayuno |
| Q17 | - |  |  | SI | Cardiovasculares |
| Q18 | - |  |  | SI | Cardiovasculares |
| Q19 | - |  |  | SI | Comentarios Cardiovasculares |
| Q20 | - |  |  | SI | Respiratorios |
| Q21 | - |  |  | SI | Respiratorios |
| Q22 | - |  |  | SI | Comentarios Respiratorios |
| Q23 | - |  |  | SI | Neurológicos |
| Q24 | - |  |  | SI | Neurológicos |
| Q25 | - |  |  | SI | Comentarios Neurológicos |
| Q26 | - |  |  | SI | Obstétricos |
| Q27 | - |  |  | SI | Obstétricos |
| Q28 | - |  |  | SI | Observaciones Obst |
| Q29 | - |  |  | SI | Anestésicos |
| Q30 | - |  |  | SI | Comentarios Anestésicos |
| Q31 | - |  |  | SI | Renales |
| Q32 | - |  |  | SI | Renales |
| Q33 | - |  |  | SI | Comentarios Renales |
| Q34 | - |  |  | SI | Hepáticos |
| Q35 | - |  |  | SI | Hepáticos |
| Q36 | - |  |  | SI | Comentarios Hepáticos |
| Q37 | - |  |  | SI | Digestivos |
| Q38 | - |  |  | SI | Digestivos |
| Q39 | - |  |  | SI | Comentarios Digestivos |
| Q40 | - |  |  | SI | Pediátricos |
| Q41 | - |  |  | SI | Comentarios Pediátricos |
| Q42 | - |  |  | SI | Endocrinos |
| Q43 | - |  |  | SI | Endocrinos |
| Q44 | - |  |  | SI | Hemato - Oncológicos |
| Q45 | - |  |  | SI | Comentarios Hemato - Oncológicos |
| Q46 | - |  |  | SI | Nivel de Actividad |
| Q47 | - |  |  | SI | Cardíaco |
| Q48 | - |  |  | SI | Descripción Cardíaco |
| Q49 | - |  |  | SI | Pulmonar |
| Q50 | - |  |  | SI | Descripción Pulmonar |
| Q51 | - |  |  | SI | Exámenes Pre-Operatorios |
| Q52 | - |  |  | SI | Observaciones Exámenes Pre-Operatorios |
| Q53 | - |  |  | SI | Pase Anestésico |
| Q54 | - |  |  | SI | Fundamento |
| Q55 | - |  |  | SI | Plan Anestésico |
| Q56 | - |  |  | SI | Consentimiento Informado |
| Q57 | - |  |  | SI | Profesional Responsable |
| Q58 | - |  |  | SI | Anestésicos |
| Q59 | - |  |  | SI | Pediátricos |
| Q60 | - |  |  | SI | Comentarios Endocrinos |
| Q61 | - |  |  | SI | Hemato - Oncológicos |
| Q62 | - |  |  | SI | ASA |
| Q63 | - |  |  | SI | Mallampati |
| Q64 | - |  |  | SI | Observaciones |
| Q65 | - |  |  | SI | Otros elementos del Examen Físico |
| Q66 | - |  |  | SI | Fecha última Ingesta |
| Q67 | - |  |  | SI | Hora última Ingesta |
| Q68 | - |  |  | SI | Otra |
| Q69 | - |  |  | SI | Profesional de Salud |
| Q70 | - |  |  | SI | Plan Anestésio |
| Q71 | - |  |  | SI | Otros Antecedentes |
| Q72 | - |  |  | SI | Paciente no aporta datos |
| Q73 | - |  |  | SI | Paciente no aporta datos (texto) |
| Q74 | - |  |  | SI | Paciente no aporta datos Chequeo Antecedentes |
| Q75 | - |  |  | SI | Paciente no aporta datos (texto) chequeo Anteceden... |
| Q76 | - |  |  | SI | Otros |
| Q77 | - |  |  | SI | Distancia Interincisivos (Apertura bucal) |
| Q78 | - |  |  | SI | Movilidad del cuello |
| Q79 | - |  |  | SI | Hemograma / Hematocrito / Hb |
| Q80 | - |  |  | SI | Comentarios Hemograma / Hematocrito / Hb |
| Q81 | - |  |  | SI | Recuento Plaquetas |
| Q82 | - |  |  | SI | Comentarios Recuento Plaquetas |
| Q83 | - |  |  | SI | Glicemia / HGT	 |
| Q84 | - |  |  | SI | Comentario Glicemia / HGT	 |
| Q85 | - |  |  | SI | Pruebas de Función Renal |
| Q86 | - |  |  | SI | Comentarios Pruebas de Función Renal |
| Q87 | - |  |  | SI | Pruebas de Función Hepática |
| Q88 | - |  |  | SI | Comentarios Pruebas de Función Hepática |
| Q89 | - |  |  | SI | Electrolitos Plasmáticos |
| Q90 | - |  |  | SI | Comentarios Electrolitos Plasmáticos |
| Q91 | - |  |  | SI | Electrocardiograma |
| Q92 | - |  |  | SI | Comentario Electrocardiograma |
| Q93 | - |  |  | SI | Radiografía de Tórax |
| Q94 | - |  |  | SI | Comentarios Radiografía de Tórax |
| Q95 | - |  |  | SI | Otros Exámenes Preoperatorios |
| Q96 | - |  |  | SI | Peso (kg) |
| Q96ObsDR | - |  |  | SI | Peso (kg) DR |
| Q97 | - |  |  | SI | Talla (cms) |
| Q97ObsDR | - |  |  | SI | Talla (cms) DR |
| Q98 | - |  |  | SI | IMC |
| Q99 | - |  |  | SI | Descripción de Antecedentes |
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
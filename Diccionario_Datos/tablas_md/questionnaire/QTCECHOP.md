# questionnaire.QTCECHOP

> Chequeo Pre-Operatorio

**Schema:** questionnaire
**Columnas:** 225
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Chequeo Pre-Operatorio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Conocimiento de la Cirugía / Procedimiento |
| Q02 | varchar |  |  | SI | Porta Brazalete de Identificación con datos comple... |
| Q03 | varchar |  |  | SI | Ayuno |
| Q04 | varchar |  |  | SI | Marcación Lateralidad |
| Q05 | varchar |  |  | SI | Premedicación |
| Q06 | varchar |  |  | SI | Lavado Intestinal |
| Q07 | varchar |  |  | SI | Vaciamiento Vesical |
| Q08 | varchar |  |  | SI | Transfusión |
| Q09 | varchar |  |  | SI | Chequeo de Patología Concomitante |
| Q10 | varchar |  |  | SI | Comentario CG |
| Q100 | varchar |  |  | SI | Otro(s) Articulo(s) |
| Q101 | varchar |  |  | SI | Camisa |
| Q102 | varchar |  |  | SI | Comentario |
| Q103 | varchar |  |  | SI | Botas |
| Q104 | varchar |  |  | SI | Comentario |
| Q105 | varchar |  |  | SI | Gorro |
| Q106 | varchar |  |  | SI | Comentario |
| Q107 | varchar |  |  | SI | PCR Covid |
| Q108 | date |  |  | SI | Fecha Resultado |
| Q109 | varchar |  |  | SI | Prueba de Compatibilidad |
| Q11 | varchar |  |  | SI | Comentario BI |
| Q110 | varchar |  |  | SI | Comentario |
| Q111 | varchar |  |  | SI | ¿Tiene Aislamiento? |
| Q112 | varchar |  |  | SI | Comentario |
| Q113 | varchar |  |  | SI | ¿Se realiza Tricotomía? |
| Q114 | varchar |  |  | SI | Comentario |
| Q115 | varchar |  |  | SI | ¿Se Usa Solución Jabonosa en Baño? |
| Q116 | date |  |  | SI | Fecha |
| Q117 | time |  |  | SI | Hora |
| Q118 | varchar |  |  | SI | ¿Quién lo Realiza? |
| Q119 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q119ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q12 | varchar |  |  | SI | Comentario CP |
| Q120 | varchar |  |  | SI | Temperatura Axilar |
| Q120ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q121 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q121ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q122 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q122ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q123 | varchar |  |  | SI | Presión Arterial Media |
| Q124 | varchar |  |  | SI | Peso |
| Q124ObsDR | varchar |  | FK | SI | Peso DR |
| Q125 | varchar |  |  | SI | Hemoglucotest |
| Q125ObsDR | varchar |  | FK | SI | Hemoglucotest DR |
| Q126 | varchar |  |  | SI | Observaciones |
| Q127 | varchar |  |  | SI | Dispositivos Invasivos |
| Q128 | varchar |  |  | SI | Comentario Dispositivos Invasivos |
| Q129 | varchar |  |  | SI | Catéter Venoso Central |
| Q13 | varchar |  |  | SI | Comentario A |
| Q130 | varchar |  |  | SI | Comentario Catéter Venoso Central |
| Q131 | varchar |  |  | SI | Vía Venosa Periférica |
| Q132 | varchar |  |  | SI | Comentario Vía Venosa Periférica |
| Q133 | varchar |  |  | SI | Sonda Nasogátrica |
| Q134 | varchar |  |  | SI | Comentario Sonda Nasogátrica |
| Q135 | varchar |  |  | SI | Gastrostomía |
| Q136 | varchar |  |  | SI | Comentario Gastrostomía |
| Q137 | varchar |  |  | SI | Traqueostomía |
| Q138 | varchar |  |  | SI | Comentario Traqueostomía |
| Q139 | varchar |  |  | SI | Drenaje Ventricular Externo |
| Q14 | varchar |  |  | SI | Comentario ML |
| Q140 | varchar |  |  | SI | Comentario Drenaje Ventricular Externo |
| Q141 | varchar |  |  | SI | Drenaje |
| Q142 | varchar |  |  | SI | Comentario Drenaje |
| Q143 | varchar |  |  | SI | Catéter Urinario Permanente |
| Q144 | varchar |  |  | SI | Comentario Catéter Urinario Permanente |
| Q145 | varchar |  |  | SI | Otro (s) Dispositivo(s) |
| Q147 | varchar |  |  | SI | Ficha Médica |
| Q148 | varchar |  |  | SI | Comentario Ficha Médica |
| Q149 | varchar |  |  | SI | Evaluación Pre-anestésica |
| Q15 | varchar |  |  | SI | Comentario CM |
| Q150 | varchar |  |  | SI | Comentario Evaluación Pre-anestésica |
| Q151 | varchar |  |  | SI | Ingreso Médico |
| Q152 | varchar |  |  | SI | Comentario Ingreso Médico |
| Q153 | varchar |  |  | SI | Ingreso de Enfermería |
| Q154 | varchar |  |  | SI | Comentario Ingreso de Enfermería |
| Q155 | varchar |  |  | SI | Escala de Riesgo LPP |
| Q156 | varchar |  |  | SI | Comentario Escala de Riesgo LPP |
| Q157 | varchar |  |  | SI | Escala de Riesgo Caídas |
| Q158 | varchar |  |  | SI | Comentario Escala de Riesgo Caídas |
| Q159 | time |  |  | SI | Hora Salida de Piso |
| Q16 | varchar |  |  | SI | Comentario P |
| Q160 | varchar |  |  | SI | PREPARACIÓN PRE-OPERATORIA |
| Q161 | varchar |  |  | SI | ARTÍCULOS RETIRADOS |
| Q162 | varchar |  |  | SI | VESTIMENTA QUIRÚRGICA |
| Q163 | varchar |  |  | SI | EXÁMENES DE LABORATORIO - IMÁGENES PARA LA CIRUGÍA... |
| Q164 | varchar |  |  | SI | GRUPO RH |
| Q165 | varchar |  |  | SI | AISLAMIENTO |
| Q166 | varchar |  |  | SI | PREPARACIÓN DE LA PIEL |
| Q167 | varchar |  |  | SI | SIGNOS VITALES |
| Q168 | varchar |  |  | SI | USO DE INVASIVOS / INFUSIONES |
| Q169 | varchar |  |  | SI | DOCUMENTACIÓN ENVIADA A PABELLÓN |
| Q170 | varchar |  |  | SI | Ambulatorio |
| Q171 | varchar |  |  | SI | Comentarios |
| Q172 | varchar |  |  | SI | Comentarios |
| Q173 | varchar |  |  | SI | Comentarios |
| Q174 | varchar |  |  | SI | Comentarios |
| Q175 | varchar |  |  | SI | Comentarios |
| Q176 | varchar |  |  | SI | Comentarios |
| Q177 | varchar |  |  | SI | Comentarios |
| Q178 | varchar |  |  | SI | Comentarios |
| Q179 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q179ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q180 | varchar |  |  | SI | Saturación de Oxígeno |
| Q180ObsDR | varchar |  | FK | SI | Saturación de Oxígeno DR |
| Q181 | varchar |  |  | SI | Otras Observaciones Generales |
| Q182 | varchar |  |  | SI | Alergias |
| Q183 | varchar |  |  | SI | Comentario de Alergias |
| Q184 | varchar |  |  | SI | Yeso |
| Q185 | varchar |  |  | SI | Comentario Yeso |
| Q20 | varchar |  |  | SI | Comentario LI |
| Q21 | varchar |  |  | SI | Comentario VV |
| Q22 | varchar |  |  | SI | Comentario T |
| Q23 | varchar |  |  | SI | Comentario MA |
| Q24 | varchar |  |  | SI | Comentario Grupo RH |
| Q26 | varchar |  |  | SI | Comentario CID |
| Q27 | varchar |  |  | SI | Comentario PR |
| Q28 | varchar |  |  | SI | Comentario JO |
| Q29 | varchar |  |  | SI | Comentario MAQ |
| Q30 | varchar |  |  | SI | Profilaxis Antibiótica |
| Q31 | varchar |  |  | SI | Medias Antiembólicas |
| Q32 | varchar |  |  | SI | Chequeo de Infusiones / Drogas In Situ |
| Q33 | varchar |  |  | SI | Prótesis |
| Q34 | varchar |  |  | SI | Joyas |
| Q35 | varchar |  |  | SI | Maquillaje |
| Q36 | varchar |  |  | SI | Esmalte de Uñas |
| Q37 | varchar |  |  | SI | Sujeciones para el Cabello (pinches) |
| Q38 | varchar |  |  | SI | Exámenes de Laboratorio - Imágenes para la Cirugía... |
| Q39 | varchar |  |  | SI | Grupo y Rh |
| Q40 | varchar |  |  | SI | Tipo Aislamiento |
| Q42 | varchar |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q43 | varchar |  |  | SI | Clasificación de Cirugía / Procedimiento |
| Q45 | varchar |  |  | SI | ¿Se realiza Tricotomía? |
| Q46 | varchar |  |  | SI | Servicio en el que se realiza Tricotomía |
| Q47 | varchar |  |  | SI | Ubicación de la Tricotomía |
| Q48 | varchar |  |  | SI | Se Usa Solución Jabonosa en Baño |
| Q49 | varchar |  |  | SI | Lugar en que se Realiza Baño Pre-Operatorio |
| Q50 | varchar |  |  | SI | Tipo de Solución Jabonosa Utilizada |
| Q51 | varchar |  |  | SI | Chequeo de medicamentos de uso habitual |
| Q52 | varchar |  |  | SI | Comentario EUN |
| Q53 | varchar |  |  | SI | Comentario SP |
| Q54 | varchar |  |  | SI | Otros Exámenes |
| Q55 | varchar |  |  | SI | Comentario CM |
| Q56 | varchar |  |  | SI | Otra Ubicación |
| Q57 | varchar |  |  | SI | Otro Lugar |
| Q58 | varchar |  |  | SI | Otra Solución |
| Q60 | varchar |  |  | SI | Comentarios Brazalete Alergias |
| Q61 | varchar |  |  | SI | Consentimiento Qx Informado Firmado |
| Q62 | varchar |  |  | SI | comentarios Consentiemiento |
| Q63 | varchar |  |  | SI | Consentimiento Anestésico Informado Firmado |
| Q64 | varchar |  |  | SI | Observaciones Vía Venosa Periférica |
| Q65 | varchar |  |  | SI | Comentario consentimiento an |
| Q66 | varchar |  |  | SI | Porta Brazalete de Alergias |
| Q67 | varchar |  |  | SI | Responsable |
| Q68 | numeric |  |  | SI | N° Vía Venosa Periférica |
| Q69 | varchar |  |  | SI | Ubicación Vía Venosa Periférica |
| Q70 | numeric |  |  | SI | N° Intentos Vía Venosa Periférica |
| Q72 | numeric |  |  | SI | N° Otro Dispositivo |
| Q73 | varchar |  |  | SI | Ubicación Otro Dispositivo |
| Q75 | numeric |  |  | SI | N° Intentos Otro Dispositivo |
| Q76 | varchar |  |  | SI | Observaciones Otro Dispositivo |
| Q77 | date |  |  | SI | Fecha de Intervención |
| Q78 | varchar |  |  | SI | Servicio Clínico |
| Q79 | varchar |  |  | SI | Sala |
| Q80 | varchar |  |  | SI | Cama |
| Q81 | varchar |  |  | SI | Diagnóstico |
| Q82 | varchar |  |  | SI | Ayuno |
| Q83 | date |  |  | SI | Fecha Última Comida |
| Q84 | time |  |  | SI | Hora Última Comida |
| Q85 | varchar |  |  | SI | Chequeo de Medicamentos de uso habitual |
| Q86 | date |  |  | SI | Fecha |
| Q87 | time |  |  | SI | Hora |
| Q88 | varchar |  |  | SI | Chequeo de Infusiones / Drogas In Situ |
| Q89 | date |  |  | SI | Fecha |
| Q90 | time |  |  | SI | Hora |
| Q91 | varchar |  |  | SI | Profilaxis Antibiótica |
| Q92 | date |  |  | SI | Fecha |
| Q93 | time |  |  | SI | Hora |
| Q94 | varchar |  |  | SI | Vaciamiento Vesical |
| Q95 | varchar |  |  | SI | Tipo Vaciamiento Vesical |
| Q96 | varchar |  |  | SI | Último registro de FUR |
| Q97 | varchar |  |  | SI | Grupo Sanguíneo |
| Q98 | varchar |  |  | SI | Lentes (Anteojos - De contacto) |
| Q99 | varchar |  |  | SI | Comentario |
| QCoJ | varchar |  |  | SI | Comentarios Solución Jabonosa |
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
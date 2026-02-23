# SQLUser.INC_ItmVenCommItems

**Schema:** SQLUser
**Columnas:** 231
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COMM_ParRef | varchar | PK |  | NO | INC_ItmVen Parent Reference |
| COMM_Childsub | double |  |  | NO | Childsub |
| COMM_CommItem_DR | bigint |  | FK | SI | Des REf CommItem |
| COMM_CreatedDate | date |  |  | SI | Created Date |
| COMM_CreatedTime | time |  |  | SI | Created Time |
| COMM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COMM_DateFrom | date |  |  | SI | DateFrom |
| COMM_DateTo | date |  |  | SI | DateTo |
| COMM_Preffered | varchar |  |  | SI | Preffered |
| COMM_Price | double |  |  | SI | Price |
| COMM_RowId | varchar |  |  | NO | - |
| COMM_UOM_DR | bigint |  | FK | SI | Des REf UOM |
| COMM_UpdatedDate | date |  |  | SI | Updated Date |
| COMM_UpdatedTime | time |  |  | SI | Updated Time |
| COMM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ146DR | - |  |  | SI | Child Reference: Infusiones Intravenosas |
| Q01 | - |  |  | SI | Conocimiento de la Cirugía / Procedimiento |
| Q02 | - |  |  | SI | Porta Brazalete de Identificación con datos comple... |
| Q03 | - |  |  | SI | Ayuno |
| Q04 | - |  |  | SI | Marcación Lateralidad |
| Q05 | - |  |  | SI | Premedicación |
| Q06 | - |  |  | SI | Lavado Intestinal |
| Q07 | - |  |  | SI | Vaciamiento Vesical |
| Q08 | - |  |  | SI | Transfusión |
| Q09 | - |  |  | SI | Chequeo de Patología Concomitante |
| Q10 | - |  |  | SI | Comentario CG |
| Q100 | - |  |  | SI | Otro(s) Articulo(s) |
| Q101 | - |  |  | SI | Camisa |
| Q102 | - |  |  | SI | Comentario |
| Q103 | - |  |  | SI | Botas |
| Q104 | - |  |  | SI | Comentario |
| Q105 | - |  |  | SI | Gorro |
| Q106 | - |  |  | SI | Comentario |
| Q107 | - |  |  | SI | PCR Covid |
| Q108 | - |  |  | SI | Fecha Resultado |
| Q109 | - |  |  | SI | Prueba de Compatibilidad |
| Q11 | - |  |  | SI | Comentario BI |
| Q110 | - |  |  | SI | Comentario |
| Q111 | - |  |  | SI | ¿Tiene Aislamiento? |
| Q112 | - |  |  | SI | Comentario |
| Q113 | - |  |  | SI | ¿Se realiza Tricotomía? |
| Q114 | - |  |  | SI | Comentario |
| Q115 | - |  |  | SI | ¿Se Usa Solución Jabonosa en Baño? |
| Q116 | - |  |  | SI | Fecha |
| Q117 | - |  |  | SI | Hora |
| Q118 | - |  |  | SI | ¿Quién lo Realiza? |
| Q119 | - |  |  | SI | Frecuencia Cardiaca |
| Q119ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q12 | - |  |  | SI | Comentario CP |
| Q120 | - |  |  | SI | Temperatura Axilar |
| Q120ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q121 | - |  |  | SI | Presión Arterial Sistólica |
| Q121ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q122 | - |  |  | SI | Presión Arterial Diastólica |
| Q122ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q123 | - |  |  | SI | Presión Arterial Media |
| Q124 | - |  |  | SI | Peso |
| Q124ObsDR | - |  |  | SI | Peso DR |
| Q125 | - |  |  | SI | Hemoglucotest |
| Q125ObsDR | - |  |  | SI | Hemoglucotest DR |
| Q126 | - |  |  | SI | Observaciones |
| Q127 | - |  |  | SI | Dispositivos Invasivos |
| Q128 | - |  |  | SI | Comentario Dispositivos Invasivos |
| Q129 | - |  |  | SI | Catéter Venoso Central |
| Q13 | - |  |  | SI | Comentario A |
| Q130 | - |  |  | SI | Comentario Catéter Venoso Central |
| Q131 | - |  |  | SI | Vía Venosa Periférica |
| Q132 | - |  |  | SI | Comentario Vía Venosa Periférica |
| Q133 | - |  |  | SI | Sonda Nasogátrica |
| Q134 | - |  |  | SI | Comentario Sonda Nasogátrica |
| Q135 | - |  |  | SI | Gastrostomía |
| Q136 | - |  |  | SI | Comentario Gastrostomía |
| Q137 | - |  |  | SI | Traqueostomía |
| Q138 | - |  |  | SI | Comentario Traqueostomía |
| Q139 | - |  |  | SI | Drenaje Ventricular Externo |
| Q14 | - |  |  | SI | Comentario ML |
| Q140 | - |  |  | SI | Comentario Drenaje Ventricular Externo |
| Q141 | - |  |  | SI | Drenaje |
| Q142 | - |  |  | SI | Comentario Drenaje |
| Q143 | - |  |  | SI | Catéter Urinario Permanente |
| Q144 | - |  |  | SI | Comentario Catéter Urinario Permanente |
| Q145 | - |  |  | SI | Otro (s) Dispositivo(s) |
| Q147 | - |  |  | SI | Ficha Médica |
| Q148 | - |  |  | SI | Comentario Ficha Médica |
| Q149 | - |  |  | SI | Evaluación Pre-anestésica |
| Q15 | - |  |  | SI | Comentario CM |
| Q150 | - |  |  | SI | Comentario Evaluación Pre-anestésica |
| Q151 | - |  |  | SI | Ingreso Médico |
| Q152 | - |  |  | SI | Comentario Ingreso Médico |
| Q153 | - |  |  | SI | Ingreso de Enfermería |
| Q154 | - |  |  | SI | Comentario Ingreso de Enfermería |
| Q155 | - |  |  | SI | Escala de Riesgo LPP |
| Q156 | - |  |  | SI | Comentario Escala de Riesgo LPP |
| Q157 | - |  |  | SI | Escala de Riesgo Caídas |
| Q158 | - |  |  | SI | Comentario Escala de Riesgo Caídas |
| Q159 | - |  |  | SI | Hora Salida de Piso |
| Q16 | - |  |  | SI | Comentario P |
| Q160 | - |  |  | SI | PREPARACIÓN PRE-OPERATORIA |
| Q161 | - |  |  | SI | ARTÍCULOS RETIRADOS |
| Q162 | - |  |  | SI | VESTIMENTA QUIRÚRGICA |
| Q163 | - |  |  | SI | EXÁMENES DE LABORATORIO - IMÁGENES PARA LA CIRUGÍA... |
| Q164 | - |  |  | SI | GRUPO RH |
| Q165 | - |  |  | SI | AISLAMIENTO |
| Q166 | - |  |  | SI | PREPARACIÓN DE LA PIEL |
| Q167 | - |  |  | SI | SIGNOS VITALES |
| Q168 | - |  |  | SI | USO DE INVASIVOS / INFUSIONES |
| Q169 | - |  |  | SI | DOCUMENTACIÓN ENVIADA A PABELLÓN |
| Q170 | - |  |  | SI | Ambulatorio |
| Q171 | - |  |  | SI | Comentarios |
| Q172 | - |  |  | SI | Comentarios |
| Q173 | - |  |  | SI | Comentarios |
| Q174 | - |  |  | SI | Comentarios |
| Q175 | - |  |  | SI | Comentarios |
| Q176 | - |  |  | SI | Comentarios |
| Q177 | - |  |  | SI | Comentarios |
| Q178 | - |  |  | SI | Comentarios |
| Q20 | - |  |  | SI | Comentario LI |
| Q21 | - |  |  | SI | Comentario VV |
| Q22 | - |  |  | SI | Comentario T |
| Q23 | - |  |  | SI | Comentario MA |
| Q24 | - |  |  | SI | Comentario Grupo RH |
| Q26 | - |  |  | SI | Comentario CID |
| Q27 | - |  |  | SI | Comentario PR |
| Q28 | - |  |  | SI | Comentario JO |
| Q29 | - |  |  | SI | Comentario MAQ |
| Q30 | - |  |  | SI | Profilaxis Antibiótica |
| Q31 | - |  |  | SI | Medias Antiembólicas |
| Q32 | - |  |  | SI | Chequeo de Infusiones / Drogas In Situ |
| Q33 | - |  |  | SI | Prótesis |
| Q34 | - |  |  | SI | Joyas |
| Q35 | - |  |  | SI | Maquillaje |
| Q36 | - |  |  | SI | Esmalte de Uñas |
| Q37 | - |  |  | SI | Sujeciones para el Cabello (pinches) |
| Q38 | - |  |  | SI | Exámenes de Laboratorio - Imágenes para la Cirugía... |
| Q39 | - |  |  | SI | Grupo y Rh |
| Q40 | - |  |  | SI | Tipo Aislamiento |
| Q42 | - |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q43 | - |  |  | SI | Clasificación de Cirugía / Procedimiento |
| Q45 | - |  |  | SI | ¿Se realiza Tricotomía? |
| Q46 | - |  |  | SI | Servicio en el que se realiza Tricotomía |
| Q47 | - |  |  | SI | Ubicación de la Tricotomía |
| Q48 | - |  |  | SI | Se Usa Solución Jabonosa en Baño |
| Q49 | - |  |  | SI | Lugar en que se Realiza Baño Pre-Operatorio |
| Q50 | - |  |  | SI | Tipo de Solución Jabonosa Utilizada |
| Q51 | - |  |  | SI | Chequeo de medicamentos de uso habitual |
| Q52 | - |  |  | SI | Comentario EUN |
| Q53 | - |  |  | SI | Comentario SP |
| Q54 | - |  |  | SI | Otros Exámenes |
| Q55 | - |  |  | SI | Comentario CM |
| Q56 | - |  |  | SI | Otra Ubicación |
| Q57 | - |  |  | SI | Otro Lugar |
| Q58 | - |  |  | SI | Otra Solución |
| Q60 | - |  |  | SI | Comentarios Brazalete Alergias |
| Q61 | - |  |  | SI | Consentimiento Qx Informado Firmado |
| Q62 | - |  |  | SI | comentarios Consentiemiento |
| Q63 | - |  |  | SI | Consentimiento Anestésico Informado Firmado |
| Q64 | - |  |  | SI | Observaciones Vía Venosa Periférica |
| Q65 | - |  |  | SI | Comentario consentimiento an |
| Q66 | - |  |  | SI | Porta Brazalete de Alergias |
| Q67 | - |  |  | SI | Responsable |
| Q68 | - |  |  | SI | N° Vía Venosa Periférica |
| Q69 | - |  |  | SI | Ubicación Vía Venosa Periférica |
| Q70 | - |  |  | SI | N° Intentos Vía Venosa Periférica |
| Q72 | - |  |  | SI | N° Otro Dispositivo |
| Q73 | - |  |  | SI | Ubicación Otro Dispositivo |
| Q75 | - |  |  | SI | N° Intentos Otro Dispositivo |
| Q76 | - |  |  | SI | Observaciones Otro Dispositivo |
| Q77 | - |  |  | SI | Fecha de Intervención |
| Q78 | - |  |  | SI | Servicio Clínico |
| Q79 | - |  |  | SI | Sala |
| Q80 | - |  |  | SI | Cama |
| Q81 | - |  |  | SI | Diagnóstico |
| Q82 | - |  |  | SI | Ayuno |
| Q83 | - |  |  | SI | Fecha Última Comida |
| Q84 | - |  |  | SI | Hora Última Comida |
| Q85 | - |  |  | SI | Chequeo de Medicamentos de uso habitual |
| Q86 | - |  |  | SI | Fecha |
| Q87 | - |  |  | SI | Hora |
| Q88 | - |  |  | SI | Chequeo de Infusiones / Drogas In Situ |
| Q89 | - |  |  | SI | Fecha |
| Q90 | - |  |  | SI | Hora |
| Q91 | - |  |  | SI | Profilaxis Antibiótica |
| Q92 | - |  |  | SI | Fecha |
| Q93 | - |  |  | SI | Hora |
| Q94 | - |  |  | SI | Vaciamiento Vesical |
| Q95 | - |  |  | SI | Tipo Vaciamiento Vesical |
| Q96 | - |  |  | SI | Último registro de FUR |
| Q97 | - |  |  | SI | Grupo Sanguíneo |
| Q98 | - |  |  | SI | Lentes (Anteojos - De contacto) |
| Q99 | - |  |  | SI | Comentario |
| QCoJ | - |  |  | SI | Comentarios Solución Jabonosa |
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
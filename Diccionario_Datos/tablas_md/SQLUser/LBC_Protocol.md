# SQLUser.LBC_Protocol

**Schema:** SQLUser
**Columnas:** 281
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPT_RowID | bigint | PK |  | NO | - |
| ChildQ169DR | - |  |  | SI | Child Reference: Inmunización |
| LBCPT_Code | varchar |  |  | SI | Code |
| LBCPT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPT_CreatedDate | date |  |  | SI | Created Date |
| LBCPT_CreatedTime | time |  |  | SI | Created Time |
| LBCPT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPT_DateFrom | date |  |  | SI | Date From |
| LBCPT_DateTo | date |  |  | SI | Date To |
| LBCPT_DepartmentRestrictionList | varchar |  |  | SI | Department Restriction List |
| LBCPT_Desc | varchar |  |  | SI | Description |
| LBCPT_LabSiteRestrictionList | varchar |  |  | SI | Lab Site Restriction List |
| LBCPT_Owner | varchar |  |  | SI | Owner |
| LBCPT_SOPCode | varchar |  |  | SI | SOP Code |
| LBCPT_SpecimenGroupList | varchar |  |  | SI | Specimen Group  |
| LBCPT_SpecimenList | varchar |  |  | SI | Specimen  |
| LBCPT_SubLevel | varchar |  |  | SI | Sub Level |
| LBCPT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01a | - |  |  | SI | Motivo de Ingreso |
| Q02a | - |  |  | SI | Acompañado por: |
| Q03a | - |  |  | SI | Medio de Llegada |
| Q04a | - |  |  | SI | Otro Medio de Llegada |
| Q05a | - |  |  | SI | Nombre Contacto Emergencia |
| Q06a | - |  |  | SI | Teléfono Contacto Emergencia |
| Q07a | - |  |  | SI | Información Entregada Por |
| Q08a | - |  |  | SI | Información Entregada por Otro |
| Q09a | - |  |  | SI | Origen del Paciente |
| Q100a | - |  |  | SI | FiO2 |
| Q100aObsDR | - |  |  | SI | FiO2 DR |
| Q101a | - |  |  | SI | Hemoglucotest |
| Q101aObsDR | - |  |  | SI | Hemoglucotest DR |
| Q102a | - |  |  | SI | Escala de Dolor (EVA) |
| Q102aObsDR | - |  |  | SI | Escala de Dolor (EVA) DR |
| Q103a | - |  |  | SI | Comentarios Examen Físico General |
| Q104a | - |  |  | SI | Cardiaco |
| Q104aObsDR | - |  |  | SI | Cardiaco DR |
| Q105a | - |  |  | SI | Ritmo Cardiaco |
| Q105aObsDR | - |  |  | SI | Ritmo Cardiaco DR |
| Q106a | - |  |  | SI | Comentario OP |
| Q107a | - |  |  | SI | Comentario AI |
| Q108a | - |  |  | SI | Comentario DC |
| Q109a | - |  |  | SI | Comentario EX |
| Q10a | - |  |  | SI | Procedencia Otro Centro Asistencial: Tiempo de Est... |
| Q110a | - |  |  | SI | Comentarios Edema |
| Q111a | - |  |  | SI | Comentarios Extremidades Inferiores |
| Q112 | - |  |  | SI | Otra Razón para no evaluar dolor |
| Q113 | - |  |  | SI | Razones para no evaluar dolor |
| Q114 | - |  |  | SI | Valoración del Dolor |
| Q115 | - |  |  | SI | Deposición |
| Q115ObsDR | - |  |  | SI | Deposición DR |
| Q116 | - |  |  | SI | Ano |
| Q116ObsDR | - |  |  | SI | Ano DR |
| Q117 | - |  |  | SI | Diuresis |
| Q117ObsDR | - |  |  | SI | Diuresis DR |
| Q118 | - |  |  | SI | Comentario Estado Psíquico |
| Q119 | - |  |  | SI | Comentarios Genito-Urinario |
| Q11a | - |  |  | SI | Paciente Porta Brazalete Identificación |
| Q120 | - |  |  | SI | Comentarios Ano |
| Q121 | - |  |  | SI | Comentarios Diuresis |
| Q122 | - |  |  | SI | Comentarios Deposición |
| Q123 | - |  |  | SI | Mamas |
| Q123ObsDR | - |  |  | SI | Mamas DR |
| Q124 | - |  |  | SI | Pezones |
| Q124ObsDR | - |  |  | SI | Pezones DR |
| Q125 | - |  |  | SI | Útero |
| Q125ObsDR | - |  |  | SI | Útero DR |
| Q126 | - |  |  | SI | Comentarios Mamas |
| Q127 | - |  |  | SI | Comentarios Pezones |
| Q128 | - |  |  | SI | Comentarios Útero |
| Q129 | - |  |  | SI | Profesional de Salud |
| Q12a | - |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q130 | - |  |  | SI | Comentario |
| Q131 | - |  |  | SI | LPP |
| Q131ObsDR | - |  |  | SI | LPP DR |
| Q132 | - |  |  | SI | Grado LPP |
| Q132ObsDR | - |  |  | SI | Grado LPP DR |
| Q133 | - |  |  | SI | Ubicación LPP |
| Q133ObsDR | - |  |  | SI | Ubicación LPP DR |
| Q134 | - |  |  | SI | Lateralidad LPP |
| Q134ObsDR | - |  |  | SI | Lateralidad LPP DR |
| Q135 | - |  |  | SI | Comentario LPP |
| Q136 | - |  |  | SI | Comentario G.LPP |
| Q137 | - |  |  | SI | Comentario U.LPP |
| Q138 | - |  |  | SI | Comentario L.LPP |
| Q139 | - |  |  | SI | Origen LPP |
| Q139ObsDR | - |  |  | SI | Origen LPP DR |
| Q13a | - |  |  | SI | Antecedentes Clínicos |
| Q140 | - |  |  | SI | Comentario O.LPP |
| Q141 | - |  |  | SI | Presión Arterial Media |
| Q142 | - |  |  | SI | Oxigenoterapia |
| Q142ObsDR | - |  |  | SI | Oxigenoterapia DR |
| Q143 | - |  |  | SI | Flujo de Oxigeno |
| Q143ObsDR | - |  |  | SI | Flujo de Oxigeno DR |
| Q144 | - |  |  | SI | Peso Ideal Hombre |
| Q145 | - |  |  | SI | Peso Ideal Mujer |
| Q146 | - |  |  | SI | IMC |
| Q147 | - |  |  | SI | Superficie Corporal |
| Q148 | - |  |  | SI | Circunferencia Creaneana |
| Q148ObsDR | - |  |  | SI | Circunferencia Creaneana DR |
| Q149 | - |  |  | SI | Circunferenca Torácica |
| Q149ObsDR | - |  |  | SI | Circunferenca Torácica DR |
| Q14a | - |  |  | SI | comentario 02 |
| Q150 | - |  |  | SI | Circunferencia Abdominal |
| Q150ObsDR | - |  |  | SI | Circunferencia Abdominal DR |
| Q151 | - |  |  | SI | Temperatura Rectal |
| Q151ObsDR | - |  |  | SI | Temperatura Rectal DR |
| Q152 | - |  |  | SI | Antecedentes Generales |
| Q153 | - |  |  | SI | Aspectos Socio-Culturales |
| Q154 | - |  |  | SI | Tipo Examen Físico |
| Q155 | - |  |  | SI | Signos Vitales |
| Q156 | - |  |  | SI | Parámetros Antropométricos |
| Q157 | - |  |  | SI | Examen Segmentario |
| Q158 | - |  |  | SI | Instruciones Generales al Paciente y su Familia |
| Q159 | - |  |  | SI | Inmunización |
| Q15a | - |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q160 | - |  |  | SI | Otra Inmunización |
| Q161 | - |  |  | SI | Primera Dosis |
| Q162 | - |  |  | SI | Segunda Dosis |
| Q163 | - |  |  | SI | Dosis de Refuerzo |
| Q164 | - |  |  | SI | Comentario Primera Dosis |
| Q165 | - |  |  | SI | Comentario Segunda Dosis |
| Q166 | - |  |  | SI | Comentario Dosis de Refuerzo |
| Q167 | - |  |  | SI | Teléfono Contacto Emergencia |
| Q168 | - |  |  | SI | FUR |
| Q16a | - |  |  | SI | comentario 03 |
| Q170 | - |  |  | SI | Inventario de Pertenencias |
| Q171 | - |  |  | SI | Comentario Inventario de Pertenencias |
| Q172 | - |  |  | SI | Educación de Prevención de Caídas |
| Q173 | - |  |  | SI | Comentario&nbsp |
| Q174 | - |  |  | SI | ¿Recibiría transfusión sanguínea en caso de necesi... |
| Q17a | - |  |  | SI | Dispositivos Artificiales |
| Q18a | - |  |  | SI | Otro Dispositivo |
| Q19a | - |  |  | SI | Dispositivos Clínicos |
| Q20a | - |  |  | SI | Otro Dispositivo Clínico |
| Q21a | - |  |  | SI | Exámenes que Trae el Paciente |
| Q22a | - |  |  | SI | Otro Examen |
| Q23a | - |  |  | SI | Anamnesis |
| Q24a | - |  |  | SI | Información Entregada por Otro |
| Q25a | - |  |  | SI | Otro Dispositivo 2 |
| Q26a | - |  |  | SI | Religión |
| Q27a | - |  |  | SI | Consumo de Alcohol |
| Q28a | - |  |  | SI | Tiempo de Consumo Alcohol |
| Q29a | - |  |  | SI | Tabaquismo |
| Q30a | - |  |  | SI | Cigarrillos por día |
| Q31a | - |  |  | SI | Años de consumo |
| Q32a | - |  |  | SI | Paquete Cigarrillos/Año |
| Q33a | - |  |  | SI | Consumo de Drogas |
| Q34a | - |  |  | SI | Otra Droga |
| Q35a | - |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q36a | - |  |  | SI | Nivel de Dependencia |
| Q37a | - |  |  | SI | Nivel Educacional |
| Q38a | - |  |  | SI | Forma de Comunicación |
| Q39a | - |  |  | SI | Otra Forma de Comunicación |
| Q40a | - |  |  | SI | Necesita Intérprete |
| Q41a | - |  |  | SI | Comentarios NI |
| Q42a | - |  |  | SI | Tipo Examen Físico |
| Q43a | - |  |  | SI | Estado General |
| Q44a | - |  |  | SI | Estado Psíquico |
| Q44aObsDR | - |  |  | SI | Estado Psíquico DR |
| Q45a | - |  |  | SI | Otro Estado Psíquico |
| Q46a | - |  |  | SI | Conciencia |
| Q46aObsDR | - |  |  | SI | Conciencia DR |
| Q47a | - |  |  | SI | Piel |
| Q47aObsDR | - |  |  | SI | Piel DR |
| Q48a | - |  |  | SI | Mucosas |
| Q48aObsDR | - |  |  | SI | Mucosas DR |
| Q49a | - |  |  | SI | Cabeza - Cara |
| Q49aObsDR | - |  |  | SI | Cabeza - Cara DR |
| Q50a | - |  |  | SI | Pupilas |
| Q50aObsDR | - |  |  | SI | Pupilas DR |
| Q51a | - |  |  | SI | Conjuntivas |
| Q51aObsDR | - |  |  | SI | Conjuntivas DR |
| Q52a | - |  |  | SI | Dentadura |
| Q52aObsDR | - |  |  | SI | Dentadura DR |
| Q53a | - |  |  | SI | Lenguaje |
| Q53aObsDR | - |  |  | SI | Lenguaje DR |
| Q54a | - |  |  | SI | Cuello |
| Q54aObsDR | - |  |  | SI | Cuello DR |
| Q55a | - |  |  | SI | Vía Aérea |
| Q55aObsDR | - |  |  | SI | Vía Aérea DR |
| Q56a | - |  |  | SI | Respiración |
| Q56aObsDR | - |  |  | SI | Respiración DR |
| Q57a | - |  |  | SI | Tórax |
| Q57aObsDR | - |  |  | SI | Tórax DR |
| Q58a | - |  |  | SI | Extremidades Superiores |
| Q58aObsDR | - |  |  | SI | Extremidades Superiores DR |
| Q59a | - |  |  | SI | Abdomen |
| Q59aObsDR | - |  |  | SI | Abdomen DR |
| Q60a | - |  |  | SI | Genito-Urinario |
| Q60aObsDR | - |  |  | SI | Genito-Urinario DR |
| Q61a | - |  |  | SI | Extremidades Inferiores |
| Q61aObsDR | - |  |  | SI | Extremidades Inferiores DR |
| Q62a | - |  |  | SI | Edema |
| Q62aObsDR | - |  |  | SI | Edema DR |
| Q63a | - |  |  | SI | Comentario Conciencia |
| Q64a | - |  |  | SI | Comentario Piel |
| Q65a | - |  |  | SI | Comentario Mucosas |
| Q66a | - |  |  | SI | Comentario Cabeza-Cara |
| Q67a | - |  |  | SI | Comentario Pupilas |
| Q68a | - |  |  | SI | Comentario Conjuntivas |
| Q69a | - |  |  | SI | Comentario Dentadura |
| Q70a | - |  |  | SI | Comentario Lenguaje |
| Q71a | - |  |  | SI | Comentario Cuello |
| Q72a | - |  |  | SI | Comentario Vía Aérea |
| Q73a | - |  |  | SI | Comentario Respiración |
| Q74a | - |  |  | SI | Comentario Tórax |
| Q75a | - |  |  | SI | Comentario Cardiaco |
| Q76a | - |  |  | SI | Comentario Ritmo Cardiaco |
| Q77a | - |  |  | SI | Comentario Abdomen |
| Q78a | - |  |  | SI | Comentario Extremidades Superiores |
| Q79a | - |  |  | SI | Nombre de la Enfermera/Matrona |
| Q80a | - |  |  | SI | Manejo de la Cama |
| Q81a | - |  |  | SI | Localización del Baño |
| Q82a | - |  |  | SI | Horarios de Comida |
| Q83a | - |  |  | SI | Horario de Visitas |
| Q84a | - |  |  | SI | Nombre de quién recibe la información |
| Q85a | - |  |  | SI | Comentario 01 |
| Q86a | - |  |  | SI | Comentario 02 |
| Q87a | - |  |  | SI | Comentario 03 |
| Q88a | - |  |  | SI | Comentario 04 |
| Q89a | - |  |  | SI | Comentario 05 |
| Q90a | - |  |  | SI | Aislamiento |
| Q91a | - |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q92a | - |  |  | SI | Presión Arterial Sistólica |
| Q92aObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q93a | - |  |  | SI | Presión Arterial Diastólica |
| Q93aObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q94a | - |  |  | SI | Peso |
| Q94aObsDR | - |  |  | SI | Peso DR |
| Q95a | - |  |  | SI | Talla |
| Q95aObsDR | - |  |  | SI | Talla DR |
| Q96 | - |  |  | SI | Frecuencia Cardiaca |
| Q96ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q97a | - |  |  | SI | Frecuencia Respiratoria |
| Q97aObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q98a | - |  |  | SI | Temperatura Axilar |
| Q98aObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q99a | - |  |  | SI | SO2 |
| Q99aObsDR | - |  |  | SI | SO2 DR |
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
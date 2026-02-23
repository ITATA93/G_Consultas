# SQLUser.LBC_TestItemRanges

**Schema:** SQLUser
**Columnas:** 279
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTIR_ParRef | bigint | PK |  | NO | Parent TestItem DR |
| LBCTIR_AgeFrom | double |  |  | SI | Age Range From (format [yy].mmdd , ddd is 0-1231)... |
| LBCTIR_AgeTo | double |  |  | SI | Age Range To (format [yy].mmdd , mmdd is 0-1231)
... |
| LBCTIR_Altitude_DR | bigint |  | FK | SI | Altitude
Optinal, Indicates any altitude-related ... |
| LBCTIR_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTIR_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTIR_AutoHighRange | double |  |  | SI | (Auto) High Range (maximum 'auto-authorise' value ... |
| LBCTIR_AutoLowRange | double |  |  | SI | (Auto) Low Range (minimum 'auto-authorise' value f... |
| LBCTIR_CareProv_DR | varchar |  | FK | SI | Care Provider |
| LBCTIR_ClinicalCondition_DR | bigint |  | FK | SI | Clinical Condition DR. Optional
Compared with LBE... |
| LBCTIR_ClinicalReviewFlag | bit |  |  | SI | Clinical Review Flag |
| LBCTIR_ClinicalReviewHighRange | double |  |  | SI | (Clinical Review High Range 
If present, must be ... |
| LBCTIR_ClinicalReviewLowRange | double |  |  | SI | Clinical Review Low Range  |
| LBCTIR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTIR_Comments | varchar |  |  | SI | Comments |
| LBCTIR_Container_DR | bigint |  | FK | SI | Container |
| LBCTIR_DateFrom | date |  |  | NO | Effective date for the record |
| LBCTIR_DateTo | date |  |  | SI | DateTo
Last day the record is active
Optional.  ... |
| LBCTIR_DisplayText | varchar |  |  | SI | Display Text
Show instead of numerical ranges.
N... |
| LBCTIR_Ethinicity_DR | bigint |  | FK | SI | Ethnicity.  Optional
Compared with PAPERIndigStat... |
| LBCTIR_Fasting | varchar |  |  | SI | Patient Fasting |
| LBCTIR_HighRange | double |  |  | SI | (Normal) High Range (maximum normal value)
Option... |
| LBCTIR_InstrumentGroup_DR | bigint |  | FK | SI | Instrument Group |
| LBCTIR_Instrument_DR | bigint |  | FK | SI | Instrument |
| LBCTIR_Interpretation_DR | bigint |  | FK | SI | Clinical Interpretation for the range |
| LBCTIR_LabSite_DR | bigint |  | FK | SI | Lab Site Location.  Optional
This is the Location... |
| LBCTIR_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTIR_LowRange | double |  |  | SI | (Normal) Low Range (minimum normal value)
Optiona... |
| LBCTIR_PanicHighRange | double |  |  | SI | (Panic) High Range (values above PathHighRange up ... |
| LBCTIR_PanicLowRange | double |  |  | SI | (Panic) Low Range (values below PathLowRange down ... |
| LBCTIR_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBCTIR_PatientLocation_DR | bigint |  | FK | SI | Patient Location DR.  Optional |
| LBCTIR_Pregnant | varchar |  |  | SI | Pregnant.
Should be set '' unless Sex='F'.
For f... |
| LBCTIR_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| LBCTIR_RowID | varchar |  |  | NO | - |
| LBCTIR_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCTIR_Sex_DR | bigint |  | FK | SI | Sex
Optional, Compared with LBEPSexDR |
| LBCTIR_SpeciesBreed_DR | varchar |  | FK | SI | Species Breeds |
| LBCTIR_Species_DR | bigint |  | FK | SI | Species
Optional, Compared with (future) PAPERSpe... |
| LBCTIR_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTIR_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTIR_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCTIR_TestMethod_DR | bigint |  | FK | SI | Test Method |
| LBCTIR_Type | varchar |  |  | SI | Ranges Type
AdmType Code Table  
Compared with t... |
| LBCTIR_UnacceptableHighRange | double |  |  | SI | (Unacceptable) High Range (values above PanicHighR... |
| LBCTIR_UnacceptableLowRange | double |  |  | SI | (Unacceptable) Low Range (values below PanicLowRan... |
| LBCTIR_WeeksOfPregnancyFrom | integer |  |  | SI | Weeks Of Pregnancy Range From
Optional.  Must onl... |
| LBCTIR_WeeksOfPregnancyTo | integer |  |  | SI | Weeks Of Pregnancy Range To
Optional.  Must only ... |
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
| Q110a | - |  |  | SI | comentario Edema |
| Q111a | - |  |  | SI | comentario Extremidades Inferiores |
| Q112 | - |  |  | SI | Especifique |
| Q113 | - |  |  | SI | Razones para no evaluar dolor |
| Q114 | - |  |  | SI | Valoración del Dolor |
| Q115 | - |  |  | SI | Deposición |
| Q115ObsDR | - |  |  | SI | Deposición DR |
| Q116 | - |  |  | SI | Ano |
| Q116ObsDR | - |  |  | SI | Ano DR |
| Q117 | - |  |  | SI | Diuresis |
| Q117ObsDR | - |  |  | SI | Diuresis DR |
| Q118 | - |  |  | SI | Comentarios Estado Psíquico |
| Q119 | - |  |  | SI | comentarios Genito-Urinario |
| Q11a | - |  |  | SI | Paciente Porta Brazalete Identificación |
| Q120 | - |  |  | SI | comentarios Ano |
| Q121 | - |  |  | SI | comentarios Diuresis |
| Q122 | - |  |  | SI | comentarios Deposición |
| Q123 | - |  |  | SI | Mamas |
| Q123ObsDR | - |  |  | SI | Mamas DR |
| Q124 | - |  |  | SI | Pezones |
| Q124ObsDR | - |  |  | SI | Pezones DR |
| Q125 | - |  |  | SI | Útero |
| Q125ObsDR | - |  |  | SI | Útero DR |
| Q126 | - |  |  | SI | Comentarios Mamas |
| Q127 | - |  |  | SI | comentarios Pezones |
| Q128 | - |  |  | SI | comentarios Útero |
| Q129 | - |  |  | SI | Profesional de Salud |
| Q12a | - |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q130 | - |  |  | SI | Signos Vitales |
| Q13a | - |  |  | SI | Comentario 01 |
| Q141 | - |  |  | SI | Presión Arterial Media |
| Q142 | - |  |  | SI | Oxigenoterapia |
| Q142ObsDR | - |  |  | SI | Oxigenoterapia DR |
| Q143 | - |  |  | SI | Flujo de Oxígeno |
| Q143ObsDR | - |  |  | SI | Flujo de Oxígeno DR |
| Q144 | - |  |  | SI | Peso Ideal Hombre |
| Q145 | - |  |  | SI | Peso Ideal Mujer |
| Q146 | - |  |  | SI | IMC |
| Q147 | - |  |  | SI | Superficie Corporal |
| Q148 | - |  |  | SI | Circunferencia Craneana |
| Q148ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q149 | - |  |  | SI | Circunferencia Torácica |
| Q149ObsDR | - |  |  | SI | Circunferencia Torácica DR |
| Q14a | - |  |  | SI | comentario 02 |
| Q150 | - |  |  | SI | Circunferencia Abdominal |
| Q150ObsDR | - |  |  | SI | Circunferencia Abdominal DR |
| Q15a | - |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q16a | - |  |  | SI | comentario 03 |
| Q17a | - |  |  | SI | Dispositivos Artificiales |
| Q18a | - |  |  | SI | Otro Dispositivo |
| Q19a | - |  |  | SI | Dispositivos Clínicos |
| Q200 | - |  |  | SI | Aspectos Socio-Culturales |
| Q201 | - |  |  | SI | Tipo Examen Físico |
| Q202 | - |  |  | SI | Signos Vitales |
| Q203 | - |  |  | SI | Parámetros Antropométricos |
| Q204 | - |  |  | SI | Examen Segmentario |
| Q205 | - |  |  | SI | Antecedentes Clínicos |
| Q206 | - |  |  | SI | Esquema de vacunas al día |
| Q207 | - |  |  | SI | Requiere licencia médica |
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
| Q41a | - |  |  | SI | Comentarios Necesita Intérprete |
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
| Q66a | - |  |  | SI | Comentario Cabeza - Cara |
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
| Q98a | - |  |  | SI | Temperatura |
| Q98aObsDR | - |  |  | SI | Temperatura DR |
| Q99a | - |  |  | SI | Saturación de O2 |
| Q99aObsDR | - |  |  | SI | Saturación de O2 DR |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
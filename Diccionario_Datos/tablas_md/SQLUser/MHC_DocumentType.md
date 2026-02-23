# SQLUser.MHC_DocumentType

**Schema:** SQLUser
**Columnas:** 168
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHCDOCUMT_RowId | bigint | PK |  | NO | - |
| CQ100 | - |  |  | SI | (null) |
| CQ103 | - |  |  | SI | (null) |
| CQ104 | - |  |  | SI | (null) |
| CQ106 | - |  |  | SI | (null) |
| CQ81 | - |  |  | SI | (null) |
| CQ82 | - |  |  | SI | (null) |
| CQ87 | - |  |  | SI | (null) |
| CQ88 | - |  |  | SI | (null) |
| CQ89 | - |  |  | SI | (null) |
| CQ90 | - |  |  | SI | (null) |
| CQ91 | - |  |  | SI | (null) |
| CQ92 | - |  |  | SI | (null) |
| CQ93 | - |  |  | SI | (null) |
| CQ94 | - |  |  | SI | (null) |
| CQ95 | - |  |  | SI | (null) |
| CQ96 | - |  |  | SI | (null) |
| CQ97 | - |  |  | SI | (null) |
| CQ98 | - |  |  | SI | (null) |
| CQ99 | - |  |  | SI | (null) |
| ChildQ108DR | - |  |  | SI | Child Reference: Historial de Atención Familiar |
| MHCDOCUMT_Code | varchar |  |  | NO | Code |
| MHCDOCUMT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHCDOCUMT_CreatedDate | date |  |  | SI | Created Date |
| MHCDOCUMT_CreatedTime | time |  |  | SI | Created Time |
| MHCDOCUMT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHCDOCUMT_DateFrom | date |  |  | SI | Date From |
| MHCDOCUMT_DateTo | date |  |  | SI | Date To |
| MHCDOCUMT_Desc | varchar |  |  | NO | Description |
| MHCDOCUMT_EditLetter_DR | bigint |  | FK | SI | Des Ref CTLetterTemplate |
| MHCDOCUMT_Owner | varchar |  |  | SI | Owner |
| MHCDOCUMT_Quest_DR | bigint |  | FK | SI | Des Ref SSUserDefWindow |
| MHCDOCUMT_UpdatedDate | date |  |  | SI | Updated Date |
| MHCDOCUMT_UpdatedTime | time |  |  | SI | Updated Time |
| MHCDOCUMT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| MHCDOCUMT_ZenReport_DR | bigint |  | FK | SI | Des Ref websys.Report |
| Q1 | - |  |  | SI | Madre Cuidadorea c/educ. basica completa |
| Q10 | - |  |  | SI | Saneamiento adecudo |
| Q100 | - |  |  | SI | ¿Qué problemas de contaminación o deterioro del en... |
| Q101 | - |  |  | SI | Ingreso Familiar |
| Q102 | - |  |  | SI | Ingreso Per Cápita |
| Q103 | - |  |  | SI | Conexión al Cableado Eléctrico |
| Q104 | - |  |  | SI | Distancia al Paradero |
| Q105 | - |  |  | SI | Conexión Telefónica |
| Q106 | - |  |  | SI | Tipo Trabajo |
| Q107 | - |  |  | SI | Familia vive en sector |
| Q11 | - |  |  | SI | Expresion de afecto |
| Q12 | - |  |  | SI | Normas claras y flexibles |
| Q13 | - |  |  | SI | Comunicacion sana |
| Q14 | - |  |  | SI | Presencia de rituales familiares |
| Q15 | - |  |  | SI | Jerarquia dentro de la familia |
| Q17 | - |  |  | SI | Actividad deportiva sistematica |
| Q18 | - |  |  | SI | Sentido de pertenencia a la familia |
| Q19 | - |  |  | SI | Sentido del humor |
| Q2 | - |  |  | SI | Jefe de hogar c/educ. media completa o superior |
| Q20 | - |  |  | SI | Otros |
| Q22 | - |  |  | SI | Alta vulnerabilidad social segun Ficha de Protecci... |
| Q24 | - |  |  | SI | Cesantia mas de 6 meses |
| Q25 | - |  |  | SI | Union de pareja inestable |
| Q26 | - |  |  | SI | Patologia Psiq. grave de algun integrante de la fa... |
| Q28 | - |  |  | SI | Desvinculacion de Redes |
| Q29 | - |  |  | SI | Ausencia de figura materna y paterna o sin figura ... |
| Q3 | - |  |  | SI | Adecuada calidad de la vivienda |
| Q33 | - |  |  | SI | Cesantia reciente (menos de 6 meses) |
| Q34 | - |  |  | SI | Embarazo no deseado |
| Q35 | - |  |  | SI | Embarazo adolescente |
| Q37 | - |  |  | SI | Ausencia de figura materna o paterna |
| Q38 | - |  |  | SI | Crisis economica reciente |
| Q39 | - |  |  | SI | Enfermedad terminal o enfermedad grave reciente de... |
| Q4 | - |  |  | SI | Participa en redes sociales de apoyo (Org. Comunit... |
| Q40 | - |  |  | SI | Duelo reciente |
| Q41 | - |  |  | SI | Analfabetismo del padre o madre |
| Q42 | - |  |  | SI | Hacinamiento |
| Q44 | - |  |  | SI | Crisis no normativas |
| Q45 | - |  |  | SI | Patologia cronica (DM, HTA, SBO, Otras) |
| Q48 | - |  |  | SI | Contaminacion Intradomiciliaria |
| Q49 | - |  |  | SI | Crisis Familiar Normativa |
| Q5 | - |  |  | SI | Apoyo de familias de origen cercano |
| Q50 | - |  |  | SI | Ausencia de espacio de recreacion y esparcimiento |
| Q51 | - |  |  | SI | Madre o cuidadora con educacion basica incompleta |
| Q53 | - |  |  | SI | Otros |
| Q54 | - |  |  | SI | Desercion Escolar |
| Q55 | - |  |  | SI | Alcoholismo |
| Q56 | - |  |  | SI | Drogadiccion |
| Q57 | - |  |  | SI | VIF |
| Q58 | - |  |  | SI | Maltrato Infantil |
| Q59 | - |  |  | SI | Delincuencia |
| Q6 | - |  |  | SI | Apoyo de Vecinos |
| Q60 | - |  |  | SI | Resultado Riesgo Familiar |
| Q60ObsDR | - |  |  | SI | Resultado Riesgo Familiar DR |
| Q61 | - |  |  | SI | Daño |
| Q62 | - |  |  | SI | Prostitucion |
| Q63 | - |  |  | SI | Psicopatia grave compensada en cualquier miembro d... |
| Q64 | - |  |  | SI | Adulto mayor que vive solo (red social insuficient... |
| Q65 | - |  |  | SI | Malas condiciones de habitabilidad (segun pauta de... |
| Q66 | - |  |  | SI | Crisis Familiar no Normativa |
| Q67 | - |  |  | SI | Abandono escolar reciente (menor de 1 año)y riesgo... |
| Q68 | - |  |  | SI | Falta de adherencia a controles de salud y tratami... |
| Q69 | - |  |  | SI | Entorno peligroso |
| Q7 | - |  |  | SI | Trabajo estable |
| Q70 | - |  |  | SI | Otros riesgos considerados por el profesional |
| Q71 | - |  |  | SI | Distribucion equitativa de las tareas del hogar |
| Q72 | - |  |  | SI | Discapacidad (psiquica, fisica o sensorial) del Pa... |
| Q73 | - |  |  | SI | Discapacidad (psiquica, fisica o sensorial) del Pa... |
| Q74 | - |  |  | SI | Asistencia de los niños y adolecentes a establecim... |
| Q75 | - |  |  | SI | Acceso a beneficios sociales |
| Q76 | - |  |  | SI | Resolucion de conflictos adecuada |
| Q8 | - |  |  | SI | Necesidades basicas cubiertas |
| Q80 | - |  |  | SI | Antecedentes Sociales, de la Vivienda y el Entorno |
| Q81 | - |  |  | SI | Tipo de vivienda |
| Q82 | - |  |  | SI | Tenencia de la vivienda |
| Q83 | - |  |  | SI | N° de piezas |
| Q85 | - |  |  | SI | N° de dormitorios |
| Q86 | - |  |  | SI | N° de camas |
| Q87 | - |  |  | SI | ¿Baño dentro de la casa? |
| Q88 | - |  |  | SI | ¿Cocina dentro de la casa? |
| Q89 | - |  |  | SI | Conservación de la vivienda |
| Q9 | - |  |  | SI | Percepcion de suficiencia economica |
| Q90 | - |  |  | SI | Fuente de origen del agua |
| Q91 | - |  |  | SI | ¿Cómo llega el agua para ser ocupada? |
| Q92 | - |  |  | SI | Sistema de eliminación de excretas |
| Q93 | - |  |  | SI | Sistema de disposición de basuras |
| Q94 | - |  |  | SI | Sistema eléctrico |
| Q95 | - |  |  | SI | Combustible que usa |
| Q96 | - |  |  | SI | Sistema de calefaccion |
| Q97 | - |  |  | SI | ¿Tiene animales domésticos? |
| Q98 | - |  |  | SI | Animales domésticos |
| Q99 | - |  |  | SI | Vectores |
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